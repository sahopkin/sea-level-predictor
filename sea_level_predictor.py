import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    

    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    x_len = len(x)

    df_2000 = df[df['Year'] >= 2000]
    
    

    x_2000 = df_2000['Year']
    y_2000 = df_2000['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(x, y)


    # Create first line of best fit
    ln_reg1 = linregress(x, y)
    x_2050 = np.linspace(1880, 2050, 171)
    y_reg1 = ln_reg1.slope * x_2050 + ln_reg1.intercept
    plt.plot(x_2050, y_reg1, c='r')
    

    # Create second line of best fit
    ln_reg2 = linregress(x_2000, y_2000)
    x2 = np.linspace(2000, 2050, 51)
    y_reg2 = ln_reg2.slope * x2 + ln_reg2.intercept
    plt.plot(x2, y_reg2, c='g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()