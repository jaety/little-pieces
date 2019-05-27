# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 10:05:26 2016

@author: jaety

When our hypothesis is that a collection of strings has regular structure
and we want to extract it, how do we model that?

It's a restricted form of the NLP exercise.

In this case, I want to recognize:
    1. Numbers
    2. A conditional
    3. A regular pattern given the two above

What would be the structure it reports?
    ${NUMBER}_${NUMBER}${CONDITIONAL("_mask")}.tif

number := [0-9]+
is_mask:= _mask
pattern:= <number>_<number><is_mask>?\.tif


How do I represent the cost of different encodings?
    The grammar itself has an encoding cost



cost(number) = len(contents) // could be better, but stick with this for now
cost(conditional) = %false * cost(false_pattern) + %true * cost(true_pattern)





Grammar Induction? https://en.wikipedia.org/wiki/Grammar_induction
    https://en.wikipedia.org/wiki/Sequitur_algorithm
    https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch
    
    http://archive.euroscipy.org/file/2041/raw/euroscipy2010_abstract-grammar-induction.pdf

"""

import os


src_dir = os.path.expanduser("~/projects/ml/kaggle-nerve/data/train")

pattern = "${user}_${slice}($is_mask)?.tif"


for item in os.listdir(src_dir):
    print item