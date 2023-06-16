# stepik algorithm course

import string
import sys

input = open('1.txt', 'r') #расскомментировать решая задачу локально
# input = sys.stdin #//расскомментировать при сдаче задачи в системе
S = []
n = int(input.readline())
for i in range(1,n+1):
  x,y = map(int, input.readline().split())
  S.append([x,y])



def getKey(item):
    return item[1]
S.sort(key = getKey)