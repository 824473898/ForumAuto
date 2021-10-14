import os
import configparser

# filepath = os.getcwd() + r"\Config\browser.ini"

# print(os.path.d)

filepath = os.path.dirname(os.path.abspath('.')) + r"\Config\browser.ini"

config = configparser.ConfigParser()
config.read(filepath, encoding='utf-8')

print(config.sections())

print(config.options('browserType'))

r = config.get('browserType', 'browserName')
print(r)
