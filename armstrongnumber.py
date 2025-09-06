#take input from the user
num=int(input("Enter a number: "))

#initialize sum
sum=0
#find the sum of the cube of each digit
temp=num
while temp>0:
    digit=temp%10 #Ex:153, digit gets 3 (since its remainder) 
    sum+=digit**3 #sum=sum+(digit**3); sum=0+(3 x 3 x 3) = 27
    temp//=10 #Next number in temp is calculated: 15; 5

#display the result
if num==sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is NOT an Armstrong number")