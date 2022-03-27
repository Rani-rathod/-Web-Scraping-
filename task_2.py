
from task_1 import data
import json



def group_by_year(adventure_movie):
    years=[]
    for i in adventure_movie:
        year=i["year"]
        if year not in years:
            years.append(year)
    movie_dict={i:[]for i in years}
    # print(movie_dict)

    for i in adventure_movie:
        year=i["year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)

    with open("task_2.json","w")as file:
        json.dump(movie_dict,file,indent=4)
    return movie_dict
print(group_by_year(data))
