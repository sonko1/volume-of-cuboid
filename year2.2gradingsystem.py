#
sub1=int(input("Enter marks of data communication: "))
sub2=int(input("Enter marks of computer system project: "))
sub3=int(input("Enter marks of multimedia: "))
sub4=int(input("Enter marks of database management2: "))
sub5=int(input("Enter marks of Object oriented programming2: "))
sub6=int(input("Enter marks of Object Oriented design and analysis: "))
sub7=int(input("Enter marks of data professional ethics: "))
avg=(sub1+sub2+sub3+sub4+sub5+sub6+sub7)/7
if(avg>=75):
    print("Grade: A")
elif(avg>=65&avg<74):
    print("Grade: B")
elif(avg>=50&avg<64):
    print("Grade: C")
elif(avg>=40&avg<49):
    print("Grade: D")
else:
    print("Grade: F")
