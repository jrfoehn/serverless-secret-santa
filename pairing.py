#!/usr/bin/python -tt

"""A 'Secret Santa' pairing script. Based on a list of names and email addresses, 
    it generates pairs such that a person won't have to buy 
    a present for themselves, or the person who has to 
    buy a present for them.
    The result is stored as a csv file.
    """

import sys
import csv
import random


""" Define a main() function that calls the necessary functions.
    """
def main(event, context):
    participants = event['body']['data']
    number_of_participants = participants.__len__()
    random_number = list(range(number_of_participants)) # array of indices
    max_iterations = 1000
    iteration = 0
    conditions_met = False
    pairs = list()
    # brute force randomisation and checking conditions
    while iteration<max_iterations and not conditions_met:
        iteration += 1           # increment iteration number
        random.shuffle(random_number) # randomise array of indices
        conditions_met = True    # unless one of following breaks
        for ind in range(number_of_participants):     # go over all indices of random index vector
            # Condition 1: not to themselves
            if random_number[ind] == ind:
                conditions_met = False
                break
            # Condition 2: not to their own Secret Valentine
            elif random_number[random_number[ind]] == ind:
                conditions_met = False
                break
    # write_file(givers_list, random_number) # write csv file with pairs
    for ind in range(number_of_participants): # print in Terminal
        # print(givers_list[ind][1])
        pairs.append(
            {
                "giver": [participants[ind][0], participants[ind][1]],
                "receiver": [participants[random_number[ind]][0], participants[random_number[ind]][1]]
            }
        )
       
if __name__ == '__main__':
    event= {
        "body": {
            "data": [
                ["JR0", "@@@@0"],
                ["JR1", "@@@@1"],
                ["JR2", "@@@@2"],
                ["JR3", "@@@@3"],
                ["JR4", "@@@@4"],
                ["JR5", "@@@@5"],
                ["JR6", "@@@@6"],
                ["JR7", "@@@@7"],
            ]
        }
    }
    context = ""
    main(event, context)