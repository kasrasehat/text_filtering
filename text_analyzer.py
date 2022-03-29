import time
from hazm import *
import json, jsonf
import pandas as pd


class farsi_analyzer():

    def __init__(self):
        pass

    def find_statement(self, main_passage, list_of_statements):

        normalizer = Normalizer()
        main_passage = normalizer.normalize(main_passage)
        main_passage = word_tokenize(main_passage)
        main_passage1 = main_passage.copy()
        lemmatizer = Lemmatizer()
        stemmer = Stemmer()

        ms_dic = {i: stemmer.stem(lemmatizer.lemmatize(f).split('#')[0]) for i, f in enumerate(main_passage)}
        ms_dic_inv = {}

        for i in ms_dic.keys():
            if ms_dic[i] in ms_dic_inv.keys():
                ms_dic_inv[ms_dic[i]].append(i)
            else:
                ms_dic_inv[ms_dic[i]] = [i]

        dic_of_words = {}
        word_repeatation = {}
        for statement in list_of_statements:

            statement1 = statement
            statement = normalizer.normalize(statement)
            statement = word_tokenize(statement)
            count = 0
            length = len(statement)
            loc = []
            command = None

            for i in range(length):
                if command:
                    continue
                if stemmer.stem(lemmatizer.lemmatize(statement[i]).split('#')[0]) in ms_dic_inv.keys():
                    loc.append(ms_dic_inv[stemmer.stem(lemmatizer.lemmatize(statement[i]).split('#')[0])])
                else:
                    print(
                        'there is not {} word and statement of {} in main signal'.format(statement[i], statement1))
                    word_repeatation[statement1] = 0
                    command = True

            if command:
                continue
            dic_of_words[statement1] = loc

            if length == 1:
                count = len(dic_of_words[statement1][0])
                for i in dic_of_words[statement1][0]: main_passage1[i] = '*'

            elif length == 2:
                for i in range(len(dic_of_words[statement1][0])):
                    for j in range(len(dic_of_words[statement1][1])):
                        if dic_of_words[statement1][0][i] < dic_of_words[statement1][1][j]:
                            count += 1
                            for k in [dic_of_words[statement1][0][i],dic_of_words[statement1][1][j]]: main_passage1[k] = '*'

            elif length == 3:
                for i in range(len(dic_of_words[statement1][0])):
                    for j in range(len(dic_of_words[statement1][1])):
                        for k in range(len(dic_of_words[statement1][2])):
                            if (dic_of_words[statement1][0][i] < dic_of_words[statement1][1][j]) & (
                                    dic_of_words[statement1][1][j] < dic_of_words[statement1][2][k]):
                                count += 1
                                for l in [dic_of_words[statement1][0][i], dic_of_words[statement1][1][j], dic_of_words[statement1][2][k]]:
                                    main_passage1[l] = '*'

            elif length == 4:
                for i in range(len(dic_of_words[statement1][0])):
                    for j in range(len(dic_of_words[statement1][1])):
                        for k in range(len(dic_of_words[statement1][2])):
                            for l in range(len(dic_of_words[statement1][3])):
                                if (dic_of_words[statement1][0][i] < dic_of_words[statement1][1][j]) & (
                                        dic_of_words[statement1][1][j] < dic_of_words[statement1][2][k]) & (
                                        dic_of_words[statement1][2][k] < dic_of_words[statement1][3][l]):
                                    count += 1
                                    for m in [dic_of_words[statement1][0][i], dic_of_words[statement1][1][j],
                                              dic_of_words[statement1][2][k], dic_of_words[statement1][3][l]]:
                                        main_passage1[m] = '*'

            elif length == 5:
                for i in range(len(dic_of_words[statement1][0])):
                    for j in range(len(dic_of_words[statement1][1])):
                        for k in range(len(dic_of_words[statement1][2])):
                            for l in range(len(dic_of_words[statement1][3])):
                                for m in range(len(dic_of_words[statement1][4])):
                                    if (dic_of_words[statement1][0][i] < dic_of_words[statement1][1][j]) & (
                                            dic_of_words[statement1][1][j] < dic_of_words[statement1][2][k]) \
                                            & (dic_of_words[statement1][2][k] < dic_of_words[statement1][3][l]) & (
                                            dic_of_words[statement1][3][l] < dic_of_words[statement1][4][m]):
                                        count += 1
                                        for n in [dic_of_words[statement1][0][i], dic_of_words[statement1][1][j],
                                                  dic_of_words[statement1][2][k], dic_of_words[statement1][3][l], dic_of_words[statement1][4][m]]:
                                            main_passage1[n] = '*'

            word_repeatation[statement1] = count

        returned_text = ' '.join(main_passage1)
        #returned_text_file = json.dumps(returned_text, indent=4, ensure_ascii=False)
        #statement_repeatation = json.dumps(word_repeatation, indent=4, ensure_ascii=False)
        with open("sample1.json", "w", encoding='utf-8') as outfile1:
            outfile1.write(json.dumps(returned_text, ensure_ascii=False))

        with open("sample.json", "w", encoding='utf-8') as outfile:
            outfile.write(json.dumps(word_repeatation, ensure_ascii=False))

        return outfile, outfile1

    def add_statement(self, list_of_statements, new_statement):
        list_of_statements.append(new_statement)
        return list_of_statements


