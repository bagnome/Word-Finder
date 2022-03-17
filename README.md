# Word-Finder
Python script that suggests guesses for word games such as Wordle or the game show Lingo.

It is cheating? Maybe? I'm on the fence about that. All this does is provide a list of suggested words, but does not take into account letters that you've guessed and are not present. With that, it's still possible to not pay attention and use a word with letters that you know are not in the word you're trying to guess.

This uses a text file with 15,918 five-letter words separated by line. So it's possible Wordle uses a word that's not in this list. But it might still help you guess.
This list also doesn't seem to use pural versions of words. I don't think Wordle does either, but if they do, then you can get close with this, but it probably won't show up in the output.

## Instructions
The script is ran with the following command:
`py word-finder.py SearchPattern`

*SearchPattern* is a stand-in for an argument to pass it. A search pattern is created with the following:
- Capital letter: Use capital letters in your search pattern to tell the script where in a word that letter is.
- Lower-case letter: Use a lower-case letter to indicate that the letter exists in the word, but not in the location you specified. You can repeat using a letter to indicate that more than one exists in the word.
- Underscore: These denote wildcard spaces in the word. Any letter can fill that space.

---
### Examples
The following tells the script to look for words that begin with "gn" and has an e anywhere but the position it is in in the search pattern.
```
py word-finder.py GNe__
```
Result:
```
gnide
gnome
```
The next two examples show how placement of the lower-case letter affects the results.
The first example:
```
py word_finder.py APPl_
```
Result:
```
appal
appel
```
The second example:
```
py word_finder.py APP_l
```
Result:
```
apple
apply
```
Using a lower-case more than once:
```
py word_finder.py _hTh_
```
Result:
```
hatch
hitch
hotch
hutch
```

---
As of right now. The script expects five-letter english words with no number, accents, or special characters to be passed to it.

## Requirments
Python 3.x.x

## Other Notes
Words sourced from [english-words](https://github.com/dwyl/english-words) by dwyl on March 16, 2022