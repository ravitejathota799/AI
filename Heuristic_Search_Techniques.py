#Best first search

from collections import defaultdict

class Graph:
  def __init__(self):
    self.g = defaultdict(list)
    self.h = {}

  def addh(self,v,value):
    self.h[v]=value

  def addedge(self,u,v):
    self.g[u].append(v)
    self.g[v].append(u)

  def pgraph(self):
    print(self.g)
    print(self.h)

  def bfs(self,start,goal):
    opened,closed = [],[]
    opened.append(start)
    while opened:
      t = opened.pop(0)
      closed.append(t)
      if t == goal: print("Goal found"); print(opened, " ", closed); return 1
      for i in self.g[t]:
        if i not in closed:
          opened.append(i)
      opened.sort(key = lambda x: self.h[x])
      print(opened, " ", closed)
    print("Not found")


if __name__=='__main__':

  g = Graph()
  n = int(input("no.of nodes???"))
  m = int(input("no.of edges???"))
  for i in range(m):
    u,v = input().split()
    g.addedge(u,v)
  for i in range(n):
    li = list(map(str,input().split()))
    g.addh(li[0],int(li[1]))

  #g.pgraph()
  g.bfs('a','e')

'''
no.of nodes???7
no.of edges???6
a b
a c
b d
b e
b f
c i
a 25
b 11
c 10
d 5
e 3
f 4
i 9
defaultdict(<class 'list'>, {'a': ['b', 'c'], 'b': ['a', 'd', 'e', 'f'], 'c': ['a', 'i'], 'd': ['b'], 'e': ['b'], 'f': ['b'], 'i': ['c']})
{'a': 25, 'b': 11, 'c': 10, 'd': 5, 'e': 3, 'f': 4, 'i': 9}
['c', 'b']   ['a']
['i', 'b']   ['a', 'c']
['b']   ['a', 'c', 'i']
['e', 'f', 'd']   ['a', 'c', 'i', 'b']
Goal found
['f', 'd']   ['a', 'c', 'i', 'b', 'e']
'''


''' Branch and bound '''
from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.n=n
        self.g={}
        self.graph=defaultdict(list)
    
    def addEdge(self,u,v,i):
        if u not in self.g: self.g[u]=0
        self.g[v]=i+self.g[u]
        self.graph[u].append((v,i+self.g[u]))
    
    def branch_bounds(self,start,goal):
        print('Branch and bound Search : ')
        print("open","close",sep='\t\t\t')
        opened,closed=[],[]
        opened.append((start,self.g[start]))
        print(opened, closed, sep='\t\t\t')
        while opened:
            p=opened.pop(0)
            closed.append(p)
            #Goal node
            if goal == p[0]:
                print(opened,closed,sep='\t\t\t')
                print('Goal node found');return
            #Successors Generation
            for v in self.graph[p[0]]:
                if v not in closed:opened.append(v)
            opened.sort(key=lambda x:x[1])
            print(opened,closed,sep='\t\t\t')
        print('Goal node not found')
    
n=int(input('Enter no.of nodes: '))
gr=Graph(n)
m=int(input('Enter no.of edges: '))
for _ in range(m):
  u,v,i=input('Enter edge nodes and heuristic :  ').split()
  gr.addEdge(u,v,int(i))
print(gr.g)
start,goal=input('Enter start and goal states: ').split()
gr.branch_bounds(start,goal)

# Sample input :-
'''
18
18
a b 5
a c 9
a d 12
b e 3
b f 5
c g 4
c h 5
d i 6
d j 7
e k 8
e l 6
f m 7
g m 7
g n 5
h o 6
i p 9
j q 3
j r 2
a m
'''

