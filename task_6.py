
import json
def analyse_movies_language():
    file=open("task_5.json","r")
    file2=json.load(file)
    # print(file2)
    list1=[]
    for i in file2:
        if i["Original Language"] not in list1:
            list1.append(i["Original Language"]) 
            # print(list)
    dict1={}
    # list2=[]
    for k in list1:
        i=0
        count=0
        while i<len(file2):
            if k==file2[i]["Original Language"]:
                count+=1
            i+=1
        dict1.update({k:count})
    list1.append(dict1)
    with open("task_6.json","w")as read_content:
        json.dump(dict1,read_content,indent=4)
    return dict1
analyse_movies_language()
