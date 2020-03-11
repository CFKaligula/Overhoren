# Read Me

Quiz yourself on wordlists with the wozzol format use command `python quiz.py`, change the file name in the code for now.

Format of wordlist is as follows:

``` bash
SourceLanguage : TargetLanguage
un momento = een ogenblik / een moment
```

All non-alphanumeric characters are stripped

* / in the answers means multiple correct answers,
* between ( ) is removed, 'u (enkelvoud)' becomes 'u'
* between [ ] loses the brackets so '[trabaja]'  becomes 'trabaja'
* between [ ] with multiple answers means the between brackets should be added to all answers so 'hij / zij / het / u [werkt]' means the possible answers are 'hij werkt/ zij werkt/ het werkt/ u werkt'
