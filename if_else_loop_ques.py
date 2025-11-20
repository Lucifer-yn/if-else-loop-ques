# Name : Yash Nagar
# Enrollment no.: 0157AL231230
# Batch: 5th
# Batch time: 10:30 AM to 12:10 PM


# CONDITIONAL STATEMENT

# if else questions

# Q1 negetive or positive
a=int(input("num is: "))
if a<0:
    print("num is negetive")
else:
    print("num is positive")

#Q2 even or odd number
a=int(input("num is: "))
if a%2==0:
    print("num is even")
else:
    print("num is odd") 

#Q3 check leap year
y = int(input("Enter a year: "))
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print(y, "is a leap year.")
else:
    print(y, "is not a leap year.")

#Q4 check greatest no. between 2 numbers
a=int(input("1st num is: ")) 
b=int(input("2nd num is: "))
c=int(input("3rd num is: "))
if a>b:
    print(a,"is greater")

else:
    print(b,"is greater")   

# Q5 check eligible for vote or not
a=int(input("age is: "))
if a>18:
    print("you are eligible for voting")
else:
    print("not elegible for voting")

# Q6 check vowel and consonant
a=input("char. is: ")
b="aeiou"
if a.lower() in b:
    print("char. is vowel")
else:
    print("char. is consonant")

# Q7 check no. is divisible by 5
a=int(input("num is: "))
if a%5==0:
    print("no. is divisible by 5")
else:
    print("no. is not divisinle by 5") 

# Q8 check the no. is single dig., 2 dig., or more
a=int(input("num is: "))
if a>=0 and a<=9:
    print("num is single digit")
elif a>= 10 and a<=90:
    print("num is 2 digit no.")
else:
    print("num has more than 2 digit")

# Q9 check the student is passing or not
a=int(input("num is: "))
if a<40:
    print("student is fail")
else:
    print("student is passed")

# Q10 multiple of both 3 and 7
a=int(input("num is: "))
if a % 3 == 0 and a %  7 == 0:
    print("num is even")
else:
    print("num is odd") 


# ladder if and nested if

# Q1 greatest among three
a=int(input("1st num is: ")) 
b=int(input("2nd num is: "))
c=int(input("3rd num is: "))
if a>b and a>c:
    print(a,"is greater")
elif b>a and b>c:
    print(b,"is greater") 
else:
    print(c,"is greater") 

    
# Q2 classify the person
a=int(input("enter the value: ")) 

if a<13:
    print(a,"is a child")
elif a>=13 and a<20:
    print(a,"is a teenager") 
elif a>=20 and a<60:
    print(a,"is a adult") 
else:
    print(a,"is a senior") 


# Q3 assign grade
a=int(input("enter the value: ")) 

if a>=90 and a <= 100:
    print("grade \'A\' ")
elif a>=75 and a<90:
    print("grade \'B\' ") 
elif a>=50 and a<75:
    print("grade \'C\' ")
elif a>=35 and a<50:
    print("grade \'D\' ")
else:
    print("grade \'F\' ")


# Q4 type of  triangle 
ab=int(input("1st side is: ")) 
bc=int(input("2nd side is: "))
ca=int(input("3rd side is: "))
if ab==bc and bc==ca and ca==ab:
    print("it's a equilateral triangle")
elif ab==ac or ab==bc or bc==ca:
    print("it's a isosceles triangle") 
else:
    print("it's a scalene triangle")


# Q5 check type of character
char =input("enter the character value: ")
a="abcdefghijklmnopqrstuvwxyz" 
b="1234567890"
c=a.upper()
if char in a:
    print(char,"is lower")
elif char in c:
    print(char,"is upper") 
elif char in d:
    print(char,"is a digit") 
else:
    print(char,"is special symbol")

# Q6 electricity
a=int(input("enter the unit: ")) 

if a<=100:
    bill= a*5
    print("bill amt is Rs",bill)
elif a>100 and a<=200:
    res=a-100
    bill= (100*5) + (res*7)
    print("bill amt is Rs",bill) 
else:
    res= a-200
    bill = (100*5) + (100*7) + (res*10)
    print("bill amt is Rs",bill) 

    
