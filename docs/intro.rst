Getting Started
***************

Installation
============

To install in the Python Client Library::

    pip install indico-client


Authentication
==============

The Indico Platform and Client Libraries use JSON Web Tokens (JWT) for user authentication. You can 
download a token from your `user dashboard`_ by clicking the large, blue "Download new API Token" button.
Most browsers will download the API token as ``indico_api_token.txt`` and place it in your Downloads directory. You
should move the token file from Downloads to either your home directory or another location in your development
environment.

Configuration
=============

Environment Variables
---------------------

You can use environment variables to control the default configuration of the Python Client Library as follows:

.. csv-table::
    :file: env-vars.csv
    :widths: 25 60
    :header-rows: 1

IndicoConfig Class
------------------

The IndicoConfig class gives you the maximum control over Python Client Library configuration. Here's how you
might instantiate an IndicoConfig object and set the host and token path::

    my_config = IndicoConfig(
        host='app.mycompany.com',
        api_token_path='/home/myuser/projects/trades/indico_api_token.txt'
    )


API Client
==========

The Indico Platform uses GraphQL to communicate with ALL clients including the company's own web application
and also the Indico Python Client. You'll use an ``IndicoClient`` object to pass GraphQL queries to the
Indico Platform. Here's a simple way to create a client::

    client = IndicoClient()

The IndicoClient constructor will read configuation options from the environment variables described above.
If you would like to manually set configuration options in an ``IndicoConfig`` object then you can pass your
config to IndicoClient as follows::

    client = IndicoClient(config=my_config)



.. _user dashboard: https://app.indico.io/auth/user