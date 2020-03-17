from wozzol import WozzolQuizUnit
import os
import requests

from yandex.Translater import Translater
tr = Translater()
# Api key found on https://translate.yandex.com/developers/keys
tr.set_key('trnsl.1.1.20200317T184210Z.859bd4e1e36decc9.54c5d73f715ded0f0b5e33e8f80d0eca61173b7d')
tr.set_from_lang('es')
tr.set_to_lang('en')


def translate_word(word):
    tr.set_text(word)
    translation = tr.translate()
    return translation


def convert_word_list_to_wozzol(word_list):
    with open('somefile.txt', 'a') as the_file:
        the_file.write('wozzol')
        the_file.write('Spanish : English')
        for word in word_list:
            the_file.write(f'{word.question} = {word.answer}')


def convert_wiktionary():
    file_path = os.path.join('web_pages', 'spanish_1000_frequency.html')
    # format from https://www.wozzol.nl/woordenlijsten
    text_file = open(file_path, encoding="utf-8")
    text_lines = text_file.readlines()
    word_list = []
    double = False
    with open('somefile.txt', 'w', encoding="utf-8") as the_file:
        the_file.write('wozzol\n')
        the_file.write('Spanish : English\n')
        for line in text_lines:
            if '" title="' in line:
                if double:
                    double = False
                else:
                    double = True
                    question = line.split('">')[1].rsplit('</a>')[0]
                    answer = translate_word(question)
                    the_file.write(f'{question} = {answer}\n')

    return word_list


word_list = convert_wiktionary()
convert_word_list_to_wozzol(word_list)
