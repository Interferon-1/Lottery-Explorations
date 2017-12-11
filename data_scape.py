#Need to scrape data
from lxml import html
from urllib.request import urlopen

file_url = 'Documents/Winners.htm' 
data_source = urlopen(file_url).read() # demonstrating a clear lack of understanding
htmlelem = html.document_fromstring(data_source)

## test out to see if selecting correct elements
lot_wins = htmlelem.cssselect('[class=wn-location]')
#print(lot_wins)
with open('winner_locations.csv', 'w') as wf:
    for elem in lot_wins:
        text = elem.text_content().split('\n')[0]
        if text[-4:] == ', GA':
            wf.write(text + '\n')