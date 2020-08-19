# Functional Parameters

## time_it()
This function receives a function object, certain paramters in the form of args and kwargs, as weel as the number of times the function needs to be executed.

It returns the average duration taken for execution of the given function using the paramters given 

## print()
This is one of the functions that can be passed to time_it. We can pass any number of parameters that need to be concatenated together, using a separator (denoted by 'sep') and ends with a string specified using 'end'. 

## squared_power_list()
This function taken in a number 'N' and 2 more integers using the keywords, 'start' and 'end'. 

It returns a list of all numbers formed by 'N' raised to the powers starting from the value denoted by 'start' till the value denoted by 'end'.

## polygon_area()
This function accepts the length of the sides, and the number of sides, and outputs the area of the regular polygon.

The function is only capable of calculating areas for triangle, square, regular pentagon and regular hexagon. 

## temp_convertor()
This function accepts a temperature value either in Farenheit or Celcius and converts that to the other format. 

## speed_convertor()
This function accepts speed given by the user in kmph and converts that into the specified units , ie., of length and time chosen by the user.


# Unit tests
A total of **35** unit tests have been written for ensuring proper usage of the functions. They are mentioned below:


### Edge cases for repetition value (Time it function)

1. It should be an integer
2. It should not be a negative Value

### Edge cases for print function

1. Parameter tuple (args) cannot be empty

### Edge cases for squared power list

1. Parameter tuple (args) cannot be empty
2. Parameter tuple (args) only have 1 value
3. Argument should be an integer
4. 'end' value should be greater than 'start' value
5. Both 'end' and 'start' values should be greater than 0

### Edge cases for Polygon area

1. Parameter tuple (args) cannot be empty
2. Parameter tuple (args) only have 1 value
3. Argument should be an integer
4. Arugment cannot be negative.
5. Value of 'sides' should be between 3 and 6 (inclusive)

### Edge Cases Temperature Converter

1. Parameter tuple (args) cannot be empty
2. Parameter tuple (args) only have 1 value
3. Argument should be an integer
4. Unit other than 'f' or 'c' cannot be specified
5. 'f' value passed cannot be lesser than -459 (0 kelvin)
6. 'c' value passed cannot be lesser than -273 (0 kelvin)


### Normal Functioning by testing the 5 sample functions provided

time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100)
time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitions=5)
time_it(squared_power_list, 2, start=0, end=5, repetitions=5) 
time_it(polygon_area, 15, sides = 3, repetitions=10) 
time_it(speed_converter, 100, dist='km', time='min', repetitions=200)


### Checking the mathematical correctness of all functions

1. temp_convertor : Converted 32F to 0C successfully. 
2. temp_convertor : Converted 0C to 32F successfully. 
3. squared_power_list : For n=2 , start =0 and end =5, output is ['1','2','4','8','16','32']
4. polygon_area : Area of triangle with side 15 is equal to 112,5
5. speed_converter : 18 kmph was converted to 5 m/s 


### Basic tests that are usually conducted

1. Readme exists or not.
2. Readme has above 500 words or not
3. Readme contents 
4. Readme formatting
5. Spacing in the code
6. Formatting of function names