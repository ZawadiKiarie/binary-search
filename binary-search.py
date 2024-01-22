import random
import time
#we prove that binary search is faster then naive search
#naive search: scan entire list and ask if its equal to the target, 
#if yes return index, if no return -1

def naive_search(l, target):
  for i in range(len(l)):
    if l[i] == target:
      return i
  return -1

#binary search uses divide and conquer
#we will leverage the fact that our list is sorted
def binary_search(l ,target, low=None, high=None):
  if low is None:
    low = 0
  if high is None:
    high = len(l)-1

  if high<low:
    return -1

  #example l = [1, 3, 5, 10, 12]-->should return index 3
  midpoint = (low+high) // 2#divide by 2 and round it down

  if l[midpoint] == target:
    return midpoint #is an index
  elif target < l[midpoint]:
    return binary_search(l, target, low, midpoint-1)# recurse so it performs divide and conquer on the left side of the list
  else:
    return binary_search(l, target,midpoint+1, high)# recurse so it performs divide and conquer on the right side of the list
  
if __name__=='__main__':
  # l = [1, 3, 5, 10, 12]
  # target = 10
  # print(naive_search(l, target))
  # print(binary_search(l, target))

  length = 1000
  sorted_list = set()
  while len(sorted_list) < length:
    sorted_list.add(random.randint(-3*length, 3*length))
  sorted_list = sorted(list(sorted_list))#saying, make the sorted_list into a list then sort it

  start = time.time()#gets the time right now
  for target in sorted_list:
    naive_search(sorted_list, target)#going through entire list and making everything the target. so we are running naive_search 10000 times
  end = time.time()
  print("Naive search time: ", (end-start)/length, "seconds")#we divide by length to get time per each iteration

  start = time.time()#gets the time right now
  for target in sorted_list:
    binary_search(sorted_list, target)#going through entire list and making everything the target. so we are running binary_search 10000 times
  end = time.time()
  print("Binary search time: ", (end-start)/length, "seconds")#we divide by length to get time per each iteration