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

"""Read csv with names, email addresses and room numbers of participants
    """
def read_file():
    with open('list.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        giver_list = list(reader)
        giver_list = giver_list[1:] # remove first row
        return giver_list

""" Write csv with names, email and addresses of givers and receivers
    """
def write_file(givers_list, random_number):
    with open('pairs.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for ind in range(givers_list.__len__()):
            writer.writerow([givers_list[ind][1] + ',' + givers_list[ind][2]
                + ',' + givers_list[random_number[ind]][1] + ','
                + givers_list[random_number[ind]][2]])

""" Define a main() function that calls the necessary functions.
    """
def main():
    # Get givers list and generate receivers list
    givers_list = read_file() # read csv file
    number_of_participants = givers_list.__len__() # number of participants
    random_number = list(range(number_of_participants)) # array of indices
    max_iterations = 1000
    iteration = 0
    conditions_met = False
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
    write_file(givers_list, random_number) # write csv file with pairs
    for ind in range(number_of_participants): # print in Terminal
        # print(givers_list[ind][1])
        print(givers_list[ind][1], "(", givers_list[ind][2], ") to", givers_list[random_number[ind]][1], "(", givers_list[random_number[ind]][2], ")")
    print ("Number of iterations needed: ", iteration) # Print number of iterations

""" This is the standard boilerplate that calls the main() function.
    """
if __name__ == '__main__':
    main()