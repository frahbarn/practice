f = open('test', 'r')
content = f.readlines()

EN=0
SN=0
count=0
listE=[]
listS=[]
returnSTR=''

casenum=int(content[0]);

for i in range(1,casenum):
    listE=[]
    listS=[]
    returnSTR=returnSTR+'Case #'+str(i)+':';
    
    count=count+1
    
    EN=int(content[count])
    
    for j in range(1,EN+1):
        linedummy=content[count+j].rstrip()
        listE.append(linedummy)
        
    count=count+EN+1
    SN=int(content[count])
    for j in range(1,SN+1):
        linedummy=content[count+j].rstrip()
        listS.append(linedummy)
    
    count=count+SN
    
    for test in listS:
        print(i)
        print(test)
