from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys

keyword = sys.argv[1]
page = 1
root = 'http://ilga.gov/'
url = f'http://ilga.gov/search/iga_results.asp?target={keyword}&rc=50&start={page}&scope=leg101'
bills = []

while True:

	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	legislinks = soup.find_all("span", class_="legislinks")

	for i in range(len(legislinks)): 
		if i % 2 == 0: # i is an even number
			# I am a bill
			bill = []
			bill_text = legislinks[i].text.replace('&nbsp', " ")
			bill_number = bill_text.split(" ")[0]
			bill.append(bill_number)
			# bill_number = re.search(r'^([^\s]+)
		else:  # i is an odd number
			# I am a bill status
			link = root + legislinks[i].find("a")['href'][3:]
			bill_status_response = requests.get(link)
			status_soup = BeautifulSoup(bill_status_response.text, 'html.parser')
			sponsors = status_soup.find_all("a", class_="content")
			sponsor_names = ', '.join([sponsor.text for sponsor in sponsors])
			bill.append(sponsor_names)

			last_action = status_soup.find_all("td", class_="content")[:3]
			date = last_action.text.strip()
			print(date)
			[1,2,3]
			[1,2,[1,2,3]]
			[1,2,1,2,3]

			bills.append(bill)

	f'{keyword}-bills.csv'

	page += 1
	url = f'http://ilga.gov/search/iga_results.asp?target=cannabis&rc=50&start={page}&scope=leg101'
	if page > 2:
		break

#print(bills)
df = pd.DataFrame(bills, columns=['bill_number', 'bill_sponsors'])
df.to_csv('bills.csv', index=False)


