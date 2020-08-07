def create_rating_mat(rating_data,items_id_list,user_id_col='user_id',item_id_col='item_id'):
    '''
    Create rating matrix from rating data information.
    Arguments: 
        - rating_data: pd.DataFrame, the records of ratings 
        - items_id_list: strings' list
    '''
    rating_mat = pd.DataFrame(columns=['user_id']+items_id_list)
    grps = rating_data.groupby(user_id_col)
    for index,df in grps:
        user_rating = {user_id_col: index}
        for _, row in df.iterrows():
            user_rating[row[item_id_col]] = row['rating']
        rating_mat = rating_mat.append(user_rating,ignore_index=True)
    return rating_mat.set_index(user_id_col)
