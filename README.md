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
Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
indexing operations.

### Goals: 
Save your file as Surname_Pandas-P2.py
Using knowledge obtained from the experiment and demonstrations:

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

### Code
```
import pandas as pd
Cars = pd.read_csv('cars.csv')
Cars.iloc[:5,::2]
Cars.loc[Cars['Model']=='Mazda RX4', ['Model']]
Cars.loc[Cars['Model']=='Camaro Z28', ['Model','cyl']]
Cars.loc[Cars['Model'].isin(['Mazda RX4 Wag','Ford Pantera L','Honda Civic']), ['Model','cyl', 'gear']]

```
### Explanation

In order to utilize the pandas library, we first need to write ```import pandas as pd``` just like what we did during the first problem.

And we also need to be able to access the data frame and in order to do so, we write:
```
Cars = pd.read_csv('cars.csv')
```

Now we proceed to the first part of the problem which is to - display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

In this problem we will utilize the syntax ```.iloc[]``` which is a integer based indexing, and whithin the parenthesis we would put firstly [:5] this specifies the number of rows to be displayed, and following that is [::2] which is an index that will select every second column.
the syntax is as follows:

```
Cars.iloc[:5,::2]
```
The output: 
```
  Model	cyl	hp	wt	vs	gear
0	Mazda RX4	6	110	2.620	0	4
1	Mazda RX4 Wag	6	110	2.875	0	4
2	Datsun 710	4	93	2.320	1	4
3	Hornet 4 Drive	6	110	3.215	1	3
4	Hornet Sportabout	8	175	3.440	0	3
```
The next part of the problem is: Display the row that contains the ‘Model’ of ‘Mazda RX4’.

And in this problem we will instead use the syntax ```.loc``` because what we are looking for are characters and not indexed based. Writing the syntax should look like the following:

```
Cars.loc[Cars['Model']=='Mazda RX4', ['Model']]
```
The first part: ```Cars['Model']=='Mazda RX4'``` specifies row location of the model "Mazda RX4" and following that:  ```, ['Model']```is the column that we want to displayed.
The output: 

```
Model
0	Mazda RX4
```
Problem C is a similar case to problem B, the only difference is that we will add another column which is the number of "cylinders". the column is labeled as 'cyl'

The code should appear as the following:

```
Cars.loc[Cars['Model']=='Camaro Z28', ['Model','cyl']]
```
Likewise, the first part specifies the row location of the "Camaro Z28" at the column "Model" ```[Cars['Model']=='Camaro Z28'```, and following that are the columns that we want to be displayed which are the model and the cylinder - ``` ['Model','cyl']]```

The output:
```
    Model	  cyl
23	Camaro Z28	8
```
The last problem, problem D which is to determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have. And in this problem we also utilize the ```.loc[]``` and because of the additional conditions, we'll need to use the syntax ```isin()``` 
The .isin() method in pandas is utilized to filter rows in a DataFrame or Series based on whether the values in a column or Series match a specified list of values. 

The code should appear as the following:
```
Cars.loc[Cars['Model'].isin(['Mazda RX4 Wag','Ford Pantera L','Honda Civic']), ['Model','cyl', 'gear']]
```

The output:
```
Model	    cyl	   gear
1	Mazda RX4 Wag	    6	    4
18	Honda Civic  	4    	4
28	Ford Pantera L  	8	    5
```
