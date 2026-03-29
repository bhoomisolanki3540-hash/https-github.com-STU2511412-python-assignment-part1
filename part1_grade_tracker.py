##Task 1 — Data Parsing & Profile Cleaning 

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

#Loop through raw_students and for each student, produce a cleaned version where:
for student in raw_students:
    #clean the name
    clean_name = student["name"].strip().title()
    #convert roll to int
    roll = int(student["roll"])
    #convert marks_str to list of ints
    marks_list = []
    for mark in student["marks_str"].split(", "):
        marks_list.append(int(mark.strip()))
    #print the cleaned data
    print(clean_name, roll, marks_list)

#For each cleaned student, verify the name is valid: check that every word in the name contains only alphabetic characters. Print "✓ Valid name" or "✗ Invalid name" next to each student.
for student in raw_students:
    clean_name = student["name"].strip().title()

    is_valid_name = all(word.isalpha() 
        for word in clean_name.split())  
    
    if is_valid_name:
        print(clean_name,"✓ Valid name")
    else:
        print(clean_name,"✗ Invalid name")

#Print a formatted profile card for each cleaned student using f-strings:

for student in raw_students:
    print("=" * 32)

    #clean the name, convert roll to int, and convert marks_str to list of ints
    clean_name = student["name"].strip().title()
    roll = int(student["roll"])
    marks_list = [int(mark.strip()) for mark in student["marks_str"].split(",")]
    
    #left-align and reserve 8 spaces
    print(f"{'Student':<8}: {clean_name}")
    print(f"{'Roll No':<8}: {roll}")
    print(f"{'Marks':<8}: {marks_list}")
    
    print("=" * 32)

#After processing all students, print the name in ALL CAPS and lowercase for the student with roll number 103.
for student in raw_students:
    if int(student["roll"]) == 103:
        clean_name = student["name"].strip().title()
        print(f"Name in ALL CAPS: {clean_name.upper()}")
        print(f"Name in lowercase: {clean_name.lower()}")

##Task 2 — Marks Analysis Using Loops & Conditionals

#Using a for loop, print each subject alongside its marks and a grade label based on this scheme:

student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

for subject, mark in zip(subjects, marks):
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"
    print(f"{subject}: {mark} - Grade: {grade}")

#Calculate and print
#Total marks
total_marks = sum(marks)
print(f"Total Marks: {total_marks}")
#Average marks
average_marks = total_marks / len(marks)
print(f"Average Marks: {average_marks:.2f}")
#Highest and lowest marks
max_mark = marks.index(max(marks))
min_mark = marks.index(min(marks))
print(f"Highest: {subjects[max_mark]} - {max(marks)}")
print(f"Lowest: {subjects[min_mark]} - {min(marks)}")

#Using a while loop, simulate a marks-entry system that allows adding new subjects
new_subject_count = 0

while True:
    new_subject = input("Enter a new subject (or 'done' to finish): ").strip()
    
    if new_subject.lower() == "done":
        break

    if not new_subject:
        print("Warning: Subject name cannot be empty. Please enter a valid subject.")
        continue
    
    # Use try and except to handle non-numeric input for marks
    try:    
        new_mark = int(input(f"Enter marks for {new_subject}: "))
        
        #Validate that marks are between 0 and 100 before adding
        
        if new_mark >= 0 and new_mark <= 100:
            subjects.append(new_subject.title())       #assuming subjects is a list defined earlier
            marks.append(new_mark)             #assuming marks is a list defined earlier
            new_subject_count += 1
            print(f"Added {new_subject} with marks {new_mark}.")
        else:
            print("Warning: Marks must be between 0 and 100. Entry not added.")

    except ValueError:
        print("Warning: Invalid input. Please enter a valid integer for marks between 0 and 100.")

#After exiting the loop, print the total number of new subjects added.
print("----- Summary -----")
print(f"New subjects added: {new_subject_count}")

#updated average marks after adding new subjects
if len(marks) > 0:
    total_marks = sum(marks)
    #calculate updated average marks
    updated_average_marks = total_marks / len(marks)
    
    print(f"Total subjects now: {len(subjects)}")
    print(f"Updated Average Marks: {round(updated_average_marks, 2)}")

else:
    print("No marks available to calculate average.")

##Task 3 — Class Performance Summary 
class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]
#Loop through class_data and for each student:
for name, student_marks in class_data:
    total = sum(student_marks)
    average = total / len(student_marks)  #Compute their average (rounded to 2 decimal places).
    print(f"{name}: Total Marks = {total}, Average Marks = {average:.2f}")
    if average >= 60:             #Assign a result status: Pass if average ≥ 60, else Fail.
        print(f"{name}: Status: Pass")
    else:        
        print(f"{name}: Status: Fail")

#Print a formatted class report:
print("----- Class Performance Summary -----")
print(f"{'Name':<20} | {'Average':<10} | {'Status'}")
print("-" * 45)
for name, marks in class_data:
    average = sum(marks) / len(marks)
    if average >= 60:
        status = "Pass"
    else:
        status = "Fail"
    print(f"{name:<20} | {average:<10.2f} | {status}")

#After the table, print:
#Number of students who passed and who failed
pass_count = 0
fail_count = 0
for name, marks in class_data:
    average = sum(marks) / len(marks)
    if average >= 60:
        pass_count += 1
    else:
        fail_count += 1

print(f"Number of students who passed: {pass_count}")
print(f"Number of students who failed: {fail_count}")

#Class topper (name + average)
topper_name = ""
topper_average = 0          
for name, marks in class_data:
    average = sum(marks) / len(marks)
    if average > topper_average:
        topper_average = average
        topper_name = name

print(f"Class topper: {topper_name} with average marks: {topper_average:.2f}")

#Class average (average of all five students' averages)
total_average = 0
for name, marks in class_data:
    average = sum(marks) / len(marks)
    total_average += average        
class_average = total_average / len(class_data)
print(f"Class average: {class_average:.2f}")    

##Task 4 — String Manipulation Utility 
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

#Clean the essay by:

#Stripping leading and trailing whitespace  
clean_essay = essay.strip()
print(f"Cleaned Essay: '{clean_essay}'")

#Convert clean_essay to Title Case and print it
title_case_essay = clean_essay.title()
print(f"Title Case Essay: '{title_case_essay}'")

#Count how many times the word "python" appears in clean_essay (case-insensitive)
python_count = clean_essay.lower().count("python")
print(f"Occurrences of 'python': {python_count}")

#Replace every occurrence of "python" in clean_essay with "Python 🐍" 
revised_essay = clean_essay.replace("python", "Python 🐍")
print(f"Revised Essay: '{revised_essay}'")

#Split clean_essay into individual sentences by splitting on ". " 
sentences = clean_essay.split(". ")     
print(f"Sentences: {sentences}")

#Print each sentence on a new line, numbered starting from 1. Add a "." at the end of each sentence if it does not already end with one.
for i, sentence in enumerate(sentences, start=1):
    if not sentence.endswith("."):
        sentence += "."
    print(f"{i}. {sentence}")
