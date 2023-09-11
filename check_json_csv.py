import json 
import pandas as pd


with open('results_json.json', 'r') as file:
    data = json.load(file)

     

male = 0
female = 0
male_dead = 0
female_dead = 0
count = 0
ageSum = 0
ageAvg = 0
for key in data:
    if "31-0.0" in data[key]:
        if data[key]["31-0.0"] == 1:
            male = male + 1
        else:
            female = female + 1
 
with open('ids_died_T860.txt', 'r') as file:
    for id in file:
        if  id.strip() in data:
            if data[id.strip()]["31-0.0"] == 1:
                male_dead = male_dead + 1
            else:
                female_dead = female_dead + 1 
            
     
countFemale = 0
countMale = 0
ageSumMale = 0
ageSumFemale = 0
with open('ids_died_T860.txt', 'r') as file:
    for id in file:
        if  id.strip() in data:
            if "40008-0.0" in data[id.strip()] :
                 if data[id.strip()]["31-0.0"] == 1:
                    ageSumMale = ageSumMale + data[id.strip()]["40008-0.0"]
                    countMale = countMale + 1
                 else:
                    ageSumFemale = ageSumFemale + data[id.strip()]["40008-0.0"]
                    countFemale = countFemale + 1
print(countMale, countFemale)
cancerDMen =  ageSumMale/countMale
cancerDWomen= ageSumFemale/countFemale
print("The avg of diagnostic cancer at first in died men: ", ageSumMale/countMale)                  
print("The avg of diagnostic cancer at first in died women: ", ageSumFemale/countFemale)                  

generalCount = 0
generalAgeSum = 0

for key in data:
    if "40008-0.0" in data[key]:
        generalAgeSum = generalAgeSum + data[key]["40008-0.0"]
        generalCount = generalCount + 1
print("generalCount = ",generalCount) 
print("generalAgeSum = ",generalAgeSum) 
print("The avg of diagnostic cancer at first in all of the people: ", generalAgeSum/generalCount)                  

ageDeadSum = 0
ageDeadCount = 0
with open('ids_died_T860.txt', 'r') as file:
    for id in file:
        if  id.strip() in data:
            if "40007-0.0" in data[id.strip()] :
                print (data[id.strip()]["40007-0.0"])
                ageDeadSum = ageDeadSum + data[id.strip()]["40007-0.0"]
                ageDeadCount = ageDeadCount + 1
print("ageDeadCount = ",ageDeadCount)               
print("The avg age dead of died people: ", ageDeadSum/ageDeadCount)   


ageDeadMenSum = 0
ageDeadMenCount = 0
with open('ids_died_T860.txt', 'r') as file:
    for id in file:
        if  id.strip() in data:
            if data[id.strip()]["31-0.0"] == 1:
                if "40007-0.0" in data[id.strip()] :
                    print (data[id.strip()]["40007-0.0"])
                    ageDeadMenSum = ageDeadMenSum + data[id.strip()]["40007-0.0"]
                    ageDeadMenCount = ageDeadMenCount + 1
print("ageDeadMenCount = ",ageDeadMenCount)               
print("The avg age dead of died Men: ", ageDeadMenSum/ageDeadMenCount)  
ageDeadMen = ageDeadMenSum/ageDeadMenCount

ageDeadWomenSum = 0
ageDeadWomenCount = 0
with open('ids_died_T860.txt', 'r') as file:
    for id in file:
        if  id.strip() in data:
            if data[id.strip()]["31-0.0"] == 0:
                if "40007-0.0" in data[id.strip()] :
                    print (data[id.strip()]["40007-0.0"])
                    ageDeadWomenSum = ageDeadWomenSum + data[id.strip()]["40007-0.0"]
                    ageDeadWomenCount = ageDeadWomenCount + 1
print("ageDeadWomenCount = ",ageDeadWomenCount)           
ageDeadWomen = ageDeadWomenSum/ageDeadWomenCount    
print("The avg age dead of died Women: ", ageDeadWomenSum/ageDeadWomenCount)  
        

# וגם להוסיף 26410 
#40007- גיל מוות להוסיף    
 
