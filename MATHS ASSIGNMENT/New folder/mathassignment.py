n=int(input("Enter number of rows:"))
m=int(input("Enter number of columns:"))
f=open("mathinput.py")
l1=[]
for j in range(n):
    l=[]
    s=f.readline().split()
    s=[int(i) for i in s]
    l1.append(s)

f.close()



def div(x):                                 #division func to be used after echelon form is formed
    while True:
        for i in range(len(x)):
            if x[i]!=0:
                a=x[i]
                break
        for j in range(len(x)):
            x[j]=x[j]/a
        break
    return x

def swap(x,y):                              #coefficient from which row is gonna be divided
    if x==y:
        return 1
    else:
        for i in range(len(x)):
            if x[i]==y[i]:
                continue
            elif x[i]==0 or y[i]==0:
                continue
            elif abs(x[i])>abs(y[i]):
                b=x[i]/y[i]
                return b,i
            elif abs(x[i])<abs(y[i]):
                b=y[i]/x[i]
                return b,i
            break

def diff(x,y):                              #for taking difference between two rows
    if x==y:
        return [0]*len(x)
    else:
        for i in range(len(x)):
            if x[i]==y[i] and x[i]!=0:
                return [y[j]-x[j] for j in range(len(x))]
            elif x[i]==y[i] and x[i]==0:
                continue
            elif abs(x[i])<abs(y[i]):
                c=swap(x,y)[0]
                d=swap(x,y)[1]
                f=[y[j]-c*x[j] for j in range(len(x))]
                return f 
            elif abs(x[i])>abs(y[i]):
                c=swap(x,y)[0]
                d=swap(x,y)[1]
                f=[x[j]-c*y[j] for j in range(len(x))]
                return f
            else:
                return [x[j]+y[j] for j in range(len(x))]
            break

def sort(x,y):                              #for arranging the rows in decending order
    for i in range(len(x)):
        if x[i]==y[i]:
            break
        elif abs(x[i])>abs(y[i]):
            break
        elif abs(x[i])<abs(y[i]):
            if l1.index(x)<l1.index(y):    
                a=l1.index(x)
                b=l1.index(y)
                l1[a]=y
                l1[b]=x
                break
            else:
                continue
for i in range(n):
    for j in range(n):
        sort(l1[i],l1[j])

for i in range(n):
    for j in range(i+1,n):
        while True:
            for k in range(m):
                if l1[i][k]!=0:
                    a=k
                    break
            if l1[j][a]==0:
                break
            else:
               l1[j]=diff(l1[i],l1[j])
               break
            
            break

def zero(x):                                            #for printing zero's at rows above pivot rows
    for i in range(n-1):
        for j in range(i+1,n):
            for k in range(m):
                if l1[j][k]!=0:
                    if l1[j-1][k]==0:
                        break
                    else:
                        b=l1[i][k]/l1[j][k]
                        for o in range(m):
                            l1[i][o]=l1[i][o]-b*l1[j][o]
                            
                    break
zero(l1)

def rref(x):                                            #for making 1 to pivot position
    for i in range(n):
        for j in range(m):
            if l1[i][j]!=0:
                a=l1[i][j]
                for k in range(m):
                    l1[i][k]=l1[i][k]/a
                break
            else:
                continue

rref(l1)
for i in range(n-1):
    for j in range(m):
        if l1[i][j]>l1[i+1][j]:
            break
        else:
            a=i
            b=i+1
            c=l1[i]
            d=l1[i+1]
            l1[b]=c
            l1[a]=d
            
for i in range(n-1):
    for k in range(i+1,n):
        for j in range(m):
        
            if l1[i][j]==l1[k][j]:
                continue
            elif l1[i][j]>l1[k][j]:
                break
            else:
                a=i
                b=k
                c=l1[i]
                d=l1[k]
                l1[b]=c
                l1[a]=d
                break
print("RREF:")
print(l1)
l2=[]                                       #list of free variables
for i in range(n):
    for j in range(m):
        if l1[i][j]!=0:
            for k in range(j+1,m):
                if l1[i][k]!=0:
                    l2.append(k+1)
l2=list(set(l2))
l3=[]                                       #list of pivot columns
for i in range(1,m+1):
    if i not in l2:
        l3.append(i)

l=[]

for i in l2:
    L=[]
    j=0
    lo=[l1[k][i-1] for k in range(n)]

    p=0
    while j<m:
        if j+1==i:
            L.append(1)
            j+=1
        elif j+1 not in l2:
            L.append((-1)*lo[p])
            j+=1
            p=p+1
        
        else:
            L.append(0)
            j+=1

    l.append(L)

if l==[]:                                           #list of parameteric vectors
    l=[0]*m

if l2==[]:
    print("Parametric Form:")
    print([0]*m)
else:
    l4=[]                                               #list of parameter
    for i in range(len(l)):
        l4.append(f'x{l2[i]}{l[i]}+')

    s=""                                                #parametric form
    for i in l4:
        s=s+str(i)

    print("Parametric Form:")
    print(s[:-1])