import re
import pandas as pd
import requests
import inspect


def _format_to_pandas(call_response, data_key):
    # mainly stolen from alpha_vantage package
    meta_data_key = 'Meta Data'

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
    data_pandas.columns = [col.split('. ')[1] for col in data_pandas.columns]
    return data_pandas, meta_data


class API(object):

    raw_url = 'https://www.alphavantage.co/query?'

    def __init__(self, api_key):
        self.key = api_key

    def time_series_intraday(self, symbol, interval='1min', outputsize='full', **kwargs):
        this_frame = inspect.currentframe()
        func_args, _, _, func_values = inspect.getargvalues(this_frame)
        kwargs.update({'function': 'TIME_SERIES_INTRADAY', 'apikey': self.key})
        kwargs.update({k:v for k,v in func_values.items() if k in func_args and k != 'self'})
        
        url = self.raw_url + '&'.join([k + '=' + str(kwargs[k]) for k in kwargs])
        data_key = "Time Series ({})".format(interval)
        r = requests.get(url)
        data_raw = r.json()
        return _format_to_pandas(data_raw, data_key)