class english_analyzer():

    def __init__(self):
        pass

    def search_english(self, main_signal, list_of_words):

        ms_dic = {i: f for i, f in enumerate(main_signal)}
        ms_dic_inv = {}

        for i in ms_dic.keys():
            if ms_dic[i] in ms_dic_inv.keys():
                ms_dic_inv[ms_dic[i]].append(i)
            else:
                ms_dic_inv[ms_dic[i]] = [i]

        dic_of_words = {}
        word_repeatation = {}
        for word in list_of_words:

            count = 0
            length = len(word)
            loc = []
            command = None

            for i in range(length):
                if word[i] in ms_dic_inv.keys():
                    loc.append(ms_dic_inv[word[i]])
                else:
                    print('there is not {} letter and word of in main signal'.format(word[i]))
                    word_repeatation[word] = 0
                    command = True

            if command: continue
            dic_of_words[word] = loc

            if length == 1:
                count = len(dic_of_words[word][0])

            elif length == 2:
                for i in range(len(dic_of_words[word][0])):
                    for j in range(len(dic_of_words[word][1])):
                        if dic_of_words[word][0][i] < dic_of_words[word][1][j]: count += 1

            elif length == 3:
                for i in range(len(dic_of_words[word][0])):
                    for j in range(len(dic_of_words[word][1])):
                        for k in range(len(dic_of_words[word][2])):
                            if (dic_of_words[word][0][i] < dic_of_words[word][1][j]) & (
                                    dic_of_words[word][1][j] < dic_of_words[word][2][k]): count += 1

            elif length == 4:
                for i in range(len(dic_of_words[word][0])):
                    for j in range(len(dic_of_words[word][1])):
                        for k in range(len(dic_of_words[word][2])):
                            for l in range(len(dic_of_words[word][3])):
                                if (dic_of_words[word][0][i] < dic_of_words[word][1][j]) & (
                                        dic_of_words[word][1][j] < dic_of_words[word][2][k]) & (
                                        dic_of_words[word][2][k] < dic_of_words[word][3][l]): count += 1

            elif length == 5:
                for i in range(len(dic_of_words[word][0])):
                    for j in range(len(dic_of_words[word][1])):
                        for k in range(len(dic_of_words[word][2])):
                            for l in range(len(dic_of_words[word][3])):
                                for m in range(len(dic_of_words[word][4])):
                                    if (dic_of_words[word][0][i] < dic_of_words[word][1][j]) & (
                                            dic_of_words[word][1][j] < dic_of_words[word][2][k]) \
                                            & (dic_of_words[word][2][k] < dic_of_words[word][3][l]) & (
                                            dic_of_words[word][3][l] < dic_of_words[word][4][m]): count += 1

            word_repeatation[word] = count

        return word_repeatation


        

