def timesOccursIn(k,A):
    return timesOccursInAux(k,A,0,0)
    
    
def timesOccursInAux(k,A,i,found):
    if i == len(A)-1:
        if A[i] == k:
            found+=1
            return found
        return found
    if A[i] == k:
        found+=1
    return timesOccursInAux(k,A,i+1,found)
    
    
timesOccursIn(5,[10,20,5,2,5,3,4,5,5,5])
