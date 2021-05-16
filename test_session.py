#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 15:22:14 2021

@author: rampfire
"""


import pytest
import os
import inspect
import re
import session4 as program
import test_session
import math
CHECK_FOR_FUNCT_IMPL = ["time_it",
                        "squared_power_list",
                        "polygon_area",
                        "temp_converter",
                        "speed_converter"
                        ]


README_CONTENT_CHECK_FOR = ["time_it",
                        "squared_power_list",
                        "polygon_area",
                        "temp_converter",
                        "speed_converter"
                        ]


# Tests related to readme
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10, "Readme is not formatted properly"


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(program)
    spaces = re.findall('\n +.', lines)
    for count,space in enumerate(spaces):
        print(count,space)
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(program, inspect.isfunction)
    for function in functions:
        print(function)
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_count():
    functions = inspect.getmembers(test_session, inspect.isfunction)
    assert len(functions) > 20, 'Test cases seems to be low. Work harder man...'


def test_function_repeatations():
    functions = inspect.getmembers(test_session, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Test cases seems to be repeating...'


def test_time_it_for_valueerror():
    with pytest.raises(ValueError):
        program.time_it(print,repetitons = -1)


def test_time_it_for_typeerror():
    i = 0
    with pytest.raises(TypeError):
        program.time_it(i,repetitons = 1)

def test_squared_power_list():
    output = program.squared_power_list(2, start=0, end=5)
    assert set(output) == set([1, 2, 4, 8, 16, 32])

def test_polygon_area_triangle():
    assert math.isclose(program.polygon_area(2,sides = 3), 1.73 ,abs_tol=0.1)
     
def test_polygon_area_rectangle():
    assert math.isclose(program.polygon_area(2,sides = 4), 4 ,abs_tol=0.1)
     
def test_polygon_area_pentagon():
    assert math.isclose(program.polygon_area(2,sides = 5), 6.88191 ,abs_tol=0.1)

def test_polygon_area_hexagon():
    assert math.isclose(program.polygon_area(2,sides = 6), 10.39 ,abs_tol=0.1)

def test_polygon_area_for_valueerror():
    with pytest.raises(ValueError):
        program.polygon_area(2,sides = 7)

def test_temp_converter_c_to_f():
    assert math.isclose(program.temp_converter(0,temp_given_in = "c"),32.0)

def test_temp_converter_f_to_c():
    assert math.isclose(program.temp_converter(32,temp_given_in = "f"),0)

def test_temp_converter_valueerror():
    with pytest.raises(ValueError):
        program.temp_converter(32,temp_given_in = "g")

def test_temp_converter_typeerror():
    with pytest.raises(TypeError):
        program.temp_converter("a",temp_given_in = "f")

def test_speed_converter_valueerror():
    with pytest.raises(ValueError):
        program.speed_converter(speed = 100,dist = "mp",time = "s")

def test_speed_converter_kmph_mph():
    math.isclose(program.speed_converter(speed = 100,dist = "m",time = "hr"),100000.0)

def test_speed_converter_kmph_kmps():
    math.isclose(program.speed_converter(speed = 100,dist = "km",time = "s"),0.02777777777)

def test_speed_converter_kmph_kmpday():
    math.isclose(program.speed_converter(speed = 100,dist = "km",time = "day"),2399.998)

def test_speed_converter_typeerror():
    with pytest.raises(TypeError):
        program.speed_converter(speed = "a",dist = "m",time = "s")
