import requests
from bs4 import BeautifulSoup
import datetime as dt

GEO_URL = "https://www.geo.tv/schedule"
ARY_URL = "https://www.ontvtonight.com/guide/listings/channel/295630272/ary-news.html"
DUNYA_URL ="https://www.ontvtonight.com/guide/listings/channel/3739649474/dunya-tv-usa.html"

date_today = dt.datetime.now()
# GEO NEWS
print("****Geo News List****")
resp = requests.get(GEO_URL)

soup_month = BeautifulSoup(resp.text, features='lxml')
res = soup_month.find('div', class_='month')
print(f"Date: {res.get_text()}")

soup_times = BeautifulSoup(resp.text, features='lxml')
res = soup_times.find_all('span', class_='timeslot')

time_list = []
for time in res:
    #print(time.get_text())
    time_list.append(time.get_text())

soup_names = BeautifulSoup(resp.text, features='lxml')
res = soup_names.find_all('span', class_='schudule_status')

name_list = []
for name in res:
    #print(name.get_text())
    name_list.append(name.get_text())

out_file = open("Geo_Schedule.txt", "a")
out_file.write("\nDate: "+str(date_today) + "\n")
for i in range(len(name_list)):
    line = time_list[i]+" "+name_list[i]
    out_file.write(line+"\n")
out_file.close()

# ARY NEWS
print("****Ary News List****")
resp2 = requests.get(ARY_URL)

soup_times = BeautifulSoup(resp2.content, features='lxml')
res2 = soup_times.find_all('h5', class_='thin')

i = 0
name_list = []
time_list = []
for content in res2:
    content_text = content.get_text().strip()
    if "More channels at the American TV Listings Guide.." in content_text or i == 0 or i == 1:
       i += 1
       continue
    if i%2 == 0:
       time_list.append(content_text)
    else:
       name_list.append(content_text)
    i += 1

out_file = open("ARY_Schedule.txt", "a")
out_file.write("\nDate: "+str(date_today) + "\n")
for i in range(len(name_list)):
    line = time_list[i]+" "+name_list[i]
    out_file.write(line+"\n")
out_file.close()

# DUNYA NEWS
print("****Dnuya News List****")
resp3 = requests.get(DUNYA_URL)

soup_times = BeautifulSoup(resp3.content, features='lxml')
res3 = soup_times.find_all('h5', class_='thin')
'''
for content in res3:
    content_text = content.get_text().strip()
    if "More channels at the American TV Listings Guide.." in content_text:
       continue
    print(content_text)
'''
i = 0
name_list = []
time_list = []
for content in res3:
    content_text = content.get_text().strip()
    if "More channels at the American TV Listings Guide.." in content_text or i == 0 or i == 1:
       i += 1
       continue
    if i%2 == 0:
       time_list.append(content_text)
    else:
       name_list.append(content_text)
    i += 1

out_file = open("Dunya_Schedule.txt", "a")
out_file.write("\nDate: "+str(date_today) + "\n")
for i in range(len(name_list)):
    line = time_list[i]+" "+name_list[i]
    out_file.write(line+"\n")
out_file.close()