#Sample output :-
'''
Branch and bound Search : 
open                                                                    close
[('a', 0)]                                                              []
[('b', 5), ('c', 9), ('d', 12)]                                         [('a', 0)]
[('e', 8), ('c', 9), ('f', 10), ('d', 12)]                              [('a', 0), ('b', 5)]
[('c', 9), ('f', 10), ('d', 12), ('l', 14), ('k', 16)]                  [('a', 0), ('b', 5), ('e', 8)]
[('f', 10), ('d', 12), ('g', 13), ('l', 14), ('h', 14), ('k', 16)]      [('a', 0), ('b', 5), ('e', 8), ('c', 9)]
[('d', 12), ('g', 13), ('l', 14), ('h', 14), ('k', 16), ('m', 17)]      [('a', 0), ('b', 5), ('e', 8), ('c', 9), ('f', 10)]
[('g', 13), ('l', 14), ('h', 14), ('k', 16), ('m', 17), ('i', 18), ('j', 19)]    [('a', 0), ('b', 5), ('e', 8), ('c', 9), ('f', 10), ('d', 12)]
[('l', 14), ('h', 14), ('k', 16), ('m', 17), ('i', 18), ('n', 18), ('j', 19), ('m', 20)]    [('a', 0), ('b', 5), ('e', 8), ('c', 9), ('f', 10), ('d', 12), ('g', 13)]
[('h', 14), ('k', 16), ('m', 17), ('i', 18), ('n', 18), ('j', 19), ('m', 20)]     [('a', 0), ('b', 5), ('e', 8), ('c', 9), ('f', 10), ('d', 12), ('g', 13), ('l', 14)]
[('k', 16), ('m', 17), ('i', 18), ('n', 18), ('j', 19), ('m', 20), ('o', 20)]     [('a', 0), ('b', 5), ('e', 8), ('c', 9), ('f', 10), ('d', 12), ('g', 13), ('l', 14), ('h', 14)]
[('m', 17), ('i', 18), ('n', 18), ('j', 19), ('m', 20), ('o', 20)]      [('a', 0), ('b', 5), ('e', 8), ('c', 9), ('f', 10), ('d', 12), ('g', 13), ('l', 14), ('h', 14), ('k', 16)]
[('i', 18), ('n', 18), ('j', 19), ('m', 20), ('o', 20)]                 [('a', 0), ('b', 5), ('e', 8), ('c', 9), ('f', 10), ('d', 12), ('g', 13), ('l', 14), ('h', 14), ('k', 16), ('m', 17)]
Goal node found
'''
# Sample input-2 :-
'''
5
6
0 1 2
0 2 8
0 3 4
1 4 11
2 4 1
3 4 7
0 4
'''
# Sample output-2 : 
'''
Branch and bound Search : 
open                                    close
[('0', 0)]                              []
[('1', 2), ('3', 4), ('2', 8)]          [('0', 0)]
[('3', 4), ('2', 8), ('4', 13)]         [('0', 0), ('1', 2)]
[('2', 8), ('4', 11), ('4', 13)]        [('0', 0), ('1', 2), ('3', 4)]
[('4', 9), ('4', 11), ('4', 13)]        [('0', 0), ('1', 2), ('3', 4), ('2', 8)]
[('4', 11), ('4', 13)]                  [('0', 0), ('1', 2), ('3', 4), ('2', 8), ('4', 9)]
Goal node found
'''


#Hillclimbing

from collections import defaultdict

class Graph:
  def __init__(self):
    self.g = defaultdict(list)
    self.h = {}

  def addh(self,v,value):
    self.h[v]=value

  def addedge(self,u,v):
    self.g[u].append(v)
    self.g[v].append(u)

  def pgraph(self):
    print(self.g)
    print(self.h)

  def hill(self,start,goal):
    opened,closed = [],[]
    opened.append(start)
    while opened:
      t = opened.pop(0)
      closed.append(t)
      li = []
      opened.sort(key = lambda x: self.h[x])
      if t == goal: print("Goal found"); print(opened, " ", closed); return 1
      for i in self.g[t]:
        if i not in closed+opened:
          li.append(i)
      opened = li + opened
      print(opened, " ", closed)
    print("Not found")


