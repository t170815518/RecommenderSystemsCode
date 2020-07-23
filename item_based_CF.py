import pandas as pd
import numpy as np


def item_based_CF(ratings,items_list,item_id_col='item_id'):
    '''
    Find similarity between items in items_list and other items.
    arguments:
        ratings: pd.DataFrame, the ratings records
        items_list: list, containing the target items' index
        item_id_col: str, the column name for items' id in ratings; default is 'item_id'
    return: pd.DataFrame
    '''
    grp = ratings.groupby(item_id_col)
    average = average_rating(ratings)
    row_list = []

    for i in items_list:
        x_aver = average.iloc[i-1]
        for j in grp.groups.keys():
            if i == j:
                continue
            users = common_users(grp, i, j)
            if users.empty:
                simi = np.nan
            else:
                simi = item_similarity(users, x_aver, y_aver=average.iloc[j-1])
            d = {'x': i, 'y': j, 'similarity': simi}
            row_list.append(d)
            # print(d)
    return pd.DataFrame(row_list)


def item_similarity(users, x_aver, y_aver):
    '''
    To calculate the similarity between x and y, using Pearson's correlation.
    arguments:
        -users: pd.DataFrame, containing users who rate both x and y
        -x_aver: float, average rating on x
        -y_aver: float, average rating on y
    return: float
    warnings: When std of either x or y is 0, np.nan is returned
    '''
    users['x-bar'] = users['rating_x'].apply(lambda x: x-x_aver)
    users['y-bar'] = users['rating_y'].apply(lambda x: x-y_aver)
    cov = users.apply(lambda x: x['x-bar']*x['y-bar'], axis=1).sum()
    var_mul = (users['x-bar']**2).sum()*(users['y-bar']**2).sum()
    if var_mul == 0:
        return np.nan
    pc = cov/var_mul**0.5
    return cov/var_mul**0.5


def average_rating(ratings):
    '''
    arguments:
        -ratings: pd.DataFrame of ratings.
    return: pd.DataFrame on average rating for items.
    '''
    return ratings[['item_id', 'rating']].groupby('item_id').mean()


def common_users(grps,x,y):
    '''
    To return the DataFrame on the users, who rate both x and y.
    arguments:
        - grps: groupby object by item_id
        - x,y: the index
    return: DataFrame
    warnings: When no common user, warning will be printed
    '''
    x_ = grps.get_group(x)
    y_ = grps.get_group(y)
    df = pd.merge(x_, y_, how='inner', on=['user_id'])
    if df.empty:
        print('Warning: No user rate both Item {} and {}'.format(x, y))
    return df


if __name__ == '__main__':
    rpath = "./test/MovieLens/"
    columns = ['movie_id', 'movie_title', 'release_date', 'video_release_date', 'IMDb_url', 'unknown', 'Action',
               'Adventure', 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
               'Film_Noir',
               'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
    items_data = pd.read_csv(rpath + 'u.item', sep='|', names=columns, encoding='ISO-8859-1', index_col='movie_id')

    columns = ['user_id', 'item_id', 'rating', 'timestamp']
    rating_data = pd.read_csv(rpath + 'u.data', sep='\t', names=columns, encoding='ISO-8859-1')

    # print(average_rating(rating_data))
    a = item_based_CF(rating_data, items_list=[5])
