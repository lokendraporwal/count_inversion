def getInvCount(li):
    count = 0
    for i in range(len(li)):
        for j in range(i + 1, len(li)): 
            if (li[i] > li[j]): 
                count += 1
    return count  
f=open("test.txt","r")
li=[]
li=list(f)
print("Number of inversions are", getInvCount(li)) 