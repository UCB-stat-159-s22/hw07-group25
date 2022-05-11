
#Testing cleanup function 
from functiontools import functions as functions
import numpy
import matplotlib.pyplot as plt
import pandas as pd

def test_cleanup():
	df = pd.read_csv (r'data/raw_data/funding_data.csv')
	years = ['2011','2012','2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
	
	df = functions.cleanup(df, years)
	
	#Testing to see "$" was deleted
	assert df["2011"].values[2] == 69
	

# Testing draw_barchart function
def test_draw_barchart():
    img = plt.imread('figures/fig1b.png')
    assert img is not None
	

#Third Test Function to test float_change function

#def test_to_float():
	#df = pd.read_csv (r'data/raw_data/funding_data.csv')
	#data2019 = df[["research_category", "2019"]]
	
	#dff = functions.change_to_float(data2019["2019"])
	
	#assert type(dff["2019"].values[2]) == numpy.float64
   