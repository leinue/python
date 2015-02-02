def getDict(**keyv):
    return keyv

def copyDict(dict):
    D={}
    for key in dict:
        D[key]=dict[key]
    return D

#def copyDict2(dict):
#    return dict[:]

oldDict=getDict(a=1,b=2)

newDict=copyDict(oldDict)
print(newDict)

#newDict2=copyDict2(oldDict)
#print(newDict2)

def addDict(dict1,dict2):
    new={}
    for key in dict1.keys():
        new[key]=dict1[key]
    for key in dict2.keys():
        new[key]=dict2[key]
    return new

dict1=getDict(fuck='shit',bitch='penis')
dict2=getDict(hh=233,hhh=23333)
intersect=addDict(dict1,dict2)
print(intersect)
