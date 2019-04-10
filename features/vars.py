# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:02:12 2019

@author: dilan
"""

import numpy as np
import pandas as pd
import tldextract
from huffman import HuffmanCoding
import matplotlib.pyplot as plt

df = pd.read_csv("urls_bad.txt")

#url length
df['url_length'] = df['url'].apply(lambda x: len(x))

#top level domain
df['tld'] = df['url'].apply(lambda x : tldextract.extract(x)[2])

#number of subdomains ? should www be excluded here? probably
df['subdomain_count'] = df['url'].apply(lambda x : len(filter(None, tldextract.extract(x)[0].split('.'))))

#entropy, the url was compressed using huffman coding and the compression ratio taken to be the entropy
#close to zero is low entropy, clos to 1 is high entropy
#An implimentation of huffman coding was used and modified to just return the length of the result
df['url_entropy'] = df['url'].apply(lambda x: float(HuffmanCoding(x).compress())/float(len(x)))

#print(df.head(100))
df['https'] = df['url'].apply(lambda x: x.startswith("https"))

print(df.to_csv())