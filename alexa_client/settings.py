import os
import json
import re
from pprint import pprint

CONFIG_FILE = './config/local.json'
with open(CONFIG_FILE) as fp:
    input_str = fp.read()

output_str = re.sub(r'\\\n', '', input_str)
output_str = re.sub(r'//.*\n', '\n', output_str)

AlexaConf = json.loads(output_str)

pprint(AlexaConf)

CLIENT_ID = AlexaConf['authDelegate']['clientId']
CLIENT_SECRET = AlexaConf['authDelegate']['clientSecret']
PRODUCT_ID = AlexaConf['authDelegate']['productId']
REFRESH_TOKEN = AlexaConf['authDelegate']['refreshToken']
SERIAL_NUMBER = AlexaConf['authDelegate']['deviceSerialNumber']
WEB_PORT = 3000


def update_token(refresh_token):
    AlexaConf['authDelegate']['refreshToken'] = refresh_token

    with open(CONFIG_FILE, 'w') as fp:
        json.dump(AlexaConf, fp)

    return
