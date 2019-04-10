# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:00:52 2019

@author: dilan
"""

import whois
import json
import pandas as pd

data = pd.read_csv("online-valid.csv")
urls = data['url']

df = pd.DataFrame()

def flatten_json(nested_json):
    """
        Flatten json object with nested keys into a single level.
        Args:
            nested_json: A nested json object.
        Returns:
            The flattened json object if successful, None otherwise.
    """
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out
    
#print(flatten_json(j))
    
i = 0

for url in urls:
    i = i+1
    print(i)
    try:
        w = whois.whois(url)
        j = json.loads(str(w))
        j['url'] = url
        df = df.append(flatten_json(j), ignore_index=True)
    except:
        df = df.append({'url': url}, ignore_index=True)
        

df.to_csv("whois.csv", encoding="utf-8")

#df = df.append(flatten_json(json.loads(str(w))), ignore_index=True)