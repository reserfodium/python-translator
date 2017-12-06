#!/usr/bin/env python3

# Author: reserfodium, 12.2017
# Python version: 3.6+
# Dependencies:
#  > yandex.translate

from sys import argv, exit
from yandex_translate import YandexTranslate

API_KEY = "trnsl.1.1.20171205T125702Z.c9a3990460e7cb48.2c2029147b887744cb59ae10b64f8fcd8472d698"

if 2 > len(argv):
    print("\ntranslate.py [lang] [what]\n")
    exit()
else:
    # In which language
    to = argv[1]

    # What to tanslate
    what = " ".join(argv[2:])

# Create API object and translate
translate = YandexTranslate(API_KEY);
translated = translate.translate(what, to)['text'][0];

# Print
print(f"\n{translated}\n");
