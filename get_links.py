import sys
from bs4 import BeautifulSoup
import quopri

filename = sys.argv[1]
with open(filename, 'r') as myfile:
	data = myfile.read()
data = quopri.decodestring(data)
soup = BeautifulSoup(data, 'html5lib')

for link in soup.find_all('a'):
    print(link.get('href'))
