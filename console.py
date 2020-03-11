
from argparse import ArgumentParser
import os
import quiz
_COMMAND_QUIZ = 'quiz'


def _add_parser_category_quiz(subparsers):
    parser = subparsers.add_parser(
        _COMMAND_QUIZ, help='performs quiz with the given wordlist')
    parser.set_defaults(command=_COMMAND_QUIZ)

    parser.add_argument(
        'file_path',
        type=str,
        help='file_path')


def _parse_arguments():
    parser = ArgumentParser(description='Console interface for the parser.')
    parser.set_defaults(command=None)

    subparsers = parser.add_subparsers(help='Category')
    _add_parser_category_quiz(subparsers)
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()

    elif args.command == _COMMAND_QUIZ:
        # Get the list of all files in directory tree at given path
        listOfFiles = list()
        for (dirpath, dirnames, filenames) in os.walk(os.curdir):
            for file in filenames:
                if file == args.file_path:
                    print(os.path.join(dirpath, file))
                    word_list = quiz.convert_text_to_objects(os.path.join(dirpath, file))
                    quiz.perform_quiz(word_list)
            #listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    return (args.command, args)


def main():
    (command, args) = _parse_arguments()


if __name__ == "__main__":
    main()
