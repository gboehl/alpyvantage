# -*- coding: utf-8 -*-
import pandas as pd


def _format_to_pandas(call_response, data_key, meta_data_key='Meta Data', **kwargs):
    # mainly taken from alpha_vantage package: https://github.com/RomelTorres/alpha_vantage

    if data_key is not None:
        data = call_response[data_key]
    else:
        data = call_response
    if meta_data_key is not None:
        meta_data = call_response[meta_data_key]
    else:
        meta_data = None
    # Allow to override the output parameter in the call
    if isinstance(data, list):
        # If the call returns a list, then we will append them
        # in the resulting data frame. If in the future
        # alphavantage decides to do more with returning arrays
        # this might become buggy. For now will do the trick.
        if not data:
            data_pandas = pd.DataFrame()
        else:
            data_array = []
            for val in data:
                data_array.append([v for _, v in val.items()])
            data_pandas = pd.DataFrame(data_array, columns=[
                k for k, _ in data[0].items()])
            data_pandas.set_index('date', inplace=True)
    else:
        try:
            data_pandas = pd.DataFrame.from_dict(data,
                                                 orient='index',
                                                 dtype='float')
        # This is for Global quotes or any other new Alpha Vantage
        # data that is added.
        # It will have to be updated so that we can get exactly
        # The dataframes we want moving forward
        except ValueError:
            data = {data_key: data}
            data_pandas = pd.DataFrame.from_dict(data,
                                                 orient='index',
                                                 dtype='object')
            return data_pandas, meta_data
    data_pandas.index.name = 'date'
    # convert to pandas._libs.tslibs.timestamps.Timestamp
    data_pandas.index = pd.to_datetime(data_pandas.index)
    data_pandas.sort_index(inplace=True)
    try:
        data_pandas.columns = [col.split('. ')[1] for col in data_pandas.columns]
    except IndexError:
        # columns names don't have a dot in them
        pass    

    return data_pandas, meta_data
