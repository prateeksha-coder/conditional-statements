marks=int(input("Enter marks:"))
if (marks>35):
    print("Passed!")
    if(marks>=90):
        print("A+")
    elif (marks >=80):
        print("B+")
    else:
        print("C+")
else:
    print("Failed!")