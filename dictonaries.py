phone_book = {}
n = int(input())
for i in range(n):
    name , number = input().split()
    phone_book[name] = number
while True:
    find = input()
    if len(find)==0: 
        break
    result = phone_book.get(find, "not found")
    if result == "not found":
        print("Not found")
    else:
        print(find , result)
      