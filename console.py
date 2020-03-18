
from argparse import ArgumentParser
import os
import quiz
import download_list
_COMMAND_QUIZ = 'quiz'


def _add_parser_category_quiz(subparsers):
    parser = subparsers.add_parser(
        _COMMAND_QUIZ, help='performs quiz with the given wordlist')
    parser.set_defaults(command=_COMMAND_QUIZ)

    parser.add_argument(
        'input',
        type=str,
        default='Spaans-raw.txt',
        nargs='?',
        help='input for the quiz, can be a file or a language')

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
        file_path = None
        for (dirpath, _, filenames) in os.walk(os.curdir):
            for file in filenames:
                if file == args.input or file.split('.')[0] == args.input:
                    file_path = os.path.join(dirpath, file)
                    break
            else:
                continue  # only executed if the inner loop did NOT break
            break

        else:
            print(f'No file with the name {args.input} was found, trying to make word list..')
            download_list.get_words_from_web_page(args.input)
            file_path = os.path.join('1000lists', f'1000_most_common_words_{args.input}.txt')
        if file_path:
            word_list = quiz.choose_word_list_converter(file_path)
            if args.reversed:
                word_list = quiz.create_reverse_list(word_list)
            quiz.perform_quiz(word_list)
        else:
            print('Unable to create quiz')

    return (args.command, args)


def main():
    (command, args) = _parse_arguments()


if __name__ == "__main__":
    main()
