


import json
def analyse_movies_language():
    file1=open("task_5.json","r")
    file2=json.load(file1)
    # print(file2)
    list1=[]
    for i in file2:
        if i["Director"] not in list1:
            list1.append(i["Director"]) 
            # print(list)
    dic={}
    # list2=[]
    for k in list1:
        i=0
        count=0
        while i<len(file2):
            if k==file2[i]["Director"]:
                count+=1
            i+=1
        dic.update({k:count})
    list1.append(dic)
    with open("task_7.json","w")as read:
        json.dump(dic,read,indent=4)
    return dic
analyse_movies_language()
