from bs4 import BeautifulSoup
import requests
import csv

url = "https://myanimelist.net/topmanga.php"

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

manga_len = []
manga_title_len = []
manga_year_len = []

#Manga 1 - 50

manga9 = doc.find_all('span', class_='text on score-label score-9')
for manga in manga9:
    rank = manga.text
    manga_len.append(rank)

manga8 = doc.find_all('span', class_='text on score-label score-8')
for manga in manga8:
    rank = manga.text
    manga_len.append(rank)



manga_title = doc.find_all('a', class_='hoverinfo_trigger fs14 fw-b')
for manga in manga_title:
    title = manga.text
    manga_title_len.append(title)


manga_year = doc.find_all('div', class_='information di-ib mt4')
for manga in manga_year:
    info_text = manga.text
    release_year = info_text.strip().split('\n')[1].split()[1]
    manga_year_len.append(release_year)

 
manga = {}
man_rank = 1
manga_list = []

for i in range(len(manga_title_len)):
    manga_dict = {}
    manga_dict['Title'] = manga_title_len[i]
    manga_dict['Score'] = manga_len[i]
    manga_dict['Year'] = manga_year_len[i]
    manga_dict['Rank'] = i + 1
    manga_list.append(manga_dict)

csv_file = 'manga_top_50.csv'

field_names = ['Title', 'Score', 'Year', 'Rank']

with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(manga_list)

print('Successful :)')
