{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e47c1a34-c81c-4550-ab3a-f703264d7682",
   "metadata": {},
   "source": [
    "Python Data Analysis - Problem 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ebbe29a4-5ff8-4507-92f7-38606c838e36",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0            Mazda RX4\n",
       "1        Mazda RX4 Wag\n",
       "2           Datsun 710\n",
       "3       Hornet 4 Drive\n",
       "4    Hornet Sportabout\n",
       "Name: Model, dtype: object"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "Cars = pd.read_csv('cars.csv')\n",
    "Cars['Model'].head(5)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b48bcf12-c61f-49c9-a180-871c9930a5fd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27      Lotus Europa\n",
       "28    Ford Pantera L\n",
       "29      Ferrari Dino\n",
       "30     Maserati Bora\n",
       "31        Volvo 142E\n",
       "Name: Model, dtype: object"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Cars['Model'].tail(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "07737563-1407-4d4b-8b4c-9e0f36677ce7",
   "metadata": {},
   "outputs": [],
   "source": []
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
