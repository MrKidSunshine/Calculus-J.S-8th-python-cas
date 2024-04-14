#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:45:03 2024

@author: A.B
"""

#this program will help you plot y = mx + b

import matplotlib.pyplot as plt

m = float(input("Please enter the slope value: "))
b = float(input("Please enter the y-intercept value: "))

# Function to generate y values for a given range of x values
def generate_y_values(x_values, m, b):
    y_values = [m * x + b for x in x_values]
    return y_values

# Function to draw the graph
def draw_graph(x_values, y_values):
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title("x vs y")
    plt.grid(True)
    plt.show()

# Define the range of x values
x_min = -10
x_max = 10
step = 0.1
x_values = [i for i in range(x_min, x_max + 1)]  # Generate x values from x_min to x_max



# Generate corresponding y values using the equation y = mx + b
y_values = generate_y_values(x_values, m, b)

# Draw the graph
draw_graph(x_values, y_values)

