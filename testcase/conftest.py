import pytest
import requests
import logging

logging.basicConfig(level=logging.DEBUG)

# @pytest.fixture()
# @pytest.fixture(scope='session')
# @pytest.fixture(scope='module')
# @pytest.fixture(scope='class')
@pytest.fixture(scope='function')
def topics():
    url = 'http://0.0.0.0:8000/topics.json'
    logging.info(url)

    # return requests.get(url).json()
    yield requests.get(url).json()
    logging.info('finished')


@pytest.fixture(params=['http://0.0.0.0:8000/topics.json',
                        'http://0.0.0.0:8000/topics.json'
                        ])
def topics2(request):
    url = request.param
    logging.info(url)

    def fin():
        logging.info('after yield teardown')

    request.addfinalizer(fin)
    return requests.get(url).json()



@pytest.fixture(params=['http://0.0.0.0:8000/topics.json',
                        'http://0.0.0.0:8000/topics.json',
                        'http://0.0.0.0:8000/topics.json'
                        ])
def topics3(request):
    url = request.param
    logging.info(url)

    def fin():
        logging.info('after yield teardown')

    request.addfinalizer(fin)
    return requests.get(url).json()
