import logging

import pytest
import requests

# @pytest.fixture()
# @pytest.fixture(scope='module')
# @pytest.fixture(scope='class')
# @pytest.fixture(scope='function')
# @pytest.fixture(scope='session')
# def topics():
#     url = 'http://0.0.0.0:8000/topics.json'
#     return requests.get(url).json()
    # return requests.get('https://testerhome.com/api/v3/topics.json?limit=2').json()


def test_1(topics):
    logging.info('test_1_xxxxxxxxxxxxx')

    # json = requests.get('https://testerhome.com/api/v3/topics.json?limit=2').json()
    assert len(topics['topics']) == 2
    logging.info('test_1_yyyyyyyyyyyyy')

def test2(topics):
    # json = requests.get('https://testerhome.com/api/v3/topics.json?limit=2').json()
    assert topics['topics'][0]['deleted'] == False