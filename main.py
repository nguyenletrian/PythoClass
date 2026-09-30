import pandas as pd

def inputHelper(data):            
    label = data["label"]
    formats = data["formats"]    
    inputTemp = input(label)    
    if inputTemp == "":
        return(None)    
    blocks =  inputTemp.split(";")  
                  
    # Check block
    if len(blocks) != len(formats):
        print("!!![ERROR] Input blocks is not correct!~")
            
    # Check type
    for i in range(len(formats)):
        if type(blocks[i]).__name__ != formats[i]:
            print("!!![ERROR] Input format is not corrects")              
    return(blocks)    
    
def displayAll():
    df = pd.read_csv("students.csv")
    print("""
==== DISPLAY ALL STUDENT =====""")
    students = df[" name"].values
    stt = 1
    for student in students:
        print(f"{stt}. {student}")
        stt += 1

def studentSearch():
    print("""
==== SEARCH STUDENT =====""")
    inputData = inputHelper({
        "label":"Please enter Student ID:",
        "formats":["str"]
    })
    if inputData:
        inputData = inputData[0]
        df = pd.read_csv("students.csv")
        result = df[df["student_id"] == inputData]
        if len(result)!=0:
            print(result)
        else:
            print("!!![ERROR] Student not found.")
        studentSearch()
    else:
        return
    
def studentAverage():
    print("""
==== STUDENT RESULT ====""")
    inputData = inputHelper({
        "label":"Please enter Student ID:",
        "formats":["str"]
    })
    if inputData:
        inputData = inputData[0]
        df = pd.read_csv("students.csv")
        result = df[(df["student_id"] == inputData)]
        if len(result)!=0:
            values = result.values
            print(f"""
Student name: {values[0][1]}
Python score: {values[0][3]}
Math score: {values[0][4]}
ML score: {values[0][5]}
Average score:{round((values[0][3] + values[0][4] + values[0][5])/3,2)}
Highest score:{max(values[0][3],values[0][4],values[0][5])}
Lowest score:{min(values[0][3],values[0][4],values[0][5])}
""")
        else:
            print("!!![ERROR] Student not found.")
        studentAverage()
    else:
        return

def analyzeSubject():
    print("""
==== SUBJECT PERFORMANCE ====""")
    df = pd.read_csv("students.csv")
    data = {
        "Average":[df["Python"].mean(),df["Math"].mean(),df["ML"].mean()],
        "Total":[df["Python"].sum(),df["Math"].sum(),df["ML"].sum()],
        "Highest":[df["Python"].max(),df["Math"].max(),df["ML"].max()],
        "Lowest":[df["Python"].min(),df["Math"].min(),df["ML"].min()],
    }
    dfShow = pd.DataFrame(data,index=["Python","Math","ML"])
    print(dfShow)


def analyzeClass():
    print("""
===== CLASS PERFORMANCE =====""")
    df = pd.read_csv("students.csv")
    studentCount =  df.groupby("class_name")["student_id"].count()
    pythonMean =  df.groupby("class_name")["Python"].mean()
    mathMean =  df.groupby("class_name")["Math"].mean()
    mlMean =  df.groupby("class_name")["ML"].mean()
    result = pd.merge(studentCount,pythonMean,on="class_name",how="outer")
    result = pd.merge(result,mathMean,on="class_name",how="outer")
    result = pd.merge(result,mlMean,on="class_name",how="outer")
    result["Overall Average"] = (result["Python"] + result["Math"] +  result["ML"])/3
    
    
    result.reset_index(inplace=True) #Trợ giúp của chat GPT ạ!~
    result.rename(columns={"student_id":"Students"}, inplace=True) #Trợ giúp của chat GPT ạ!~
    result.rename(columns={"class_name":"Class"}, inplace=True)
    
    result = result.round(2) # Trợ giúp của chat GPT ạ!~
    
    print(result)

def top3():
    print("""
===== TOP 3 STUDENTS =====""")
    df = pd.read_csv("students.csv")
    df["Average"] =   (df["Python"] + df["Math"] +  df["ML"])/3
    dfSorted = df.sort_values(by="Average",ascending=False)
    dfSorted.drop(columns=["Python","Math","ML"], inplace=True) # Trợ giúp của chat GPT ạ!~
    dfSorted.rename(columns={"class_name":"Class","student_id":"Student ID"}, inplace=True)
    dfSorted = dfSorted.round(2)
    
    print(dfSorted.head(3))    

# MENU()
def menu():
    choice = 0
    while True:
        print("""
================================
 STUDENT PERFORMANCE ANALYSIS
------------------------------------------------------
1. Display all students
2. Search for a student
3. Calculate student average
4. Analyze subject performance
5. Analyze class performance
6. Show top 3 students
7. Exit         
        """)
        # nhap lua chon
        inputData =input("Please select (1-7): ")
        if inputData.isnumeric():
            choice = int(inputData)
            if choice == 1:
                displayAll()
            elif choice == 2:
                studentSearch()
            elif choice == 3:
                studentAverage()
            elif choice == 4:
                analyzeSubject()
            elif choice == 5:
                analyzeClass()
            elif choice == 6:
                top3()
            elif choice == 7:
                break
            else:
                print("!!![ERROR] Please enter from 1 to 7")
        else:
            print("!!![ERROR] Please enter from 1 to 7")

# goi ham
menu()
