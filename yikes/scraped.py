
with open ("mydefaults.ini") as countme:
    counting = countme.read()
    
    c=0
    letters = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'

    

    numbers = (1,2,3,4,5,6,7,8,9,0)


for i in counting:
    list = counting.lower()
    if (letters in list):
        c+=1
if (c==0):
    print("Impossible")
else:
    print("The amount of letters a-z A-Z is,",c)


