f = open('test', 'r')

casenum=0;
counter=0;
wina=0
winb=0;
left=0;
i=0;
j=0;
returnSTR=""
list=[];
for line in f:	
	if(counter==0):
		casenum=int(line)
	
	if(counter!=0):
	    if(line[0]!='\n'):
	        linedummy=line.rstrip()
	        list.append(linedummy)
	counter=counter+1;
	
for i in range(0,casenum):
    returnSTR=returnSTR+'Case #'+str(i+1)+':';
    a=list[j]
    if(a=='OOOO'):
        wina=1;
    elif(a=='XXXX'):
        winb=1;
    else:
        wina=0;
        wib=0;
    j=j+1
    b=list[j]
    if(b=='OOOO'):
        wina=1;
    elif(b=='XXXX'):
        winb=1;
    else:
        wina=0;
        wib=0;
    j=j+1
    c=list[j]
    if(c=='OOOO'):
        wina=1;
    elif(c=='XXXX'):
        winb=1;
    else:
        wina=0;
        wib=0;
    j=j+1
    d=list[j]
    if(d=='OOOO'):
        wina=1;
    elif(d=='XXXX'):
        winb=1;
    else:
        wina=0;
        wib=0;
    j=j+1
    for k in range(0,3):
        if(a[k]=='O' and b[k]=='O' and c[k]=='O' and d[k]=='O'):
            wina=1;
        elif(a[k]=='X' and b[k]=='X' and c[k]=='X' and d[k]=='X'):
            winb=1;          
        else: 
            wina=0;
            wib=0;
    if((a[0]=='O' and b[1]=='O' and c[2]=='O' and d[3]=='O') or (a[3]=='O' and b[2]=='O' and c[1]=='O' and d[0]=='O')):
        wina=1;
    elif((a[0]=='X' and b[1]=='X' and c[2]=='X' and d[3]=='O') or (a[3]=='X' and b[2]=='X' and c[1]=='X' and d[0]=='X')):
        wina=1; 
    else: 
        wina=0;
        wib=0;
    if(('.' in a) or ('.' in b) or ('.' in c) or ('.' in d)):
        left=1;
    else: 
        left=0;
        
    if(wina==1):
        returnSTR=returnSTR+" O won\n";
    elif(winb==1):
        returnSTR=returnSTR+" X won\n";
    elif(left==1):
        returnSTR=returnSTR+" Game has not completed\n";
    else:
        returnSTR=returnSTR+" Draw\n";
        
#print(returnSTR)
out = open('out', 'w')
out.write(returnSTR);
