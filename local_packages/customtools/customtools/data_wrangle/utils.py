import numpy as np
import pandas as pd


# get numerical columns
def get_numerical_mask(df):
    """

    :param df: 

    """
    type_mask = []
    for i in df.dtypes:
        is_numeric = str(i).startswith('float') or str(i).startswith('int')

        if is_numeric:   # or str(i).startswith('bool')
            type_mask.append(True)
        else:
            type_mask.append(False)

    num_cols = list(np.array(df.columns)[type_mask])
    other_cols = list(np.array(df.columns)[[not elem for elem in type_mask]])

    return num_cols, other_cols


#TODO: perguntar ao Marcelo sobre essa função
def duplicate_cleanup(df, col_id):
    """drop duplicated rows from selected columns

    :param df: pandas.DataFrame  
    :param col_id: list of columns to account for duplicated rows/registers

    >>> import pandas as pd
        df = pd.DataFrame([[1, 2], [1, 2], [3, 4]], columns=['a', 'b'])
        duplicate_cleanup(df).values
    
    array([[1, 2],
       [3, 4]])
    """
    original_size = df.shape[0]
    col_subset = df.columns.to_list()
    n_duplicates = df[(df.duplicated(col_subset))].shape[0]

    df.drop_duplicates(col_subset, inplace=True)
    print('number of removed duplicates:', n_duplicates)

    true_duplicates = df[(df.duplicated(col_id))].shape[0]

    if true_duplicates != 0:
        raise ValueError('There are still duplicates to verify')

    return df
