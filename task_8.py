
# import os
# import json
# from task_1 import data
# from task_4 import scrap_movies_details


# url=data[0]['movie_URL'] 
# def movie_details_with_url(URL):
#     for i in data:
#         # print(URL)
#         if i['movie_URL']==URL:
#             url1=i['movie_URL'][33:]
#             # NAME=i["name"]
#             print(url1)
#             # print(NAME)
#     # name1=movie_id+"json"
#     var=os.path.exists("/home/desktop/python/Web scrapping"+url1+".json")
#     # print(var)
#     if var==True:
#         with open ("movies_details_url.json","r") as f:
#             a=json.load(f)
#     else:
#         data1=scrap_movies_details(URL)
#         with open ("task_8.json","w") as f:
#             json.dump(data1,f,indent=4)
#     return data1
# movie_details_with_url(url)



from bs4 import BeautifulSoup
import requests
import json
from task_1 import data

# url=data[0]["movie URL"]
movie_details=[]
def details_movie(link):
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
    # print(movie_bio)4 
    d1['Bio']=movie_bio
    title=soup.find_all('div',class_='meta-label subtle')

    value=soup.find_all('div',class_='meta-value')
    for i in range(len(title)):
        d1[str(title[i].get_text().strip())[:-1]]=value[i].get_text().replace(" ","").strip().replace("\n"," ")
    movie_details.append(d1)

    with open(file_name,"w") as file:
        json.dump(movie_details,file,indent=4)

details_movie( "https://www.rottentomatoes.com/m/star_wars_the_last_jedi")