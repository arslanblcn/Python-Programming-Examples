midtermExam = int(input("Please input midterm exam:"))
finalExam = int(input("Please input final exam:"))
#We have got input from user

result = 0.4 * midtermExam + 0.6 * finalExam

#Calculating of midterm and final exams

print("Result : ",format(result))

#Screen output

if(result >= 85):
    print("You got AA")
elif(result >= 70 and result <=84):
    print("You got BB")
elif(result >= 60 and result <=69):
    print("You got CC")
else:
    print("You got DD")