import os
import sys
sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(100000000)
def inp(): return int(input())
def strng(): return input().strip()

def jn(x, l): return x.join(map(str, l))
def strl(): return list(input().strip())


def mul(): return map(int, input().strip().split())
def mulf(): return map(float, input().strip().split())
def seq(): return list(map(int, input().strip().split()))


def ceil(x): return int(x) if (x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if (x % d == 0) else x//d+1


def CPP_function(cppfile , x):
    f = open('cinput.txt', 'w')
    f.write(f"{x}\n")
    f.close()
    os.system(f"{cppfile}")
    f = open('coutput.txt', 'r')
    s = f.read()
    f.close()
    return s

i = inp()
s = CPP_function("CPP_file" , 2*i)
print(s)


sys.stdin.close()


