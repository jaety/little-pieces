#!/usr/bin/env python
# Checvachish

import os
import csv
import re
import sys
import subprocess

class Translator:
    def __init__(self,word_file):
        self.word_file = word_file
        self.dictionaries = self._load(word_file)

    def _load(self, word_file):
        eng2chec = {}
        chec2eng = {}
        with open(word_file) as fin:
            for row in csv.reader(fin):
                eng = row[0].lower()
                chec= row[1].lower()
                eng2chec[eng] = chec
                chec2eng[chec]= eng
        return {"eng2chec":eng2chec, "chec2eng":chec2eng}

    def tokenize(self, sentence):
        return re.split('\W+', sentence.lower())

    def translate(self, sentence, target="chec"):
        dictionary =  self.dictionaries["eng2chec" if target is "chec" else "chec2eng"]
        translated_words = [dictionary.get(s) or s for s in self.tokenize(sentence)]
        translated = " ".join(translated_words)
        return translated

    def sayraw(self, sentence):
        subprocess.call(["say"] + self.tokenize(sentence))

    def say(self, sentence):
        word_list = self.tokenize(sentence)
        w = word_list[0]
        # TODO: Could make this robust to collisions (e.g. same word in both languages) by checking next word, etc.
        if w in self.dictionaries["chec2eng"]:
            target = "eng"
        elif w in self.dictionaries["eng2chec"]:
            target = "chec"
        else:
            self.sayraw("I don't recognize the first language")
        translated = self.translate(sentence, target)
        self.sayraw(translated)
        print translated

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description="translate to and from Checvachish")
    parser.add_argument("-e","--echo",action="store_true")
    parser.add_argument("sentence", nargs="*")
    args = parser.parse_args()

    words_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),"chec_words.csv")
    translator = Translator(words_file)
    sentence = " ".join(args.sentence)
    if args.echo:
        translator.sayraw(sentence)
    translator.say(sentence)
