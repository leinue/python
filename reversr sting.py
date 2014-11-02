def rev(str):
    if len(str)==1:
        return str
    else:
        newStr=rev(str[1:])+str[0]
        return newStr

print(rev('abcdefg'))

