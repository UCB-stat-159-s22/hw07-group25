#Adding required packages
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import wavfile


#Data Cleanup Function 



def cleanup(df, years):
	
	"""This function cleans NIH funding data to remove problematic excel formatting

    Parameters:
    df: pandas dataframe of NIH funding data that you want to remove +, -, * symbols from as well as dollar signs and commas from numerical values.
	years: the number of years in your data set (column headers based on NIH format that you want to fix the formatting of

    Returns:
    df: cleaned data frame

   """
    # replace + and - and * so they are coded as missing
	df = df.replace('+', np.NaN, regex=False)
	df = df.replace('-', np.NaN, regex=False)
	df = df.replace('*', np.NaN, regex=False)
	
	# remove $ sign
	df[years] = df[years].replace('[\$,]', '', regex=True).astype(float)

	# remove , in mortality
	df['2019_US_Mortality_19'] = df['2019_US_Mortality_19'].replace('[,,]', '',regex=True).astype(float)
	pd.to_numeric(df['2019_US_Mortality_19'])
	
	return df

def draw_barchart(df, year):
	
	"""This function draws a barchart of NIH funding data

    Parameters:
    df: pandas dataframe of NIH funding data.
	year: the year that you want to draw the barchart for

    Returns:
    plot

   """

	datayear = df[["research_category", year]]
    
	# Based on the year it will output a top 10 spending categories for that year
	datayear[year] = datayear[year].replace('[\$,]', '', regex=True).astype(float)
	datayeartop10 = datayear.sort_values(year, ascending=False)[:10]
    
	fig, ax = plt.subplots(figsize=(15, 8))
    
	# Graphs a top 10 for the categories in that year
	ax.barh(datayeartop10["research_category"],datayeartop10[year])
	ax.set_title("Top 10 Spending Categories")
	ax.set_xlabel("Spending ($)")
	ax.set_ylabel("Spending Category")
	ax.grid(which='major', axis='x', linestyle='-')
	plt.savefig('figures/fig1b.png');


def change_to_float(data):
	
	'''data is a column in a dataframe where you need to remove dollar signs and convert to float'''
	
	return data.replace('[\$,]', '', regex=True).astype(float)

