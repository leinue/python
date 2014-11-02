def isValid(strr,i=0,left=0,right=0):
    recursionCnt=len(strr)
    
    if i<=recursionCnt-1:
        currentStr=strr[i]
        print(currentStr)
        i+=1
        
        if currentStr=='(':
            left+=1
            print('left is '+str(left))
            
        if currentStr==')':
            right+=1
            print('right is '+str(right))

        isValid(strr,i,left,right)

    return left,right

print(isValid('fuck)'))
