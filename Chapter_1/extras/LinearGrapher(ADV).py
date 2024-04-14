#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 12:43:19 2024

@author: A.B
"""

import matplotlib.pyplot as plt

def generate_y_values(x_values, m, b, x_translation=0, y_translation=0):
    """
    Function to generate y values for a given range of x values with optional translations.
    """
    y_values = [m * (x - x_translation) + b + y_translation for x in x_values]
    return y_values

def draw_graph(x_values, y_values):
    """
    Function to draw the graph with a four quadrant setup.
    """
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title("Graph of y = mx + b with Translations")
    plt.grid(True)
    
    # Set the limits of the x and y axes to display four quadrants
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    
    # Add horizontal and vertical lines at x=0 and y=0
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    plt.show()


def main():
    """
    Main function to get user input and draw the graph.
    """
    # Prompt the user for parameters
    m = float(input("Please enter the slope value (m): "))
    b = float(input("Please enter the y-intercept value (b): "))
    x_translation = float(input("Please enter the translation along the x-axis: "))
    y_translation = float(input("Please enter the translation along the y-axis: "))

    # Define the range of x values
    x_min = -10
    x_max = 10
    step = 0.1
    x_values = [i for i in range(x_min, x_max + 1)]  # Generate x values from x_min to x_max

    # Generate corresponding y values using the equation y = mx + b with translations
    y_values = generate_y_values(x_values, m, b, x_translation, y_translation)

    # Draw the graph
    draw_graph(x_values, y_values)

if __name__ == "__main__":
    main()
