import logging

import pytest

logging.basicConfig(level=logging.DEBUG)

def setup_module():
    logging.info('setup_module')

def teardown_module():
    logging.info('teardown_module')


class TestPytestObject2:
    def test_three(self):
        assert [1,2] == [1,3]

    def test_four(self):
        assert {"a":1,"b":2} =={"a":2,"b":"ss"}

class TestPytestObject:


    @classmethod
    def setup_class(cls):
        logging.info('setup_class')


    def setup_method(self):
        logging.info('setup__method')


    @pytest.mark.run(order=1)
    def test_two(self):
        assert 1==2

    @pytest.mark.run(order=2)
    def test_one(self):
        assert  True==False

    def teardown_method(self):
        logging.info('teardown__method')

    @classmethod
    def teardown_class(cls):
        logging.info('teardown_class')