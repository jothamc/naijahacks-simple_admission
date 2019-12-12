

# def awt(arr,arr1):
#   arr2 = []
#   cwt = 0
#   for i,j in zip(arr,arr1):
#     if i == 0:
#       arr2.append(j)
#     else:
#       cwt = arr2[-1] + j - 1
#       arr2.append(cwt)

#   # print(arr2)
#   # print( sum(arr2)/len(arr2) )



# arr1 = [0,1,2]
# arr2 = [3,9,6]

# awt(arr1,arr2)


# def mwt(arr,arr1):
#   s_arr = sorted(arr1)
  
from itertools import permutations,combinations
dice = range(1,10)
p_a = []
to = 0
for i,j in permutations(dice,2):
  if sum([i,j]) < 10:
    p_a.append([i,j])
  to = to + 1

print(len(p_a), to)