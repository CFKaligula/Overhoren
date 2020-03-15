
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
        default='Spaans-raw.txt',
        nargs='?',
        help='file_path')

    parser.add_argument(
        '-r',
        '--reversed',
        action='store_true',
        help='whether the word list should be reversed')


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
        for (dirpath, dirnames, filenames) in os.walk(os.curdir):
            for file in filenames:
                if file == args.file_path or file.split('.')[0] == args.file_path:
                    word_list = quiz.choose_word_list_converter(os.path.join(dirpath, file))

                    if args.reversed:
                        word_list = quiz.create_reverse_list(word_list)
                    quiz.perform_quiz(word_list)
        else:
            print('No file with this name was found')
            print(args.file_path)

    return (args.command, args)


def main():
    (command, args) = _parse_arguments()


if __name__ == "__main__":
    main()
