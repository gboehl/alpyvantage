alpyvantage
=============

**An alternative python backend to the Alpha Vantage API**

.. image:: https://img.shields.io/badge/GitHub-gboehl%2Falpyvantage-blue.svg?style=flat
    :target: https://github.com/gboehl/alpyvantage

.. image:: https://readthedocs.org/projects/alpyvantage/badge/?version=stable
    :target: https://alpyvantage.readthedocs.io

.. image:: https://badge.fury.io/py/alpyvantage.svg
    :target: https://badge.fury.io/py/alpyvantage

.. image:: https://github.com/gboehl/alpyvantage/actions/workflows/continuous-integration.yml/badge.svg
    :target: https://github.com/gboehl/alpyvantage/actions

**alpyvantage** provides a python backend to the Alpha Vantage API. Alpha Vantage provides access to a wide range of financial data and time series. Details can be found in the `official API documentation <https://www.alphavantage.co/documentation/>`_. You can get a free `API key here <https://www.alphavantage.co/support/#api-key>`_.


Installation
------------

Installing the `repository version <https://pypi.org/project/econpizza/>`_ is as simple as typing

.. code-block:: bash

   pip install alpyvantage

in your terminal or Anaconda Prompt.


Documentation
-------------

API calls are straightforward. Either use the build-in functions such as ``time_series_intraday``, ``time_series_weekly``, etc.:

.. code-block:: python

    import alpyvantage as av

    api = av.API(<your_api_key>)

    data, meta_data = api.time_series_intraday('DAX', interval='1min', month='2015-01')

    print(data) # its a pandas.DataFrame

Or use the ``function`` keyword from the `official API documentation <https://www.alphavantage.co/documentation/>`_ and provide the parameters as keyword arguments:

.. code-block:: python

    data, meta_data = api('TIME_SERIES_INTRADAY', symbol='DAX', interval='1min', month='2015-01')

A detailed documentation of the individual functions can be `found here <https://alpyvantage.readthedocs.io>`_.


Issues and contributions
------------------------

Please use the `issues <https://github.com/gboehl/alpyvantage/issues>`_ for questions or if you think anything doesn't do what it is supposed to do. Pull requests are welcome, please include some documentation.
