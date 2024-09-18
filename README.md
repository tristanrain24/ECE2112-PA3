# Python Data Analysis (Pandas) 
### Welcome to my PA3 Pandas repository! 
In this assignment we will utilize the power of pandas library to enhance and simplify data analysis tasks

Firstly, some information about the Pandas library, Pandas is a tool for data analysis in python. It is a robust tool with capabilities that will be utilized at this 
programming assignment

In order to utilize the pandas library we need to write the following:

```import pandas as np```

## Overview
In this project we will use pandas to:
#### Load and Analyze Data:
Efficiently load data and utilize pandas' powerful functions to perform data analysis tasks

#### Transform and Visualize Data: 
Transform and reshape the data and generate outputs.
 
 ---


### <p align="center"> Problem 1 </p>


### Getting Started

In this problem we'll need to extract data and create specified outputs, but the data set is contained in another file and in order to access the file we first need to import it to the same directory as our .ipnyb file.  


![image](https://github.com/user-attachments/assets/f1e912b8-7a23-459e-8a7c-ed2d3379b0f1)


After which, we can now start creating our output.

### Goals: 
Save your file as Surname_Pandas-P1.py
Using knowledge obtained from the experiment and demonstrations:

  a. Load the corresponding .csv file into a data frame named cars using pandas

  b. Display the first five and last five rows of the resulting cars.
### Code: 
```
import pandas as pd
Cars = pd.read_csv('cars.csv')
Cars['Model'].head(5)
Cars['Model'].tail(5)
Cars.to_csv('Montales_Pandas-P1.py', index=False)
```
### Explanation
The first problem is loading the data frame. We can use the pandas library in order to read the data frame and for us to be able to utilize it. To do so, we write the following:

```
Cars = pd.read_csv('cars.csv')
```

The next part of the problem is displaying the first five and last five rows of the resulting car, luckily with pandas library we can use ```.head()``` and ```.tail()``` syntax. The .head() syntax extracts the data starting from row index 0. and the .tail() syntax extracts from the final rows and if there are no values inside the parethesis the default result will be five rows. That is why there is no value inside the parenthesis because by default it will only extract 5.

```
Cars['Model'].head(5)
Cars['Model'].tail(5)
```
Respectively, the output of these are: 
```
          .head()                              .tail()
0            Mazda RX4                    27      Lotus Europa                 
1        Mazda RX4 Wag                    28    Ford Pantera L
2           Datsun 710                    29      Ferrari Dino   
3       Hornet 4 Drive                    30     Maserati Bora   
4    Hornet Sportabout                    31        Volvo 142E
Name: Model, dtype: object                Name: Model, dtype: object  

```

---

### <p align="center"> Problem 2 </p>


### Getting Started
