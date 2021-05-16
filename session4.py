#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 23:18:43 2021

@author: rampfire
"""


import time
import math

def time_it(fn, *args, repetitons=1, **kwargs):
    if repetitons < 0:
        raise ValueError(f"repetitons cannot be less than zero")
    start_time = time.perf_counter()

    for i in range(repetitons):
        fn(*args, **kwargs)

    return (time.perf_counter()-start_time)/repetitons

def squared_power_list(num,*,start=0, end=5):
    return [num**i for i in range(start,end+1)]

def polygon_area(side_length,*,sides):
    sqrt_3 = math.sqrt(3)
    if sides not in [3,4,5,6]:
        raise ValueError("sides not valid")
    area = {3:(sqrt_3/4)*(side_length**2),
            4:side_length**2,
            5:(1/4)*math.sqrt(5*(5+(2*math.sqrt(5))))*(side_length**2),
            6:(3/2)*sqrt_3*(side_length**2)}
    return area[sides]

def temp_converter(temp,*,temp_given_in):
    if temp_given_in =="c":
        return (temp*(9/5)) + 32
    elif temp_given_in == "f":
        return (temp - 32)*(5/9)
    else:
        raise ValueError("temp_given_in not valid")

def speed_converter(speed,*,dist,time):
    km_conv = {"km":1,"m":1000,"ft":3280,"yrd":1093}
    time_conv = {"hr":1,"day":0.0416667,"m":60,"s":3600,"ms":3600000}
    if (dist not in km_conv.keys()) or (time not in time_conv.keys()):
        raise ValueError("dist or time units invalid")
    return speed*(km_conv[dist]/time_conv[time])