# import numpy as np
from random import sample

nVoters = 5
nCandidates = 5

# this is not good, we need candidates to be in the form: {A, B, C, ...}
# candidates = range(nCandidates)
candidates = [chr(i) for i in range(ord('A'), ord('A') + nCandidates)]
preferences = {}

# Dictionary with the output of the vote
voting = {}
for candidate in range(ord('A'), ord('A') + nCandidates):
    voting[chr(candidate)] = 0

# ouput (giorgos says that maybe this should be in a function, probably he's right
for voter in range(nVoters):
    preferences[voter] = sample(candidates, len(candidates))
    print("For voter " +str(voter)+ " the preferences are: " +str(preferences[voter]))

# implementation of voting schemes
def voting_for_two(preference):
    for voter, preference in preferences.items():
        voting[preference[0]] += 1
        voting[preference[1]] += 1

def plurality_voting(preference):
    for voter, preference in preferences.items():
        voting[preference[0]] += 1

def anti_plurality_voting(preference):
    # print(preferences)
    for voter, preference in preferences.items():
        for i, p in enumerate(preference):
            if i is len(preference) - 1:
                break
            voting[p] += 1

def borda_voting(preference):
    for voter, preference in preferences.items():
        for i, p in enumerate(preference):
            voting[p] += len(preference) - 1 - i

