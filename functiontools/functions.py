#Adding required packages
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import wavfile


#Data Cleanup Function 

def cleanup(df, years):
    # replace + and - and * so they are coded as missing
    df = df.replace('+', np.NaN, regex=False)
    df = df.replace('-', np.NaN, regex=False)
    df = df.replace('*', np.NaN, regex=False)
    
    # remove $ sign
    df[years] = df[years].replace('[\$,]', '', regex=True).astype(float)

    # remove , in mortality
    df['2019_US_Mortality_19'] = df['2019_US_Mortality_19'].replace('[,,]', '', regex=True).astype(float)
    pd.to_numeric(df['2019_US_Mortality_19'])
    
    return df

def change_to_float(data):
    return data.replace('[\$,]', '', regex=True).astype(float)

