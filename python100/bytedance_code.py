#coding=utf-8
import sys
def countZero(number):
    count = 0
    if (number == 0):
        count+=1
    else:
        while(number != 0):
            if(number%10 == 0):
                count += 1
            number = number // 10
        count = count -1
    return count

def find_greatest_sub_array(n,array):
    """
    sum_of_array记录当前子组和，当子组合<0,则重置为0，重新开始计和
    greatest_sum记录目前出现过最大的子组和
    """
    if not array:
        return

    sum_of_array = 0
    greatest_sum = array[0]
    ans = 0
    for number in array:
        ans += countZero(number)
        sum_of_array += number
        while(ans <= 3):
            if sum_of_array > greatest_sum:
                greatest_sum = sum_of_array
                ans = 0
            if sum_of_array < 0:
                sum_of_array = 0
    return greatest_sum
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    print(find_greatest_sub_array(n, values))



#coding=utf-8
import sys
import math
def count(new):
    n = len(new)
    ans = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if (new[i]>new[j]):
                ans+= math.floor(new[i]-new[j])
            else:
                ans+= math.floor(new[j]-new[i])

    return ans

if __name__ == "__main__":
    # 读取第一行的n,m
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    new = []
    for i in range(values[0]):
        # 读取每一行的一个数
        number = int(sys.stdin.readline().strip())
        new.append(number/values[1])
    ans =count(new)
    print(ans)