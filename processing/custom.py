import pandas as pd

def read_dataset(path: str) -> pd.DataFrame:
    
    df = pd.read_csv(path)
    
    return df



def ambil_sebagian_kolom(data , kolom: list):
    temp = data.copy()
    
    return temp.loc[:, f"{kolom[0]}" : f"{kolom[1]}"]
    
