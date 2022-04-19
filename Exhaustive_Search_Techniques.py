'''BFS and DFS'''
from collections import defaultdict
class Graph:
    def __init__(self):
        self.g=defaultdict(list)
        
    def addEdge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)
        
    def bfs(self,start,goal):
        opened,closed=[start],[]
        while opened:
            p=opened.pop(0)
            closed.append(p)
            if p==goal:print('Goal node found');return closed
            for j in self.g[p]:
                if j not in opened and j not in closed:opened.append(j)
        print('Goal node not found');return closed
    
    def dfs(self,start,goal):
        opened,closed=[start],[]
        while opened:
            p=opened.pop(0)
            closed.append(p)
            if p==goal:print('Goal node found');return closed
            c=0
            for j in self.g[p]:
                if j not in opened and j not in closed:opened.insert(c,j);c+=1  
        print('Goal node not found');return closed
    
g=Graph()
n=int(input("Enter no.of Edges: "))
for _ in range(n):
    u,v=input("Enter u v :").split()
    g.addEdge(u,v)
start,goal=input('Start node: '),input('Goal node: ')
bfs_path=g.bfs(start,goal)
dfs_path=g.dfs(start,goal)
print(bfs_path)
print(dfs_path)

#sample Input output
'''Enter no.of Edges: 6
Enter u v :a b
Enter u v :a c
Enter u v :b d
Enter u v :b e
Enter u v :b f
Enter u v :c i
Start node: a
Goal node: e
Goal node found
Goal node found
['a', 'b', 'c', 'd', 'e']
['a', 'b', 'd', 'e']
'''


'''DFID'''
from collections import defaultdict
class Graph:
    def __init__(self):
        self.g=defaultdict(list)
    def addEdge(self,u,v):
        self.g[u].append([v,0])
        self.g[v].append([u,0])
    def dfs(self, start, goal, i):
        opened,closed=[],[]
        opened.append([start,0])
        while opened:
            u,v=opened.pop()
            closed.append(u)
            if u==goal:print(u,' ',opened,' ', closed);return 1
            if v<i :
                for j in self.g[u]:
                    j[1]=v+1
                    if j[0] not in closed:opened.append(j)
            print(u,' ',opened,' ', closed)
        return 0
    def dfid(self, start, goal):
        i=x=0
        while x!=1:
            print('DFID with depth = ',i)
            x=self.dfs(start, goal, i)
            i+=1
        print('Goal found')
g=Graph()
n=int(input('No.of edges : '))
for _ in range(n):                              # Enter  Space seperated edge nodes
    u,v=input('Enter Edge nodes : ').split()
    g.addEdge(u,v)
start,goal=input('Enter start and goal nodes : ').split()
g.dfid(start,goal)

#sample I/O
'''
No.of edges : 6
Enter Edge nodes : a b
Enter Edge nodes : a c
Enter Edge nodes : b d
Enter Edge nodes : b e
Enter Edge nodes : b f
Enter Edge nodes : c i
Enter start and goal nodes : a e
DFID with depth =  0
a   []   ['a']
DFID with depth =  1
a   [['b', 1], ['c', 1]]   ['a']
c   [['b', 1]]   ['a', 'c']
b   []   ['a', 'c', 'b']
DFID with depth =  2
a   [['b', 1], ['c', 1]]   ['a']
c   [['b', 1], ['i', 2]]   ['a', 'c']
i   [['b', 1]]   ['a', 'c', 'i']
b   [['d', 2], ['e', 2], ['f', 2]]   ['a', 'c', 'i', 'b']
f   [['d', 2], ['e', 2]]   ['a', 'c', 'i', 'b', 'f']
e   [['d', 2]]   ['a', 'c', 'i', 'b', 'f', 'e']
Goal found'''


#bi-directional

from collections import defaultdict

class Graph:
  def __init__(self):
    self.g = defaultdict(list)
    self.c1,self.c2 = [],[]

  def addedge(self,u,v):
    self.g[u].append(v)
    self.g[v].append(u)

  def bidirectional(self,start,goal):
    o1,o2 = [],[]
    o1.append(start)
    o2.append(goal)
    while o1 and o2:
      t1 = o1.pop(0)
      self.c1.append(t1)
      t2 = o2.pop(0)
      self.c2.append(t2)
      for i in self.g[t1]:
        if i not in self.c1:
          o1.append(i)
      for i in self.g[t2]:
        if i not in self.c2:
          o2.append(i)
      for i in o1:
        if i in o2:print(o1, " ", self.c1, " ", o2, " ", self.c2); print('Goal Found'); return
      print(o1, " ", self.c1, " ", o2, " ", self.c2)
    print("Not found")

g = Graph()
n = int(input("No.of edges...."))
for i in range(n):
  u,v = input().split()
  g.addedge(u,v)
start, goal = input().split()
g.bidirectional(start,goal)

#SAMPLE INPUT & OUTPUT

'''
No.of edges....9
a b
a c
a d
b e
b f
c g
c h
d i
d j
a z
['b', 'c', 'd']   ['a']   []   ['z']
Not found
'''
