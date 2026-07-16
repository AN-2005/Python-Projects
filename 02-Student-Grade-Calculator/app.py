print ("================Student Grade Calculator=================")
name = input("Enter Student Name:")
math = float(input("Enter Math marks:"))
science = float(input("Enter Science marks:"))
english = float(input("Enter English marks:"))

total = math + science + english
percentage = total/3

print("\n Students name:" ,name)
print("Total Marks:" ,total)
print("Percentage:", round(percentage, 2), "%")
if percentage >= 90:
    grade = "A+"

elif percentage >= 80:
    grade = "A"

elif percentage >= 70:
    grade = "B"

elif percentage >= 60:
    grade = "C"

elif percentage >= 40:
    grade = "D"

else:
    grade = "Fail"

print("Grade:", grade)

