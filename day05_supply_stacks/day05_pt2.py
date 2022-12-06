import requests
from enum import Enum

day = "5"
url = f"https://adventofcode.com/2022/day/{day}/input"


SESSIONID = "53616c7465645f5fbefe639536f4494cf0cf8cd653bbab17826e6a37f2b4ee6fc7fa12a606b2419d275e8dc9ecbede1796bae328bf608adc7ab647bf20133600"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"


def createSet(startId, finishId):
    return set(range(int(startId), int(finishId)+1))


try:
    response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

    num = 0

    stacks = list()
    for line in response.text.splitlines():
        s_line = line.lstrip()

        # Parse stacks of crates
        if len(s_line) > 0 and s_line[0]=='[':
            if num==0:
                num = (len(line)+1) // 4
                print(f'There are {num} stacks')

            for ix in range(len(line)):
                if (ix-1)%4 == 0:
                    stack_no = (ix-1) // 4
                    if len(stacks) < (stack_no+1):
                        stacks.append(list())
                    if line[ix]!=' ':
                        stacks[stack_no].insert(0,line[ix])

        if len(s_line) > 0 and s_line[0]=='1':
            continue

        # Execute crane program
        if len(s_line) > 0 and s_line[0:4]=='move':
            _,quantity,_,stack_from,_,stack_to = [ int(s) if s.isnumeric() else None for s in line.split(sep=" ") ]
            
            # take {quantity} of crates at once and move from {stack_from} -> {stack_to}'
            crane_holder = list()
            while quantity > 0:
                crane_holder.insert(0,stacks[stack_from-1].pop())                
                quantity -= 1     

            while len(crane_holder)>0:
                stacks[stack_to-1].append(crane_holder.pop(0))              
    
    topCrates = ""
    for ix in range(len(stacks)):
        if len(stacks[ix])>0:
            topCrates += stacks[ix][-1]

    print(topCrates)

except Exception as e:
    print(f'Error: {str(e)}')