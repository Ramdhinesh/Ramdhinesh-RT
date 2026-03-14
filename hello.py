##Task 1 – Print Formatting
##Print the following output using sep and end.
print("Hello world",end =" ")
print ("welcome python")
print ("Laptop","Mouse","Keyboard",sep="/")
##Task 2 – Variables
name = "Ravi"
age = 22
city = "Chennai"
print(name,age,city,sep="-")
##ask 3 – Multiple Assignment
name = "Meena"
age = 20
student = True
print("student information -",name,age,student)
## Task 4 – Indexing
word = "Python"
print(word[0])
print(word[2])
print(word[5])
## Task 5 – Arithmetic Operators
##Calculate and print:
print(25 + 10)
print(50 - 20)
print(8 * 5)
print(100 / 10)
print(10 % 30)  
print(2 ** 4)
print(20 // 3)
##Task 6 – BODMAS Expression
##Find the result:
print(3 + 2 * 5 ** 2)
## Task 7 – Assignment Operator

num = 50
num += 25
print("final value is;",num)
num = 100
num /= 10
print("print the result:",num)
## Task 10 – Logical Operators
print(10 > 5 and 5 == 5)
print(5 > 10 or 10 == 10)
print(not(5 > 2))
##Task 11 – Membership Operator
numbers = [10,20,30,40,50]
print(20 in numbers)
print(60 in numbers)
print(30 not in numbers)
##Task 12 – Swap Variables
a = 10
b = 20
a,b=b,a
print(a,b)
##Task 13 – Bitwise XOR
a = 6
b = 3
print(a ^ b)

##Bitwise Operator Tasks (1–8)
 ##1.Create two variables a = 10 and b = 6.Print the result of a & b. 
a = 10 
b= 6
print(a & b)
## 2.Create two variables x = 12 and y = 5.Print the result of x | y.
x =12
y= 5
print(x | y)
## 3.Create a variable num = 8.Print the result of ~num.
num = 8
print(~num)
##4. Create two variables a = 15 and b = 9.Print the result of a ^ b.
a =15
b= 9
print (a^b)
## 5. Create a variable num = 7.Perform left shift by 2 and print the result.
num=7 
result = num<<2 
print("left shof result:",result)

## 6. Create a variable num = 20. Perform right shift by 1 and print the result.
num = 20
result = num >> 1
print("Right shift result:", result)
## 7. Take two numbers from user input and print AND result
a=int(input("enter a first nnumber :"))
b= int(input ("enter a second number:"))
print (a&b)
##8. Take two numbers from user input and print XOR result
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a ^ b) 

##9. Create a string "hi" and print it 4 times using replication
a = "hi"
print(a*4)
## 10. Create a string "python" and print it 3 times
s = "python"
print(s * 3)
##11. Create two strings "super" and "man" and combine them using + operator
a1 = "super"
b1="man"
print(a1+b1)
##12. Create three strings "hello", " " and "world" and print "hello world"
a="hello"
b=""
c="world"
print(a+b+c)
##13. Take a name from user input and print it 5 times
a = input("user name :")
print(a*5)
##14. Take two strings from user input and concatenate them
a= input("user first name :")
b= input("user second name :")
print(a+b)
##15. Take a name from user input and print its data type
a= input("user first name :")
print(type(a))
##16. Take age from user input and convert it into integer
age= int(input("user age :"))
print(type(age))
##17. Take two numbers from user input and print their sum
a= input("user first no :")
b= input("user second no :")
print(a+b)
##18. Take two marks from user input and print their average
a= float(input("users maths mark :"))
b= float(input("users tamil mark :"))
print(a+b/2)
## 19. Take two numbers from user input and print 3*a*2 + b - 2
a= int(input("user first no :"))
b= int(input("user second no :"))
print(3*a*2 + b - 2)
##20. Take a number from user input and print its data type before and after type casting
a= input("user first no :")
print(a,type(a))
a= int(input("user first no :"))
print(a,type(a))
##21. Take a number as string input and print the last digit
a= input("Enter number:")
print("last digit",a[-1])
##22. Take a number and print the unit digit using % operator
a= int(input("Enter number:"))
print("unit digit",a%10)
## 23. Take a number and remove the last digit using // operator
a= int(input("Enter number:"))
print("remove the last digit",a//10)
##24. Take a number and print the second last digit
a= int(input("Enter number:"))
print("Second last digit",(a//10)%10)
##25. Take a 5 digit number and print its last digit
a=98426
print(a%10)
##If Condition Tasks
##26. Check if 10 ≥ 55
if 10>=5:
    print("10 is greater than 5")
##27. Check if number is greater than 50
num = int(input("enter the number"))
if num>50:
    print("number is greater than 50")
else:
    print ("not greater than 50")    
##28. Check if age ≥ 18    
age = int(input("enter the number"))
if age >=18:
   print("your are eligible ")
else:
    print("you are not eligible")   
##29. Check if number is greater than 100
num = int(input("enter the number"))
if num > 100:
    print("Number is greater than 100")
else:
    print("Number is not greater than 100")  
## 30. Check if number ≥ 0    
num = int(input("Enter a number: "))

if num >= 0:
    print("Number is greater than or equal to 0")
else:
    print("Number is not greater than or equal to 0")    
##31. Check if number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
##32. Check pass or fail (pass ≥ 35)
marks = int(input("Enter marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")    
##Check positive or negative
num = int(input("Enter a number: "))

if num >= 0:
    print("Positive number")
else:
    print("Negative number")
##. Check if number is greater than 10
num = int(input("Enter a number: "))

if num > 10:
    print("Number is greater than 10")
else:
    print("Number is not greater than 10")
##35. Job eligibility program
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")
##36. College admission program
marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Admission Rejected")
else:
    print("Admission Rejected")
##37. Sports selection program             
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))
if age >= 16:
    if height >=150:
        if weight >=50:
            print("you are selected")
        else:
            print("your weight is not eligible")
    else:
        print("your height is not eligible") 
else:
    print("your age is not eligible")      

 ##38. Print day name (1–7)
day = int(input("Enter a number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")    
## 39. Print color
num = int(input("Enter a number (1-3): "))
match num:
    case 1:
        print("red")
    case 2:
        print("blue") 
    case 3:
        print("green")       

##40. Print fruit
num = int(input("Enter a number (1-4): "))

match num:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")        
