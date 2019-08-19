import csv
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd


results = []
def scrape():
	offset = 1
	url = f'https://www.marketwatch.com/search?q=sectorwatch&m=Keyword&rpp=15&mp=3264&bd=false&rs=false&o={offset}'

	while True:
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'html.parser')
		resultlist = soup.find("div", class_="resultlist")
		# If no results, break out of while loop
		if resultlist is None:
			break
		blocks = resultlist.find_all("div", class_="block")
		for block in blocks:
			searchresult = block.find("div", class_="searchresult")
			# Sometimes it returns an iframe, skip to next iteration
			if searchresult is None:
				continue
			date_string = block.find("div", class_="deemphasized").find("span").text
			name = searchresult.text.strip()
			link = searchresult.find("a")['href']
			time = re.search(r'((1[0-2]|[0-9]):([0-5][0-9]) ?([ap]\.[m]\.))', date_string).group(0)
			date = re.search(r'(Jan.|Feb.|March|April|May|June|July|Aug.|Sept.|Oct.|Nov.|Dec.)\s+(\d{1,2}),\s+(\d{4})', date_string).group(0)
			results.append([name, date, time, link])


		offset += 15
		url = f'https://www.marketwatch.com/search?q=sectorwatch&m=Keyword&rpp=15&mp=3264&bd=false&rs=false&o={offset}'
		print(offset)

def write():
	df = pd.DataFrame(results, columns=['name', 'date', 'time', 'link'])
	df.to_csv('output.csv', index=False)

scrape()
write()