import requests


url = "https://adventofcode.com/2022/day/1/input"


SESSIONID = "53616c7465645f5fbefe639536f4494cf0cf8cd653bbab17826e6a37f2b4ee6fc7fa12a606b2419d275e8dc9ecbede1796bae328bf608adc7ab647bf20133600"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"


try:
    response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

    maxCal = 0  # top calories elf
    curCal = 0

    myList = list()
    for line in response.text.splitlines():
        isEmpty = not len(line.strip())
        if isEmpty:
            myList.append(curCal)
            if (len(myList)>3):
                myList.sort(reverse=True)
                myList = myList[:3]

            if maxCal < curCal:
                maxCal = curCal

            curCal = 0
        else:
            curCal += int(line)


    print(myList[0])
    if len(myList) >= 3:
        print(myList[0]+myList[1]+myList[2])

except IOError:
    print("I/O error occured")

