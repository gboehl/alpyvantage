pythonvantage
=============

**An alternative python backend to the Alpha Vantage API **

.. image:: https://img.shields.io/badge/GitHub-gboehl%2Fpythonvantage-blue.svg?style=flat
    :target: https://github.com/gboehl/pythonvantage

**pythonvantage** provides a python backend to the Alpha Vantage API as presented in the `official API documentation <https://www.alphavantage.co/documentation/>`_. You can get a free `API key here <https://www.alphavantage.co/support/#api-key>`_.


Documentation
-------------

API keys are straightforward. Either use the build-in functions such as `time_series_intraday`, `time_series_weekly`, etc:

.. code-block:: python

    import pythonvantage

    api = pythonvantage.API(<your_api_key>)

    data, meta_data = api.time_series_intraday('DAX', interval='1min', month='2015-01')

Or use the function keyword from the `official API documentation <https://www.alphavantage.co/documentation/>`_:

.. code-block:: python

    data, meta_data = api('TIME_SERIES_INTRADAY', symbol='DAX', interval='1min', month='2015-01')


