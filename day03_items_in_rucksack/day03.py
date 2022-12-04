import requests
from enum import Enum

url = "https://adventofcode.com/2022/day/3/input"

SESSIONID = "53616c7465645f5fbefe639536f4494cf0cf8cd653bbab17826e6a37f2b4ee6fc7fa12a606b2419d275e8dc9ecbede1796bae328bf608adc7ab647bf20133600"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"


def getPrio(item):
    if ord('A') <= ord(item) and ord(item) < ord('a'):
        return 27 + ord(item) - ord('A')
    if ord(item) >= ord('a'):
        return ord(item) - ord('a') + 1


def processRucksack(sack):
    
    half_len = len(sack)//2
    part1 = sack[:half_len]
    part2 = sack[half_len:]
    print(f'rucksack: {sack} with part 1 {part1} and part 2 {part2}')
    dict2 = dict.fromkeys(part2)
    dictDupes = dict()
    itemsPrio = 0
    for c in part1:
        if c in dict2 and c not in dictDupes:
            dictDupes[c] = True
            prio = getPrio(c)
            print(f'item {c} is in both compartments with prio = {prio}')
            itemsPrio += prio
    print(f'total priority of duplicates is {itemsPrio}')
    return itemsPrio


try:
    response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})
    prioSum = 0
    for line in response.text.splitlines():

        prioSum += processRucksack(line)
    print(prioSum)
except:
    print("error")
