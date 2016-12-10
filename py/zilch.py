# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:20:21 2016

@author: jaety

Caitlyn introduced me to this game from class: Zilch. 
On each turn the player rolls 6 dice. You score as follows:

6 of a kind: 1000 points + roll again
1,2,3,4,5,6: 500 points + roll again
3 pairs: 500 points + roll again
1's are 100 pts
5's are 50 pts
3 ones 1000 pts
3 of a kind (other than 1s) 100 x value on the die.
If none of the above you go back to zero

first to 5000 wins

I wondered what the distribution of number of turns looked like.
"""
import numpy as np

def to_dice_list(idx):
    """ Mapping between integer and 6 element dice definition """
    s = np.base_repr(idx, base=6)
    return map(lambda s: int(s)+1, "0"*(6-len(s)) + s)

def to_dice_idx(lst):
    return int("".join(map(lambda x: str(x-1), lst)),6)

# Predicates. Let's assume they're sorted here
def all_of_a_kind(dice):
    return all(map(lambda x: x==dice[0], dice[1:]))

def one_of_each(dice):
    return np.all(np.diff(dice) == 1)
    
def three_pairs(dice):
    a = np.array(dice)
    return all(a[::2] == a[1::2])

def calc_others(dice):
    def inner(score, dice_left):
        if len(dice_left) == 0:
            return score
        elif len(dice_left) >= 3 and np.all(np.array(dice_left[:3]) == 1):
            return inner(score + 1000, dice_left[3:])
        elif len(dice_left) >= 3 and dice_left[0] == dice_left[1] == dice_left[2]:
            return dice_left[0] * 100
        elif dice_left[0] == 5:
            return inner(score + 50, dice_left[1:])
        elif dice_left[0] == 1:
            return inner(score + 100, dice_left[1:])
        else:
            return inner(score, dice_left[1:])
    return inner(0, dice)

def score(dice):
    if all_of_a_kind(dice):
        return (1000, True)
    elif one_of_each(dice) or three_pairs(dice):
        return (500, True)
    else:
        return (calc_others(dice), False)
        
def outcomes():
    results = {}
    for i in xrange(0, 6**6):
        key = score(to_dice_list(i))
        results.setdefault(key, 0) 
        results[key] += 1
    return results

# Need to account for repeats. No sure of the cleanest way to do that yet


def probs(results):
    total = float(np.sum(results.values()))
    out = {}
    for key, value in results.items():
        out.setdefault(key[0], 0)
        out[key[0]] += value / total
    return out        
    
def probs_next(cum_probs, one_step_probs):
    results = {}
    for (score, prob) in cum_probs.items():
        for (next_score, next_prob) in one_step_probs.items():
            res_score = score + next_score
            results.setdefault(res_score,0)
            results[res_score] += prob * next_prob
    return results
    
def prob_finished(probs):
    cum_prob = probs
    for round in xrange(20):
        cum_prob = probs_next(cum_prob, probs)
    return cum_prob