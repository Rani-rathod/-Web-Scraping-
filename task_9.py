

from bs4 import BeautifulSoup
import requests
import json
from task_1 import data

# url=data[0]["movie URL"]
i=0
while i<=10:
    url=data[i]["movie_URL"]
    movie_details=[]
    def details_movie(link):
        i=0
        while i<10:
            movie_id=' '
            for id in link[33:]:
                if "/" not in id:
                    movie_id+=id
                else:
                    break
            file_name=movie_id+".json"
            d1={}

            link1=requests.get(link)
            # print(link1)
            soup=BeautifulSoup(link1.text,'html.parser')
            # print(soup)
            d1['name']=soup.find('h1').text
            movie_bio=soup.find('div',class_='movie_synopsis clamp clamp-6 js-clamp' ).get_text().strip()
            # print(movie_bio)
            d1['Bio']=movie_bio
            title=soup.find_all('div',class_='meta-label subtle')

            value=soup.find_all('div',class_='meta-value')
            for i in range(len(title)):
                d1[str(title[i].get_text().strip())[:-1]]=value[i].get_text().replace(" ","").strip().replace("\n"," ")
            movie_details.append(d1)
            # i+=1
        with open(file_name,"w") as file:
            json.dump(movie_details,file,indent=4)
            # i+=1
    details_movie(url)
    i+=1