# Chatbot that searches a webpage and replies to your answers.

# Outline
* [Pre-requisites](#pre-requisites)
* [How to run](#how-to-run)

## Pre-requisites
**NLTK(Natural Language Toolkit)**

[Natural Language Processing with Python](http://www.nltk.org/book/) provides a practical introduction to programming for language processing.

For platform-specific instructions, read [here](https://www.nltk.org/install.html)

### Installation of NLTK
```
pip install nltk
```
### Installing required packages
After NLTK has been downloaded, install required packages
```
import nltk
import sklearn
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading popular packages
nltk.download('punkt') 
nltk.download('wordnet') 
```
## How to run
* Jupyter Notebook [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/codeliteratur/SearchWebpageBot/0c11023f1a3c0d07578e2e8e1f9e5e13048c0fac)

You can run the [webpagebot.ipynb](https://github.com/codeliteratur/SearchWebpageBot/blob/master/webpagebot.ipynb) which also includes step by step instructions.
* Through Terminal
```
python searchbot.py
