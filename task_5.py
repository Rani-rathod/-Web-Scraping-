
# a=[]
#     for i in top_movies:
#         a.append(i)
#         if i["movie_rank"]=="10":
#             break
#         url={}
#     for k in a:
#         url.update({k["movie_URL"]:k["movie_name"]})
#         # print(url)
#     for a,b in url.items():
#         print(a)



import requests
import json
from bs4 import BeautifulSoup
from task_1 import data


list1=[]
for i in data:
    url=i['movie_URL']
    # print(url)
    def get_movie_list_details(movie_url):
        page=requests.get(movie_url)
        soup=BeautifulSoup(page.text,"html.parser")
        title_div=soup.find("ul",class_="content-meta info")
        sub_title=title_div.find_all("li",class_="meta-row clearfix")
        # list1=[]

        movie_dict={}
        name=soup.find("h1", class_="scoreboard__title").get_text()
        movie_dict.update({'name': name})
        for i in sub_title:

            # print(i.get_text())
            key=i.find("div",class_="meta-label subtle").get_text().replace(":","")
            # print(key)
            Value=(i.find("div",class_="meta-value").text.replace(" ","").replace("\n","").strip())
            # print(Value)
            movie_dict.update({key:Value})
        list1.append(movie_dict)
        # print(movie_dict)
        # print(list1)
        with open("task_5.json","w") as file:
            json.dump(list1,file,indent=4)
        return list1
    get_movie_list_details(url)





import json
import pprint
# from task_4 import scrap_movies_details
from task_5 import get_movie_list_details

