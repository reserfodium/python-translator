#!/usr/bin/env python3

# Author: reserfodium, 12.2017
# Python version: 3.6+
# Dependencies:
#  > yandex.translate


#! CONST

BOLD = "\033[1m"
DEF = "\033[0m"
NL = "\n"

API_KEY = "trnsl.1.1.20171205T125702Z.c9a3990460e7cb48.2c2029147b887744cb59ae10b64f8fcd8472d698"


#! IMPORT

from sys import argv, exit

try: from yandex_translate import YandexTranslate
except: print(f'{NL}YandexTranslate {BOLD}not found{DEF}{NL}'); exit()


#! PARSE ARGS

if 2 > len(argv):
    print("{NL}translate.py [lang] [what]{NL}")
    exit()
else:
    # In which language
    to = argv[1]

    # What to tanslate
    what = " ".join(argv[2:])


#! TRANSLATE

try:
    # Create API object and translate
    translate = YandexTranslate(API_KEY);
    translated = translate.translate(what, to)['text'][0];

    # Print
    print(f"{NL}{translated}{NL}");
except:
    print(f'{NL}Internal error was occorupted!{NL}')
