'''
    Quadric equalation solver.
    PS: not including any library.
'''

def calculatingDelta(a= 0,b= 0,c= 0){
    return b**2 - 4*a*c
}

def checkingExistingOfSolution(delta){
    if delta >= 0 : return True
    else : return False
}

def solution(a= 0,b= 0,c= 0){
    delta = calculatingDelta(a,b,c)
    solution = checkingExistingOfSolution(delta)
    if solution:
        x1 = (-b - delta**(0.5))/2*a
        x2 = (-b - delta**(0.5))/2*a
        return (x1,x2)
    else:
        return "No solution"
}
