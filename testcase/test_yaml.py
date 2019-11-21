import json

import yaml


def test_json():
    # f = open('calc.json')
    r = json.load(open('/Users/apple/Desktop/AutomatorProject/PyTest/testcase/calc.json'))
    print(r)

def test_yaml():
    print(yaml.load(open('/Users/apple/Desktop/AutomatorProject/PyTest/testcase/calc.yaml')))