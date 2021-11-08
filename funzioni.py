import re
import unicodedata
import altair as alt
import pandas as pd
from stop_words import get_stop_words


def formatString(string):
    return re.sub("[^a-z]", " ", unicodedata.normalize('NFD', string.decode("utf-8")).encode('ascii', 'ignore').decode("utf-8").lower())


def orderDict(dict):
    sorted_dict = {}
    for ch in reversed(sorted(dict, key = dict.get)):
        sorted_dict[ch] = dict[ch]

    return sorted_dict


def countWords( file):
    dict = {}
    stopWords = get_stop_words('it')
    for line in file:
        line = formatString(line)
        for word in line.split():
            if word not in stopWords:
                if word not in dict:
                    dict[word] = 0
                dict[word] += 1

    return orderDict(dict)

def createGraph(dict,num):
    the_dict = pd.DataFrame({"Frequenza": [dict[item] for item in dict][:num], "Parole": [item for item in dict][:num]})
    fig = alt.Chart(the_dict).mark_bar().encode(x=alt.X("Parole", sort=[item for item in dict][:num]), y="Frequenza")

    return fig