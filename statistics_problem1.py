# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
n = int(input())
lis_num = [int(x) for x in input().split()]

#mean
print(sum(lis_num)/len(lis_num))
#median
x = sorted(lis_num)

if type(len(lis_num)-1/2) =="int":
    print(x[len(lis_num)-1/2])
else:
    avg = (x[int((len(lis_num)-1)/2)]+x[int((len(lis_num)-1)/2)+1])/2
    print(avg)
    
#mode
count_dict = {}
for each in x :
    if each in count_dict:
        count_dict[each] +=1
    else:
        count_dict[each]=1
#nums = list(count_dict.keys())
#counts = list(count_dict.values())
#max_cnt = 1
#max_idx = 0
#for i,c in enumerate(counts):
#    if c > max_cnt:
#        max_cnt =c
#        max_idx = c
#print(nums[max_idx])
#sorted_x = sorted(count_dict.items(), key=lambda kv: kv[1],reversed=True)
#print(sorted_x[0][0])
print(statistics.mode(x))



