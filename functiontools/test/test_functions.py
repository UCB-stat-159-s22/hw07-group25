
#Testing cleanup function 
from functiontools import functions as functions
import numpy

def test_cleanup():
	df = pd.read_csv (r'data/raw_data/funding_data.csv')
	years = ['2011','2012','2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
	
	df = functions.cleanup(df, years)
	
	#Testing to see "$" was deleted
	assert df["2011"].values[2] == 69
	
	
def test_to_float():
	df = pd.read_csv (r'data/raw_data/funding_data.csv')
	
	df = functions.change_to_float(df)
	
	assert type(df["2011"].values[2]) == numpy.float64
	
	