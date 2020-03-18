from time import sleep
import sys
import os
from random import shuffle
from abstract_quiz_unit import AbstractQuizUnit
from wozzol import WozzolQuizUnit
import wozzol
import shutil
_ESCAPE_COMMAND = 'q()'


def print_gradually(input_string):
    os.system('cls')
    for character in input_string:
        print(character, flush=True, end="")
        sleep(0.01)


def create_reverse_list(word_list):
    reverse_word_list = []
    for entry in word_list:
        if issubclass(entry.__class__, AbstractQuizUnit):
            reverse_word_list.append(entry.__class__(question=entry.answer,
                                                     answer=entry.question,
                                                     source_language=entry.target_language,
                                                     target_language=entry.source_language
                                                     ))
        else:
            raise TypeError(
                f"Entry must be a subclass of AbstractQuizUnit, but it was {entry.__class__}.")
    return reverse_word_list


def choose_word_list_converter(file_path):
    word_list = None
    if file_path or 'wozzol' in open(file_path, encoding="utf-8").readlines()[0]:
        word_list = wozzol.convert_wozzol_list_to_word_list(file_path)
    else:
        print(open(file_path, encoding="utf-8").readlines()[0])
        raise Exception(
            'Unclear what type of word list is used')
    return word_list


def perform_quiz(word_list):
    question_queue = []
    for entry in word_list:
        #  add all the words to the queue in the form of QueueEntries
        question_queue.append(QueueEntry(entry))
    # shuffle the entries in the queue
    shuffle(question_queue)
    while len(question_queue) > 0:
        top_question = question_queue[0]
        if top_question.ask_question():
            # if the user answered the question correctly less than it was answered incorrectly
            # or answered correctly less than 2 times we add it again to the end of the question_queue
            if top_question.times_answered_correctly < top_question.times_answered_incorrectly or top_question.times_answered_correctly < 2:
                question_queue.insert(len(question_queue), top_question)
        else:
            # if the question was answered incorrectly, we insert it at place 2 and 5 in the queue
            question_queue.insert(2, top_question)
            question_queue.insert(5, top_question)
        # remove the top question from the stack
        question_queue.pop(0)


class QueueEntry():
    def __init__(self, quiz_unit):
        self.quiz_unit = quiz_unit
        self.times_answered_correctly = 0
        self.times_answered_incorrectly = 0

    def ask_question(self):
        result = False
        print_gradually(
            f'What is the {self.quiz_unit.target_language} translation for the {self.quiz_unit.source_language} word "{self.quiz_unit.question}" \n')
        user_answer = input().strip()
        # if the user (accidentally) pressed enter so the answer is empty, re-ask the question until there is an answer
        while len(user_answer) == 0:
            os.system('cls')
            user_answer = input(
                f'What is the {self.quiz_unit.target_language} translation for the {self.quiz_unit.source_language} word "{self.quiz_unit.question}" \n').strip()
        # quit if the user pressed the escape command
        if user_answer == _ESCAPE_COMMAND:
            shutil.rmtree('1000lists')
            os.makedirs('1000lists')
            os.system('cls')
            sys.exit()

        if user_answer in self.quiz_unit.answers:
            other_correct_answers = [ans for ans in self.quiz_unit.answers if ans != user_answer]
            if len(other_correct_answers) > 0:
                print_gradually(
                    f'Correct, other correct answers were "{" or ".join(other_correct_answers)}"\n')
            else:
                print_gradually(f'***Correct*** (^O^)\n')
                sleep(0.5)
            self.times_answered_correctly += 1
            result = True
        else:
            print_gradually(
                f'Incorrect, the correct answer would be "{",".join(self.quiz_unit.answers)}"\n')
            os.system("pause")
            self.times_answered_incorrectly += 1
        return result
