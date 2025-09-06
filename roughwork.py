i=5
while i<=10: #checks number before added, 9<10 but it because it is incremented before printing, it becomes 11
    i=i+2
    print(i) 
    #if print is after, it increments first leading to larger number
    #i=5, (5+2=7); i=7, (7+2=9), i=9; 9+2=11 (the previous value less than 10 is only accounted for while i<=10) 

while i<20: #i=11 (bc of previouss number), (11<20); i=12, i=13, 
    print("blue")
    i=i+1 #increments before printing, ensuring it stays within limit

num=input("Enter a number: ") #100

digit=0
for i in num: #considers each digit 1, 0, 0
    digit=digit+1 #for each number, count 1; digit=0+1; digit=1+1
    #print(digit) 
    # prints:
    # 1
    # 2
    # 3 
print(digit) #prints final count
    
         
    