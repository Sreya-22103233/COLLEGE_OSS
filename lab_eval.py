#ADD STUDENT
l=[{"Student_ID":101,"Name":"Sreya","Class":"B8","Grades":[8,9,7,8,9]},{"Student_ID":102,"Name":"Nandini","Class":"B8","Grades":[9,9,10,8,9]},{"Student_ID":103,"Name":"Manasvi","Class":"B8","Grades":[8,8,7,8,9]}]

def add_newStd(l,name,ID,cl,list_of_grades):
    d=dict()
    d["Student_ID"]=ID
    d["Name"]=name
    d["Class"]=cl
    d["Grades"]=list_of_grades
    l.append(d)
    return l

n=input("Enter Name: ")
Id=input("Enter ID: ")
batch=input("Enter Batch: ")
log=input("Enter list of grades in square brackets: ")
s=add_newStd(l,n,Id,batch,[8,9,8,6,5])
print(s)

#UPDATE GRADES
def update_grades(l,ID,list_of_grades):
    for i in l:
        if i["Student_ID"]==ID:
            i["Grades"]=list_of_grades
            break
    return l

t=update_grades(l,int(4545),[8,10,9,9,7])
print(t)



#CALCULATE AVERAGE
def calculate_avg(l,ID):
    Sum=0
    C=0
    for i in l:
        if i["Student_ID"]==ID:
            for j in i["Grades"]:
                Sum+=j
                C+=1
            break
    return Sum/C

r=calculate_avg(l,101)
print("Average Score for given Student: ",r)

#GENERATE TOP STUDENTS SCORE
def generate_top_students_report(l):
    dic=dict()
    for i in l:
        Sum=0
        C=0
        for j in i["Grades"]:
            Sum+=j
            C+=1
        dic[Sum/C]=i["Student_ID"]
    s=sorted(dic,reverse=True)
    f={i:dic[i] for i in s}
    return f

u=generate_top_students_report(l)
print("Students on the basis of performances: ",u)


