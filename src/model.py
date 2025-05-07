from sklearn.neighbors import NearestNeighbors 
def train_model(data_path):
    df = pd.read_csv(data_path)
    model = NearestNeighbors().fit(df)
    return model