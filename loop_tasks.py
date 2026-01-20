#for loop to print numbers
for i in range(1,101):
    print(i)

#while loop for countdown timer
count=10
while count>=0:
    print(count)
    count-=1

#use of break statement
for i in range(0,10):
    if i==5:
        break
    print(i)

#use of continue statement
for i in range(0,10):
    if i==6:
        continue
    print(i)    

#iterate over string characters
s="nitin"
for ch in s:
    print(ch)

#multiplication table
for i in range(1,11):
    print(f"2*{i}={2*i}")

#loop with steps
for i in range(0,10,3):
    print(i)

#if with for loop
for i in range(0,10):
    if i%2==0:
        print(i)

#Real-world example: Login attempts
print("8. Real-World Example: Login Attempts")
attempts = 3
while attempts > 0:
    print(f"Login attempt remaining: {attempts}")
    attempts -= 1
print("Account locked due to too many failed attempts.")
