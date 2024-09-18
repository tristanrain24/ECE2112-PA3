{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f6b8a0d7-ec5e-49d9-b383-d4eb42bbc4b9",
   "metadata": {},
   "source": [
    "Python Data Analysis - Problem 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8369b264-9a0a-4469-aaf0-e0d89cc30c25",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "Cars = pd.read_csv('cars.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c26341c-a9f1-4648-8dd3-37791213aba2",
   "metadata": {},
   "source": [
    "a.) Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8c73753f-6e4e-4f93-875e-220a97fd9c64",
   "metadata": {},
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
       "      <th>Model</th>\n",
       "      <th>cyl</th>\n",
       "      <th>hp</th>\n",
       "      <th>wt</th>\n",
       "      <th>vs</th>\n",
       "      <th>gear</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "      <td>6</td>\n",
       "      <td>110</td>\n",
       "      <td>2.620</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>6</td>\n",
       "      <td>110</td>\n",
       "      <td>2.875</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Datsun 710</td>\n",
       "      <td>4</td>\n",
       "      <td>93</td>\n",
       "      <td>2.320</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Hornet 4 Drive</td>\n",
       "      <td>6</td>\n",
       "      <td>110</td>\n",
       "      <td>3.215</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Hornet Sportabout</td>\n",
       "      <td>8</td>\n",
       "      <td>175</td>\n",
       "      <td>3.440</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Model  cyl   hp     wt  vs  gear\n",
       "0          Mazda RX4    6  110  2.620   0     4\n",
       "1      Mazda RX4 Wag    6  110  2.875   0     4\n",
       "2         Datsun 710    4   93  2.320   1     4\n",
       "3     Hornet 4 Drive    6  110  3.215   1     3\n",
       "4  Hornet Sportabout    8  175  3.440   0     3"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Cars.iloc[:5,::2]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d8d5a591-4e9e-433a-bd3c-ce1f55485733",
   "metadata": {},
   "source": [
    "Display the row that contains the ‘Model’ of ‘Mazda RX4’"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "25222fa2-8c20-4e08-be5d-a5013260318f",
   "metadata": {},
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
       "      <th>Model</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Model\n",
       "0  Mazda RX4"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Cars.loc[Cars['Model']=='Mazda RX4', ['Model']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33137e06-0421-4fea-853a-8acf4e0d4629",
   "metadata": {},
   "outputs": [],
   "source": [
    "How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8201b082-4272-4f3f-8531-93f26ddb7c5c",
   "metadata": {},
   "outputs": [],
   "source": [
    "Cars.loc[Cars['Model']=='Camaro Z28', ['Model','cyl']]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