if __name__=='__main__':

  g = Graph()
  n = int(input("no.of nodes???"))
  for i in range(n):
    li = list(map(str,input().split()))
    g.addh(li[0],int(li[1]))
  m = int(input("no.of edges???"))
  for i in range(m):
    u,v = input().split()
    g.addedge(u,v)

  #g.pgraph()
  u,v = input("Enter start and goal states: ").split()
  g.hill(u,v)
  
  #SAMPLE INPUT & OUTPUT
'''
no.of nodes???12
a 10
b 10
i 8
f 7
d 4
c 2
h 0
k 0
e 5
j 6
g 3
m 0
no.of edges???11
a b
a i
a f
b d
b c
c h
i k
f e
f g
e j
j m
a j
['b', 'i', 'f']   ['a']
['d', 'c', 'f', 'i']   ['a', 'b']
['c', 'f', 'i']   ['a', 'b', 'd']
['h', 'f', 'i']   ['a', 'b', 'd', 'c']
['f', 'i']   ['a', 'b', 'd', 'c', 'h']
['e', 'g', 'i']   ['a', 'b', 'd', 'c', 'h', 'f']
['j', 'g', 'i']   ['a', 'b', 'd', 'c', 'h', 'f', 'e']
Goal found
['g', 'i']   ['a', 'b', 'd', 'c', 'h', 'f', 'e', 'j']
'''


'''Beam Search'''
from collections import defaultdict
class Graph:
    def __init__(self, n, w, h):
        self.graph=defaultdict(list) 
        self.n=n
        self.w=w
        self.h=h

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def beams(self, start, goal):
        not_found=True
        if goal not in self.h:print('Goal node not found');return
        w_opened,opened,closed=[],[],[]
        if start==goal:print("Goal node found");not_found=False;return
        closed.append(start)
        print(opened,w_opened,closed)
        for i in self.graph[start]:
            opened.append(i)
        opened.sort(key=lambda x:self.h[x])
        w_opened=opened[:self.w]
        print(opened,w_opened,closed)
        while not_found:
            opened.clear()
            while w_opened:
                p=w_opened.pop(0)
                closed.append(p)
                if p==goal:print(opened,w_opened,closed);print('Goal node found');not_found=False;return
                for v in self.graph[p]:
                    if v not in closed:opened.append(v)
            opened.sort(key=lambda x:self.h[x])
            w_opened=opened[:self.w]  
            print(opened,w_opened,closed)
            if all(i in closed for i in w_opened):print('Goal node not found');return

n=int(input("Enter no.of nodes : "))
w=int(input("Enter w : "))
h={}
for _ in range(n):
    u,i=input('Enter node and it\'s heuristic : ').split()
    h[u]=int(i)
g=Graph(n,w,h)
m=int(input('Enter no.of Edges : '))
for _ in range(m):
    u,v=input('Enter edge nodes : ').split()
    g.addEdge(u,v)
start,goal=input('Enter start and goal nodes : ').split()
g.beams(start,goal)


#Sample input:
'''
18
2
a 20
b 10
c 13
d 9
e 7
f 11
g 8
h 9
i 4
j 12
k 9
l 5
m 7
n 10
o 12
p 14
q 3
r 9
17
a b
a c
a d
b e
b f
c g
d h
d i
d j
e k
e l
f m
g n
h o
i p
i q
j r
a q
'''
#Sample Output: 
'''
[] [] ['a']
['d', 'b', 'c'] ['d', 'b'] ['a']
['i', 'e', 'h', 'f', 'j'] ['i', 'e'] ['a', 'd', 'b']
['q', 'l', 'k', 'p'] ['q', 'l'] ['a', 'd', 'b', 'i', 'e']
[] ['l'] ['a', 'd', 'b', 'i', 'e', 'q']
Goal node found
'''
