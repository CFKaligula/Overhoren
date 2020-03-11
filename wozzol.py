from abstract_quiz_unit import AbstractQuizUnit


def convert_wozzol_list_to_word_list(file_path):
    # format from https://www.wozzol.nl/woordenlijsten
    text_file = open(file_path, encoding="utf-8")
    text_lines = text_file.readlines()
    word_list = []
    for line in text_lines:
        if ':' in line:
            source_language = line.split(':')[0].strip()
            target_language = line.split(':')[1].strip()
        if '=' in line:
            word_list.append(WozzolQuizUnit(question=line.split('=', 1)[0].strip(),
                                            answer=line.split('=', 1)[1].strip(),
                                            source_language=source_language,
                                            target_language=target_language
                                            ))
    return word_list


class WozzolQuizUnit(AbstractQuizUnit):

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
