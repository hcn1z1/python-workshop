n = float(input("enter the speed of the ball: "))
m = float(input("enter the distance between two walls: "))

speed_decreased_by_impact = m + 2.5
x = 0
k = 0
while n>=0:
    #checking
    if m<= n:
        x = x+1
        n = n - speed_decreased_by_impact
    else:
        break
if n<0: n = 0
else: pass
if x % 2 == 1:
    k = m - n
else:
    k = n
print(f"k = {k} and x = {x}")
