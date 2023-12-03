import sys

import numpy as np
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

from utils import *


class KNNRecommender:
    """
    Recommender based on KNN
    """

    def __init__(self, n_neighbors=10):
        self.n_neighbors = n_neighbors
        self.model = NearestNeighbors(metric='cosine', n_neighbors=n_neighbors)

    def fit(self, X):
        self.model.fit(X)

    def _predict(self, tfidf, user_index):
        """
        Predicts movies for user
        :param tfidf: TF-IDF matrix
        :param query_index: user index
        :return: list of movie ids
        """
        self.fit(csr_matrix(tfidf))

        distances, idx = self.model.kneighbors(tfidf[user_index, :].reshape(1, -1))

        results = []
        for i in range(0, len(distances.flatten())):
            tmp_idx = idx.flatten()[i]
            results.append(tmp_idx)

        return results

    def evaluate(self, rating_test, tfidf):
        """
        Evaluates recommender
        :param rating_test: Test dataset
        :param tfidf: TF-IDF matrix
        :return: hit rate and RMSE
        """
        hits = 0
        watched_movies_list = []
        predicted_movies_list = []

        # get predictions
        for user_id in rating_test['user_id'].unique():
            # get all movies that user watched
            watched_movies = rating_test[rating_test['user_id'] == user_id]['item_id'].tolist()
            watched_movies_list.append(watched_movies)

            predicted_movies = self._predict(tfidf, user_id)
            predicted_movies_list.append(predicted_movies)

        # calculate hit rate
        for i in range(len(watched_movies_list)):
            watched_movies = watched_movies_list[i]
            predicted_movies = predicted_movies_list[i]

            # check if any of predicted movies is in watched
            for movie_id in predicted_movies:
                if movie_id in watched_movies:
                    hits += 1
                    break

        hits = hits / rating_test['user_id'].nunique()

        # calculate MSE
        mse = 0
        for i in range(len(watched_movies_list)):
            watched_movies = watched_movies_list[i]
            predicted_movies = predicted_movies_list[i]

            # check if any of predicted movies is in watched
            for movie_id in predicted_movies:
                if movie_id in watched_movies:
                    mse += (1 - predicted_movies.index(movie_id) / self.n_neighbors) ** 2
                    break

        mse = mse / rating_test['user_id'].nunique()
        rmse = np.sqrt(mse)

        return hits, rmse


if __name__ == "__main__":
    # load data
    if len(sys.argv) > 1:
        BASE_DATASET_NAME = sys.argv[1]
        TEST_DATASET_NAME = sys.argv[2]
    else:
        BASE_DATASET_NAME = 'u1.base'
        TEST_DATASET_NAME = 'u1.test'

    rating_train = load_movielens_ratings(BASE_DATASET_NAME)
    rating_test = load_movielens_ratings(TEST_DATASET_NAME)

    item_info = load_movielens_item_info()
    movies = load_movielens_item_info()

    # load genres
    genres_path = os.path.join(DATASET_PATH_100K_MOVIELENS, "u.genre")
    genres = pd.read_csv(genres_path, sep='|', header=None, names=['genre', 'id'])
    genres_as_list = genres['genre'].tolist()

    # unite columns on genres in lists respectively
    movies['genres'] = movies.iloc[:, 5:].values.tolist()
    movies['genres'] = movies['genres'].apply(lambda x: [genres_as_list[i] for i, v in enumerate(x) if v == 1])
    movies.drop(movies.columns[5:24], axis=1, inplace=True)

    # create TF-IDF matrix
    tfidf = TfidfVectorizer(tokenizer=lambda x: x, lowercase=False)
    tfidf_genres = tfidf.fit_transform(movies['genres'])

    # create recommender
    recommender = KNNRecommender(n_neighbors=50)

    # evaluate recommender
    hits, rmse = recommender.evaluate(rating_test, tfidf_genres)
    print("Hit rate: {}".format(hits))
    print("RMSE: {}".format(rmse))
