import os
import requests
import urllib.request
import quiz


def get_words_from_web_page(language):
    language = language.lower()
    url = f'https://1000mostcommonwords.com/1000-most-common-{language}-words/'
    if requests.get(url).status_code == 404:
        raise Exception(f"No list of words for this language '{language.capitalize()}'")

    response = urllib.request.urlopen(url)
    web_page = response.readlines()

    index = 0
    source_words = []
    target_words = []
    for line in web_page:
        line = line.decode('utf-8')
        if '<td>' in line:
            index += 1
            if index % 3 == 2:
                word = line.split('<td>')[1].rsplit('</td>')[0]
                source_words.append(word)
            elif index % 3 == 0:
                word = line.split('<td>')[1].rsplit('</td>')[0]
                target_words.append(word)
    with open(os.path.join('1000lists', f'1000_most_common_words_{language}.txt'), 'w', encoding='utf-8') as the_file:
        the_file.write('wozzol\n')
        the_file.write(f'{language.capitalize()} : English\n')
        while len(source_words) > 0:
            the_file.write(f'{source_words.pop(0)} = {target_words.pop(0)}\n')
