import pandas as pd 
def clean_data(raw_path, output_path):
    df = pd.read_csv(raw_path)
    df.dropna(inplace=True)
    df.to_csv(output_path, index=False)