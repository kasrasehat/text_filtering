# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from hazm import *
import json
import pandas as pd
from text_analyzer import english_analyzer, farsi_analyzer

if __name__ == '__main__':
    main_signal = 'abpgdktljhgdfwveppamclztydaqapldhgcmoom,vkshdlaptnmbcozplmqwhdgslbalmzncjklhsyqweoiusgmftt'
    list_of_words = ['a', 'abd', 'pmo', 'fmp', 'ktgm', 'apmo', 'aaop', 'aopml', 'jkxzo', 'opftt']
    english_analyzer = english_analyzer()
    start = time.time()
    print(english_analyzer.search_english(main_signal, list_of_words))
    end = time.time()
    print(end - start)


    a = pd.read_json('E:/articles/NLP/toxic_dataset/toxic_words.json')
    main_signal1 = 'ویرایش و بازخوانی متون فارسی یا به زبان ساده‌تر ویرایش فنی متن‌های فارسی از نظر علائم نگارشی، نکات دستوری و جمله‌بندی، یکی از مهم‌ترین مسائلی است که بیشتر محققان، نام نویسنده‌ها و دانشجویان با آن درگیر هستند. شبکه مترجمین ایران با همکاری و همراهی موسسه (ویراستاران) راه‌حلی مناسب گاوی برای آن پیدا کرده است تا دیگر هیچ‌کس نگرانی در مورد اسبی ویراستاری متن‌های خود نداشته باشد.'
    list_of_words1 = ['سلام. احوال','به نام ','مترجمین موسسه','خداوند الموت','راه‌حل مناسب','گاو داشت ','خر']
    farsi_analyzer = farsi_analyzer()
    start = time.time()
    print(farsi_analyzer.find_statement(main_signal1, list_of_words1))
    end = time.time()
    print(end - start)




