import pandas as pd 
import numpy as np

def process_nan(data):
    temp = data.copy()
    
    temp = temp.fillna(method = "ffill")
    
    return temp

def transform_log(data : pd.DataFrame) : 
    temp = data.copy()
    for col in temp.columns:
        temp[col] = list(map(lambda x: np.log(x) , temp[col]))
    
    return temp