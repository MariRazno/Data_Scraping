"""
Mariia Razno

Download animals` names from "http://a-z-animals.com/animals/"  and "https://switchzoo.com/animallist.htm".

for each set: lowercases each word,
filters out animal names with more than one word, but remembers the names that are followed by a comma.

creates a file in the same directory as the script with the list of unique animal names
(from both web pages united) in the alphabetical order one per line.

"""

import sys
import requests
from lxml import html

def get_animals(text_file):

    zoo_1 = requests.get(r"http://a-z-animals.com/animals/")
    tree = html.fromstring(zoo_1.text)
    animals_1 = tree.xpath(r'//div[@class="letter"]/ul/li/a//text()')
    zoo_2 = requests.get(r"https://switchzoo.com/animallist.htm")
    tree = html.fromstring(zoo_2.text)
    animals_2 = tree.xpath("//td/p/a/text()")
    #lower case animals` names from the first link and extract only one word names
    goodAnimals = []
    skip = []
    for i in animals_1:
        i = i.lower()
        if " " not in i:
            goodAnimals.append(i)
        else:
            skip.append(i)
    # lower case animals` names from the second link and extract only one word names
    goodAnimals2 = []
    for p in animals_2:
        p = p.lower()
        if " " not in p:
            goodAnimals2.append(p)
        else:
            skip.append(p)
    xz = set(goodAnimals).union(set(goodAnimals2))
    print(sorted(list(xz)))
    with open(text_file, 'w', encoding="utf-8") as f:
        for item in xz:
            item = "".join(item)
            f.write(item+"\n")


if __name__ == '__main__':
    # execute only if run as a script
    get_animals(sys.argv[1])


