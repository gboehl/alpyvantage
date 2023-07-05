import requests
from .data_formating import _format_to_pandas
from .__version__ import __version__


class API(object):
    """Base class storing the API key and some options
    """

    raw_url = 'https://www.alphavantage.co/query?'

    def __init__(self, api_key, to_pandas=True, outputsize='full'):
        """Initialize the API
        Parameters
        ----------
        api_key : string
            the API key as a string
        to_pandas : bool, optional
            whether to return time series as pandas.DataFrame, `True` by default
        outputsize : bool, optional
            return full output by default for any call
        """
        self.key = api_key
        self.use_pandas = to_pandas
        self.outputsize = outputsize

    def __call__(self, function, data_key=None, **kwargs):
        """API call. Requires the function as in the original Alpha Vantage documentation (https://www.alphavantage.co/documentation/) and takes the API key as given
        Parameters
        ----------
        function : string
            the API call function
        data_key : string or None, optional
            the key for the data in the returned json object
        kwargs : dict
            any other optional keyword(s)
        Returns
        -------
        data : dict or pandas.DataFrame
            the requested data
        meta_data : None or dict
            the meta data if data is a DataFrame
        """

        # using python to download csv files is not very interesting
        if 'datatype' in kwargs:
            raise NotImplementedError(
                "The 'datatype' API parameter is not implemented.")

        # build url from keywords args
        kwargs.update({'function': function, 'apikey': self.key})
        url = self.raw_url + \
            '&'.join([k + '=' + str(kwargs[k]) for k in kwargs])
        r = requests.get(url)
        data_raw = r.json()

        # API error handling
        if 'Note' in data_raw:
            raise AlphaVantageError(data_raw['Note'])
        if 'Information' in data_raw:
            raise AlphaVantageError(data_raw['Information'])

        # return as pandas dataframe if desired
        if self.use_pandas and data_key is not None:
            return _format_to_pandas(data_raw, data_key)
        else:
            return data_raw, None

    def time_series_intraday(self, symbol, interval='1min', **kwargs):
        """API call to TIME_SERIES_INTRADAY
        Parameters
        ----------
        symbol : string
            the ticker symbol
        interval : string, optional
            data frequency, defaults to '1min'. See the original Alpha Vantage documentation (https://www.alphavantage.co/documentation/) for options.
        kwargs : dict
            any other optional keyword(s)
        Returns
        -------
        data : dict or pandas.DataFrame
            the requested data
        meta_data : None or dict
            the meta data if data is a DataFrame
        """
        kwargs.update({'symbol': symbol, 'interval': interval,
                      'outputsize': self.outputsize})
        return self.__call__('TIME_SERIES_INTRADAY', data_key=f"Time Series ({interval})", **kwargs)

    def time_series_daily(self, symbol, **kwargs):
        """API call to TIME_SERIES_DAILY
        Parameters
        ----------
        symbol : string
            the ticker symbol
        kwargs : dict
            any other optional keyword(s)
        Returns
        -------
        data : dict or pandas.DataFrame
            the requested data
        meta_data : None or dict
            the meta data if data is a DataFrame
        """
        kwargs.update({'symbol': symbol, 'outputsize': self.outputsize})
        return self.__call__('TIME_SERIES_DAILY', data_key=f"Time Series (Daily)", **kwargs)

    def time_series_daily_adjusted(self, symbol, **kwargs):
        """API call to TIME_SERIES_DAILY_ADJUSTED
        Parameters
        ----------
        symbol : string
            the ticker symbol
        kwargs : dict
            any other optional keyword(s)
        Returns
        -------
        data : dict or pandas.DataFrame
            the requested data
        meta_data : None or dict
            the meta data if data is a DataFrame
        """
        kwargs.update({'symbol': symbol, 'outputsize': self.outputsize})
        return self.__call__('TIME_SERIES_DAILY_ADJUSTED', data_key=f"Time Series (Daily)", **kwargs)

    def time_series_weekly(self, symbol, **kwargs):
        """API call to TIME_SERIES_WEEKLY
        Parameters
        ----------
        symbol : string
            the ticker symbol
        kwargs : dict
            any other optional keyword(s)
        Returns
        -------
        data : dict or pandas.DataFrame
            the requested data
        meta_data : None or dict
            the meta data if data is a DataFrame
        """
        kwargs.update({'symbol': symbol, 'outputsize': self.outputsize})
        return self.__call__('TIME_SERIES_WEEKLY', data_key=f"Weekly Time Series", **kwargs)

    def time_series_weekly_adjusted(self, symbol, **kwargs):
        """API call to TIME_SERIES_WEEKLY_ADJUSTED
        Parameters
        ----------
        symbol : string
            the ticker symbol
        kwargs : dict
            any other optional keyword(s)
        Returns
        -------
        data : dict or pandas.DataFrame
            the requested data
        meta_data : None or dict
            the meta data if data is a DataFrame
        """
        kwargs.update({'symbol': symbol, 'outputsize': self.outputsize})
        return self.__call__('TIME_SERIES_WEEKLY_ADJUSTED', data_key=f"Weekly Adjusted Time Series", **kwargs)

    def time_series_monthly(self, symbol, **kwargs):
        """API call to TIME_SERIES_MONTHLY
        Parameters
        ----------
        symbol : string
            the ticker symbol
        kwargs : dict
            any other optional keyword(s)
        Returns
        -------
        data : dict or pandas.DataFrame
            the requested data
        meta_data : None or dict
            the meta data if data is a DataFrame
        """
        kwargs.update({'symbol': symbol, 'outputsize': self.outputsize})
        return self.__call__('TIME_SERIES_MONTHLY', data_key=f"Monthly Time Series", **kwargs)

    def time_series_monthly_adjusted(self, symbol, **kwargs):
        """API call to TIME_SERIES_MONTHLY_ADJUSTED
        Parameters
        ----------
        symbol : string
            the ticker symbol
        kwargs : dict
            any other optional keyword(s)
        Returns
        -------
        data : dict or pandas.DataFrame
            the requested data
        meta_data : None or dict
            the meta data if data is a DataFrame
        """
        kwargs.update({'symbol': symbol, 'outputsize': self.outputsize})
        return self.__call__('TIME_SERIES_MONTHLY_ADJUSTED', data_key=f"Monthly Adjusted Time Series", **kwargs)

    def quote_endpoint(self, symbol, **kwargs):
        """API call to GLOBAL_QUOTE
        Parameters
        ----------
        symbol : string
            the ticker symbol
        kwargs : dict
            any other optional keyword(s)
        Returns
        -------
        data : dict
            the requested data
        meta_data : None
            placeholder for consistency
        """
        kwargs.update({'symbol': symbol})
        return self.__call__('GLOBAL_QUOTE', **kwargs)

    def ticker_search(self, keywords, **kwargs):
        """API call to SYMBOL_SEARCH
        Parameters
        ----------
        symbol : string
            the ticker symbol
        kwargs : dict
            any other optional keyword(s)
        Returns
        -------
        data : dict
            the requested data
        meta_data : None
            placeholder for consistency
        """
        kwargs.update({'keywords': keywords})
        return self.__call__('SYMBOL_SEARCH', **kwargs)

    def global_market_status(self):
        """API call to MARKET_STATUS
        Parameters
        ----------
        symbol : string
            the ticker symbol
        kwargs : dict
            any other optional keyword(s)
        Returns
        -------
        data : dict
            the requested data
        meta_data : None
            placeholder for consistency
        """
        return self.__call__('MARKET_STATUS')


class AlphaVantageError(Exception):
    pass
