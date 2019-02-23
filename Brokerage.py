stockCount=int(input())
Rate=float(input())
result=transDetails=paid=0
for _ in range(stockCount):
    transDetails=input().strip().split()
    result+=int(transDetails[0])*float(transDetails[2])
paid=(result*Rate)/100   
print(round(paid,2))