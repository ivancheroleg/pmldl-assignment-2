import os
import pandas as pd

DATASET_PATH_100K_MOVIELENS = "../data/raw/ml-100k/"


def load_movielens_info():
    """
    Load the info file from the movielens dataset
    :return: a dataframe with the info
    """
    path = os.path.join(DATASET_PATH_100K_MOVIELENS, "u.info")
    names = ["count", "type"]
    info = pd.read_csv(path, sep=" ", header=None, names=names)
    return info


def load_movielens_ratings(partition):
    """
    Load the ratings file from the movielens dataset
    :return: a dataframe with the ratings
    """
    path = os.path.join(DATASET_PATH_100K_MOVIELENS, partition)
    names = ["user_id", "item_id", "rating", "timestamp"]
    ratings = pd.read_csv(path, sep="\t", header=None, names=names)
    return ratings


def load_movielens_item_info():
    """
    Load the item info file from the movielens dataset
    :return: a dataframe with the item info
    """
    path = os.path.join(DATASET_PATH_100K_MOVIELENS, "u.item")
    names = [
        "movie_id",
        "movie_title",
        "release_date",
        "video_release_date",
        "IMDb_URL"]

    # load genres
    genres_path = os.path.join(DATASET_PATH_100K_MOVIELENS, "u.genre")
    genres = pd.read_csv(genres_path, sep='|', header=None, names=['genre', 'id'])
    genres_as_list = genres['genre'].tolist()

    names.extend(genres_as_list)

    item_info = pd.read_csv(path, sep="|", header=None, names=names, encoding="latin-1")
    return item_info


def load_movielens_user_info():
    """
    Load the user info file from the movielens dataset
    :return: a dataframe with the user info
    """
    path = os.path.join(DATASET_PATH_100K_MOVIELENS, "u.user")
    names = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
    user_info = pd.read_csv(path, sep='|', header=None, names=names)
    return user_info


def load_movielens_occupation():
    """
    Load the user info file from the movielens dataset
    :return: a dataframe with the user info
    """
    path = os.path.join(DATASET_PATH_100K_MOVIELENS, "u.occupation")
    names = ['occupation']
    occupation_info = pd.read_csv(path, sep=' ', header=None, names=names)
    return occupation_info
