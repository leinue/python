'''
编写一个实现将整数型数组中的数据按元素值递增的顺序进行排序的程序
'''

def bubble(bubbleList):
    listLength=len(bubbleList)
    while listLength>0:
        for i in range(listLength-1):
            print(str(i)+"::"+str(bubbleList[i])+':'+str(bubbleList[i+1]))
            if bubbleList[i]>bubbleList[i+1]:
                bubbleList[i]=bubbleList[i]+bubbleList[i+1]
                bubbleList[i+1]=bubbleList[i]-bubbleList[i+1]
                bubbleList[i]=bubbleList[i]-bubbleList[i+1]
            print('******')
            print(str(i)+"::"+str(bubbleList[i])+':'+str(bubbleList[i+1]))
        print('------------')
        listLength-=1
    print(bubbleList)
    
bubbleList=[3,4,1,2,5,8,0]
bubble(bubbleList)

