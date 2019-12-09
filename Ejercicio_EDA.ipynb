{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Ejemplo de EDA: Análisis Exploratorio de Datos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:02:37.412568Z",
     "start_time": "2019-12-08T22:02:37.407961Z"
    }
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import statsmodels.api as sm\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Carga de archivo csv desde una URL"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:02:38.571087Z",
     "start_time": "2019-12-08T22:02:37.416370Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  alpha_2 alpha_3      area           capital continent currency_code  \\\n",
      "0      AD     AND     468.0  Andorra la Vella        EU           EUR   \n",
      "1      AE     ARE   82880.0         Abu Dhabi        AS           AED   \n",
      "2      AF     AFG  647500.0             Kabul        AS           AFN   \n",
      "3      AG     ATG     443.0        St. John's       NaN           XCD   \n",
      "4      AI     AIA     102.0        The Valley       NaN           XCD   \n",
      "\n",
      "  currency_name eqivalent_fips_code fips  geoname_id          languages  \\\n",
      "0          Euro                 NaN   AN     3041565                 ca   \n",
      "1        Dirham                 NaN   AE      290557  ar-AE,fa,en,hi,ur   \n",
      "2       Afghani                 NaN   AF     1149361  fa-AF,ps,uz-AF,tk   \n",
      "3        Dollar                 NaN   AC     3576396              en-AG   \n",
      "4        Dollar                 NaN   AV     3573511              en-AI   \n",
      "\n",
      "                   name         neighbours  numeric   phone  population  \\\n",
      "0               Andorra              ES,FR       20     376       84000   \n",
      "1  United Arab Emirates              SA,OM      784     971     4975593   \n",
      "2           Afghanistan  TM,CN,IR,TJ,PK,UZ        4      93    29121286   \n",
      "3   Antigua and Barbuda                NaN       28  +1-268       86754   \n",
      "4              Anguilla                NaN      660  +1-264       13254   \n",
      "\n",
      "  postal_code_format postal_code_regex  tld  \n",
      "0              AD###  ^(?:AD)*(\\d{3})$  .ad  \n",
      "1                NaN               NaN  .ae  \n",
      "2                NaN               NaN  .af  \n",
      "3                NaN               NaN  .ag  \n",
      "4                NaN               NaN  .ai  \n"
     ]
    }
   ],
   "source": [
    "url = 'https://raw.githubusercontent.com/lorey/list-of-countries/master/csv/countries.csv'\n",
    "df = pd.read_csv(url, sep=\";\") #index_col=0\n",
    "print(df.head(5))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Conocer información básica"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T23:09:35.570049Z",
     "start_time": "2019-12-08T23:09:35.562245Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cantidad de Filas y columnas: (252, 19)\n",
      "Nombre columnas: Index(['alpha_2', 'alpha_3', 'area', 'capital', 'continent', 'currency_code',\n",
      "       'currency_name', 'eqivalent_fips_code', 'fips', 'geoname_id',\n",
      "       'languages', 'name', 'neighbours', 'numeric', 'phone', 'population',\n",
      "       'postal_code_format', 'postal_code_regex', 'tld'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print('Cantidad de Filas y columnas:',df.shape)\n",
    "print('Nombre columnas:',df.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:02:38.606905Z",
     "start_time": "2019-12-08T22:02:38.587047Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 252 entries, 0 to 251\n",
      "Data columns (total 19 columns):\n",
      "alpha_2                251 non-null object\n",
      "alpha_3                252 non-null object\n",
      "area                   252 non-null float64\n",
      "capital                246 non-null object\n",
      "continent              210 non-null object\n",
      "currency_code          251 non-null object\n",
      "currency_name          251 non-null object\n",
      "eqivalent_fips_code    1 non-null object\n",
      "fips                   249 non-null object\n",
      "geoname_id             252 non-null int64\n",
      "languages              249 non-null object\n",
      "name                   252 non-null object\n",
      "neighbours             165 non-null object\n",
      "numeric                252 non-null int64\n",
      "phone                  247 non-null object\n",
      "population             252 non-null int64\n",
      "postal_code_format     154 non-null object\n",
      "postal_code_regex      152 non-null object\n",
      "tld                    250 non-null object\n",
      "dtypes: float64(1), int64(3), object(15)\n",
      "memory usage: 37.5+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:02:38.666169Z",
     "start_time": "2019-12-08T22:02:38.613732Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>area</th>\n",
       "      <th>geoname_id</th>\n",
       "      <th>numeric</th>\n",
       "      <th>population</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>count</td>\n",
       "      <td>2.520000e+02</td>\n",
       "      <td>2.520000e+02</td>\n",
       "      <td>252.000000</td>\n",
       "      <td>2.520000e+02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>mean</td>\n",
       "      <td>5.952879e+05</td>\n",
       "      <td>2.427870e+06</td>\n",
       "      <td>434.309524</td>\n",
       "      <td>2.727679e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>std</td>\n",
       "      <td>1.904818e+06</td>\n",
       "      <td>1.632093e+06</td>\n",
       "      <td>254.663139</td>\n",
       "      <td>1.164127e+08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>min</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>4.951800e+04</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000e+00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>25%</td>\n",
       "      <td>1.098000e+03</td>\n",
       "      <td>1.163774e+06</td>\n",
       "      <td>217.000000</td>\n",
       "      <td>1.879528e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>50%</td>\n",
       "      <td>6.489450e+04</td>\n",
       "      <td>2.367967e+06</td>\n",
       "      <td>436.000000</td>\n",
       "      <td>4.268583e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>75%</td>\n",
       "      <td>3.622245e+05</td>\n",
       "      <td>3.478296e+06</td>\n",
       "      <td>652.500000</td>\n",
       "      <td>1.536688e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>max</td>\n",
       "      <td>1.710000e+07</td>\n",
       "      <td>8.505033e+06</td>\n",
       "      <td>894.000000</td>\n",
       "      <td>1.330044e+09</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               area    geoname_id     numeric    population\n",
       "count  2.520000e+02  2.520000e+02  252.000000  2.520000e+02\n",
       "mean   5.952879e+05  2.427870e+06  434.309524  2.727679e+07\n",
       "std    1.904818e+06  1.632093e+06  254.663139  1.164127e+08\n",
       "min    0.000000e+00  4.951800e+04    0.000000  0.000000e+00\n",
       "25%    1.098000e+03  1.163774e+06  217.000000  1.879528e+05\n",
       "50%    6.489450e+04  2.367967e+06  436.000000  4.268583e+06\n",
       "75%    3.622245e+05  3.478296e+06  652.500000  1.536688e+07\n",
       "max    1.710000e+07  8.505033e+06  894.000000  1.330044e+09"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Matriz de Correlación"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:08:56.919335Z",
     "start_time": "2019-12-08T22:08:49.847520Z"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAUYAAAEYCAYAAAAgU193AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAgAElEQVR4nO3deZhcZZn+8e+dhEU2BYKyb4qIosMSNtEBBZy4gRuyueDGTxSdwWXEZRBQ51J0ZEZEIKCCiIIiapQoKIuALKYBQQNGw6KJrNGwr0nfvz/e06S60t1VSVfqVHfuz3XV1VXnnDrnqXT6qXc/sk1ERCw2oe4AIiJ6TRJjRESTJMaIiCZJjBERTZIYIyKaJDFGRDRJYoyOkHSHpL2X8b0vlzS70zF1m6RTJP1X3XHE6CUxjhOSDpbUJ+lhSXdJ+oWkl9Ud11AkWdLzBl7bvsL21svhOptX17q+aftkSU9KuqPN8xwq6cpWx9l+v+3PLWO40UOSGMcBSR8B/hf4b+A5wKbAN4D9luFck9rZNsasLmnbhtcHA7d38gKSJnbyfFGvJMYxTtIzgeOAD9o+3/Yjtp+y/TPbH6+OWUXS/0q6s3r8r6RVqn17Spon6ROS7ga+PdS26tjXSfq9pPslXSXpJcPEtLOkq6vj7pL0dUkrV/surw67sSrdHjBwvYb3byPpsur9syTt27DvDEknSbpA0kOSrpX03Bb/TGcB72x4/Q7gO00xHyXp1uqcN0t640AswCnAblW89zfEcbKkGZIeAV5Rbft8tf8Tkq4Z+FKRdHj1WVZtEWv0Att5jOEHMBVYCEwa4ZjjgGuAZwPrAVcBn6v27Vm9/0vAKsAzhtm2A3AvsAswkZJo7gBWqc5zB7B39XxHYFdgErA5cAvwHw3xGHhew+s9gXnV85WAOcCngJWBVwIPAVtX+88A/gnsXJ3/bOCcYT735tW1NgfmVnFvA8wG9gbuaDh2f2BDSmHhAOARYINq36HAlU3nPgN4ANi9es+q1bbPV/snAJcDxwBbAQuA7ev+/5JHe4+UGMe+dYH5theOcMwhwHG277V9H3As8PaG/f3AZ20/YfuxYba9DzjV9rW2F9k+E3iCkgAHsX2d7WtsL7R9B3AqsEebn2dXYA3gi7aftH0J8HPgoIZjzrf9u+oznw1s1+Kc81icDN9JU2mxivmHtu+03W/7XOAvlOQ7kp/a/m31nsebztdPKZl+GJgOHG/7hhbnix6RxDj2/QOY3KIdcEPgrw2v/1ptG3Bf8x/2ENs2Az5aVW/vr6qUmzSdBwBJz5f0c0l3S3qQ0vY5uc3PsyEwt0osjfFu1PD67obnj1ISaSvfoZT8DgK+O0TM72hoJrgf2LaNmOeOtLP6UriUUmI9qY0Yo0ckMY59VwOPA28Y4Zg7KYltwKbVtgFDLbHUvG0u8AXbz2p4rGb7+0O892TgT8BWtteiVIvV4nM0xrqJpMb/m5sCf2/z/cP5EfBa4DbbjV8SSNoMOA04AljX9rOAPzbEPNwSVCMuTSXpNcBuwMXAl5c99Oi2JMYxzvYDwNHASZLeIGk1SStJerWk46vDvg98RtJ6kiZXxy9RamrhNOD9knZRsbqk10pac4hj1wQeBB6W9ALg8Kb99wBbDnOdaynte/9ZfY49gdcD5yxlvIPYfoTSXvneIXavTkly9wFIehelxNgY78YDHUjtqP6dv1ld753A66tEGWNAEuM4YPurwEeAz1D+uOdSSj8/qQ75PNAH3AT8Abi+2rY01+ijtDN+ndKRMIdSNR3KxyhDYh6iJNRzm/YfA5xZVVvf2nSdJ4F9gVcD8ynDjt5h+09LE+9wn8H2rUNsvxn4H0rp+x7gxcBvGw65BJgF3C1pfpuXm0Zpg5xh+x/Ae4DTJa07ms8Q3SE7C9VGRDRKiTEiokkSY0SMaZK+JeleSX8cZr8kfU3SHEk3Sdqh1TmTGCNirDuDMtFhOK+mDLLfCjiMMmpiREmMETGm2b6cMhtqOPsB33FxDfAsSRuMdM6xvjhAx6ypiV6PleoOY9TW2XFb5i54tO4wRm2TtVfj5lvuqzuMUXvhNuvR//RkorHrb3+9k/nzF7Q7FrWlf9HqfohFLY+7nSdmUcbpDphme9pSXm4jBg/Gn1dtu2u4NyQxVtZjJT4/aAz02HRwXx9Hnjv2Z56dcMD27LDLN+oOY9T6rv0ADz81q+4wRu1fd31r64OWwkMsauvv7RD+/LjtKaO83FAJfcThOEmMEdF1Aia1k31GWgGgffMo01cHbMzgmV9LSBtjRHSfYMKE1o8OmQ68o+qd3hV4wPaw1WhIiTEiaiA6l/gkfZ+ydN3kal3Pz1KWr8P2KcAM4DWU2VqPAu9qdc4kxoioxYQOdeXYPqjFfgMfXJpzJjFGRNdJbbYx1qSHQ4uIcUsdbUPsuCTGiOi6TrYxLg9JjBFRiyTGiIgGaWOMiBiC1LEZhh2XxBgR3ZfOl4iIwVKVjohokl7piIghJDFGRDRKG2NExGBpY4yIaCI6t4jE8pDEGBG1SFU6IqJBqtIREUsQE3q4Lp3EGBHdJ9DEJMaIiKcJUEqMy4ekCbb7644jIpaSYMJKvdv70vOJUdJzgLOBlYF7gU8AZwB3AzMlnQecDKwC3GD7SEkvBv4PWBW43vYRw5z7MOAwgMm9/08RMX5IKTGO0gJgqu2Fkr4KvBLYENjL9pOSfgh8wPatkk6UNAWYVe23pPMlbWX7L80ntj0NmAawpVYd8QbcEdFZaWMcnXWAUyStDWwAPADcaPvJav/WwDertd3WBC4GHgG+Kmk1YAtKIl0iMUZEPSTSKz1KhwAX2f5GVWL8K/Dihv2zgY/Z/qtKdpwInACcaHuGpPMpbb0R0SvSxjhqFwNnSfo3Sknwpqb9n6CUKFcB+oF3Az8DTpD0HkqijIieItTDU196PjHa/j2DS4hQOl8G9t8GvLpp/9+AFy3fyCJiWSnjGCMimggmTEqJMSKigVJijIho1Ou90r1blo2IcU0T1PLR1nmkqZJmS5oj6agh9m8q6VJJN0i6SdJrWp0zJcaI6L4ODdeRNBE4CdgHmEeZDTfd9s0Nh30G+IHtkyW9EJgBbD7SeZMYI6L71LE2xp2BOdXoFCSdA+wHNCZGA2tVz58J3NnqpEmMEdF1ZXWdtkqMkyX1NbyeVk3lHbARMLfh9Txgl6ZzHANcJOlDwOrA3q0umsQYEd2ntpcdm297yshnWkLzugcHAWfY/h9Ju1EmjGw70spcSYwR0XWSmNiZKYHzgE0aXm/MklXl9wBTAWxfLWlVYDJlta4hpVc6ImqhiWr5aMNMYCtJW0haGTgQmN50zN+AvQAkbUNZjvC+kU6aEmNEdF/7VekRVcsRHgFcSFkX4Vu2Z0k6DuizPR34KHCapCMp1exDbY+4zGASY0R0n0AdWl3H9gzKEJzGbUc3PL8Z2H1pzpnEGBE1EEzs3Za8JMaI6D4BPTwlMIkxImqRRSQiIhpJkBW8IyIWU4d6pZeXJMaIqEc6XyIiGkgdG66zPCQxVh7Zcktm/vfZdYcxagcDOx14YN1hjN4Bs9l46vPqjqIjXjH16rpDGLXZf3mksycU0MOdL2oxAHyFMWXKFPf19bU+MGIFtPpam/PIg3d0LJPtuMnavvojr2x53CofOf+6FotILBcpMVbmLniUI8+9oe4wRu2EA7bne9q67jBG7WDPZt/PXlR3GKM2/dhXsdNep9cdRu/p8RJjEmNEdJ+EVurdW74nMUZEPTJcJyKiQarSERHN2r8LYB2SGCOi+yYAK6eNMSLiaeVmWCkxRkQsJqWNMSJikA6u4L08JDFGRD3au690LZIYI6IGSmKMiBhEJDFGRAwiwaQM14mIGCwlxoiIRmljjIgYLG2MERFNJJjUu+mndyOLiPEtUwIjIpr0cFW6dyOLiPFLQhMntXy0dypNlTRb0hxJRw1zzFsl3SxplqTvtTpnSowRUYPO9EpLmgicBOwDzANmSppu++aGY7YCPgnsbnuBpGe3Ou+4KjFKOlTSbk3bVpV0WU0hRcRQBnqlWz1a2xmYY/s2208C5wD7NR3zPuAk2wsAbN/b6qTjqsRo+4y6Y4iINrXX+TJZUuN9jafZntbweiNgbsPrecAuTed4PoCk3wITgWNs/3Kki7ZMjJImUbLws4BbgDWr15+uLnKi7e9LeglwMuW74ALbX5B0DLAVsA6wOjAVeBz4JbAy8BTwZtsPSroFuA7YDvgCJeu/EPiQ7d9Imtp8zSFiPQbos/1zSScB2wLXtPqMEdFl7Q/Xmd/ivtJDZVc3vZ5EyUN7AhsDV0ja1vb9w520nbLqG4E/294buLF6z9HAXsDLgPdX9fz/Bt4L7A68QtLm1ftn2341cAWwt+1+YD/bewI/Aw6ojlsfeD8lIf4PcCjwduD/SRrumkOSNAVY2/YewK9HOO4wSX2S+h57cEEb/xQR0TGdqUrPAzZpeL0xcOcQx/zU9lO2bwdmUxLl8KG1ceHnUkpyADOBydVJLwIuqV6vBzzH9i22DfRV7wMYuIv9XGBtSasDp0m6nJJIN6z232b7YeDvwF9sP149X3uEaw7neQ0x/264g2xPsz3F9pRnrLV2y3+IiOgQqVOJcSawlaQtJK0MHAhMbzrmJ8ArymU1mVK1vm2kk7Zz5VuB7avnOwLzKVXqfapS33a27wbukbSNJAFTqvfB4GKtKNXpO23/K3A6i4vCjcc1v2e4aw5nTkPMIxXDI6IOoqyu0+rRgu2FwBHAhZQc8QPbsyQdJ2nf6rALgX9Iuhm4FPi47X+MdN52Kvk/AQ6SdDEl4TxBaQP8taR+4D7grZT2v9Mpyfbntu8oOXIJ1wCflnQBcBelmDsi2/2ShrrmcMf3SXqwKpVe28ZnjIiu6twiErZnADOath3d8NzAR6pHW1omRttPSTqg+vleYF3bF1KycONxN1LaFxu3HdPw/JSGXTsMcZ0p1c/HKY2k2J5PKWEy1DWHOEfj9T7Q6rNFRI16eOZLu8N1fippDUpp8YBWB3eDpAOAwxs23W37wLriiYiloHGw7Jjt1yzvQJaW7XOBc+uOIyKW0YTeHUbdu5FFxPg1HkqMEREdN3TnbE9IYoyIeiglxoiIxSRoc1mxOvRuZBExjiklxoiIJSQxRkQ0EkxoPeWvLkmMEdF9uX1qREQzoVSlIyKaJDFGRDRQ2hgjIpaUNsaIiCapSkdENFAGeEdENMmUwIiIJaXEGBHRQGTZsbHgobsf4TdfvbruMEbvgO055+gT645i1A4GDjzuQ3WHMXrHzmalZ65SdxSjpomdTmLq6RW8VW6gFVOmTHFfX1/dYUT0pDXW3oKHF9zesew4ZcrWntk3reVxE7TndQM3yuum3k3ZXXbzLfexwy7fqDuMUbv+2g+w72cvqjuMUZt+7Kv4nrauO4xRO9izeembzqo7jB4k7LQxRkQMYjLzJSLiaUb0u3fTT+9GFhHjmOhPVToiYrBUpSMiGti9XZXu3bJsRIxr/Uxo+WiHpKmSZkuaI+moEY57iyRLajn8p3dTdkSMY50ZriNpInASsA8wD5gpabrtm5uOWxP4MHBtO+dNiTEius6UNsZWjzbsDMyxfZvtJ4FzgP2GOO5zwPHA4+2cNIkxImpQ2hhbPYDJkvoaHoc1nWgjYG7D63nVtsVXkrYHNrH983ajS1U6IrrO7Q/Xmd9iSuBQ0xSfnuescsetE4BDlya+JMaIqEWHhuvMAzZpeL0xcGfD6zWBbYHLVFbzWR+YLmlf28MujpDEGBE16Nhc6ZnAVpK2AP4OHEhZnAkA2w8Ak5++qnQZ8LGRkiIkMUZEHUxHxjHaXijpCOBCYCLwLduzJB0H9NmeviznTWKMiK4zor9DM19szwBmNG07ephj92znnEmMEVGLLDsWETFIb08J7N3IImLc6mRVenlIYoyIWqQqHRExiHAPT7xLYoyIrrNhYX/v3oivd1P2MpJ0VDXYMyJ6lul360ddxlWJUdIE21+sO46IGJmBHi4wdicxStoTOAp4AtgceBvw7YHJ4ZKusb2rpGOA5wPrVsdeCOwLPGL7TZJWBU4HNgQers6zDnAWcDdlLbYXAl8BZgFfB14C9ANvtP3PbnzeiGitzhJhK92sSq9kez/gY8C7Rjhulu1/Ax4AJlXPJen5wHuBS2y/EjgTGFiCaEPgENvHN5xnX2Ch7Zfb3gO4v/lCkg4bWM5o4cKHR/0BI6I9NjzV75aPunSzKv376udcYO2mfY1LB91U/fx70/O1gRcCO0l6B7AScEW1/8ZqkcpGL2jYj+3+5oBsTwOmAay2+ma9+/UVMc6UqnTv/sl1MzE2/isIWCRprer1VsMc1/yePwFX2z4LQNJKlEUpl0h6wC3AK4DzqmNl9/BvImIF08ttjHX2Sn8duBw4mcHrp41kGrCPpEskXQK8aoRjfwasKunK6th1RhVtRHTMwHCdVo+6dKXEaPsy4LLq+Z9YvJruWU3HHdPw/KiG50c0HPaOIS7xloZjD23YfvgyBRwRy1m9w3FaGVfDdSJibEgbY0TEEHq5jTGJMSK6rtenBCYxRkQtUpWOiGjgdL5ERAxmqHVmSytJjBHRfU7nS0TEElKVjohokHGMERFNTIbrREQMZugfaumXHpHEGBE1MP0pMUZELJY2xoiIJjY8tbB369Lj7i6BETE2dOougZKmSpotaY6ko4bY/xFJN0u6SdLFkjZrdc4kxojoOru0MbZ6tCJpInAS8GrKrU8Oqm6I1+gGYIrtl1BW9D+eFpIYI6LrbFi4sL/low07A3Ns31bd9+kcYL/B1/Klth+tXl4DbNzqpGljjIhatFlVniypr+H1tOomdgM2otxgb8A8YJcRzvce4BetLprEGBFdZ2BRe8N15g/cf34YGmLbkCeW9DZgCrBHq4smMUZE97lj4xjnAZs0vN6YIW6uJ2lv4NPAHrafaHXSJMbKC7dZj75rP1B3GB0x/diRbp44dhzs2XWH0BFXnf/2ukMYtS31vo6ez8DCRR0ZrjMT2ErSFpT7zx8IHNx4gKTtgVOBqbbvbeekSYyVfj/Gw0/NqjuMUVtjpRex016n1x3GqM28+L289E1ntT6wx111/tv5nrauO4zeYzpSYrS9UNIRwIXAROBbtmdJOg7osz0d+DKwBvBDSQB/s73vSOdNYoyIrjOdSYwAtmcAM5q2Hd3wfO+lPWcSY0R0nW2eWpQpgRERg2QRiYiIJkmMEREN7KyuExExiHFPr66TxBgR3deh4TrLSxJjRHRdFqqNiBhCSowREQ1st7usWC2SGCOi+wz9GeAdETGYe/j+qUmMEdF1qUpHRDRxhutERCwpbYwREY1SYoyIGMyYRQsX1R3GsJIYI6L7UmKMiBjMpI0xImKwHi8xTqg7gEaS9pT0lRH2Hypp5Ybnu3UvuojoFNssWtjf8lGXsVZiPBQ4D3jS9hn1hhIRozFuS4xVCe+C6vE7SVtJ+pikqyVdJWnH6rjrJZ1UHfPBatsZkratnn9R0p5N5/6KpMuq92xXlQ63A34h6d8lHSPpddWxJ0i6sjp+i2rbLZLOlnSDpLF/Y9+IccTVXOlWj7p0osT4TODlwG7AicBqwO7A5sA0YG9gbeD/gNuAayR9u43zHm37UUkvAT5h+xBJvwdeZ/thSccASNoJ2MD2yyTtARwNvAtYHzgc6Ad+BSxxk2JJhwGHAWyy6QbL9ukjYqkZs7CHh+t0oo3xBtsGrgP2Am603W/7NkrSBHjY9p9tLwT+AmxA6ZgaoCHO+1FJVwJfBzYc4frPBWZWz68Fnlc9v832g7YfHub82J5me4rtKZMnr936k0ZEZ1SdL60edelEYtxOkoDtgYur1xMkbQncXx2zRlXNnkhJZHcBC4BNqv07NJ5Q0rrA6ygl0SNYnNieAiY2XX8OsFP1fBdK4oXBiTciekwvJ8ZOVKUfAi4AJgOHAPsBv6Ukpg9VxywAPkpJgGdWVeQzgLMkHU5JeI0WAPcAlwJXNWyfDvxA0g8GNtjuk3RXVbpcSKlGR0QPs8HjfBzjzbY/1vD6K9WjUb/t9zdusH0T8C9DnO+y6ue+zTtsn0hpx2zefuQQ26Y0PN91uOAjogY9vuxYT41jjIgVgykL1bZ6tEPSVEmzJc2RdNQQ+1eRdG61/1pJm7c656hKjLYvY3EJb6TjprQ6JiJWIB2qSlf9FicB+wDzgJmSptu+ueGw9wALbD9P0oHAl4ADRjpvSowR0X02/U/1t3y0YWdgju3bbD8JnEPp52i0H3Bm9fw8YK+qw3hYSYwRUQv3u+WjDRsBcxtez6u2DXlMNWTwAWDdkU461qYERsR4YGBRWyXCyZL6Gl5Psz2t4fVQJb/mjNrOMYMkMUZE15m2S4TzW/RRzGPxeGiAjYE7hzlmnqRJlIkn/xzpoqlKR0T3mU61Mc4EtpK0RbXy1oGU8c6NpgPvrJ6/Bbikmq03rJQYI6IeHbivtO2Fko4ALqTMivuW7VmSjgP6bE8HvkmZTDKHUlI8sNV5kxgjovvsjs18sT0DmNG07eiG548D+y/NOZMYI6IWbbYx1iKJMSK6zlUbY69KYoyI7rPbHa5TiyTGiOg+pyodETFYqtIREYOZzvVKLw9JjBHRfaYj4xiXlyTGiKhFSowREY2qZcd6VRJjRHRfqtIREUvq5aq0WiwyscKQdB/w1+V8mcnA/OV8jW7I5+gt3fgcm9ler1Mnk/RLStytzLc9tVPXbVcSYxdJ6hsP97/J5+gt4+Vz9JKsxxgR0SSJMSKiSRJjd01rfciYkM/RW8bL5+gZaWOMiGiSEmNERJMkxoiIJkmMERFNkhhjCZK2qn4OdaPyMUNS/n/HMsl/nA6StFLdMYyWpBcBP5L0Mtseq8lR0kTb/ZLWl7Rz3fEsK0kT645hRZTE2CGSNgS+JukISevXHc+ykDTJ9izgI8AxknYaq8nR9iJJzwbOB15cdzzLQtKE6nNI0l6Stqs7phVFEmMHSFoX+DFwMfAy4AuSthlrCaW6eflEYGfgduBLknYfK8mxSiDbNZSy3glcavubdca1rKoSr4DvAIcAp0p6S81hrRCSGDtjLeAo4BJgA2B14AjgBXUG1S5JW0tauXp5NLCO7fcBJ1BKji/12Bjw+kJgXcqiVgAzgUWSNgCQ9EZJu9YV3NJo+CL6LnC/7XcD7wU+KOmA+iJbMSQxjoKktSVtD9wNXAH8B/A5SkJ5NnBfjeG1pYp/M9tPVptuASxpFds/A/4IfFHSWr1caqyqnbOA3wHHSdoXuB94Eni3pE8BnwL+WWOYLQ2Udhu+iH4NvFnSNrb/AHwcOFLSc3r59zHWZebLMpK0MXAqMAd4DDgP2AvYFHgpsL/tOfVFuHQkvZ2SSO4A9qas1Xk98BbgFNs31hfdyCSpqu4/G3gX8DiwLaW09TCwDuV3cnYv/06q5N5f9aYfBdxK+cLdFvgMcITtmyStafuhOmMd75IYl5GkzwA3URLJOcC/AitTqtL32f5bfdEtPUnvBjYE+oBHgJcArwROtX1RnbG1Q9IawA+AH9n+pqR9gP2Bn9ueXm90rUla2faTVSnwTOAhSlPAQBX6JcAngD2BJ2wvrCvWFUES41KStB6wE7Al8AxgD8q3+drAVsBpY6Q9bgmSDqR8rhts/0LS6rYfqTuu4QyUsKrnqwInAusDb6w6kl4NvA74hO2Hawx1RFWct9meLWlT4CTgDVWP9L7ADraPkbSR7b/XG+2KIW2MS6FKiidS2g6vBA6ufj6TkhyvHItJcaCtyvY5wFzgZZLWHQtJUdIGkg6lDMk5hvL7+LKklWz/Avh4LyfFytwqKe5AaQP9LfC+at8jwCbV7+iuugJc0aTE2Kaq3ec1wCnAC2w/LGl3StvVZOBM2zfXGWMr1aDnRdXzVWw/0bBPA0ld0jq2e7qTAkDSc4BvAxdR2nbvBk4HPglg++ONn6vXSNrS9m3V84OAHYFfARMp7YpTgPWAr9i+oLZAV0BJjG2ohnt8GrgQeBulQf+Ttu+tNbBlUCX4EygdFJcP/MFVJRJVpbDXA/fY/l2NoQ6robPlYEqb7vmUjpb3AX+nJBbZ/keNYY6o6n0+EliVMoJhBrAGZYjXTOBGYCPgSdt/6OUEPx6lKt1CNYvlPGA28Abgb5Sq9ImS1q4ztmV0KuWz/AY4XdImAzuqpPgmyh9szyUVLZ77vEr184+UDqPvAx+gtPN+jpJMei7+AQMzWigLzL4V2N32L22fRxkutQewne3rqiE6JCl2VxJjaxsCXwLOBv6F0rj/V8p/4FVrjKstDclkYC73PyntcPsDHyqb9eKqBLY/ZWD6+23fWkvAw6hKTP3VF9X3Jf0nsIgyTvEqYDdKG+OpvdymqMVzuCdRep7fDvyhGuUAcDnli/cvdcUYqUq3pZoVcjrwLWBNFvd03l9rYC00dFAI2By4E3gzcBrwUeBc4EfAccANlMHD37X9p3oiHlrD51gNOIzSIbEFcC9wDWXM5SbAzF4epzig+rI6D7iOUjKfRin13kNpGviU7STGGiUxtknSfwDbUBrF39FrJapmTUnxl5QksgolCU6hDEZfGzi5oZ1xNduP1hXzUBo+x/rAF4GFwBcoTRr/SRkydZrtuTWG2ZKknQfabCV9E/gTpdPoLEr8J0p6DXCv7b4aQw2SGNtWzarYAbi117/Nm8b37QTsafvLkt5KGWJ0pO3bJU22Pb/x+F5UteV+jdIpsTllgYvvUqqiHwbOst2z0y8lbU1pt73U9rmSplJmtPwIuIBSA7nS9udqDDMaJDGOM00lxZ9Rep+fD+xm+5Fq6t/bKG2MD/Vqo37T5/gksB1lBsgqwOGUaZin215QY5htqQaf7wpMBa61/WNJr6XMLDqKsnDHDNtX1xhmNEjnyzjTUPL7DvAr22+htGedJulZts8CDrX9YK8mRXi6h3wyZSrc6ZR5w2+hJMRplHbFMcH245RhRL8AdpL0RspiF1Mo89EvTVLsLSkxjhONg7er1xcBj9vet3p9LLA98Eagv1eTYlMzwEuBM4CDKB1HH6DM/jgTeKyXq/+Nqpk5kynjYNcB/o3SLPALYFPbf64vuhhKSozjwEBSlDRB0j7VHHAnv0AAAASzSURBVOdXAfMlnQJg+7OUtsVFvZoUYXFJUdL6tq+i9EJ/nTIP/RuU9RYnjZWkWLmAMrRrN0on2MCCxmsmKfamlBjHiWoIyPco4/ruAq6w/XNJZ1LGBx/ay7MnGtoUJ1HaQI8AXmv7Hkl7U5LL9sCf3cMryzRNrfwk8DfbZ1fz7I+lLO32PeDOsTDtckWVEuMYN7AABGVJqusp4xNfARwg6WDb7wS+Ar07e6IhKW5IqV5OogzePr0au/gEZcrcYz2eFCc0/Rv/EthL0n5Vr/lPgF2AB5MUe1tKjGPUEG2KoiSU71LWJVwTeDnwadt31xNl+6ohOSdRbg/RB+xH6WzpAzYDDrc9u74IR9bQnCFKu+gqlDGKDwOHUkrxU4F/t31FXXFGe8ZMz14spsV3j5tAWV2mD7iaUmK8HXgOZSjIF8dIUhQlib+AspLM7yU9QWlPnAt82D2+YnVDUjya8vv4FfBZSrX5o8DWlEVzr6ovymhXSoxjVPVHeDzwFKXHdk3g95QvuzcDP7A9o74Il46kZwAHUOajf9f2dZK2ARb0cnJv6kX/V+CnlNta/FrSZpTS4yG276wxzFhKaWMcQxraE6EMdt6KUmI8iXKLhRcDDwLvtj2j6fieZvsxShPAVcD/k7Sd7Vt6PCkOLAghSRvYvpxym9Mvqyw6C9USaPVFGcsiVekxQoMXmX0GZZ7tJpSOlgcoDfv7A/MGSjC92tkyHNuPSppB6Xjp+dWqG5ozLgRuk7QtZU3IT1MG1V9JaVPM7QjGmFSlx5Dqj/BUyuIPP6YkxB0oK7T8AJg/1pLhUHp5WBEs8SV1KPAil9XCXwl8mTKA++WUtsX9bd/V658pBktVemz5MiUZfhR4EWUWxbmUNSNXHS9/eL38ORo6viTpRZT1OdeT9AzblwA/BJ5r+8eUXulvV8vWxRiSEmMPa171RtLHKIsQXFGt9nMWZTD0Q9V83OiCqu32HMoSaBMoq+NMo1Spv0ZZlm5gibG1bD9YV6yxbNLG2KOaVpfZlbL+YB9wvKT3AitRGvbX6OUlt8apzwIP236Pyv2sf0zpCHsK+KDt3zV8qfX0MKMYWhJjD6raowaS4m+AS4F9KdPkTgb+nXIDpRNt315fpCueagmxu4GXS3qp7ask/YRyK4JfDTQDjNUOsChSle4xTePidgT2sP1VSdcDnxkYm1i1aT2WRv3uk7QK8CbKeNHLKKv//FfVxhjjQBJjD2maVvZflKlwm1Haso6nVKc/T1mo9YExtsLMuFINmToYeD0w3fa38iU1fqQq3UMaxsV9lfK7eZBy06cHgQWUzpZjPQZWrR7vqtL69ym/m1dIutH2dXXHFZ2RxNh7jgJWs31YVZWeSBnIvQXlzoSX1xpdPK1pQPq8uuOJzsk4xt5zFXCnpHWqEsjdlFLJItuXj6VpfisC248AP7Z9T92xROekxNh7ZgF7AAdKegDYkdIrvQGkl7MX5Xcy/qTE2GOqMYmnU9oUX0OpWt8L7CNppZQYI5a/9Er3sKojZndKj/S7bd9Sc0gRK4Qkxh4naVNgJdu31h1LxIoiiTEioknaGCMimiQxRkQ0SWKMiGiSxBgR0SSJMSKiyf8HigXwmKRawpwAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "corr = df.set_index('alpha_3').corr()\n",
    "sm.graphics.plot_corr(corr, xnames=list(corr.columns))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Cargar una segunda fuente de datos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:02:39.201638Z",
     "start_time": "2019-12-08T22:02:38.669191Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       country  year  population\n",
      "0  Afghanistan  1952     8425333\n",
      "1  Afghanistan  1957     9240934\n",
      "2  Afghanistan  1962    10267083\n",
      "3  Afghanistan  1967    11537966\n",
      "4  Afghanistan  1972    13079460\n"
     ]
    }
   ],
   "source": [
    "url = 'https://raw.githubusercontent.com/DrueStaples/Population_Growth/master/countries.csv'\n",
    "df_pop = pd.read_csv(url)\n",
    "print(df_pop.head(5))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Aqui vemos la población año tras año de España"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:02:39.223694Z",
     "start_time": "2019-12-08T22:02:39.204902Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>year</th>\n",
       "      <th>population</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>1416</td>\n",
       "      <td>Spain</td>\n",
       "      <td>1952</td>\n",
       "      <td>28549870</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1417</td>\n",
       "      <td>Spain</td>\n",
       "      <td>1957</td>\n",
       "      <td>29841614</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1418</td>\n",
       "      <td>Spain</td>\n",
       "      <td>1962</td>\n",
       "      <td>31158061</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1419</td>\n",
       "      <td>Spain</td>\n",
       "      <td>1967</td>\n",
       "      <td>32850275</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1420</td>\n",
       "      <td>Spain</td>\n",
       "      <td>1972</td>\n",
       "      <td>34513161</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     country  year  population\n",
       "1416   Spain  1952    28549870\n",
       "1417   Spain  1957    29841614\n",
       "1418   Spain  1962    31158061\n",
       "1419   Spain  1967    32850275\n",
       "1420   Spain  1972    34513161"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_pop_es = df_pop[df_pop[\"country\"] == 'Spain' ]\n",
    "df_pop_es.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:02:39.242255Z",
     "start_time": "2019-12-08T22:02:39.233781Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(12, 3)"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_pop_es.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Visualicemos datos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:02:39.496444Z",
     "start_time": "2019-12-08T22:02:39.249756Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x12091aef0>"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_pop_es.drop(['country'],axis=1)['population'].plot(kind='bar')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:02:39.520411Z",
     "start_time": "2019-12-08T22:02:39.499275Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>year</th>\n",
       "      <th>population</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>48</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>1952</td>\n",
       "      <td>17876956</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>49</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>1957</td>\n",
       "      <td>19610538</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>50</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>1962</td>\n",
       "      <td>21283783</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>51</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>1967</td>\n",
       "      <td>22934225</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>52</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>1972</td>\n",
       "      <td>24779799</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      country  year  population\n",
       "48  Argentina  1952    17876956\n",
       "49  Argentina  1957    19610538\n",
       "50  Argentina  1962    21283783\n",
       "51  Argentina  1967    22934225\n",
       "52  Argentina  1972    24779799"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_pop_ar = df_pop[(df_pop[\"country\"] == 'Argentina')]\n",
    "df_pop_ar.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:02:39.549547Z",
     "start_time": "2019-12-08T22:02:39.523476Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(12, 3)"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_pop_ar.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:02:39.807622Z",
     "start_time": "2019-12-08T22:02:39.552783Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x123026c50>"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXQAAAEhCAYAAABvIFsXAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAat0lEQVR4nO3dfZhU5Z3m8e8tEDEimoXWsIC2mWDUKIJpUceo+DI7qIxkV0k0o4IaiTEOmszORLO7vmWTMfuHTFwTXWb1CrIGieRFxmiMUYk6vjYICKIj4xDtaLQDijJGtOG3f5wDU5bV3dVwqrrq4f5cV1196pyn6vecKrj76VPPOaWIwMzMmt9O/d0BMzMrhgPdzCwRDnQzs0Q40M3MEuFANzNLhAPdzCwR/Rrokm6R9LqkFVW0nSVpaX77Z0lv1qOPZmbNQv05D13SMcAG4NaIOKgPj/srYHxEnFezzpmZNZl+HaFHxEPAutJ1kv5E0i8lLZb0sKT9Kzz0TGBeXTppZtYkBvZ3ByqYDVwYES9IOhz4AXD8lo2S9gH2BR7op/6ZmTWkhgp0SUOAPwXukLRl9c5lzc4AFkTEpnr2zcys0TVUoJMdAnozIsb10OYM4Kt16o+ZWdNoqGmLEfEW8K+SpgIoc8iW7ZI+BXwMeKyfumhm1rD6e9riPLJw/pSkDknnA38JnC9pGbASmFLykDOB28OXiDQz+5B+nbZoZmbFaahDLmZmtu0c6GZmiei3WS7Dhw+P1tbW/ipvZtaUFi9e/IeIaKm0rd8CvbW1lfb29v4qb2bWlCT9trttPuRiZpYIB7qZWSIc6GZmiWioU//ff/99Ojo6ePfdd/u7K0kaPHgwo0aNYtCgQf3dFTOrgYYK9I6ODnbbbTdaW1spuTiXFSAiWLt2LR0dHey777793R0zq4GGOuTy7rvvMmzYMId5DUhi2LBh/uvHLGFVB7qkAZKelnRXhW07S5ovabWkJyS1bmuHHOa149fWLG19GaFfAqzqZtv5wBsR8UlgFvDd7e1YqtasWcNBB/X8bXtr1qzhRz/60db77e3tzJw5s9ZdM7MmV9UxdEmjgFOAbwNfr9BkCnBVvrwAuEGStveqiK2X/WJ7Hv4ha649pdDnq5Utgf7FL34RgLa2Ntra2vq5V2bWV9uaYduaVdWO0P8e+FtgczfbRwIvA0REF7AeGLZNPepna9asYf/992fatGmMHTuW008/nXfeeYf777+f8ePHc/DBB3PeeeexceNGIDvj9Rvf+AYTJkxgwoQJrF69GoDp06ezYMGCrc87ZMiQirWOPvpoDj30UA499FAeffRRAC677DIefvhhxo0bx6xZs1i0aBGTJ08GYN26dXzuc59j7NixHHHEESxfvhyAq666ivPOO4+JEyfyiU98guuvv76mr5OZNZ5eA13SZOD1iFjcU7MK6z40Opc0Q1K7pPbOzs4+dLO+nn/+eWbMmMHy5csZOnQo1113HdOnT2f+/Pk888wzdHV1ceONN25tP3ToUJ588kkuvvhiLr300qrr7Lnnntx3330sWbKE+fPnbz2scu2113L00UezdOlSvva1r33gMVdeeSXjx49n+fLlfOc73+Gcc87Zuu25557j3nvv5cknn+Tqq6/m/fff385XwsyaSTUj9KOAUyWtAW4Hjpf0/8radACjASQNBHYH1pU/UUTMjoi2iGhraal4bZmGMHr0aI466igAzjrrLO6//3723Xdf9ttvPwCmTZvGQw89tLX9mWeeufXnY49V/2VK77//PhdccAEHH3wwU6dO5dlnn+31MY888ghnn302AMcffzxr165l/fr1AJxyyinsvPPODB8+nD333JPXXnut6r6YWfPr9Rh6RFwOXA4gaSLwXyPirLJmC4FpZN8+dDrwQDN/q1BfZ4OUtt+yPHDgQDZvzo5QRQTvvffehx43a9Ys9tprL5YtW8bmzZsZPHhwr7Uqvaxbau68879/n/aAAQPo6urq036YWXPb5nnokq6RdGp+92ZgmKTVZB+aXlZE5/rLSy+9tHWkPW/ePE488UTWrFmz9fj43LlzOfbYY7e2nz9//tafRx55JJAdW1+8ODtKdeedd1Y8/LF+/XpGjBjBTjvtxNy5c9m0aRMAu+22G2+//XbFvh1zzDHcdtttACxatIjhw4czdOjQInbbzJpcn84UjYhFwKJ8+YqS9e8CU4vsWH864IADmDNnDl/+8pcZM2YM3/ve9zjiiCOYOnUqXV1dHHbYYVx44YVb22/cuJHDDz+czZs3M2/ePAAuuOACpkyZwoQJEzjhhBPYddddP1Tnoosu4rTTTuOOO+7guOOO29pm7NixDBw4kEMOOYTp06czfvz4rY+56qqrOPfccxk7diwf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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_pop_ar.set_index('year').plot(kind='bar')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Comparativa entre 2 países"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:02:40.139905Z",
     "start_time": "2019-12-08T22:02:39.810381Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x11ef1d780>"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "anios = df_pop_es['year'].unique()\n",
    "pop_ar = df_pop_ar['population'].values\n",
    "pop_es = df_pop_es['population'].values\n",
    "\n",
    "df_plot = pd.DataFrame({'Argentina': pop_ar,\n",
    "                    'Spain': pop_es}, \n",
    "                       index=anios)\n",
    "df_plot.plot(kind='bar')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Filtremos paises hispano-hablantes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:02:40.199235Z",
     "start_time": "2019-12-08T22:02:40.142691Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>alpha_2</th>\n",
       "      <th>alpha_3</th>\n",
       "      <th>area</th>\n",
       "      <th>capital</th>\n",
       "      <th>continent</th>\n",
       "      <th>currency_code</th>\n",
       "      <th>currency_name</th>\n",
       "      <th>eqivalent_fips_code</th>\n",
       "      <th>fips</th>\n",
       "      <th>geoname_id</th>\n",
       "      <th>languages</th>\n",
       "      <th>name</th>\n",
       "      <th>neighbours</th>\n",
       "      <th>numeric</th>\n",
       "      <th>phone</th>\n",
       "      <th>population</th>\n",
       "      <th>postal_code_format</th>\n",
       "      <th>postal_code_regex</th>\n",
       "      <th>tld</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>9</td>\n",
       "      <td>AR</td>\n",
       "      <td>ARG</td>\n",
       "      <td>2766890.0</td>\n",
       "      <td>Buenos Aires</td>\n",
       "      <td>SA</td>\n",
       "      <td>ARS</td>\n",
       "      <td>Peso</td>\n",
       "      <td></td>\n",
       "      <td>AR</td>\n",
       "      <td>3865483</td>\n",
       "      <td>es-AR,en,it,de,fr,gn</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>CL,BO,UY,PY,BR</td>\n",
       "      <td>32</td>\n",
       "      <td>54</td>\n",
       "      <td>41343201</td>\n",
       "      <td>@####@@@</td>\n",
       "      <td>^[A-Z]?\\d{4}[A-Z]{0,3}$</td>\n",
       "      <td>.ar</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>13</td>\n",
       "      <td>AW</td>\n",
       "      <td>ABW</td>\n",
       "      <td>193.0</td>\n",
       "      <td>Oranjestad</td>\n",
       "      <td></td>\n",
       "      <td>AWG</td>\n",
       "      <td>Guilder</td>\n",
       "      <td></td>\n",
       "      <td>AA</td>\n",
       "      <td>3577279</td>\n",
       "      <td>nl-AW,es,en</td>\n",
       "      <td>Aruba</td>\n",
       "      <td></td>\n",
       "      <td>533</td>\n",
       "      <td>297</td>\n",
       "      <td>71566</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td>.aw</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>28</td>\n",
       "      <td>BO</td>\n",
       "      <td>BOL</td>\n",
       "      <td>1098580.0</td>\n",
       "      <td>Sucre</td>\n",
       "      <td>SA</td>\n",
       "      <td>BOB</td>\n",
       "      <td>Boliviano</td>\n",
       "      <td></td>\n",
       "      <td>BL</td>\n",
       "      <td>3923057</td>\n",
       "      <td>es-BO,qu,ay</td>\n",
       "      <td>Bolivia</td>\n",
       "      <td>PE,CL,PY,BR,AR</td>\n",
       "      <td>68</td>\n",
       "      <td>591</td>\n",
       "      <td>9947418</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td>.bo</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>30</td>\n",
       "      <td>BR</td>\n",
       "      <td>BRA</td>\n",
       "      <td>8511965.0</td>\n",
       "      <td>Brasilia</td>\n",
       "      <td>SA</td>\n",
       "      <td>BRL</td>\n",
       "      <td>Real</td>\n",
       "      <td></td>\n",
       "      <td>BR</td>\n",
       "      <td>3469034</td>\n",
       "      <td>pt-BR,es,en,fr</td>\n",
       "      <td>Brazil</td>\n",
       "      <td>SR,PE,BO,UY,GY,PY,GF,VE,CO,AR</td>\n",
       "      <td>76</td>\n",
       "      <td>55</td>\n",
       "      <td>201103330</td>\n",
       "      <td>#####-###</td>\n",
       "      <td>^\\d{5}-\\d{3}$</td>\n",
       "      <td>.br</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>36</td>\n",
       "      <td>BZ</td>\n",
       "      <td>BLZ</td>\n",
       "      <td>22966.0</td>\n",
       "      <td>Belmopan</td>\n",
       "      <td></td>\n",
       "      <td>BZD</td>\n",
       "      <td>Dollar</td>\n",
       "      <td></td>\n",
       "      <td>BH</td>\n",
       "      <td>3582678</td>\n",
       "      <td>en-BZ,es</td>\n",
       "      <td>Belize</td>\n",
       "      <td>GT,MX</td>\n",
       "      <td>84</td>\n",
       "      <td>501</td>\n",
       "      <td>314522</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td>.bz</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>45</td>\n",
       "      <td>CL</td>\n",
       "      <td>CHL</td>\n",
       "      <td>756950.0</td>\n",
       "      <td>Santiago</td>\n",
       "      <td>SA</td>\n",
       "      <td>CLP</td>\n",
       "      <td>Peso</td>\n",
       "      <td></td>\n",
       "      <td>CI</td>\n",
       "      <td>3895114</td>\n",
       "      <td>es-CL</td>\n",
       "      <td>Chile</td>\n",
       "      <td>PE,BO,AR</td>\n",
       "      <td>152</td>\n",
       "      <td>56</td>\n",
       "      <td>16746491</td>\n",
       "      <td>#######</td>\n",
       "      <td>^(\\d{7})$</td>\n",
       "      <td>.cl</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>48</td>\n",
       "      <td>CO</td>\n",
       "      <td>COL</td>\n",
       "      <td>1138910.0</td>\n",
       "      <td>Bogota</td>\n",
       "      <td>SA</td>\n",
       "      <td>COP</td>\n",
       "      <td>Peso</td>\n",
       "      <td></td>\n",
       "      <td>CO</td>\n",
       "      <td>3686110</td>\n",
       "      <td>es-CO</td>\n",
       "      <td>Colombia</td>\n",
       "      <td>EC,PE,PA,BR,VE</td>\n",
       "      <td>170</td>\n",
       "      <td>57</td>\n",
       "      <td>47790000</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td>.co</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>49</td>\n",
       "      <td>CR</td>\n",
       "      <td>CRI</td>\n",
       "      <td>51100.0</td>\n",
       "      <td>San Jose</td>\n",
       "      <td></td>\n",
       "      <td>CRC</td>\n",
       "      <td>Colon</td>\n",
       "      <td></td>\n",
       "      <td>CS</td>\n",
       "      <td>3624060</td>\n",
       "      <td>es-CR,en</td>\n",
       "      <td>Costa Rica</td>\n",
       "      <td>PA,NI</td>\n",
       "      <td>188</td>\n",
       "      <td>506</td>\n",
       "      <td>4516220</td>\n",
       "      <td>####</td>\n",
       "      <td>^(\\d{4})$</td>\n",
       "      <td>.cr</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>50</td>\n",
       "      <td>CU</td>\n",
       "      <td>CUB</td>\n",
       "      <td>110860.0</td>\n",
       "      <td>Havana</td>\n",
       "      <td></td>\n",
       "      <td>CUP</td>\n",
       "      <td>Peso</td>\n",
       "      <td></td>\n",
       "      <td>CU</td>\n",
       "      <td>3562981</td>\n",
       "      <td>es-CU</td>\n",
       "      <td>Cuba</td>\n",
       "      <td>US</td>\n",
       "      <td>192</td>\n",
       "      <td>53</td>\n",
       "      <td>11423000</td>\n",
       "      <td>CP #####</td>\n",
       "      <td>^(?:CP)*(\\d{5})$</td>\n",
       "      <td>.cu</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>60</td>\n",
       "      <td>DO</td>\n",
       "      <td>DOM</td>\n",
       "      <td>48730.0</td>\n",
       "      <td>Santo Domingo</td>\n",
       "      <td></td>\n",
       "      <td>DOP</td>\n",
       "      <td>Peso</td>\n",
       "      <td></td>\n",
       "      <td>DR</td>\n",
       "      <td>3508796</td>\n",
       "      <td>es-DO</td>\n",
       "      <td>Dominican Republic</td>\n",
       "      <td>HT</td>\n",
       "      <td>214</td>\n",
       "      <td>+1-809 and 1-829</td>\n",
       "      <td>9823821</td>\n",
       "      <td>#####</td>\n",
       "      <td>^(\\d{5})$</td>\n",
       "      <td>.do</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>62</td>\n",
       "      <td>EC</td>\n",
       "      <td>ECU</td>\n",
       "      <td>283560.0</td>\n",
       "      <td>Quito</td>\n",
       "      <td>SA</td>\n",
       "      <td>USD</td>\n",
       "      <td>Dollar</td>\n",
       "      <td></td>\n",
       "      <td>EC</td>\n",
       "      <td>3658394</td>\n",
       "      <td>es-EC</td>\n",
       "      <td>Ecuador</td>\n",
       "      <td>PE,CO</td>\n",
       "      <td>218</td>\n",
       "      <td>593</td>\n",
       "      <td>14790608</td>\n",
       "      <td>@####@</td>\n",
       "      <td>^([a-zA-Z]\\d{4}[a-zA-Z])$</td>\n",
       "      <td>.ec</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>67</td>\n",
       "      <td>ES</td>\n",
       "      <td>ESP</td>\n",
       "      <td>504782.0</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>EU</td>\n",
       "      <td>EUR</td>\n",
       "      <td>Euro</td>\n",
       "      <td></td>\n",
       "      <td>SP</td>\n",
       "      <td>2510769</td>\n",
       "      <td>es-ES,ca,gl,eu,oc</td>\n",
       "      <td>Spain</td>\n",
       "      <td>AD,PT,GI,FR,MA</td>\n",
       "      <td>724</td>\n",
       "      <td>34</td>\n",
       "      <td>46505963</td>\n",
       "      <td>#####</td>\n",
       "      <td>^(\\d{5})$</td>\n",
       "      <td>.es</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>82</td>\n",
       "      <td>GI</td>\n",
       "      <td>GIB</td>\n",
       "      <td>6.5</td>\n",
       "      <td>Gibraltar</td>\n",
       "      <td>EU</td>\n",
       "      <td>GIP</td>\n",
       "      <td>Pound</td>\n",
       "      <td></td>\n",
       "      <td>GI</td>\n",
       "      <td>2411586</td>\n",
       "      <td>en-GI,es,it,pt</td>\n",
       "      <td>Gibraltar</td>\n",
       "      <td>ES</td>\n",
       "      <td>292</td>\n",
       "      <td>350</td>\n",
       "      <td>27884</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td>.gi</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>87</td>\n",
       "      <td>GQ</td>\n",
       "      <td>GNQ</td>\n",
       "      <td>28051.0</td>\n",
       "      <td>Malabo</td>\n",
       "      <td>AF</td>\n",
       "      <td>XAF</td>\n",
       "      <td>Franc</td>\n",
       "      <td></td>\n",
       "      <td>EK</td>\n",
       "      <td>2309096</td>\n",
       "      <td>es-GQ,fr</td>\n",
       "      <td>Equatorial Guinea</td>\n",
       "      <td>GA,CM</td>\n",
       "      <td>226</td>\n",
       "      <td>240</td>\n",
       "      <td>1014999</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td>.gq</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>90</td>\n",
       "      <td>GT</td>\n",
       "      <td>GTM</td>\n",
       "      <td>108890.0</td>\n",
       "      <td>Guatemala City</td>\n",
       "      <td></td>\n",
       "      <td>GTQ</td>\n",
       "      <td>Quetzal</td>\n",
       "      <td></td>\n",
       "      <td>GT</td>\n",
       "      <td>3595528</td>\n",
       "      <td>es-GT</td>\n",
       "      <td>Guatemala</td>\n",
       "      <td>MX,HN,BZ,SV</td>\n",
       "      <td>320</td>\n",
       "      <td>502</td>\n",
       "      <td>13550440</td>\n",
       "      <td>#####</td>\n",
       "      <td>^(\\d{5})$</td>\n",
       "      <td>.gt</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>96</td>\n",
       "      <td>HN</td>\n",
       "      <td>HND</td>\n",
       "      <td>112090.0</td>\n",
       "      <td>Tegucigalpa</td>\n",
       "      <td></td>\n",
       "      <td>HNL</td>\n",
       "      <td>Lempira</td>\n",
       "      <td></td>\n",
       "      <td>HO</td>\n",
       "      <td>3608932</td>\n",
       "      <td>es-HN</td>\n",
       "      <td>Honduras</td>\n",
       "      <td>GT,NI,SV</td>\n",
       "      <td>340</td>\n",
       "      <td>504</td>\n",
       "      <td>7989415</td>\n",
       "      <td>@@####</td>\n",
       "      <td>^([A-Z]{2}\\d{4})$</td>\n",
       "      <td>.hn</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>157</td>\n",
       "      <td>MX</td>\n",
       "      <td>MEX</td>\n",
       "      <td>1972550.0</td>\n",
       "      <td>Mexico City</td>\n",
       "      <td></td>\n",
       "      <td>MXN</td>\n",
       "      <td>Peso</td>\n",
       "      <td></td>\n",
       "      <td>MX</td>\n",
       "      <td>3996063</td>\n",
       "      <td>es-MX</td>\n",
       "      <td>Mexico</td>\n",
       "      <td>GT,US,BZ</td>\n",
       "      <td>484</td>\n",
       "      <td>52</td>\n",
       "      <td>112468855</td>\n",
       "      <td>#####</td>\n",
       "      <td>^(\\d{5})$</td>\n",
       "      <td>.mx</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>165</td>\n",
       "      <td>NI</td>\n",
       "      <td>NIC</td>\n",
       "      <td>129494.0</td>\n",
       "      <td>Managua</td>\n",
       "      <td></td>\n",
       "      <td>NIO</td>\n",
       "      <td>Cordoba</td>\n",
       "      <td></td>\n",
       "      <td>NU</td>\n",
       "      <td>3617476</td>\n",
       "      <td>es-NI,en</td>\n",
       "      <td>Nicaragua</td>\n",
       "      <td>CR,HN</td>\n",
       "      <td>558</td>\n",
       "      <td>505</td>\n",
       "      <td>5995928</td>\n",
       "      <td>###-###-#</td>\n",
       "      <td>^(\\d{7})$</td>\n",
       "      <td>.ni</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>173</td>\n",
       "      <td>PA</td>\n",
       "      <td>PAN</td>\n",
       "      <td>78200.0</td>\n",
       "      <td>Panama City</td>\n",
       "      <td></td>\n",
       "      <td>PAB</td>\n",
       "      <td>Balboa</td>\n",
       "      <td></td>\n",
       "      <td>PM</td>\n",
       "      <td>3703430</td>\n",
       "      <td>es-PA,en</td>\n",
       "      <td>Panama</td>\n",
       "      <td>CR,CO</td>\n",
       "      <td>591</td>\n",
       "      <td>507</td>\n",
       "      <td>3410676</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td>.pa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>174</td>\n",
       "      <td>PE</td>\n",
       "      <td>PER</td>\n",
       "      <td>1285220.0</td>\n",
       "      <td>Lima</td>\n",
       "      <td>SA</td>\n",
       "      <td>PEN</td>\n",
       "      <td>Sol</td>\n",
       "      <td></td>\n",
       "      <td>PE</td>\n",
       "      <td>3932488</td>\n",
       "      <td>es-PE,qu,ay</td>\n",
       "      <td>Peru</td>\n",
       "      <td>EC,CL,BO,BR,CO</td>\n",
       "      <td>604</td>\n",
       "      <td>51</td>\n",
       "      <td>29907003</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td>.pe</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>182</td>\n",
       "      <td>PR</td>\n",
       "      <td>PRI</td>\n",
       "      <td>9104.0</td>\n",
       "      <td>San Juan</td>\n",
       "      <td></td>\n",
       "      <td>USD</td>\n",
       "      <td>Dollar</td>\n",
       "      <td></td>\n",
       "      <td>RQ</td>\n",
       "      <td>4566966</td>\n",
       "      <td>en-PR,es-PR</td>\n",
       "      <td>Puerto Rico</td>\n",
       "      <td></td>\n",
       "      <td>630</td>\n",
       "      <td>+1-787 and 1-939</td>\n",
       "      <td>3916632</td>\n",
       "      <td>#####-####</td>\n",
       "      <td>^00[679]\\d{2}(?:-\\d{4})?$</td>\n",
       "      <td>.pr</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>186</td>\n",
       "      <td>PY</td>\n",
       "      <td>PRY</td>\n",
       "      <td>406750.0</td>\n",
       "      <td>Asuncion</td>\n",
       "      <td>SA</td>\n",
       "      <td>PYG</td>\n",
       "      <td>Guarani</td>\n",
       "      <td></td>\n",
       "      <td>PA</td>\n",
       "      <td>3437598</td>\n",
       "      <td>es-PY,gn</td>\n",
       "      <td>Paraguay</td>\n",
       "      <td>BO,BR,AR</td>\n",
       "      <td>600</td>\n",
       "      <td>595</td>\n",
       "      <td>6375830</td>\n",
       "      <td>####</td>\n",
       "      <td>^(\\d{4})$</td>\n",
       "      <td>.py</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>187</td>\n",
       "      <td>QA</td>\n",
       "      <td>QAT</td>\n",
       "      <td>11437.0</td>\n",
       "      <td>Doha</td>\n",
       "      <td>AS</td>\n",
       "      <td>QAR</td>\n",
       "      <td>Rial</td>\n",
       "      <td></td>\n",
       "      <td>QA</td>\n",
       "      <td>289688</td>\n",
       "      <td>ar-QA,es</td>\n",
       "      <td>Qatar</td>\n",
       "      <td>SA</td>\n",
       "      <td>634</td>\n",
       "      <td>974</td>\n",
       "      <td>840926</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td>.qa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>210</td>\n",
       "      <td>SV</td>\n",
       "      <td>SLV</td>\n",
       "      <td>21040.0</td>\n",
       "      <td>San Salvador</td>\n",
       "      <td></td>\n",
       "      <td>USD</td>\n",
       "      <td>Dollar</td>\n",
       "      <td></td>\n",
       "      <td>ES</td>\n",
       "      <td>3585968</td>\n",
       "      <td>es-SV</td>\n",
       "      <td>El Salvador</td>\n",
       "      <td>GT,HN</td>\n",
       "      <td>222</td>\n",
       "      <td>503</td>\n",
       "      <td>6052064</td>\n",
       "      <td>CP ####</td>\n",
       "      <td>^(?:CP)*(\\d{4})$</td>\n",
       "      <td>.sv</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>226</td>\n",
       "      <td>TT</td>\n",
       "      <td>TTO</td>\n",
       "      <td>5128.0</td>\n",
       "      <td>Port of Spain</td>\n",
       "      <td></td>\n",
       "      <td>TTD</td>\n",
       "      <td>Dollar</td>\n",
       "      <td></td>\n",
       "      <td>TD</td>\n",
       "      <td>3573591</td>\n",
       "      <td>en-TT,hns,fr,es,zh</td>\n",
       "      <td>Trinidad and Tobago</td>\n",
       "      <td></td>\n",
       "      <td>780</td>\n",
       "      <td>+1-868</td>\n",
       "      <td>1228691</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td>.tt</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>233</td>\n",
       "      <td>US</td>\n",
       "      <td>USA</td>\n",
       "      <td>9629091.0</td>\n",
       "      <td>Washington</td>\n",
       "      <td></td>\n",
       "      <td>USD</td>\n",
       "      <td>Dollar</td>\n",
       "      <td></td>\n",
       "      <td>US</td>\n",
       "      <td>6252001</td>\n",
       "      <td>en-US,es-US,haw,fr</td>\n",
       "      <td>United States</td>\n",
       "      <td>CA,MX,CU</td>\n",
       "      <td>840</td>\n",
       "      <td>1</td>\n",
       "      <td>310232863</td>\n",
       "      <td>#####-####</td>\n",
       "      <td>^\\d{5}(-\\d{4})?$</td>\n",
       "      <td>.us</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>234</td>\n",
       "      <td>UY</td>\n",
       "      <td>URY</td>\n",
       "      <td>176220.0</td>\n",
       "      <td>Montevideo</td>\n",
       "      <td>SA</td>\n",
       "      <td>UYU</td>\n",
       "      <td>Peso</td>\n",
       "      <td></td>\n",
       "      <td>UY</td>\n",
       "      <td>3439705</td>\n",
       "      <td>es-UY</td>\n",
       "      <td>Uruguay</td>\n",
       "      <td>BR,AR</td>\n",
       "      <td>858</td>\n",
       "      <td>598</td>\n",
       "      <td>3477000</td>\n",
       "      <td>#####</td>\n",
       "      <td>^(\\d{5})$</td>\n",
       "      <td>.uy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>238</td>\n",
       "      <td>VE</td>\n",
       "      <td>VEN</td>\n",
       "      <td>912050.0</td>\n",
       "      <td>Caracas</td>\n",
       "      <td>SA</td>\n",
       "      <td>VEF</td>\n",
       "      <td>Bolivar</td>\n",
       "      <td></td>\n",
       "      <td>VE</td>\n",
       "      <td>3625428</td>\n",
       "      <td>es-VE</td>\n",
       "      <td>Venezuela</td>\n",
       "      <td>GY,BR,CO</td>\n",
       "      <td>862</td>\n",
       "      <td>58</td>\n",
       "      <td>27223228</td>\n",
       "      <td>####</td>\n",
       "      <td>^(\\d{4})$</td>\n",
       "      <td>.ve</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>251</td>\n",
       "      <td>AN</td>\n",
       "      <td>ANT</td>\n",
       "      <td>960.0</td>\n",
       "      <td>Willemstad</td>\n",
       "      <td></td>\n",
       "      <td>ANG</td>\n",
       "      <td>Guilder</td>\n",
       "      <td></td>\n",
       "      <td>NT</td>\n",
       "      <td>8505032</td>\n",
       "      <td>nl-AN,en,es</td>\n",
       "      <td>Netherlands Antilles</td>\n",
       "      <td>GP</td>\n",
       "      <td>530</td>\n",
       "      <td>599</td>\n",
       "      <td>300000</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td>.an</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    alpha_2 alpha_3       area         capital continent currency_code  \\\n",
       "9        AR     ARG  2766890.0    Buenos Aires        SA           ARS   \n",
       "13       AW     ABW      193.0      Oranjestad                     AWG   \n",
       "28       BO     BOL  1098580.0           Sucre        SA           BOB   \n",
       "30       BR     BRA  8511965.0        Brasilia        SA           BRL   \n",
       "36       BZ     BLZ    22966.0        Belmopan                     BZD   \n",
       "45       CL     CHL   756950.0        Santiago        SA           CLP   \n",
       "48       CO     COL  1138910.0          Bogota        SA           COP   \n",
       "49       CR     CRI    51100.0        San Jose                     CRC   \n",
       "50       CU     CUB   110860.0          Havana                     CUP   \n",
       "60       DO     DOM    48730.0   Santo Domingo                     DOP   \n",
       "62       EC     ECU   283560.0           Quito        SA           USD   \n",
       "67       ES     ESP   504782.0          Madrid        EU           EUR   \n",
       "82       GI     GIB        6.5       Gibraltar        EU           GIP   \n",
       "87       GQ     GNQ    28051.0          Malabo        AF           XAF   \n",
       "90       GT     GTM   108890.0  Guatemala City                     GTQ   \n",
       "96       HN     HND   112090.0     Tegucigalpa                     HNL   \n",
       "157      MX     MEX  1972550.0     Mexico City                     MXN   \n",
       "165      NI     NIC   129494.0         Managua                     NIO   \n",
       "173      PA     PAN    78200.0     Panama City                     PAB   \n",
       "174      PE     PER  1285220.0            Lima        SA           PEN   \n",
       "182      PR     PRI     9104.0        San Juan                     USD   \n",
       "186      PY     PRY   406750.0        Asuncion        SA           PYG   \n",
       "187      QA     QAT    11437.0            Doha        AS           QAR   \n",
       "210      SV     SLV    21040.0    San Salvador                     USD   \n",
       "226      TT     TTO     5128.0   Port of Spain                     TTD   \n",
       "233      US     USA  9629091.0      Washington                     USD   \n",
       "234      UY     URY   176220.0      Montevideo        SA           UYU   \n",
       "238      VE     VEN   912050.0         Caracas        SA           VEF   \n",
       "251      AN     ANT      960.0      Willemstad                     ANG   \n",
       "\n",
       "    currency_name eqivalent_fips_code fips  geoname_id             languages  \\\n",
       "9            Peso                       AR     3865483  es-AR,en,it,de,fr,gn   \n",
       "13        Guilder                       AA     3577279           nl-AW,es,en   \n",
       "28      Boliviano                       BL     3923057           es-BO,qu,ay   \n",
       "30           Real                       BR     3469034        pt-BR,es,en,fr   \n",
       "36         Dollar                       BH     3582678              en-BZ,es   \n",
       "45           Peso                       CI     3895114                 es-CL   \n",
       "48           Peso                       CO     3686110                 es-CO   \n",
       "49          Colon                       CS     3624060              es-CR,en   \n",
       "50           Peso                       CU     3562981                 es-CU   \n",
       "60           Peso                       DR     3508796                 es-DO   \n",
       "62         Dollar                       EC     3658394                 es-EC   \n",
       "67           Euro                       SP     2510769     es-ES,ca,gl,eu,oc   \n",
       "82          Pound                       GI     2411586        en-GI,es,it,pt   \n",
       "87          Franc                       EK     2309096              es-GQ,fr   \n",
       "90        Quetzal                       GT     3595528                 es-GT   \n",
       "96        Lempira                       HO     3608932                 es-HN   \n",
       "157          Peso                       MX     3996063                 es-MX   \n",
       "165       Cordoba                       NU     3617476              es-NI,en   \n",
       "173        Balboa                       PM     3703430              es-PA,en   \n",
       "174           Sol                       PE     3932488           es-PE,qu,ay   \n",
       "182        Dollar                       RQ     4566966           en-PR,es-PR   \n",
       "186       Guarani                       PA     3437598              es-PY,gn   \n",
       "187          Rial                       QA      289688              ar-QA,es   \n",
       "210        Dollar                       ES     3585968                 es-SV   \n",
       "226        Dollar                       TD     3573591    en-TT,hns,fr,es,zh   \n",
       "233        Dollar                       US     6252001    en-US,es-US,haw,fr   \n",
       "234          Peso                       UY     3439705                 es-UY   \n",
       "238       Bolivar                       VE     3625428                 es-VE   \n",
       "251       Guilder                       NT     8505032           nl-AN,en,es   \n",
       "\n",
       "                     name                     neighbours  numeric  \\\n",
       "9               Argentina                 CL,BO,UY,PY,BR       32   \n",
       "13                  Aruba                                     533   \n",
       "28                Bolivia                 PE,CL,PY,BR,AR       68   \n",
       "30                 Brazil  SR,PE,BO,UY,GY,PY,GF,VE,CO,AR       76   \n",
       "36                 Belize                          GT,MX       84   \n",
       "45                  Chile                       PE,BO,AR      152   \n",
       "48               Colombia                 EC,PE,PA,BR,VE      170   \n",
       "49             Costa Rica                          PA,NI      188   \n",
       "50                   Cuba                             US      192   \n",
       "60     Dominican Republic                             HT      214   \n",
       "62                Ecuador                          PE,CO      218   \n",
       "67                  Spain                 AD,PT,GI,FR,MA      724   \n",
       "82              Gibraltar                             ES      292   \n",
       "87      Equatorial Guinea                          GA,CM      226   \n",
       "90              Guatemala                    MX,HN,BZ,SV      320   \n",
       "96               Honduras                       GT,NI,SV      340   \n",
       "157                Mexico                       GT,US,BZ      484   \n",
       "165             Nicaragua                          CR,HN      558   \n",
       "173                Panama                          CR,CO      591   \n",
       "174                  Peru                 EC,CL,BO,BR,CO      604   \n",
       "182           Puerto Rico                                     630   \n",
       "186              Paraguay                       BO,BR,AR      600   \n",
       "187                 Qatar                             SA      634   \n",
       "210           El Salvador                          GT,HN      222   \n",
       "226   Trinidad and Tobago                                     780   \n",
       "233         United States                       CA,MX,CU      840   \n",
       "234               Uruguay                          BR,AR      858   \n",
       "238             Venezuela                       GY,BR,CO      862   \n",
       "251  Netherlands Antilles                             GP      530   \n",
       "\n",
       "                phone  population postal_code_format  \\\n",
       "9                  54    41343201           @####@@@   \n",
       "13                297       71566                      \n",
       "28                591     9947418                      \n",
       "30                 55   201103330          #####-###   \n",
       "36                501      314522                      \n",
       "45                 56    16746491            #######   \n",
       "48                 57    47790000                      \n",
       "49                506     4516220               ####   \n",
       "50                 53    11423000           CP #####   \n",
       "60   +1-809 and 1-829     9823821              #####   \n",
       "62                593    14790608             @####@   \n",
       "67                 34    46505963              #####   \n",
       "82                350       27884                      \n",
       "87                240     1014999                      \n",
       "90                502    13550440              #####   \n",
       "96                504     7989415             @@####   \n",
       "157                52   112468855              #####   \n",
       "165               505     5995928          ###-###-#   \n",
       "173               507     3410676                      \n",
       "174                51    29907003                      \n",
       "182  +1-787 and 1-939     3916632         #####-####   \n",
       "186               595     6375830               ####   \n",
       "187               974      840926                      \n",
       "210               503     6052064            CP ####   \n",
       "226            +1-868     1228691                      \n",
       "233                 1   310232863         #####-####   \n",
       "234               598     3477000              #####   \n",
       "238                58    27223228               ####   \n",
       "251               599      300000                      \n",
       "\n",
       "             postal_code_regex  tld  \n",
       "9      ^[A-Z]?\\d{4}[A-Z]{0,3}$  .ar  \n",
       "13                              .aw  \n",
       "28                              .bo  \n",
       "30               ^\\d{5}-\\d{3}$  .br  \n",
       "36                              .bz  \n",
       "45                   ^(\\d{7})$  .cl  \n",
       "48                              .co  \n",
       "49                   ^(\\d{4})$  .cr  \n",
       "50            ^(?:CP)*(\\d{5})$  .cu  \n",
       "60                   ^(\\d{5})$  .do  \n",
       "62   ^([a-zA-Z]\\d{4}[a-zA-Z])$  .ec  \n",
       "67                   ^(\\d{5})$  .es  \n",
       "82                              .gi  \n",
       "87                              .gq  \n",
       "90                   ^(\\d{5})$  .gt  \n",
       "96           ^([A-Z]{2}\\d{4})$  .hn  \n",
       "157                  ^(\\d{5})$  .mx  \n",
       "165                  ^(\\d{7})$  .ni  \n",
       "173                             .pa  \n",
       "174                             .pe  \n",
       "182  ^00[679]\\d{2}(?:-\\d{4})?$  .pr  \n",
       "186                  ^(\\d{4})$  .py  \n",
       "187                             .qa  \n",
       "210           ^(?:CP)*(\\d{4})$  .sv  \n",
       "226                             .tt  \n",
       "233           ^\\d{5}(-\\d{4})?$  .us  \n",
       "234                  ^(\\d{5})$  .uy  \n",
       "238                  ^(\\d{4})$  .ve  \n",
       "251                             .an  "
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_espanol = df.replace(np.nan, '', regex=True)\n",
    "df_espanol = df_espanol[ df_espanol['languages'].str.contains('es') ]\n",
    "df_espanol"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:02:40.210324Z",
     "start_time": "2019-12-08T22:02:40.202616Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(29, 19)"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_espanol.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Visualicemos por población"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:02:40.806679Z",
     "start_time": "2019-12-08T22:02:40.213973Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x11ef08898>"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABIEAAAJoCAYAAADxrfGxAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAgAElEQVR4nOzdf7jcdX3n/debBMkioC4JlgU02FqkyO9IYK2KKCsV7uItsEVXJaKiWH/g1d0VrZegveuyd1u5pFpYrCzIRSkVldKC9TeL3uKPhAUMoit3m9WsrsZQI5SCBD77x0zS0xA8J8mcM5N8Ho/rOteZH99z5n3OmTPzned85zvVWgsAAAAAO7adxj0AAAAAALNPBAIAAADogAgEAAAA0AERCAAAAKADIhAAAABAB0QgAAAAgA6MNQJV1WVV9eOqWjmDZZ9SVV+sqv9eVXdU1YvnYkYAAACAHcG4twS6PMkJM1z2XUn+orV2eJLTk/zJbA0FAAAAsKMZawRqrd2c5J6pp1XVL1fV31TViqr6UlU9Y8PiSfYYHn5Ckh/M4agAAAAA27X54x5gMy5N8obW2neramkGW/wcl+T8JJ+pqjcneXySF45vRAAAAIDty0RFoKraLcm/TvKxqtpw8i7Dzy9Lcnlr7Y+q6pgkV1bVM1trj4xhVAAAAIDtykRFoAxenvbT1tphmznvNRnuP6i1dktVLUiyMMmP53A+AAAAgO3SuHcM/c+01n6W5O+q6rQkqYFDh2d/L8kLhqcfmGRBkjVjGRQAAABgO1OttfFdeNXVSY7NYIueHyU5L8kXklycZO8kOyf589bae6vq15J8OMluGewk+j+21j4zjrkBAAAAtjdjjUAAAAAAzI2JejkYAAAAALNjbDuGXrhwYVu8ePG4Lh4AAABgh7NixYqftNYWbe68sUWgxYsXZ/ny5eO6eAAAAIAdTlX9z8c6z8vBAAAAADogAgEAAAB0QAQCAAAA6MDY9gkEAAAA7LgeeuihrF69Og888MC4R9khLViwIPvuu2923nnnGX+NCAQAAACM3OrVq7P77rtn8eLFqapxj7NDaa1l7dq1Wb16dfbff/8Zf52XgwEAAAAj98ADD2TPPfcUgGZBVWXPPffc4q2sRCAAAABgVghAs2drfrciEAAAAEAH7BMIAAAAmHWLz71hpN9v1QUnjvT7bdUMq1blpJNOysqVK3/hMl/5ylfy8pe/PEmyfPnyfPSjH81FF100V2NuZEsgAAAAgFmyatWq/Nmf/dnG40uWLBlLAEpEIAAAAGAHtWrVqjzjGc/IGWeckUMOOSSnnnpq7r///nz+85/P4YcfnoMPPjhnnnlmHnzwwSTJ4sWL8/a3vz1HHXVUjjrqqNx9991JkmXLluXaa6/d+H132223zV7Wc57znBxxxBE54ogj8pWvfCVJcu655+ZLX/pSDjvssFx44YW56aabctJJJyVJ7rnnnrzkJS/JIYcckqOPPjp33HFHkuT888/PmWeemWOPPTZPe9rTRhaNRCAAAABgh/Wd73wnZ511Vu64447sscceef/7359ly5blmmuuyTe/+c2sX78+F1988cbl99hjj3z961/Pm970ppxzzjkzvpy99torn/3sZ3PrrbfmmmuuyVve8pYkyQUXXJDnPOc5ue222/K2t73tn33Neeedl8MPPzx33HFH3ve+9+VVr3rVxvO+/e1v59Of/nS+/vWv5z3veU8eeuihbfxNiEAAAADADmy//fbLs5/97CTJK17xinz+85/P/vvvn1/91V9Nkpxxxhm5+eabNy7/spe9bOPnW265ZcaX89BDD+V1r3tdDj744Jx22mn51re+Ne3XfPnLX84rX/nKJMlxxx2XtWvXZt26dUmSE088MbvssksWLlyYvfbaKz/60Y9mPMtjsWNoAAAAYIe1pW+lPnX5DYfnz5+fRx55JEnSWsvPf/7zR33dhRdemCc/+cm5/fbb88gjj2TBggXTXlZr7TEvf5dddtl42rx587J+/fot+jk2x5ZAAAAAwA7re9/73sYteq6++uq88IUvzKpVqzbu7+fKK6/M8573vI3LX3PNNRs/H3PMMUkG+wpasWJFkuQv//IvN/vSrHXr1mXvvffOTjvtlCuvvDIPP/xwkmT33XfPvffeu9nZnvvc5+aqq65Kktx0001ZuHBh9thjj1H82JtlSyAAAABg1o3rLd0PPPDAXHHFFXn961+fpz/96fnABz6Qo48+OqeddlrWr1+fZz3rWXnDG96wcfkHH3wwS5cuzSOPPJKrr746SfK6170uJ598co466qi84AUvyOMf//hHXc4b3/jGnHLKKfnYxz6W5z//+RuXOeSQQzJ//vwceuihWbZsWQ4//PCNX3P++efn1a9+dQ455JDsuuuuueKKK2b1d1Gb2/RoLixZsqQtX758LJcNAAAAzK677rorBx544FhnWLVqVU466aSsXLlyRssvXrw4y5cvz8KFC2d5stHY3O+4qla01pZsbnkvBwMAAADogJeDAQAAADukxYsXz3groGSw5dCOzJZAAAAAAB0QgQAAAAA6IAIBAAAAdEAEAgAAAOiAHUMDAAAAs+/8J4z4+60b7ffrgAgEAAAAE2TxuTfMaLlVF5w4y5P04eGHH868efPGPcac8HIwAAAAYIf1kpe8JEceeWQOOuigXHrppUmS3XbbLe9+97uzdOnS3HLLLVmxYkWe97zn5cgjj8yLXvSi/PCHP0ySfPjDH86znvWsHHrooTnllFNy//33j/NH2WYiEAAAALDDuuyyy7JixYosX748F110UdauXZt/+Id/yDOf+cx87Wtfy9KlS/PmN7851157bVasWJEzzzwzv/u7v5skeelLX5pvfOMbuf3223PggQfmIx/5yJh/mm3j5WAAAADADuuiiy7KJz/5ySTJ97///Xz3u9/NvHnzcsoppyRJvvOd72TlypU5/vjjkwxeHrb33nsnSVauXJl3vetd+elPf5r77rsvL3rRi8bzQ4yICAQAAADskG666aZ87nOfyy233JJdd901xx57bB544IEsWLBg436AWms56KCDcssttzzq65ctW5brrrsuhx56aC6//PLcdNNNc/wTjJaXgwEAAAA7pHXr1uVJT3pSdt1113z729/OV7/61Uctc8ABB2TNmjUbI9BDDz2UO++8M0ly7733Zu+9985DDz2Uq666ak5nnw22BAIAAABm3xje0v2EE07IJZdckkMOOSQHHHBAjj766Ect87jHPS7XXntt3vKWt2TdunVZv359zjnnnBx00EH5vd/7vSxdujRPfepTc/DBB+fee++d859hlEQgAAAAYIe0yy675FOf+tSjTr/vvvv+2fHDDjssN99886OWO/vss3P22WfP2nxzzcvBAAAAADogAgEAAAB0QAQCAAAAZkVrbdwj7LC25ncrAgEAAAAjt2DBgqxdu1YImgWttaxduzYLFizYoq+zY2gAAABg5Pbdd9+sXr06a9asGfcoO6QFCxZk33333aKvEYEAAACAkdt5552z//77j3sMppj25WBVtaCqvl5Vt1fVnVX1ns0ss0tVXVNV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\n",
      "text/plain": [
       "<Figure size 1440x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_espanol.set_index('alpha_3')[['population','area']].plot(kind='bar',rot=65,figsize=(20,10))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Detección de Outliers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:02:55.543787Z",
     "start_time": "2019-12-08T22:02:55.521193Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-102872707.87855022\n",
      "167589161.25786057\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['BRA', 'USA']"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "anomalies = []\n",
    "\n",
    "# Funcion ejemplo para detección de outliers\n",
    "def find_anomalies(data):\n",
    "    # Set upper and lower limit to 2 standard deviation\n",
    "    data_std = data.std()\n",
    "    data_mean = data.mean()\n",
    "    anomaly_cut_off = data_std * 2\n",
    "    lower_limit  = data_mean - anomaly_cut_off \n",
    "    upper_limit = data_mean + anomaly_cut_off\n",
    "    print(lower_limit.iloc[0])\n",
    "    print(upper_limit.iloc[0])\n",
    "\n",
    "    # Generate outliers\n",
    "    for index, row in data.iterrows():\n",
    "        outlier = row # # obtener primer columna\n",
    "        # print(outlier)\n",
    "        if (outlier.iloc[0] > upper_limit.iloc[0]) or (outlier.iloc[0] < lower_limit.iloc[0]):\n",
    "            anomalies.append(index)\n",
    "    return anomalies\n",
    "\n",
    "find_anomalies(df_espanol.set_index('alpha_3')[['population']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:03:21.432811Z",
     "start_time": "2019-12-08T22:03:21.427535Z"
    }
   },
   "outputs": [],
   "source": [
    "# Quitemos BRA y USA por ser outlies y volvamos a graficar:\n",
    "df_espanol.drop([30,233], inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:03:22.946923Z",
     "start_time": "2019-12-08T22:03:22.477307Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1235486a0>"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABIEAAAJoCAYAAADxrfGxAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAgAElEQVR4nOzdf7jcdX3n/debBMiNgPUmwVKDBltEQEA0Eliq4g9WFG7xFtyCq4Io+Auttle3sfUCxK3LXVu55C7FUnVRboogW5UWFOsPFltRSapSQFm5bVayemsMykJZfn/uP2aSHkMgA5mTmZPP43FduXJm5nvOeZ8zZ3495/OdqdZaAAAAANi6bTPpAQAAAACYfSIQAAAAQAdEIAAAAIAOiEAAAAAAHRCBAAAAADogAgEAAAB0YKIRqKo+VlU/raobRtj2yVX1lar6VlVdX1Uv2xIzAgAAAGwNJr0S6IIkR4y47XuSXNpaOzDJcUn+fLaGAgAAANjaTDQCtdauSXLbzOOq6ter6vNVtbKqvlpVT1+3eZKdhx8/PsmPtuCoAAAAAHPa/EkPsBHnJ3lza+37VbUsgxU/L0xyRpIvVNXbkzwuyYsnNyIAAADA3DJVEaiqdkzyb5J8qqrWHb398P/jk1zQWvvTqjokyYVV9YzW2oMTGBUAAABgTpmqCJTB7mm/aK09cyOnvSHD1w9qrV1bVQuSLEzy0y04HwAAAMCcNOkXhv4lrbX/meSfq+pVSVIDBwxP/mGSFw2P3zvJgiRrJjIoAAAAwBxTrbXJffOqi5MclsGKnp8kOT3Jl5Ocl2S3JNsm+WRr7cyq2ifJXybZMYMXif4PrbUvTGJuAAAAgLlmohEIAAAAgC1jqnYHAwAAAGB2TOyFoRcuXNiWLFkyqW8PAAAAsNVZuXLlz1prizZ22sQi0JIlS7JixYpJfXsAAACArU5V/feHO83uYAAAAAAdEIEAAAAAOiACAQAAAHRgYq8JBAAAAGy97rvvvqxevTp33333pEfZKi1YsCCLFy/OtttuO/LniEAAAADA2K1evTo77bRTlixZkqqa9DhbldZa1q5dm9WrV2ePPfYY+fPsDgYAAACM3d13351ddtlFAJoFVZVddtnlUa+yEoEAAACAWSEAzZ7H8rsVgQAAAAA64DWBAAAAgFm3ZPkVY/16q846cqxf7zHNsGpVjjrqqNxwww2PuM3Xvva1vPrVr06SrFixIp/4xCdyzjnnbKkx17MSCAAAAGCWrFq1Kn/1V3+1/vDSpUsnEoASEQgAAADYSq1atSpPf/rTc8IJJ2T//ffPsccem7vuuitf+tKXcuCBB2a//fbLSSedlHvuuSdJsmTJkvz+7/9+DjrooBx00EG55ZZbkiQnnnhiLrvssvVfd8cdd9zo93ruc5+bZz3rWXnWs56Vr33ta0mS5cuX56tf/Wqe+cxn5uyzz87VV1+do446Kkly22235RWveEX233//HHzwwbn++uuTJGeccUZOOumkHHbYYXnqU586tmgkAgEAAABbrZtvvjmnnHJKrr/++uy888754Ac/mBNPPDGXXHJJ/umf/in3339/zjvvvPXb77zzzvnmN7+ZU089Ne985ztH/j677rpr/u7v/i7/+I//mEsuuSTveMc7kiRnnXVWnvvc5+bb3/523vWud/3S55x++uk58MADc/311+f9739/Xve6160/7Xvf+16uuuqqfPOb38x73/ve3HfffZv5mxCBAAAAgK3Y7rvvnkMPPTRJ8prXvCZf+tKXsscee+RpT3takuSEE07INddcs377448/fv3/11577cjf57777svJJ5+c/fbbL6961aty0003bfJz/v7v/z6vfe1rkyQvfOELs3bt2tx+++1JkiOPPDLbb799Fi5cmF133TU/+clPRp7l4XhhaAAAAGCr9WjfSn3m9us+nj9/fh588MEkSWst995770M+7+yzz84Tn/jEfOc738mDDz6YBQsWbPJ7tdYe9vtvv/3264+bN29e7r///kf1c2yMlUAAAADAVuuHP/zh+hU9F198cV784hdn1apV61/v58ILL8zzn//89dtfcskl6/8/5JBDkgxeK2jlypVJks9+9rMb3TXr9ttvz2677ZZtttkmF154YR544IEkyU477ZQ77rhjo7M973nPy0UXXZQkufrqq7Nw4cLsvPPO4/ixN8pKIAAAAGDWTeot3ffee+98/OMfz5ve9Kbsueee+dCHPpSDDz44r3rVq3L//ffnOc95Tt785jev3/6ee+7JsmXL8uCDD+biiy9Okpx88sk5+uijc9BBB+VFL3pRHve4xz3k+7z1rW/NMccck0996lN5wQtesH6b/fffP/Pnz88BBxyQE088MQceeOD6zznjjDPy+te/Pvvvv3922GGHfPzjH5/V30VtbOnRlrB06dK2YsWKiXxvAAAAYHZ997vfzd577z3RGVatWpWjjjoqN9xww0jbL1myJCtWrMjChQtnebLx2NjvuKpWttaWbmx7u4MBAAAAdMDuYAAAAMBWacmSJSOvAkoGK4e2ZlYCAQAAAHRABAIAAADogAgEAAAA0AERCAAAAKADXhgaAAAAmH1nPH7MX+/28X69DohAAABsliXLrxh521VnHTmLkwDAo/fAAw9k3rx5kx5ji7A7GAAAALDVesUrXpFnP/vZ2XfffXP++ecnSXbcccecdtppWbZsWa699tqsXLkyz3/+8/PsZz87L3nJS/LjH/84SfKXf/mXec5znpMDDjggxxxzTO66665J/iibTQQCAAAAtlof+9jHsnLlyqxYsSLnnHNO1q5dm3/5l3/JM57xjHzjG9/IsmXL8va3vz2XXXZZVq5cmZNOOil/+Id/mCR55Stfmeuuuy7f+c53svfee+ejH/3ohH+azWN3MAAAAGCrdc455+TTn/50kuTWW2/N97///cybNy/HHHNMkuTmm2/ODTfckMMPPzzJYPew3XbbLUlyww035D3veU9+8Ytf5M4778xLXvKSyfwQYyICAQAAAFulq6++Ol/84hdz7bXXZocddshhhx2Wu+++OwsWLFj/OkCttey777659tprH/L5J554Yj7zmc/kgAMOyAUXXJCrr756C/8E42V3MAAAAGCrdPvtt+cJT3hCdthhh3zve9/L17/+9Ydss9dee2XNmjXrI9B9992XG2+8MUlyxx13ZLfddst9992Xiy66aIvOPhusBAIAAABm3wTe0v2II47Ihz/84ey///7Za6+9cvDBBz9km+222y6XXXZZ3vGOd+T222/P/fffn3e+853Zd9998773vS/Lli3LU57ylOy333654447tvjPME4iEAAAALBV2n777fO5z33uIcffeeedv3T4mc98Zq655pqHbPeWt7wlb3nLW2Ztvi3N7mAAAAAAHRCBAAAAADogAgEAAACzorU26RG2Wo/ldysCAQAAAGO3YMGCrF27VgiaBa21rF27NgsWLHhUn+eFoQEAAICxW7x4cVavXp01a9ZMepSt0oIFC7J48eJH9TkiEAAAADB22267bfbYY49Jj8EMdgcDAAAA6IAIBAAAANABEQgA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\n",
      "text/plain": [
       "<Figure size 1440x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_espanol.set_index('alpha_3')[['population','area']].plot(kind='bar',rot=65,figsize=(20,10))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graficamos ordenando por tamaño Población"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:03:26.045129Z",
     "start_time": "2019-12-08T22:03:25.515844Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x123883a58>"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABIEAAAJoCAYAAADxrfGxAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAgAElEQVR4nOzde5TkdX3n/9ebGWB+CBh/zGCIgw4mqICA6MjgGhUvrCj8xBXdiOsFUfASNLo5WcfEo4gbl9VEjmxQQ9RF+REE2agkoBgvrCaCMhglgLKyZlZm8eg4KosSbvLZP6pm0jQNU8xUT1XP5/E4Z053fes73e+u6rr08/v9VlVrLQAAAABs33aY9AAAAAAAzD8RCAAAAKADIhAAAABAB0QgAAAAgA6IQAAAAAAdEIEAAAAAOjDRCFRVH62qH1fVNSOs+/Cq+nJV/UNVXV1Vz90WMwIAAABsDya9J9DZSY4ccd23JbmgtXZIkhcn+cB8DQUAAACwvZloBGqtfSXJT2cuq6rfrKrPVdVVVfXVqnrMxtWT7D78/MFJbtqGowIAAAAsaIsnPcAczkry2tba96pqVQZ7/DwjySlJPl9Vb0jyoCTPmtyIAAAAAAvLVEWgqto1yb9K8smq2rh45+HH45Kc3Vr706p6UpJzquqxrbW7JzAqAAAAwIIyVREog8PTft5ae9wc570qw9cPaq1dXlVLkixN8uNtOB8AAADAgjTpF4a+h9ba/0nyT1X1oiSpgYOHZ/8gyTOHy/dLsiTJ+okMCgAAALDAVGttct+86rwkh2ewR8+PkrwjyZeSfDDJXkl2TPKJ1tqpVbV/kr9IsmsGLxL9H1prn5/E3AAAAAALzUQjEAAAAADbxlQdDgYAAADA/JjYC0MvXbq0rVixYlLfHgAAAGC7c9VVV/2ktbZsrvMmFoFWrFiRNWvWTOrbAwAAAGx3qup/3dd5DgcDAAAA6IAIBAAAANABEQgAAACgAxN7TaC53HnnnVm3bl1uu+22SY+yXVqyZEmWL1+eHXfccdKjAAAAANvYVEWgdevWZbfddsuKFStSVZMeZ7vSWsuGDRuybt267LPPPpMeBwAAANjGpupwsNtuuy177LGHADQPqip77LGHvawAAACgU1MVgZIIQPPIZQsAAAD9mroIBAAAAMD4TdVrAs22YvXFY/16a087aqxfb4tmWLs2Rx99dK655pr7XedrX/taXvKSlyRJ1qxZk49//OM544wzttWYAAAAwHbGnkBTaO3atfnLv/zLTadXrlwpAAEAAABbRQSaZe3atXnMYx6TV7ziFTnooIPywhe+MLfeemu++MUv5pBDDsmBBx6YE044IbfffnuSZMWKFXnLW96SQw89NIceemhuuOGGJMnxxx+fCy+8cNPX3XXXXef8Xk95ylPy+Mc/Po9//OPzta99LUmyevXqfPWrX83jHve4nH766bnsssty9NFHJ0l++tOf5vnPf34OOuigHHbYYbn66quTJKecckpOOOGEHH744XnkIx8pGgEAAAD3IALN4frrr89JJ52Uq6++Orvvvnve97735fjjj8/555+ff/zHf8xdd92VD37wg5vW33333fONb3wjJ598ct70pjeN/H323HPP/O3f/m2++c1v5vzzz88b3/jGJMlpp52WpzzlKfnWt76VN7/5zff4P+94xztyyCGH5Oqrr8673/3uvPzlL9903ne/+91ceuml+cY3vpF3vvOdufPOO7fykgAAAAC2FyLQHPbee+88+clPTpK89KUvzRe/+MXss88+edSjHpUkecUrXpGvfOUrm9Y/7rjjNn28/PLLR/4+d955Z0488cQceOCBedGLXpTrrrtus//n7/7u7/Kyl70sSfKMZzwjGzZsyM0335wkOeqoo7Lzzjtn6dKl2XPPPfOjH/1o5FkAAACA7dtUvzD0pDzQt1Kfuf7GzxcvXpy77747SdJayx133HGv/3f66afnoQ99aL797W/n7rvvzpIlSzb7vVpr9/n9d955503LFi1alLvuuusB/RwAAADA9sueQHP4wQ9+sGmPnvPOOy/Petazsnbt2k2v93POOefkaU972qb1zz///E0fn/SkJyUZvFbQVVddlST5zGc+M+ehWTfffHP22muv7LDDDjnnnHPyq1/9Kkmy22675ZZbbplztqc+9ak599xzkySXXXZZli5dmt13330cPzYAAACwHZvqPYEm9Zbu++23Xz72sY/lNa95Tfbdd9+8//3vz2GHHZYXvehFueuuu/LEJz4xr33tazetf/vtt2fVqlW5++67c9555yVJTjzxxBxzzDE59NBD88xnPjMPetCD7vV9Xv/61+fYY4/NJz/5yTz96U/ftM5BBx2UxYsX5+CDD87xxx+fQw45ZNP/OeWUU/LKV74yBx10UHbZZZd87GMfm+dLAwAAANge1FyHF20LK1eubGvWrLnHsu985zvZb7/9JjLPRmvXrs3RRx+da665ZqT1V6xYkTVr1mTp0qXzPNl4TMNlDAAAAMyPqrqqtbZyrvMcDgYAAADQgak+HGwSVqxYMfJeQMlgzyEAAACAaWdPIAAAAIAOiEAAAAAAHRCBAAAAADogAgEAAAB0YLpfGPqUB4/569083q8HAAAAsEBMdwSaUr/61a+yaNGiSY8BAAAATKEVqy8eab21px01z5Pck8PB5vD85z8/T3jCE3LAAQfkrLPOSpLsuuuuefvb355Vq1bl8ssvz1VXXZWnPe1pecITnpBnP/vZ+eEPf5gk+Yu/+Is88YlPzMEHH5xjjz02t9566yR/FAAAAIAkItCcPvrRj+aqq67KmjVrcsYZZ2TDhg355S9/mcc+9rH5+te/nlWrVuUNb3hDLrzwwlx11VU54YQT8kd/9EdJkhe84AW58sor8+1vfzv77bdfPvKRj0z4pwEAAABwONiczjjjjHzqU59Kktx444353ve+l0WLFuXYY49Nklx//fW55pprcsQRRyQZHB621157JUmuueaavO1tb8vPf/7z/OIXv8izn/3syfwQAAAAADOIQLNcdtll+cIXvpDLL788u+yySw4//PDcdtttWbJkyabXAWqt5YADDsjll19+r/9//PHH59Of/nQOPvjgnH322bnsssu28U8AAAAAcG8OB5vl5ptvzkMe8pDssssu+e53v5srrrjiXus8+tGPzvr16zdFoDvvvDPXXnttkuSWW27JXnvtlTvvvDPnnnvuNp0dAAAA4L5M955AE3hL9yOPPDIf+tCHctBBB+XRj350DjvssHuts9NOO+XCCy/MG9/4xtx8882566678qY3vSkHHHBA3vWud2XVqlV5xCMekQMPPDC33HLLNv8ZAAAAAGab7gg0ATvvvHM++9nP3mv5L37xi3ucftzjHpevfOUr91rvda97XV73utfN23wAAAAAW8LhYAAAAAAdEIEAAAAAOjB1Eai1NukRtlsuWwAAAOjXVEWgJUuWZMOGDWLFPGitZcOGDVmyZMmkRwEAAAAmYKpeGHr58uVZt25d1q9fP+lRtktLlizJ8uXLJz0GAAAAMAFTFYF23HHH7LPPPpMeAwAAAGC7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\n",
      "text/plain": [
       "<Figure size 1440x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_espanol.set_index('alpha_3')[['population','area']].sort_values([\"population\"]).plot(kind='bar',rot=65,figsize=(20,10))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Visualización por Área"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:03:28.127698Z",
     "start_time": "2019-12-08T22:03:27.680006Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x123cf0630>"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "4df_espanol.set_index('alpha_3')[['area']].sort_values([\"area\"]).plot(kind='bar',rot=65,figsize=(20,10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:36:50.772742Z",
     "start_time": "2019-12-08T22:36:50.738258Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>alpha_2</th>\n",
       "      <th>area</th>\n",
       "      <th>capital</th>\n",
       "      <th>continent</th>\n",
       "      <th>currency_code</th>\n",
       "      <th>currency_name</th>\n",
       "      <th>eqivalent_fips_code</th>\n",
       "      <th>fips</th>\n",
       "      <th>geoname_id</th>\n",
       "      <th>languages</th>\n",
       "      <th>name</th>\n",
       "      <th>neighbours</th>\n",
       "      <th>numeric</th>\n",
       "      <th>phone</th>\n",
       "      <th>population</th>\n",
       "      <th>postal_code_format</th>\n",
       "      <th>postal_code_regex</th>\n",
       "      <th>tld</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>alpha_3</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>ARG</td>\n",
       "      <td>AR</td>\n",
       "      <td>2766890.0</td>\n",
       "      <td>Buenos Aires</td>\n",
       "      <td>SA</td>\n",
       "      <td>ARS</td>\n",
       "      <td>Peso</td>\n",
       "      <td></td>\n",
       "      <td>AR</td>\n",
       "      <td>3865483</td>\n",
       "      <td>es-AR,en,it,de,fr,gn</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>CL,BO,UY,PY,BR</td>\n",
       "      <td>32</td>\n",
       "      <td>54</td>\n",
       "      <td>41343201</td>\n",
       "      <td>@####@@@</td>\n",
       "      <td>^[A-Z]?\\d{4}[A-Z]{0,3}$</td>\n",
       "      <td>.ar</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>BOL</td>\n",
       "      <td>BO</td>\n",
       "      <td>1098580.0</td>\n",
       "      <td>Sucre</td>\n",
       "      <td>SA</td>\n",
       "      <td>BOB</td>\n",
       "      <td>Boliviano</td>\n",
       "      <td></td>\n",
       "      <td>BL</td>\n",
       "      <td>3923057</td>\n",
       "      <td>es-BO,qu,ay</td>\n",
       "      <td>Bolivia</td>\n",
       "      <td>PE,CL,PY,BR,AR</td>\n",
       "      <td>68</td>\n",
       "      <td>591</td>\n",
       "      <td>9947418</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td>.bo</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>CHL</td>\n",
       "      <td>CL</td>\n",
       "      <td>756950.0</td>\n",
       "      <td>Santiago</td>\n",
       "      <td>SA</td>\n",
       "      <td>CLP</td>\n",
       "      <td>Peso</td>\n",
       "      <td></td>\n",
       "      <td>CI</td>\n",
       "      <td>3895114</td>\n",
       "      <td>es-CL</td>\n",
       "      <td>Chile</td>\n",
       "      <td>PE,BO,AR</td>\n",
       "      <td>152</td>\n",
       "      <td>56</td>\n",
       "      <td>16746491</td>\n",
       "      <td>#######</td>\n",
       "      <td>^(\\d{7})$</td>\n",
       "      <td>.cl</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>COL</td>\n",
       "      <td>CO</td>\n",
       "      <td>1138910.0</td>\n",
       "      <td>Bogota</td>\n",
       "      <td>SA</td>\n",
       "      <td>COP</td>\n",
       "      <td>Peso</td>\n",
       "      <td></td>\n",
       "      <td>CO</td>\n",
       "      <td>3686110</td>\n",
       "      <td>es-CO</td>\n",
       "      <td>Colombia</td>\n",
       "      <td>EC,PE,PA,BR,VE</td>\n",
       "      <td>170</td>\n",
       "      <td>57</td>\n",
       "      <td>47790000</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td>.co</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>CUB</td>\n",
       "      <td>CU</td>\n",
       "      <td>110860.0</td>\n",
       "      <td>Havana</td>\n",
       "      <td></td>\n",
       "      <td>CUP</td>\n",
       "      <td>Peso</td>\n",
       "      <td></td>\n",
       "      <td>CU</td>\n",
       "      <td>3562981</td>\n",
       "      <td>es-CU</td>\n",
       "      <td>Cuba</td>\n",
       "      <td>US</td>\n",
       "      <td>192</td>\n",
       "      <td>53</td>\n",
       "      <td>11423000</td>\n",
       "      <td>CP #####</td>\n",
       "      <td>^(?:CP)*(\\d{5})$</td>\n",
       "      <td>.cu</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>ECU</td>\n",
       "      <td>EC</td>\n",
       "      <td>283560.0</td>\n",
       "      <td>Quito</td>\n",
       "      <td>SA</td>\n",
       "      <td>USD</td>\n",
       "      <td>Dollar</td>\n",
       "      <td></td>\n",
       "      <td>EC</td>\n",
       "      <td>3658394</td>\n",
       "      <td>es-EC</td>\n",
       "      <td>Ecuador</td>\n",
       "      <td>PE,CO</td>\n",
       "      <td>218</td>\n",
       "      <td>593</td>\n",
       "      <td>14790608</td>\n",
       "      <td>@####@</td>\n",
       "      <td>^([a-zA-Z]\\d{4}[a-zA-Z])$</td>\n",
       "      <td>.ec</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>ESP</td>\n",
       "      <td>ES</td>\n",
       "      <td>504782.0</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>EU</td>\n",
       "      <td>EUR</td>\n",
       "      <td>Euro</td>\n",
       "      <td></td>\n",
       "      <td>SP</td>\n",
       "      <td>2510769</td>\n",
       "      <td>es-ES,ca,gl,eu,oc</td>\n",
       "      <td>Spain</td>\n",
       "      <td>AD,PT,GI,FR,MA</td>\n",
       "      <td>724</td>\n",
       "      <td>34</td>\n",
       "      <td>46505963</td>\n",
       "      <td>#####</td>\n",
       "      <td>^(\\d{5})$</td>\n",
       "      <td>.es</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>HND</td>\n",
       "      <td>HN</td>\n",
       "      <td>112090.0</td>\n",
       "      <td>Tegucigalpa</td>\n",
       "      <td></td>\n",
       "      <td>HNL</td>\n",
       "      <td>Lempira</td>\n",
       "      <td></td>\n",
       "      <td>HO</td>\n",
       "      <td>3608932</td>\n",
       "      <td>es-HN</td>\n",
       "      <td>Honduras</td>\n",
       "      <td>GT,NI,SV</td>\n",
       "      <td>340</td>\n",
       "      <td>504</td>\n",
       "      <td>7989415</td>\n",
       "      <td>@@####</td>\n",
       "      <td>^([A-Z]{2}\\d{4})$</td>\n",
       "      <td>.hn</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>MEX</td>\n",
       "      <td>MX</td>\n",
       "      <td>1972550.0</td>\n",
       "      <td>Mexico City</td>\n",
       "      <td></td>\n",
       "      <td>MXN</td>\n",
       "      <td>Peso</td>\n",
       "      <td></td>\n",
       "      <td>MX</td>\n",
       "      <td>3996063</td>\n",
       "      <td>es-MX</td>\n",
       "      <td>Mexico</td>\n",
       "      <td>GT,US,BZ</td>\n",
       "      <td>484</td>\n",
       "      <td>52</td>\n",
       "      <td>112468855</td>\n",
       "      <td>#####</td>\n",
       "      <td>^(\\d{5})$</td>\n",
       "      <td>.mx</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>NIC</td>\n",
       "      <td>NI</td>\n",
       "      <td>129494.0</td>\n",
       "      <td>Managua</td>\n",
       "      <td></td>\n",
       "      <td>NIO</td>\n",
       "      <td>Cordoba</td>\n",
       "      <td></td>\n",
       "      <td>NU</td>\n",
       "      <td>3617476</td>\n",
       "      <td>es-NI,en</td>\n",
       "      <td>Nicaragua</td>\n",
       "      <td>CR,HN</td>\n",
       "      <td>558</td>\n",
       "      <td>505</td>\n",
       "      <td>5995928</td>\n",
       "      <td>###-###-#</td>\n",
       "      <td>^(\\d{7})$</td>\n",
       "      <td>.ni</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>PER</td>\n",
       "      <td>PE</td>\n",
       "      <td>1285220.0</td>\n",
       "      <td>Lima</td>\n",
       "      <td>SA</td>\n",
       "      <td>PEN</td>\n",
       "      <td>Sol</td>\n",
       "      <td></td>\n",
       "      <td>PE</td>\n",
       "      <td>3932488</td>\n",
       "      <td>es-PE,qu,ay</td>\n",
       "      <td>Peru</td>\n",
       "      <td>EC,CL,BO,BR,CO</td>\n",
       "      <td>604</td>\n",
       "      <td>51</td>\n",
       "      <td>29907003</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td>.pe</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>PRY</td>\n",
       "      <td>PY</td>\n",
       "      <td>406750.0</td>\n",
       "      <td>Asuncion</td>\n",
       "      <td>SA</td>\n",
       "      <td>PYG</td>\n",
       "      <td>Guarani</td>\n",
       "      <td></td>\n",
       "      <td>PA</td>\n",
       "      <td>3437598</td>\n",
       "      <td>es-PY,gn</td>\n",
       "      <td>Paraguay</td>\n",
       "      <td>BO,BR,AR</td>\n",
       "      <td>600</td>\n",
       "      <td>595</td>\n",
       "      <td>6375830</td>\n",
       "      <td>####</td>\n",
       "      <td>^(\\d{4})$</td>\n",
       "      <td>.py</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>URY</td>\n",
       "      <td>UY</td>\n",
       "      <td>176220.0</td>\n",
       "      <td>Montevideo</td>\n",
       "      <td>SA</td>\n",
       "      <td>UYU</td>\n",
       "      <td>Peso</td>\n",
       "      <td></td>\n",
       "      <td>UY</td>\n",
       "      <td>3439705</td>\n",
       "      <td>es-UY</td>\n",
       "      <td>Uruguay</td>\n",
       "      <td>BR,AR</td>\n",
       "      <td>858</td>\n",
       "      <td>598</td>\n",
       "      <td>3477000</td>\n",
       "      <td>#####</td>\n",
       "      <td>^(\\d{5})$</td>\n",
       "      <td>.uy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>VEN</td>\n",
       "      <td>VE</td>\n",
       "      <td>912050.0</td>\n",
       "      <td>Caracas</td>\n",
       "      <td>SA</td>\n",
       "      <td>VEF</td>\n",
       "      <td>Bolivar</td>\n",
       "      <td></td>\n",
       "      <td>VE</td>\n",
       "      <td>3625428</td>\n",
       "      <td>es-VE</td>\n",
       "      <td>Venezuela</td>\n",
       "      <td>GY,BR,CO</td>\n",
       "      <td>862</td>\n",
       "      <td>58</td>\n",
       "      <td>27223228</td>\n",
       "      <td>####</td>\n",
       "      <td>^(\\d{4})$</td>\n",
       "      <td>.ve</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        alpha_2       area       capital continent currency_code  \\\n",
       "alpha_3                                                            \n",
       "ARG          AR  2766890.0  Buenos Aires        SA           ARS   \n",
       "BOL          BO  1098580.0         Sucre        SA           BOB   \n",
       "CHL          CL   756950.0      Santiago        SA           CLP   \n",
       "COL          CO  1138910.0        Bogota        SA           COP   \n",
       "CUB          CU   110860.0        Havana                     CUP   \n",
       "ECU          EC   283560.0         Quito        SA           USD   \n",
       "ESP          ES   504782.0        Madrid        EU           EUR   \n",
       "HND          HN   112090.0   Tegucigalpa                     HNL   \n",
       "MEX          MX  1972550.0   Mexico City                     MXN   \n",
       "NIC          NI   129494.0       Managua                     NIO   \n",
       "PER          PE  1285220.0          Lima        SA           PEN   \n",
       "PRY          PY   406750.0      Asuncion        SA           PYG   \n",
       "URY          UY   176220.0    Montevideo        SA           UYU   \n",
       "VEN          VE   912050.0       Caracas        SA           VEF   \n",
       "\n",
       "        currency_name eqivalent_fips_code fips  geoname_id  \\\n",
       "alpha_3                                                      \n",
       "ARG              Peso                       AR     3865483   \n",
       "BOL         Boliviano                       BL     3923057   \n",
       "CHL              Peso                       CI     3895114   \n",
       "COL              Peso                       CO     3686110   \n",
       "CUB              Peso                       CU     3562981   \n",
       "ECU            Dollar                       EC     3658394   \n",
       "ESP              Euro                       SP     2510769   \n",
       "HND           Lempira                       HO     3608932   \n",
       "MEX              Peso                       MX     3996063   \n",
       "NIC           Cordoba                       NU     3617476   \n",
       "PER               Sol                       PE     3932488   \n",
       "PRY           Guarani                       PA     3437598   \n",
       "URY              Peso                       UY     3439705   \n",
       "VEN           Bolivar                       VE     3625428   \n",
       "\n",
       "                    languages       name      neighbours  numeric phone  \\\n",
       "alpha_3                                                                   \n",
       "ARG      es-AR,en,it,de,fr,gn  Argentina  CL,BO,UY,PY,BR       32    54   \n",
       "BOL               es-BO,qu,ay    Bolivia  PE,CL,PY,BR,AR       68   591   \n",
       "CHL                     es-CL      Chile        PE,BO,AR      152    56   \n",
       "COL                     es-CO   Colombia  EC,PE,PA,BR,VE      170    57   \n",
       "CUB                     es-CU       Cuba              US      192    53   \n",
       "ECU                     es-EC    Ecuador           PE,CO      218   593   \n",
       "ESP         es-ES,ca,gl,eu,oc      Spain  AD,PT,GI,FR,MA      724    34   \n",
       "HND                     es-HN   Honduras        GT,NI,SV      340   504   \n",
       "MEX                     es-MX     Mexico        GT,US,BZ      484    52   \n",
       "NIC                  es-NI,en  Nicaragua           CR,HN      558   505   \n",
       "PER               es-PE,qu,ay       Peru  EC,CL,BO,BR,CO      604    51   \n",
       "PRY                  es-PY,gn   Paraguay        BO,BR,AR      600   595   \n",
       "URY                     es-UY    Uruguay           BR,AR      858   598   \n",
       "VEN                     es-VE  Venezuela        GY,BR,CO      862    58   \n",
       "\n",
       "         population postal_code_format          postal_code_regex  tld  \n",
       "alpha_3                                                                 \n",
       "ARG        41343201           @####@@@    ^[A-Z]?\\d{4}[A-Z]{0,3}$  .ar  \n",
       "BOL         9947418                                                .bo  \n",
       "CHL        16746491            #######                  ^(\\d{7})$  .cl  \n",
       "COL        47790000                                                .co  \n",
       "CUB        11423000           CP #####           ^(?:CP)*(\\d{5})$  .cu  \n",
       "ECU        14790608             @####@  ^([a-zA-Z]\\d{4}[a-zA-Z])$  .ec  \n",
       "ESP        46505963              #####                  ^(\\d{5})$  .es  \n",
       "HND         7989415             @@####          ^([A-Z]{2}\\d{4})$  .hn  \n",
       "MEX       112468855              #####                  ^(\\d{5})$  .mx  \n",
       "NIC         5995928          ###-###-#                  ^(\\d{7})$  .ni  \n",
       "PER        29907003                                                .pe  \n",
       "PRY         6375830               ####                  ^(\\d{4})$  .py  \n",
       "URY         3477000              #####                  ^(\\d{5})$  .uy  \n",
       "VEN        27223228               ####                  ^(\\d{4})$  .ve  "
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# En este caso, podriamos quitar por \"lo bajo\", area menor a 110.000 km2:\n",
    "df_2 = df_espanol.set_index('alpha_3')\n",
    "df_2 = df_2[df_2['area'] > 110000]\n",
    "df_2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-12-08T22:36:55.622303Z",
     "start_time": "2019-12-08T22:36:55.227650Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1c2777a048>"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_2[['area']].sort_values([\"area\"]).plot(kind='bar',rot=65,figsize=(20,10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
