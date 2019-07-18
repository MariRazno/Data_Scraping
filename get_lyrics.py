"""
Mariia Razno

Download song lyrics.

download all songs of an artist from the website https://www.lyrics.com:

"""

import sys
import requests
from lxml import html

def get_lyrics(link, text_file):
    artist = requests.get(link)
    tree = html.fromstring(artist.text)
    headlines = tree.xpath(r'//td/strong/a/@href')
    lyrics = []
    for i in headlines:
        songLink = "https://www.lyrics.com"+i
        song = requests.get(songLink)
        tree1 = html.fromstring(song.text)
        text = tree1.xpath(r'//pre[@id="lyric-body-text"]//text()')
        lyrics.append(text)
    with open(text_file, 'w', encoding="utf-8") as f:
        for item in lyrics:
            item = " ".join(item)
            f.write(item)

if __name__ == '__main__':
    # execute only if run as a script
    get_lyrics(sys.argv[1], sys.argv[2])

