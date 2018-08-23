'''
二分查找

def binarySearch(list,item):
    low = 0
    high = len(list)-1
    while low<= high: #小于等于很重要
        mid = (low+high)//2   #此处取整很重要
        if item == list[mid]:
            return mid
        elif item<list[mid]:
            high = mid-1
        else:
            low = mid+1
    return None
my_list = [1, 3, 5, 7, 9]
print(binarySearch(my_list, 3)) # => 1

# 'None' means nil in Python. We use to indicate that the item wasn't found.
print(binarySearch(my_list, -1)) # => None
'''

'''
选择排序
def findSmallest(arr):
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[smallest_index]>arr[i]:
            smallest_index=i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        newArr.append(arr.pop(findSmallest(arr)))
    return newArr

print(selectionSort([5,3,6,2,10])
'''
'''
#第三章的递归系列算法
def look_for_key(main_box):
    pile= main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("found the key!")
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key()
            print("found the key")

def count(i):
    print(i)
    if i <= 0:
        return
    else:
        count(i-1)
def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
print(fact(5))
count(5)


# 第四章 quicksort 排序系列
def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]
        less=[i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot] #此处用了循环
        return quicksort(less)+[pivot]+quicksort(greater)#此处需注意要把 pivot 变成 list 对象

def sum(arr):
    total = 0
    for x in arr:
        total+= x
    return total
def sum2(list):
    if list == []:
        return 0
    else:
        return list[0]+sum(list[1:])
def countlsit(list):
    if list == []:
        return 0
    else:
        return 1+countlsit(list[1:])

def max(list):
    if (len(list)== 0):
        return None
    if (len(list)==1):
        return list[0]
    else:
        submax= max(list[1:])
        return list[0] if list[0] > submax else submax
print(max([123,2,232,23,232,11,111]))
print(countlsit([1,23,23,2,23,4]))
print(sum2([1,2,3,4,5]))
print(sum([1,2,3,4]))
print (quicksort([10,5,2,3,4]))
def quicksort2(array):
    if len(array)< 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < =pivot]
        greater = [i for i in array[1:] if i >pivot]
        return quicksort2(less)+[pivot]+quicksort2(greater)'''

'''#第五章  哈希表
book = {'apple':0.067,'milk':1.49,'avocado':1.59}
print(book["apple"])
voted ={}
def check_voter(name):
    if voted.get(name):
        print('kick them out')
    else:
        voted[name]=True
        print('let them vote!')
check_voter('tom')
check_voter('mike')
check_voter('mike')
'''
'''
#第六章 广度优先搜索
from collections import deque
def person_is_seller(name):
    return name[-1] == 'm'
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    search_deque=deque()
    search_deque+=graph[name]
    searched=[]
    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person+' is a seller')
                return True
            else:
                search_deque+=graph[person]
                searched.append(person)
    return False

search('you')'''
