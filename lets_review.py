number =input("enter the num")

for n in range(int(number)):
    word = input("enter word")
    even = str()
    odd = str()
    for l in range(len(word)):
        if l%2==0:
            even = even + word[l] 
        else: 
            odd = odd + word[l]
    print(even,odd)
