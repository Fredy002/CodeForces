problems= int(input())
while problems<1 or problems>1000:
    problems= int(input())
    
ct=0
for i in range(problems):
    opinion = input()
    opinion= opinion.split(' ')
    c=0
    for i in range(len(opinion)):
        opinion[i]= int(opinion[i])
        if opinion[i]==1:
            c+=1
    if c>1:
        ct+=1
    else:
        ct=ct
print(ct)