import pandas as pd


def data_postprocessing(data_table, k):
    unique_users = set(data_table['userId'].values.tolist())
    temp_df = pd.DataFrame()

    for i in unique_users:
        tmp = data_table[data_table['userId'] == i]
        tmp_df = pd.DataFrame()
        if tmp.shape[0] >= k:
            tmp = tmp.sort_values(by='rating', ascending=False).head(k)
            tmp_df['userId'] = [i]
            tmp_df['movies'] = [tmp['movieId'].values.tolist()]
            temp_df = temp_df.append(tmp_df)
        else:
            None

    return temp_df


def hit_rate_at_k(y_true, y_pred):

    y_true_list = y_true['movies'].values.tolist()
    y_pred_list = y_pred['movies'].values.tolist()

    s = 0
    l = 0

    for i in range(y_true.shape[0]):
        a = y_true_list[i]
        b = y_pred_list[i]
        TP = len(set(a).intersection(set(b)))
        N = len(y_true_list[i])
        s += TP/N
        l += 1
    hit_rate = s/l
    return hit_rate


def evaluate(data_table_pred, data_table_true, k: int = 10):
    y_true = data_postprocessing(data_table_true, k)
    y_pred = data_postprocessing(data_table_pred, k)
    hr = hit_rate_at_k(y_true, y_pred)
    return hr
