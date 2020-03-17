# Read Me

Quiz yourself on wordlists, can either give a filename or a language, if you give a filename it will quiz you on the words in that file, if you give a language as input it wil download 1000 most common words in that language and quiz you on them. You can also choose to reverse the word list with the tag -r.
 currently only implemented with the with the wozzol format (see <https://www.wozzol.nl/woordenlijsten).> use command `python console.py WORDLISTFILENAME`, where `WORDLISTFILENAME` is the name of the file with the word list (you can leave out the file type extension). The file can be placed anywhere in the directory.

To quit the quiz prematurely input q().
To ask the word list in reverse, so from right to left instead of left to right, use the -r tag.

## Format from Wozzol

Format of wozzol wordlist is as follows:

``` bash
wozzol
SourceLanguage : TargetLanguage
un momento = een ogenblik / een moment
...
```

wordlists are detected to be in wozzol format either if the word 'wozzol' is in the file path or if the word wozzol is on the first line.
All non-alphanumeric characters are stripped

* / in the answers means multiple correct answers,
* between ( ) is removed, 'u (enkelvoud)' becomes 'u'
* between [ ] loses the brackets so '[trabaja]'  becomes 'trabaja'
* between [ ] with multiple answers means the between brackets should be added to all answers so 'hij / zij / het / u [werkt]' means the possible answers are 'hij werkt/ zij werkt/ het werkt/ u werkt'
