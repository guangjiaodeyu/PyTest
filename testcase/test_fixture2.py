import logging

import pytest
import requests


@pytest.mark.a
def test_1(topics2):
    logging.info('start111111')
    assert len(topics2['topics']) == 2
    logging.info('end1111111')


@pytest.mark.b
def test2(topics3):
    assert topics3['topics'][0]['deleted'] == False


@pytest.mark.b
def test3(topics2):
    assert topics2['topics'][0]['deleted'] == False