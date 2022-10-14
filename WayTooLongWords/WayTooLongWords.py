word_range= int(input())
while word_range<1 or word_range>100:
    word_range= int(input())

for i in range(word_range):
    word= input()
    while len(word)<1 or len(word)>100:
        word= input()
    if len(word)<=10:
        print(word)
    else:
        print(word[0]+str(len(word)-2)+word[-1])