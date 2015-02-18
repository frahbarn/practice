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

x=0;
o=0;
t=0;
min1=0
max1=0



for line in f:	
	if(counter==0):
		casenum=int(line)
	
	if(counter!=0):
	    if(line[0]!='\n'):
	        linedummy=line.rstrip()
	        list.append(linedummy)
	counter=counter+1;
	
for i in range(0,casenum):
    wina=0;
    winb=0;
    returnSTR=returnSTR+'Case #'+str(i+1)+':';
    min1=max1
    max1=max1+4

    
    for z in range (min1,max1):
       # if(wina==1 or winb==1): 
        #    break;
        o=0
        x=0
        t=0
        if('.' in list[z]):
            left=1;
        else: 
            left=0;

        for j in range (0,4):
            if(list[z][j]=='X' ):
                x=x+1;
            elif(list[z][j]=='O' ):
                o=o+1;           
            elif(list[z][j]=='T' ):
                t=t+1; 
        
        if((o+t)==4):
            wina=1
            
        elif((x+t)==4):
            print(x+t)
            winb=1
           
        #S="O="+str(o)+" X="+str(x)+" T="+str(t)+" A="+str(wina)+" B="+str(winb)+"\n"
        #print(S)
        
        
        
        
                   #diagnal  
        o=0
        x=0
        t=0
        for j in range (0,4):
            if(list[min1+j][j]=='X' ):
                x=x+1;
            elif(list[min1+j][j]=='O' ):
                o=o+1;           
            elif(list[min1+j][j]=='T' ):
                t=t+1; 
        if((o+t)==4):
            wina=1
            break;
        elif((x+t)==4):
            winb=1
            break;
                
         #diagnal
        o=0
        x=0
        t=0        
        for j in range (0,4):
            if(list[min1+j][3-j]=='X' ):
                x=x+1;
            elif(list[min1+j][3-j]=='O' ):
                o=o+1;           
            elif(list[min1+j][3-j]=='T' ):
                t=t+1; 
        if((o+t)==4):
            wina=1
            break;
        elif((x+t)==4):
            winb=1
            break;
        
        
        for j in range (0,4):
            x=0
            o=0
            t=0
            for k in range(0,4):
                if(list[min1+k][j]=='X' ):
                    x=x+1;
                elif(list[min1+k][j]=='O' ):
                    o=o+1;           
                elif(list[min1+k][j]=='T' ):
                    t=t+1; 
            if((o+t)==4):
                wina=1
                break;
            elif((x+t)==4):
                winb=1 
                break;

                
      
      
      
       

            
    if(wina==1):
        returnSTR=returnSTR+" O won\n";
    elif(winb==1):
        returnSTR=returnSTR+" X won\n";
    elif(left==1):
        returnSTR=returnSTR+" Game has not completed\n";
    else:
        returnSTR=returnSTR+" Draw\n";
        
print(returnSTR)
#out = open('out', 'w')
#out.write(returnSTR);      