# Q7 greates number using nested if
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = int(input("Enter 4th number: "))
if a > b:
    if a > c:
        if a > d:
            large = a
        else:
            large = d
    else:
        if c > d:
            large = c
        else:
            large = d
else:
    if b > c:
        if b > d:
            large = b
        else:
            large = d
    else:
        if c > d:
            large = c
        else:
            large = d
print("largest number:", large)


# Q8 check centuri and leap year
y = int(input("Enter a year: "))
if y % 100 ==0:
    print(y," is a century")
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print(y, "is a leap year.")
    else:
        print(y, "is not a leap year.")
else:
    print(y," is not a century")
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print("but ",y, "is a leap year.")
    else:
        print("also ",y, "is not a leap year.")

# Q9 check BMI status
bmi = float(input("Enter BMI value: "))
if bmi<18.5:
    print("BMI =", bmi, " Underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("BMI =", bmi, " Normal weight")
elif bmi>=25 and bmi<=29.9:
    print("BMI =", bmi, " Overweight")
else:
    print("BMI =", bmi, " Obese")

    
# Q10 smallest number 
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
if a < b:
    if a < c:
        small = a
    else:
        small = c
else:
    if b < c:
        small = b
    else:
        small = c
print("smallest number is: ",small)



# for loop questions
# # question 1: armstrong numbers b/w 100 and 999 
for i in range (100,999):
    j = i
    ctr = 0
    while j > 0:
        temp = j%10
        ctr = ctr + temp**3
        j = j//10
    if ctr == i:
        print(i)


# question 2: display n prime numbers
n = int(input("Enter the number:"))
print(f"First {n} prime numbers are:")
for i in range(1, n):
    ctr = 0
    for j in range(1, i):
        if i%j == 0:
            ctr = ctr + 1
    if ctr<2:
        print(i)


# question 3: no divisible by 3 but sum of digits < 10

for i in range (1, 500):    
    if i%3 == 0:
        j = i
        ctr = 0
        while j > 0:
            temp = j % 10
            ctr = ctr + temp
            j = j//10
        if ctr < 10:
            print(i)


# question 4: triangle with n height

n = int(input("Enter the number:"))
for i in range(1,n+1):
    print(" "*(n-i),"*"*(2*i - 1))


# question 5: 
inp = input("Enter your Sentence: ")
Sen = inp.lower()
alpha = "abcdefghijklmnopqrstuvwxyz"
a = True	
for i in alpha:
	if i not in Sen:
		a = False
		print("The entered sentence is not a pangram")	
if a:
	print("The entered sentence is a pangram")


# question 6: printtwin prime numbers b/w 1 and 100

a = 1
print("Twin prime numbers b/w 1 and 100:")
for i in range(1,100):
    ctr = 0
    for j in range(1,i):
        if i%j == 0:
            ctr= ctr + 1
    if ctr<2:
        if i-a == 2:
            print(f"({a},{i})")
        a = i




# question 7: harshad number- no. divisible by sum of it's digits

num = int(input("Enter the number:"))
temp = num
for i in str(temp):
    dig_sum += int(i)

if num %sum == 0:
    print(f"{num} is a harshad number")
else: 
    print(f"{num} is  not a harshad number")
    

# question 8: Pascal's triangle upto n rows

def print_list(list):
    for x in list:
        print(x, " ", end="")
    print("")
        
n = int(input("Enter the number(>2): "))
a = [1]
b = [1,1]
print_list(a)
print_list(b)

for i in range(3,n+1):
    a = b.copy()
    b.clear()
    for j in range(1,i+1):
        if j == 1 or j == i:
            b.append(1)
        else:
            c = a[j-2] + a [j-1]
            b.append(c)
    print_list(b)



# question 9: 1^2 + 2^2 + 3^2 + ... + n^2

n = int(input("Enter the number: "))
sum =0
for i in range (1,n+1):
    sum = sum + i*i

print("the sum is: ", sum)


# question 10:

num = int(input("Enter the number: "))
temp = num
sum=0
for i in str(temp):
    dig = int(i)
    fact=1
    for j in range(1,dig+1):
        fact *= j
    sum += fact
    
if sum == num:
    print(f"{num} is a strong number")   
else:
    print(f"{num} is not a strong number")   


#while loop question

# Q11
num = int(input("enter the no.: "))
temp=num
rev=0
while temp>0:
    dig = temp%10
    rev = rev * 10 + dig
    temp //= 10

print(f"number is {num} and reverse {rev}")
 
i = 2
count = 0
while i <= rev:
    if rev % i == 0:
        count += 1
    i += 1

if count >= 2:
    print(f"{rev} is not a prime number")
else:
    print(f"{rev} is a prime number")



# Q12
total=0
while total<=100:
    num = int(input("enter the number"))
    temp = num
    dsum = 0
    while temp >0:
        dsum += temp % 10
        temp //= 10
    
    total += dsum

    print(f"sum of the digits is {dsum} of number {num}")
    print(f"total sum = {total}")

print("stop your sum is exceed more than 100! ")



# Q13
num = int(input("enter the no. : "))
temp=num
while temp >0:
    if temp % 10 == 0:
        print(f"{num} is a duck number")
        temp //= 10 
    else:
        temp //= 10



# Q14
num = int(input("enter a number. : "))
org = num
seen = []
while num != 1 and num not in seen:
    seen.append(num)
    temp = num
    dsum = 0
    while temp > 0:
        dig = temp % 10
        dsum += dig**2
        temp //= 10
    
    num = dsum

if num == 1:
    print(f"{org} is a happy number")
else:
    print(f"{org} is not a happy number")


# Q15
num = int(input("enter the number: "))
temp=num
large = 1
i = 2
while i <= num:

    if temp % i == 0:
        large = i
        temp //= 10
    else:
        i += 1

print(f"largest prime no. of {num} is {large}")


# Q 16
pali = False
while pali == False:
    inp = input("enter the string: ")
    rev = inp[::-1]
    if rev == inp:
        print(f"stopped! because {inp} is a palindrome")
        pali = True
    else:
        
        print(f"{inp} is not a palindrome")
        pali= False


# Q 17
num = int(input("enter the number: "))
while num>9:
    temp = num
    sum=0
    while temp>0:
        dig = temp % 10
        sum += dig
        temp //= 10
    num = sum
print(f"sum number is {num}")


# Q 18

num = int(input("enter the no.: "))
temp=num

while temp != 1:
    print(temp,end=" -> ")
    if temp % 2 == 0 :
        temp //= 2
    else:
        temp = 3*temp + 1
print(1)


# Q 19
num = int(input("enter the no.: "))
temp = num
sq= temp**2
dig=0
while temp>0:
    dig += 1
    temp //= 10

pr1=sq%(10**dig)
pr2=sq//(10**dig) 

if pr1+pr2 == num:
    print(f"{num} is a kaprekar number")
else:
    print(f"{num} is not a kaprekar number")


    
# Q20. ATM machine

print("Welcome to ATM")
print("Insert your card")
pin = 1234
tries = 3
while tries > 0:
    entered_pin = int(input("Enter your PIN: "))
    if entered_pin == pin:
        print("PIN accepted")
        balance = 10000
        while True:
            print("Please select an option:")
            print("1. Withdraw Money")
            print("2. Check Balance")
            print("3. Deposit Money")
            print("4. Exit")
            option = int(input("Enter your option: "))
            if option == 1:
                amount = int(input("Enter amount to withdraw: "))
                if amount <= balance:
                    balance -= amount
                    print("Please collect your cash")
                    print("Thank you for using ATM")
                else:
                    print("Insufficient balance")
                    print("Thank you for using ATM")
            elif option == 2:
                print("Your balance is Rs", balance)
                print("Thank you for using ATM")
            elif option == 3:
                amount = int(input("Enter amount to deposit: "))
                balance += amount
                print("Thank you for your deposit")
                print("Your balance is Rs", balance)
                print("Thank you for using ATM")       
            elif option == 4:
                print("Thank you for using ATM")
                break
            else:
                print("Invalid option")
                print("Thank you for using ATM")
        break
    else:
        tries -= 1
        print("Incorrect PIN")
        print(f"You have {tries} tries left")
        if tries == 0:
            print("Card blocked")
        else:
            continue
