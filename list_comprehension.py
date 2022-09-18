squares = [x * x for x in (1, 2, 3, 4)]
print(squares)

print([[x , y , z] for x in range(6) for y in range(6) for z in range(5) if x+y+z <= 5 ])





if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
#print a list of coordinates by i,j,k
     
    print([[i , j , k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n])
