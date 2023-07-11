import os
# esto es para eviatar un error en Windows: OMP: Error #15: Initializing libiomp5md.dll, but found libiomp5md.dll already initialized.
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

from argparse import ArgumentParser

import cv2
import numpy as np
from ultralytics.nn.autobackend import AutoBackend
from ultralytics.yolo.utils.plotting import Annotator, colors
import torch
from bytetrack.byte_tracker import BYTETracker
from ultralytics.yolo.data.dataloaders.stream_loaders import LoadImages
from ultralytics.yolo.utils.ops import non_max_suppression, scale_boxes

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-v", "--video", dest="video", type=str, required=True, help="archivo de video")
    return parser.parse_args()

args  = parse_args()


save_vid = True
video_file = args.video  #"skateboard_02.mp4"
vid_writer = None
save_path = video_file[:-4] + "_output.mp4"

model = AutoBackend("yolov8n.pt")
model.warmup()
stride, names, pt = model.stride, model.names, model.pt

bytetracker = BYTETracker(
    track_thresh=0.6, match_thresh=0.8, track_buffer=120, frame_rate=30
)
tracker = bytetracker

conf_thres = 0.25
iou_thres = 0.45
classes = None
agnostic_nms = False
max_det = 1000
line_thickness = 2
half = False
imgsz = (640, 640)
vid_stride = 1

dataset = LoadImages(
    video_file,
    imgsz=imgsz,
    stride=stride,
    auto=pt,
    transforms=None,
    vid_stride=vid_stride,
)

for frame_idx, batch in enumerate(dataset):
    path, im, im0s, vid_cap, s = batch
    detections = np.empty((0, 5))
    im = torch.from_numpy(im).to("cpu")
    im = im.half() if half else im.float()  # uint8 to fp16/32
    im /= 255.0  # 0 - 255 to 0.0 - 1.0
    im = torch.unsqueeze(im, 0)

    result = model(im)

    p = non_max_suppression(
        result, conf_thres, iou_thres, classes, agnostic_nms, max_det=max_det
    )

    for i, det in enumerate(p):
        p, im0, _ = path, im0s.copy(), getattr(dataset, "frame", 0)

        if det is not None and len(det):
            det[:, :4] = scale_boxes(
                im.shape[2:], det[:, :4], im0.shape
            ).round()  # rescale boxes to im0 size

        track_result = tracker.update(det.cpu(), im0)

        annotator = Annotator(im0, line_width=line_thickness, example=str(names))

        # draw boxes for visualization
        if len(track_result) > 0:
            for j, (output) in enumerate(track_result):
                bbox = output[0:4]
                id = output[4]
                cls = output[5]
                conf = output[6]

                c = int(cls)  # integer class
                id = int(id)  # integer id
                label = f"{id} {names[c]} {conf:.2f}"
                color = colors(c, True)
                annotator.box_label(bbox, label, color=color)

    # Stream results
    im0 = annotator.result()
    cv2.imshow(str(p), im0)
    if cv2.waitKey(1) == ord("q"):  # 1 millisecond
        exit()

    if save_vid:
        if not vid_writer:
            fps = vid_cap.get(cv2.CAP_PROP_FPS)
            w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            vid_writer = cv2.VideoWriter(
                save_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h)
            )

        vid_writer.write(im0)

if vid_writer:
    vid_writer.release()
cv2.destroyAllWindows()

