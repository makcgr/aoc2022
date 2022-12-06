import requests
from enum import Enum

day = "6"
url = f"https://adventofcode.com/2022/day/{day}/input"


SESSIONID = "53616c7465645f5fbefe639536f4494cf0cf8cd653bbab17826e6a37f2b4ee6fc7fa12a606b2419d275e8dc9ecbede1796bae328bf608adc7ab647bf20133600"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"

try:
    response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

    signal = response.text

    if len(signal)==0:
        print("Signal is empty")
        exit

    marker = ""
    diffCount = 0    
    prevSymbols = set()
    for idx in range(1,len(signal)):
        if signal[idx] not in prevSymbols:
            marker += signal[idx]
            diffCount += 1
        else:
            prevSymbols.clear()            
            marker = signal[idx]
            diffCount = 1

        prevSymbols.add(signal[idx])
        print(f'Last ix: {idx} Marker: {marker}')

        if diffCount == 4:
            print(idx)
            break


    print(f'Answer: {marker} Number of symbols: {idx+1}')

except Exception as e:
    print(f'Error: {str(e)}')
