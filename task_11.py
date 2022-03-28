


from task_5 import data1
import json

def movie_gener():
    list1=[]
    dict1={}
    for i in data1:
        gener=i["Genre"].split(",")
        for i in gener:
            list1.append(i)
            # print(list1)                                                                        
        count=0
        for j in list1:
            count+=1
        dict1.update({j:count})
    with open("task_11.json","w") as file:
        json.dump(dict1,file,indent=4)
movie_gener()

