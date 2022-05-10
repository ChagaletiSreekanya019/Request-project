import requests
import json

url=requests.get('https://api.merakilearn.org/courses')
r=json.loads(url.text)
with open("requts.json","w") as f:
    json.dump(r,f,indent=4)
i=0
while i<len(r):
    print(i+1,r[i]["name"],r[i]["id"])
    i+=1
course_no=int(input("select which course you want display  :"))
print(course_no,r[course_no-1]["name"])
course_id=r[course_no-1]["id"]

url1=requests.get('https://api.merakilearn.org/courses/'+str(course_id)+"/exercises")
r1=json.loads(url1.text)
with open("parent.json","w") as f2:
    json.dump(r1,f2,indent=6)
print(r[course_no-1]['name'],"-",r[course_no-1]["id"])
serial=1
serial1=1
list=[]
list1=[]
n=1
for i in r1["course"]["exercises"]:
    if i["parent_exercise_id"]==None:
        print(serial,i["name"])
        print(" ",serial1,i["slug"])
        serial+=1
        list.append(i)
        list1.append(i)
    elif i["parent_exercise_id"]==i["id"]:
        print(serial,i["name"])
        serial+=1
        list.append(i)
    elif i["parent_exercise_id"]!=i["id"]:
        print(" ",n,i["name"])
        n+=1
        list1.append(i)
t=open("l.json","w")
json.dump(list,t,indent=3)
t=open("l1.json","w")
json.dump(list1,t,indent=3)



parent_id=int(input("enter enter no: "))
serial=1
for i in list1:
    if i["parent_exercise_id"]==i["id"]:
        print(serial,list1[parent_id-1]["name"])
        serial+=1
        break
    else:
        if i["parent_exercise_id"]!=i["id"]:
            print(serial,list1[parent_id-1]["name"])
            print("",list1[parent_id-1]["content"])
            serial+=1
            break






# import requests
# import json
# import os 

# path_exists=os.path.exists("requests.json")
# if path_exists==False:
#     url=requests.get('https://api.merakilearn.org/courses')
#     r=json.loads(url.text)
#     with open("requests.json","w") as f:
#         json.dump(r,f,indent=4)
#     serial=0
#     for i in range(len(r)):
#         for k,v in r[i].items():
#             if k=="name":
#                 serial+=1

#                 print(serial,v,"-",r[i]["id"])
#     course=int(input("select which course you want display  :"))
#     print(course,r[course-1]["name"])

#     course_id=r[course-1]["id"]
#     url1=requests.get('https://api.merakilearn.org/courses/'+str(course_id)+"/exercises")
#     r1=json.loads(url1.text)
#     with open("res.json","w") as f2:
#         json.dump(r1,f2,indent=6)
#     print(r[course-1]['name'],"-",r[course-1]["id"])
# #     list2=[]
#     j=0
#     k=1
#     for i in r1["course"]["exercises"]:   
#         if i["parent_exercise_id"]==None:
#             j=j+1
#             list2.append(i)
        
#         elif i["parent_exercise_id"]==i["id"]:
#             print(j+1,".",i["name"])
#             list2.append(i)
#             j=j+1   
#         elif i["parent_exercise_id"]!=i["id"]:
#             print(" ",k,".",i["name"])
#             list2.append(i)
#         k=k+1

#     with open("lis.json","w") as f:
#         json.dump(list2,f,indent=4)
#     parent_id=int(input(" which parent id you want to enter : "))
#     for i in range(0,len(list2)):
#         if parent_id==i+1:
#             print(parent_id,list2[i]["name"])
#             a=list2[i]["parent_exercise_id"]
#     s=1
#     w=[]
#     g=[]
#     for d in range(0,len(list2)):
#         if list2[d]["parent_exercise_id"]==a:
#             print(" ",s,list2[d]["name"])
#             w.append(list2[d]["name"])
#             g.append(list2[d]["content"])
#             s+=1
#     child_number=int(input("which child you want to print"))
#     print(g[child_number-1])


# if path_exists==True:
#     url=open("requests.json","r")
#     r=json.load(url)
#     serial=0
#     for i in range(len(r)):
#         for k,v in r[i].items():
#             if k=="name":
#                 serial+=1
#                 print(serial,v,"-",r[i]["id"])
#     course=int(input("enter the course do you want : "))

#     course_id=r[course-1]["id"]
#     file=os.path.exists("requests.json")
#     if file==False:
#         url1=requests.get('https://api.merakilearn.org/courses/'+str(course_id)+"/exercises")
#         r1=json.loads(url1.text)
#         file=open("res.json","w")
#         json.dump(r1,file,indent=4)
#     elif file==True:
#         url1=open("res.json","r")
#         r1=json.load(url1)
#         print(r[course-1]["name"],"-",r[course-1]["id"])

#         list2=[]
#         j=0
#         k=1
#         for i in list2:   
#             if i["parent_exercise_id"]==None:
#                 j=j+1
#                 list2.append(i)
#             elif i["parent_exercise_id"]==i["id"]:
#                 print(j+1,".",i["name"])
#                 list2.append(i)
#                 j=j+1   
#             elif i["parent_exercise_id"]!=i["id"]:
#                 print(" ",k,".",i["name"])
#                 list2.append(i)
#             k=k+1
#         file=os.path.exists("lis.json")


        
#         if file==True:
#             f=open("lis.json","r") 
#             a=json.load(f)
#             parent_id=int(input(" which parent id you want to enter : "))
#             for i in range(0,len(list2)):
#                 if parent_id==i+1:
#                     print(parent_id,list2[i]["name"])
#                     a=list2[i]["parent_exercise_id"]
#                     parent_id=int(input(" which parent id you want to enter : "))
#             s=1
#             w=[]
#             g=[]
#             for d in range(0,len(list2)):
#                 if list2[d]["parent_exercise_id"]==a:
#                     print(" ",s,list2[d]["name"])
#                     w.append(list2[d]["name"])
#                     g.append(list2[d]["content"])
#                     s+=1
#                     child_number=int(input("which child you want to print"))
#                     print(g[child_number-1])
                
