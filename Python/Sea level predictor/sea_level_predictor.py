import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
   df = pd.read_csv('epa-sea-level.csv')
   x = df['Year']
   y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
   fig, ax = plt.subplots()
   plt.scatter(x, y) 
   


    # Create first line of best fit
   res = linregress(x, y)
   xpred = pd.Series([i for i in range(1880,2051)])
   ypred = res.slope*xpred+res.intercept
   plt.plot(xpred, ypred,'r')

    # Create second line of best fit
   df1 = df.loc[df['Year']>=2000]
   x1 = df1['Year']
   y1 = df1['CSIRO Adjusted Sea Level']
   res1 = linregress(x1, y1)
   xpred1 = pd.Series([i for i in range(2000,2051)])
   ypred1 = res1.slope*xpred1+res1.intercept
   plt.plot(xpred1, ypred1, 'g')


    # Add labels and title
   ax.set_xlabel('Year')
   ax.set_ylabel('Sea Level (inches)')
   ax.set_title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
   plt.savefig('sea_level_plot.png')
   return plt.gca()