# store classes you have taken.
def store_taken_classes() :
    answer = input("수업을 입력하겠습니까? (Y / N) ")

    while (answer == 'Y') | (answer == 'y') :
        course = input(" Enter class (Ex. COSC XXXX) : ")
        if course in taken_class :
            print("You already entered this course. ")
            answer = input(" Continue? (Y / N) ")
            continue
        if course in computer_science_class :
            taken_class.append(course)
            answer = input(" Continue? (Y / N) ")
        else :
            print("""
            Class information is wrong.
            Please check again.
            """)

# show classes you have taken.
def show_taken_classes() :
    print("------------------------------------------------------------")
    for i in taken_class :
        print(i, ":", computer_science_class.get(i))

# check
def show_true () :
    pass

computer_science_class = {
    "COSC 1336" : "Computer Science and Programming",
    "COSC 1437" : "Introduction to Programming",
    "COSC 2306" : "Data Programming",
    "COSC 2425" : "Computer Organization and Architecture",
    "COSC 2436" : "Programming and Data Sturctures",
    "COSC 3320" : "Algorithms and Data Structures",
    "COSC 3337" : "Data Science I",
    "COSC 3340" : "Introduction to Automata and Computability",
    "COSC 3360" : "Fundamentals of Operating Systems",
    "COSC 3380" : "Database Systems",
    "COSC 3396" : "Senior Research Project",
    "COSC 3399" : "Senior Honors Thesis",
    "COSC 4298" : "Independent Study",
    "COSC 4331" : "Real-Time Systems and Embedded Programmin",
    "COSC 4337" : "Data Science II",
    "COSC 4348" : "Introduction to Game Art and Animation",
    "COSC 4351" : "Fundamentals of Software Engineering",
    "COSC 4353" : "Software Design",
    "COSC 4354" : "Software Development Practices",
    "COSC 4359" : "Intermediate Interactive Game Development",
    "COSC 4364" : "Numerical Methods",
    "COSC 4368" : "Fundamentals of Artifical Intelligence",
    "COSC 4370" : "Interactive Computer Graphics",
    "COSC 4377" : "Introduction To Computer Networks",
    "COSC 4393" : "Digital Image Processing",
    "COSC 4396" : "Senior Research Project",
    "COSC 4397" : "Sel Top-Computer Science",
    "COSC 4399" : "Senior Honors Thesis"
    }

taken_class = []

store_taken_classes()
show_taken_classes()