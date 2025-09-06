#Input the value of terms
n=int(input("Enter the value of terms: "))

sum=0 #initialise
i=1 #initialise, not needed for for loop since it mentions in range (1,n+1)
while i<=n: #loop will run from 1 to n
    sum=sum+i #sum is overrided each time
    i=i+1

print("\nSum=", sum)