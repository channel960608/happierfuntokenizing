# Happiest Fun Tokenizer for python3
This code is modified in order to adapt to Python3. And according to my own requirements, auther added some functions or params to preserve the specific tokens like nicknames, urls, and hashtags.
The former version of code implements a basic, Twitter-aware tokenizer. Originally developed by [Christopher Potts](http://web.stanford.edu/~cgpotts/) 
([Happy Fun Tokenizer](http://sentiment.christopherpotts.net/code-data/happyfuntokenizing.py)) and updated by [H. Andrew Schwartz](http://www3.cs.stonybrook.edu/~has/). Shared with Christopher's permission. Further updated by [Caspar Chan](https://github.com/channel960608/happiestfuntokenizing).  


### Usage

```python
from happiestfuntokenizing.happiestfuntokenizing import Tokenizer

tokenizer = Tokenizer()

message = """OMG!!!! :) I looooooove this tokenizer lololol"""
tokens = tokenizer.tokenize(message)
print(tokens)
['omg', '!', '!', '!', '!', ':)', 'i', 'looooooove', 'this', 'tokenizer', 'lololol']

message = """OMG!!!! :) I looooooove this tokenizer LoLoLoLoLooOOOOL"""
tokenizer = Tokenizer(preserve_case=True)
tokens = tokenizer.tokenize(message)
print(tokens)
['OMG', '!', '!', '!', '!', ':)', 'I', 'looooooove', 'this', 'tokenizer', 'LoLoLoLoLooOOOOL']

message = """RT @cahnnle #happyfuncoding: this is a typical Twitter tweet :-) https://twiter/test.phd"""  
tokenizer = Tokenizer(preserve_keywords=True)  
tokens = tokenizer.tokenize(message)
print(tokens)
['rt', '@cahnnle', '#happyfuncoding', ':', 'this', 'is', 'a', 'typical', 'twitter', 'tweet', ':-)']   
print(tokenizer..get_preserve_dict())
{'username': ['@cahnnle'], 'url': ['https://twiter/test.phd'], 'hashtag': ['#happyfuncoding']}


```

### Installation

This is available through `pip`

```sh
pip install happiestfuntokenizing
```

If you do not have sudo privileges you can use the `--user` flag

```sh
pip install --user happiestfuntokenizing
```

## Requirements

This uses Python 3.* Package dependencies include `re` and `html`.

## License

Licensed under a [GNU General Public License v3 (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.en.html)

## Background

Adapted by the [World Well-Being Project](http://www.wwbp.org) based out of the University of Pennsylvania
and Stony Brook University. Originally developed by [Christopher Potts](http://web.stanford.edu/~cgpotts/). 