decileLevelMenSum = 0 
decileLevelCountMen = 0
decileLevelCountWomen = 0
decileLevelWomenSum = 0
for key in data:
    if data[key]["31-0.0"] == 1:
        if "26424-0.0" in data[key]:
            #print(data[key]["26424-0.0"])
            decileLevelMenSum = decileLevelMenSum + data[key]["26424-0.0"]
            decileLevelCountMen = decileLevelCountMen + 1
        if "26410-0.0" in data[key]:
            #print(data[key]["26410-0.0"])
            decileLevelMenSum = decileLevelMenSum + data[key]["26410-0.0"]
            decileLevelCountMen = decileLevelCountMen + 1
    else:
        if "26424-0.0" in data[key]:
            #print(data[key]["26424-0.0"])
            decileLevelWomenSum = decileLevelWomenSum + data[key]["26424-0.0"]
            decileLevelCountWomen = decileLevelCountWomen + 1
        if "26410-0.0" in data[key]:
            #print(data[key]["26410-0.0"])
            decileLevelWomenSum = decileLevelWomenSum + data[key]["26410-0.0"]
            decileLevelCountWomen = decileLevelCountWomen + 1
print("decileLevelCountMen = ",decileLevelCountMen) 
print("decileLevelCountWomen = ",decileLevelCountWomen) 

print("decileLevel = ",decileLevelMenSum) 
decileLevelMen = decileLevelMenSum / decileLevelCountMen
decileLevelWomen = decileLevelWomenSum / decileLevelCountWomen
print("The avg of decile level in all of the people: ", decileLevelMen, decileLevelWomen)    

decileLevelDeadMenSum = 0
decileLevelCountDeadMen = 0
decileLevelCountDeadWomen = 0
decileLevelDeadWomenSum = 0
with open('ids_died_T860.txt', 'r') as file:
    for id in file:
        if  id.strip() in data:
            if data[id.strip()]["31-0.0"] == 1:
                if "26424-0.0" in data[id.strip()]:
                    print (data[id.strip()]["26424-0.0"])
                    decileLevelDeadMenSum = decileLevelDeadMenSum + data[id.strip()]["26424-0.0"]
                    decileLevelCountDeadMen = decileLevelCountDeadMen + 1
                if "26410-0.0" in data[id.strip()]:
                    print (data[id.strip()]["26410-0.0"])
                    decileLevelDeadMenSum = decileLevelDeadMenSum + data[id.strip()]["26410-0.0"]
                    decileLevelCountDeadMen = decileLevelCountDeadMen + 1
            else:
                if "26424-0.0" in data[id.strip()]:
                    print (data[id.strip()]["26424-0.0"])
                    decileLevelDeadWomenSum = decileLevelDeadWomenSum + data[id.strip()]["26424-0.0"]
                    decileLevelCountDeadWomen = decileLevelCountDeadWomen + 1
                if "26410-0.0" in data[id.strip()]:
                    print (data[id.strip()]["26410-0.0"])
                    decileLevelDeadWomenSum = decileLevelDeadWomenSum + data[id.strip()]["26410-0.0"]
                    decileLevelCountDeadWomen = decileLevelCountDeadWomen + 1
decileLevelDeadWomen = decileLevelDeadWomenSum / decileLevelCountDeadWomen
decileLevelDeadMen = decileLevelDeadMenSum / decileLevelCountDeadMen
print("decil:", decileLevelDeadMen, decileLevelDeadWomen) 
            
#print("decileLevelDead = ",decileLevelDead) 
#print("decileLevelCountDead = ",decileLevelCountDead)               
#print("The avg of decile level in dead people ", decileLevelDead/decileLevelCountDead) 

lukemiaCount = 0
countElse = 0
countC = 0
countC44 = 0
countC8 = 0
with open('ids_died_T860.txt', 'r') as file:
    for id in file:
        if  id.strip() in data:
             if "40006-0.0" in data[id.strip()]:
                 if "C92" in data[id.strip()]["40006-0.0"] or "C91" in data[id.strip()]["40006-0.0"]:
                     print(data[id.strip()]["40006-0.0"])
                     print(id.strip())
                     lukemiaCount = lukemiaCount + 1
                 if "D" in data[id.strip()]["40006-0.0"]:
                    countElse = countElse+1
                 if "C" in data[id.strip()]["40006-0.0"]:
                    countC = countC+1
                 if "C44" in data[id.strip()]["40006-0.0"]:
                    countC44 = countC44+1
                 if "C8" in data[id.strip()]["40006-0.0"]:
                    countC8 = countC8+1
print("lukemia in dead people = ",lukemiaCount) 
print("else in dead people = ",countElse) 
print("c in dead people = ",countC) 
print("c44 in dead people = ",countC44) 
print("c8 in dead people = ",countC8) 

