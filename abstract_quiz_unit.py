class AbstractQuizUnit:
    def __init__(self, question, answer, source_language=None, target_language=None):
        self.question = question
        self.answer = answer
        self.source_language = source_language
        self.target_language = target_language
        self.answers = []
        self.get_multiple_answers()
        self.answer = self.clean_input(self.answer)
        self.question = self.clean_input(self.question)

    def clean_input(self, input_string):
        raise NotImplementedError

    def get_multiple_answers(self):
        raise NotImplementedError
