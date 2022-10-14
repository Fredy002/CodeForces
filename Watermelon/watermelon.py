watermelon_weight= int(input())

if watermelon_weight>=1 and watermelon_weight<=100:
    if watermelon_weight%2==0:
        if watermelon_weight==2:
            print("NO")
        else:
            print ('YES')
    else:
        print ('NO')
