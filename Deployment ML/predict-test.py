#!/usr/bin/env/python
# coding: utf-8

import requests

host = 'churn-serving-env.eba-ywfsmphm.eu-west-1.elasticbeanstalk.com'
url = f'http://{host}/predict'

customer_id = 'xyz-123'
customer = {
    'gender': 'male',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'yes',
    'tenure': 6,
    'phoneservice': 'yes',
    'multiplelines': 'yes',
    'internetservice': 'dsl',
    'onlinesecurity': 'yes',
    'onlinebackup': 'no',
    'deviceprotection': 'yes',
    'techsupport': 'yes',
    'streamingtv': 'yes',
    'streamingmovies': 'yes',
    'contract': 'one_year',
    'paperlessbilling': 'yes',
    'paymentmethod': 'bank_transfer_(automatic)',
    'monthlycharges': 109.85,
    'totalcharges': 5320.75
}

response = requests.post(url, json=customer).json()
print(response)

if response['churn'] == True:
    print('sending promo email to %s' % customer_id)
else:
    print('not sending promo email to %s' % customer_id)

