import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='steelblue', label='Original Data')

    # Create first line of best fit (using all data)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create an extended range of years from 1880 to 2050 for the first prediction line
    x_pred_all = pd.Series([i for i in range(1880, 2051)])
    y_pred_all = res_all.slope * x_pred_all + res_all.intercept
    ax.plot(x_pred_all, y_pred_all, color='red', label='Best Fit Line 1 (1880-2050)')

    # Create second line of best fit (using data from 2000 through the most recent year)
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    
    # Create an extended range of years from 2000 to 2050 for the second prediction line
    x_pred_2000 = pd.Series([i for i in range(2000, 2051)])
    y_pred_2000 = res_2000.slope * x_pred_2000 + res_2000.intercept
    ax.plot(x_pred_2000, y_pred_2000, color='green', label='Best Fit Line 2 (2000-2050)')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()