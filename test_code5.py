import subprocess
import sys
import pytest
import code5
from code5 import *
import time
import os.path
import re
import inspect 

README_CONTENT_CHECK_FOR = [
    'time_it()',
    'print()',
    'squared_power_list()',
    'polygon_area()',
    'temp_convertor()',
    'speed_convertor()',
]

# Basic Functions 

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_fourspace():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(code5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(code5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"



# Edge cases for repetition value:

# Negative Value
def test_rep_neg():
    with pytest.raises(AssertionError):
        time_it(polygon_area, 15, sides = 5, repetitions= -10)

# Non-integer value
def test_rep_nonint():
    with pytest.raises(AssertionError):
        time_it(polygon_area, 15, sides = 5, repetitions= 'a')




# Edge cases for print function

# No value given
def test_print_novalue():
    with pytest.raises(AssertionError):
        time_it(print, sep='-', end= ' ***\n', repetitions=5)




# Edge cases for squared power list

# No value given
def test_squared_novalue():
    with pytest.raises(AssertionError):
        time_it(squared_power_list, start=0, end=5, repetitions=1) 
        
# More than one argument passed
def test_squared_multiple():
    with pytest.raises(AssertionError):
        time_it(squared_power_list, 2,5, start=0, end=5, repetitions=1) 
        
# Non integer value passed
def test_squared_nonint():
    with pytest.raises(AssertionError):
        time_it(squared_power_list, 'a', start=0, end=5, repetitions=1) 
        
# End value greater than start value
def test_squared_endvalue():
    with pytest.raises(AssertionError):
        time_it(squared_power_list, 'a', start=5, end=0, repetitions=1) 

# Ensure start and end value greater than zero
def test_squared_startend_zero():
    with pytest.raises(AssertionError):
        time_it(squared_power_list, 'a', start=-1, end=5, repetitions=1) 
        time_it(squared_power_list, 'a', start=0, end=-5, repetitions=1)




# Edge cases for Polygon area

# No arguments given
def test_polygon_novalue():
    with pytest.raises(AssertionError):
        time_it(polygon_area, sides = 3, repetitions=10)

# More than one argument given
def test_polygon_multiple():
    with pytest.raises(AssertionError):
        time_it(polygon_area, 15, 10, sides = 3, repetitions=10)
        
# Negative argument
def test_polygon_negative():
    with pytest.raises(AssertionError):
        time_it(polygon_area, -10, sides = 3, repetitions=10)
        

# Non-integer argument
def test_polygon_multiple():
    with pytest.raises(AssertionError):
        time_it(polygon_area, 'a', sides = 3, repetitions=10)


# #Sides to be between 3 and 6
def test_polygon_side():
    with pytest.raises(AssertionError):
        time_it(polygon_area, 'a', sides =2, repetitions=10)
        time_it(polygon_area, 'a', sides =7, repetitions=10)




# Edge Cases Temperature Converter
    
# No arguments given
def test_temp_novalue():
    with pytest.raises(AssertionError):
        time_it(temp_converter, temp_given_in = 'c', repetitions=10) 

# More than one argument given
def test_temp_multiple():
    with pytest.raises(AssertionError):
        time_it(temp_converter, 100, 45, temp_given_in = 'c', repetitions=10) 
        
# Non-integer argument given
def test_temp_nonint():
    with pytest.raises(AssertionError):
        time_it(temp_converter, '100', temp_given_in = 'c', repetitions=10) 
        
# Unit other than 'f' or 'c' specified
def test_temp_unit():
    with pytest.raises(AssertionError):
        time_it(temp_converter, 100, temp_given_in = 'k', repetitions=10) 
        
# 'f' value passed cannot be lesser than -459 (0 kelvin)
def test_temp_f_legal():
    with pytest.raises(AssertionError):
        time_it(temp_converter, -1000, temp_given_in = 'f', repetitions=10) 
        
# 'c' value passed cannot be lesser than -273 (0 kelvin)
def test_temp_c_legal():
    with pytest.raises(AssertionError):
        time_it(temp_converter, -300, temp_given_in = 'c', repetitions=10) 



# Normal Functioning by testing the 5 sample functions provided

# Temp Converter
def test_temp_test():
    t, value = time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100)
    assert isinstance(t, float), 'Improper functioning of temp converter'
    

# Print
def test_print_test():
    t, value = time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitions=5)
    assert isinstance(t, float), 'Improper functioning of temp converter'
    

# Squared Power List
def test_squared_test():
    t, value = time_it(squared_power_list, 2, start=0, end=5, repetitions=5) 
    assert isinstance(t, float), 'Improper functioning of temp converter'
    

# Polygon Area
def test_polygon_test():
    t, value = time_it(polygon_area, 15, sides = 3, repetitions=10) 
    assert isinstance(t, float), 'Improper functioning of temp converter'
    

# Speed Converter
def test_speed_test():
    t, value = time_it(speed_converter, 100, dist='km', time='min', repetitions=200)
    assert isinstance(t, float), 'Improper functioning of temp converter'




# Checking the mathematical correctness of all functions

# c to f
def test_temp_test1():
    t, value = time_it(temp_converter, 32, temp_given_in = 'f', repetitions=10)
    assert value == 0, 'Improper functioning of temp converter from f to c'

    
# f to c
def test_temp_test2():
    t, value = time_it(temp_converter, 0, temp_given_in = 'c', repetitions=10)
    assert value == 32, 'Improper functioning of temp converter from c to f'


# Squared Power List
def test_squared_test():
    t, value = time_it(squared_power_list, 2, start=0, end=5, repetitions=10) 
    assert value  == [1,2,4,8,16,32], 'Improper functioning of Squared Power List function'
    

# Polygon Area
def test_polygon_test():
    t, value = time_it(polygon_area, 15, sides = 3, repetitions=10) 
    assert value == 112.5, 'Improper functioning of Polygon area function'
    

# Speed Converter
def test_speed_test():
    t, value = time_it(speed_converter, 18, dist='m', time='s', repetitions=10)
    assert value == 5, 'Improper functioning of speed converter'