# How much i can hit the wall ?

# Desciption

two walls facing each other of ****D**** distance. a ball X stuck to *wall number1*. the ball starts moving with a changeable speed ****V**** all the distance ****D****.
****V**** decrease 1 per 1 meter ``(supposing D is measurable in meter and V in meter/second)`` and decrease 2.5 when it hits one of the walls.

# Exercise

make an algorithme that returns ****x****>=0, the number of times the ball hits a wall, and ****k****>=0 the distance between the ball X at V = 0 and the *wall number 1*.

# inputs

**d** : float>0 (distance between the walls)

**v** : float>=0 (the initial speed of the ball X)

# outputs

**x** : float (number of hits with the wall)

**k** : float (distance between the wall 1 and the ball at speed  = 0)

# example:

d = 3

v = 15

output : x = 3 and k = 3

# explanation  
 the ball starts with speed of 15 , when it hits the wall first time it loses 2.5 m/s along with  m/s of the distance traveled, which is the total of 5.5 m/s.
 For the second loop it will loos another 5.5 which is in total 11 at wall number 1. finally it will hit the wall for the third time and the speed will be 0 at wall number 2.
 
 So the output will be : x = 3 and k = 3