lukemiaGeneralCount = 0
for key in data:
    if "40006-0.0" in data[key]:
        if "C92" in data[key]["40006-0.0"] or "C91" in data[key]["40006-0.0"]:
                     lukemiaGeneralCount = lukemiaGeneralCount + 1
print("c91 or c92 in all of the people:" , lukemiaGeneralCount)

lukemiaDeadWomenCount = 0
lukemiaDeadMenCount = 0
with open('ids_died_T860.txt', 'r') as file:
    for id in file:
        if  id.strip() in data:
             if "40006-0.0" in data[id.strip()]:
                 if (data[id.strip()]["31-0.0"] == 1):
                    if "C92" in data[id.strip()]["40006-0.0"] or "C91" in data[id.strip()]["40006-0.0"]:
                        print(data[id.strip()]["40006-0.0"])
                        print(id.strip())
                        lukemiaDeadMenCount = lukemiaDeadMenCount + 1
                 if (data[id.strip()]["31-0.0"] == 0):
                    if "C92" in data[id.strip()]["40006-0.0"] or "C91" in data[id.strip()]["40006-0.0"]:
                        print(data[id.strip()]["40006-0.0"])
                        print(id.strip())
                        lukemiaDeadWomenCount = lukemiaDeadWomenCount + 1
                
print("lukemia in dead people = ",lukemiaCount) 
print("lukemia in dead Men people = ",lukemiaDeadMenCount) 
print("lukemia in dead women people = ",lukemiaDeadWomenCount) 


otherDeadWomenCount = 0
otherDeadMenCount = 0
with open('ids_died_T860.txt', 'r') as file:
    for id in file:
        if  id.strip() in data:
             if "40006-0.0" in data[id.strip()]:
                 if (data[id.strip()]["31-0.0"] == 1):
                    if "D" in data[id.strip()]["40006-0.0"]:
                        print(data[id.strip()]["40006-0.0"])
                        print(id.strip())
                        otherDeadMenCount = otherDeadMenCount + 1
                 if (data[id.strip()]["31-0.0"] == 0):
                    if "D" in data[id.strip()]["40006-0.0"]:
                        print(data[id.strip()]["40006-0.0"])
                        print(id.strip())
                        otherDeadWomenCount = otherDeadWomenCount + 1
print("other in dead women  = ",otherDeadWomenCount)
print("other in dead men  = ",otherDeadMenCount) 
 
                
cDeadWomenCount = 0
cDeadMenCount = 0
with open('ids_died_T860.txt', 'r') as file:
    for id in file:
        if  id.strip() in data:
             if "40006-0.0" in data[id.strip()]:
                 if (data[id.strip()]["31-0.0"] == 1):
                    if "C" in data[id.strip()]["40006-0.0"]:
                        print(data[id.strip()]["40006-0.0"])
                        print(id.strip())
                        cDeadMenCount = cDeadMenCount + 1
                 if (data[id.strip()]["31-0.0"] == 0):
                    if "C" in data[id.strip()]["40006-0.0"]:
                        print(data[id.strip()]["40006-0.0"])
                        print(id.strip())
                        cDeadWomenCount = cDeadWomenCount + 1
print("C in dead women  = ",cDeadWomenCount)
print("C in dead men  = ",cDeadMenCount) 
                
print("male = ", male)
print("female = ", female)
print("male  dead = ", male_dead)
print("female  dead = ", female_dead)


data = {
    # 'Gender': ['Male', 'Female'],
    # 'Total number of GvHD cases': [male, female],
    # 'Number of deaths': [male_dead, female_dead],
    # 'age at first cancer diagnosis for deceased individuals': [cancerDMen, cancerDWomen],
    # 'avearge age of death': [ageDeadMen, ageDeadWomen],
    
    'Fields': ['Total number of GvHD cases', 'Number of deaths', 'Age at first cancer diagnosis for deceased'
               , 'Average age of death', 'Decile of all', 'Decile of the deceased', 'Number of deceased individuals with leukemia'],
    'Male':[male,male_dead, cancerDMen, ageDeadMen,decileLevelMen, decileLevelDeadMen, lukemiaDeadMenCount],
    'Female':[female,female_dead, cancerDWomen, ageDeadWomen, decileLevelWomen,decileLevelDeadWomen
              , lukemiaDeadWomenCount]
    
    
}

df = pd.DataFrame(data)
df['Male'] = df['Male'].round(2)
df['Female'] = df['Female'].round(2)

print(df)
with open ("/home/yuvalyh@mta.ac.il/table_results.txt", 'w') as file:
    file.write(str(df))
    
   



