
#Testing cleanup function 
from functiontools import functions as functions

def test_cleanup():
	df = pd.read_csv (r'data/raw_data/funding_data.csv')
	
	data = functions.cleanup(df, years)
	
	assert years is not None