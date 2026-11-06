name=input("Enter your name: ")
sub1=int(input("Enter Math marks :"))
sub2=int(input("Enter English marks :"))
sub3=int(input("Enter phython marks :"))

if sub1 < 0 or sub1 >100 or sub2 < 0 or sub2 > 100 or sub3 < 0 or sub3 > 100 :
    print("Invalid Marks!")

else:
    average = (sub1+sub2+sub3)/3

if average >=80:
    grade = "A+"

elif average >=70:
    grade="A"

elif average >=60:
    grade="A-"

elif average >=50:
    grade="B"

elif average >=40:
    grade="C"

else:
    grade="F"


print("Student Name :",name)
print("Average marks :",average)
print("Grade is :",grade)