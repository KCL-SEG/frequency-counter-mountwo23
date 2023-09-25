"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    finalFrequencies = {}
    for x in items:
        stringKey = str(x)
        if stringKey in finalFrequencies:
            count = finalFrequencies[stringKey] + 1
        else:
            count = 1
        finalFrequencies[stringKey] = count

    # Your code goes here
    return finalFrequencies
