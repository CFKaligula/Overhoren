from sys import stdout
from time import sleep
import sys
import os


def print_gradually(input_string):

    os.system('cls')
    for character in input_string:
        print(character, flush=True, end="")
        sleep(0.01)


def convert_text_to_objects(file_path):
    # format from https://www.wozzol.nl/woordenlijsten
    text_file = open(file_path, encoding="utf-8",)
    text_lines = text_file.readlines()
    word_list = []
    for line in text_lines:
        if ':' in line:
            source_language = line.split(':')[0].strip()
            target_language = line.split(':')[1].strip()
        if '=' in line:
            word_list.append(QuizUnit(input_question=line.split('=', 1)[0].strip(),
                                      input_answer=line.split('=', 1)[1].strip(),
                                      source_language=source_language,
                                      target_language=target_language
                                      ))
    return word_list


def create_reverse_list(word_list):
    reverse_word_list = []
    for entry in word_list:
        reverse_word_list.append(QuizUnit(entry.answer, entry.question))


def perform_quiz(word_list):
    queue = []
    for entry in word_list:
        queue.append(QueueEntry(entry))
    while len(queue) > 0:
        top_question = queue[0]
        if top_question.ask_question():
            # if the user answered the question correctly more than it was answered incorrectly we stop
            if top_question.times_answered_correctly < top_question.times_answered_incorrectly or top_question.times_answered_correctly < 2:
                queue.insert(10, top_question)
        else:
            queue.insert(2, top_question)
            queue.insert(5, top_question)
        queue.pop(0)


class QueueEntry():
    def __init__(self, quiz_unit):
        self.quiz_unit = quiz_unit
        self.times_asked = 0
        self.times_answered_correctly = 0
        self.times_answered_incorrectly = 0

    def ask_question(self):
        result = False
        print_gradually(
            f'What is the {self.quiz_unit.target_language} translation for the {self.quiz_unit.source_language} word "{self.quiz_unit.question}" \n')
        user_answer = input().strip()
        if user_answer == 'q()':
            sys.exit()
        if user_answer in self.quiz_unit.answers:
            other_correct_answers = [ans for ans in self.quiz_unit.answers if ans != user_answer]
            print_gradually(
                f'Correct, other correct answers were "{",".join(other_correct_answers)}"\n')
            os.system("pause")
            self.times_answered_correctly += 1
            result = True
        else:
            print_gradually(
                f'Incorrect, the correct answer would be "{",".join(self.quiz_unit.answers)}"\n')
            os.system("pause")
            self.times_answered_incorrectly += 1
        self.times_asked += 1
        return result


class QuizUnit:
    def __init__(self, input_question, input_answer, source_language=None, target_language=None):
        self.question = input_question
        self.answer = input_answer
        self.source_language = source_language
        self.target_language = target_language
        self.answers = []
        self.get_multiple_answers()
        self.answer = self.clean_input(self.answer)
        self.question = self.clean_input(self.question)

    def clean_input(self, input_string):
        processed_string = input_string
        if '[' in processed_string:
            processed_string = processed_string[processed_string.find(
                "[")+1:processed_string.find("]")]
        if '(' in processed_string:
            processed_string = processed_string.split('(')[0].strip()
        return ''.join(ch for ch in processed_string if ch.isalnum() or ch == ' ' or ch == '/')

    def get_multiple_answers(self):
        if '/' in self.answer:
            word_in_brackets = None
            if '[' in self.answer:
                word_in_brackets = self.answer[self.answer.find("[")+1:self.answer.find("]")]
            answer_list = self.answer.split('/')
            for entry in answer_list:
                if '[' in entry:
                    entry = entry.split('[')[0].strip()
                if '(' in entry:
                    entry = entry.split('(')[0].strip()
                self.answers.append(entry.strip()) if word_in_brackets is None else self.answers.append(
                    f'{entry.strip()} {word_in_brackets}')
        else:
            self.answers.append(self.clean_input(self.answer))


def main():
    file_path = os.path.join('wozzol_wordlists', 'Portugees-raw.txt')
    word_list = convert_text_to_objects(file_path)
    perform_quiz(word_list)


if __name__ == "__main__":
    main()
