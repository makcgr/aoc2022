import requests
from enum import Enum

url = "https://adventofcode.com/2022/day/4/input"


SESSIONID = "53616c7465645f5fbefe639536f4494cf0cf8cd653bbab17826e6a37f2b4ee6fc7fa12a606b2419d275e8dc9ecbede1796bae328bf608adc7ab647bf20133600"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"


def createSet(startId, finishId):
    return set(range(int(startId), int(finishId)+1))

try:
    response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

    count = 0
    
    for line in response.text.splitlines():

        first, second = [ createSet(*s.split(sep="-")) for s in line.split(sep=",") ]

        if first.issuperset(second) or first.issubset(second):
            count+=1

    print(f'Count of fully intersecting areas: {count}')
except:
    print("error")


