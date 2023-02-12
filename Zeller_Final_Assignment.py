#Mohammed Tahmid Chowdhury 


ANTALDAGAR = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) 
VECKODAG = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
monthAD = ("Januray", "February", "Mars", "April", "May", "June", "July", "August", "September", "October", "November", "December")

while True:
    year = int(input("Year: "))
    if year == year < 1583 or year > 9999:
        continue
    else:
        break
    
while True:
    month = int(input("Month: "))
    if month == month < 1 or month > 12:
        continue
    else:
        break
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
               leap_year = 1
        else:
            leap_year = 0
    else:
        leap_year = 1
else:
    leap_year = 0

if month in [1, 3, 5, 7, 8, 10, 12]:
    while True:
        day = int(input("Day; "))
        if day == day < 1 or day > 31:
                print(" out of range 1-31")
                continue
        else:
            break
if month in [4, 6, 9, 11]:
    while True:
        day = int(input("Day; "))
        if day == day < 1 or day > 30:
            print("out of range 1-30")
            continue
        else:
            break
if month in [2] and leap_year != 1:
    while True:
        day = int(input("Day: "))
        if day == day < 1 or day > 28:
            print("out of range 1-28")
            continue
        else:
            break
if month in [2] and leap_year == 1:
    while True:
        day = int(input("Day: "))
        if day == day < 1 or day > 29:
            print("Out of range 1-29")
            continue
        else:
            break                
         

if month == 1 or month == 2:
    month += 12
    year -= 1
J = year // 100
K = year % 100
m = month
q = day
Y = [year // 4] 
h = (q + 13 * (m + 1) // 5 + K + (K // 4) + (J // 4) + (5 * J)) % 7
    

print("Year: " + str(year))
print("Month: " + str(month))
print("Day: " + str(day))
print()
print("It is a " + VECKODAG[h])
    

    
    
        
