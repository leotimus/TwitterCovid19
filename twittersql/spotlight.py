import re

import spotlight

SPOTLIGHT_DE = 'http://89.145.161.92/rest/annotate'
SPOTLIGHT_NL = 'http://89.145.162.101/rest/annotate'

def get_annotation(language, text):
    if language == 'nl':
        url = SPOTLIGHT_NL
    elif language == 'de':
        url = SPOTLIGHT_DE
    else:
        raise ValueError("Language not recognized: {}".format(language))

    r = spotlight.annotate(url, text, confidence=0.6, support=20)
    return r

def clean_tweet(text):
    """Remove URLs, mentions, RT and hashtag sign"""
    return re.sub(r"(?:\@|https?\://)\S+", "", text).replace('RT ', '').replace('#', '').strip()
