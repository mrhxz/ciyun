#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud
import os

d = path.dirname(__file__)

# Read the whole text.
#text = open(path.join(d, 'constitution.txt')).read()
text = open(u"santi.txt").read().decode('gbk')

# Generate a word cloud image
font=os.path.join(os.path.dirname(__file__), "DroidSansFallbackFull.ttf")
wordcloud = WordCloud(font_path=font).generate(text)
wordcloud = WordCloud(font_path=font,max_font_size=40).generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(font_path=font).generate(text)
wordcloud = WordCloud(font_path=font,max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
