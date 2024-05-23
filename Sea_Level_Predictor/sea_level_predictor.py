import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # print(df)
    # Create scatter plot
    plt.scatter(
        data=df,
        x='Year',
        y='CSIRO Adjusted Sea Level',
        c='darkorange')

    # Create first line of best fit
    slope, y_intp, corr_coef, prob, std_err = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level'])
    start_year = df['Year'].min()
    end_year = 2050
    years = list(range(start_year, end_year + 1))
    sea_levels = [slope * year + y_intp for year in years]
    plt.plot(years, sea_levels, 'royalblue')

    # Create second line of best fit
    df_rec = df[df['Year'] >= 2000]
    slope_rec, y_intp_rec, corr_coef_rec, prob_rec, std_err_rec = linregress(
        df_rec['Year'], df_rec['CSIRO Adjusted Sea Level'])
    recent_years = list(range(2000, 2051))
    recent_sea_levels = [slope_rec * year +
                         y_intp_rec for year in recent_years]
    plt.plot(recent_years, recent_sea_levels, 'forestgreen')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
