from sklearn.neighbors import NearestNeighbors
model = NearestNeighbors(n_neighbors=3).fit(user_item_matrix) # type: ignore