pass_threshold = 80

students = [{"name" : "Nhico", "year" : 12, "credits" : 119 , "endorsement" : "E"}, 
            {"name" : "Arya", "year" : 12, "credits" : 99 , "endorsement" : "M"}, 
            {"name" : "Kian", "year" : 12, "credits" : 67 , "endorsement" : "NA"}]

def get_int(): #for whenever we want an input thats an integer
    while True:
        try:
            num = int(input("Enter Here: "))
            return num
        except ValueError:
            print("Invalid intput, Try Again.")


def menu(): #menu so it can be called whenever
    print(f"\n{'--- NCEA STUDENT MANAGEMENT SYSTEM ---':^40}")
    print("1. Show summary of all student data")
    print("2. Show students who have passed NCEA")
    print("3. Show students eligible for endorsement")
    print("4. Show summary for a specific year level")
    print("5. Add credits to an existing student")
    print("6. Add a new student and their credit data")
    print("7. Exit program")

def show_data(): #shows all student data
    for student in students:
        print(f"\n{student['name']} is year {student['year']} with {student['credits']} credits at a {student['endorsement']} endorsement.")

def show_pass(): #shows whether students have passed ncea or not
    for student in students: # if the students credits are above the pass threshold it tells them they have passed
        if student['credits'] < pass_threshold:
            print(f"\nStudent {student['name']} did not pass the year")
        elif student['credits'] >= pass_threshold:
            print(f"\nStudent {student['name']} has passed the year")

def endorse_egb(): #checks student and what endorsement they have
    count = 1 #added this count as index starts from zero
    for student in students:
        print(count, student['name'])
        count += 1
    print("\nWhich student do you want to check?")
    student_view = get_int()
    student_view -= 1
    print(f"\nStudent {students[student_view]['name']} has a {students[student_view]['endorsement']} endorsement")



def yr_summary():

    print("which student year would you like to look at? (11-13)")
    target_year = get_int()
    
    for student in students:
        if student['year'] == target_year: # if the key matches the inputted student year then all the students wiht the same key will have their data printed.
            print(f"Name:{student['name']}, Credits: {student['credits']}, Endorsement: {student['endorsement']} ")

        else:
            print("invalid try again")


def add_credits():   
    count = 1
    for student in students:
        print(count, student['name'])
        count += 1
    print("\nWhich student do you want to add credits to?")
    student_choice = get_int()
    student_choice -=1
    print(f"\nStudent{students[student_choice]['name']} has {students[student_choice]['credits']}")
    print("How many credits do you want to add?")
    added_credits = get_int()
    students[student_choice]['credits'] += added_credits # adds credits
    print(f"\nStudent {students[student_choice]['name']} has {students[student_choice]['credits']}")
    if students[student_choice]['credits'] >= pass_threshold and students[student_choice]['endorsement'] == "NA":
        students[student_choice]['endorsement'] = "A" #changes endorsement if student has not passed



def add_student(target_list): #adds student dictionary to the list.
    print("\n-----Enter Student Details-----")
    target_list.append({
        "name": input("Name: ").capitalize(),
        "year": int(input("Year: ")),
        "credits": int(input("Credits: ")),
        "endorsement": input("Endorsement: ").upper()
    })


    print("Student list updated")
    print(students)






while True: #main code

    print(menu())
    print("Choice (1-7) ")
    option = get_int()
        
    if option == 1:
        show_data()

    elif option == 2:
        show_pass()

    elif option == 3:
        endorse_egb()

    elif option == 4:
        yr_summary()

    elif option == 5:
        add_credits()

    
    elif option == 6:
        add_student(students)

    elif option == 7:
        break

    else:
        print("please enter a proper choice")




#hello