

import json
from task_5 import data1


def analyse_language_and_directors(movie_directer):
    dic={}
    for directer in movie_directer:
        directer=directer["Director"]
        dic[directer]={}
        # print(directer)
        count=0
        for  directer1 in range(len(movie_directer)):
            if directer==movie_directer[directer1]["Director"]:
                language=movie_directer[directer1]["Original Language"]
                count+=1
                dic[directer].update({language:count})
    with open("task_10.json","w") as file:
        json.dump(dic,file,indent=4)
analyse_language_and_directors(data1)

