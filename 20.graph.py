'''
graph is a non linear data structure

in this the data is stored in vertises/node's and they are connected through edges
similer as tree but tree dose'nt make a cycle 

here V is a vertix and E is edges

V={v0,v1,v2,v3,v4}

E={e0,e1,e2,e3,e4}

to represent the edge we use
when we use the square bracket it meant it is the unordered graph,,it means we can travel to both 
direction
e0=[v0,v1]
e1=[v1,v2]

and if we use the round bracket then it's directed graph it     
e0=(v0,v1)                              
e1=(v1,v2)   
in this it will only allow to travel to only in one direction from v0 to v1

graph genlarlized 
= a)A set 'V' of elements called nodes
  b)A set 'E' of edges such that each edge e in 'E' is identified with a unique (unordered)
    pair [u,v] of node in V, denoted by e=[u,v] 
  c)we indicate the parts of the graph by writing G=(V,E)

Adjacent nodes

    if e=[u,v], then u and v are called adjacent nodes or neighbors

    u----------v

Degree of node
    The degree of node u,written deg(u),is the number of edges containing u.

    if deg(u)=0,then u is called isolated node

Path 
    A path of length n from a node u to a node v is define as a sequence of n+1 nodes

    P=(v0,v1,v2,v3,.......Vn)
    the path is said to be closed if v0=vn

Simple and complex path 
    the path is said to be simple if all the nodes are distint,with the exception that v0 may equal to
    vn otherwise it is complex path 

Connected graph
    A graph is said to be connected if there is a path between any two of it's nodes

Tree Graph 
    A connected graph T without any cycles is called a tree graph or free tree ,or simply a tree

    this means in particular ,that there is a unique simple path p between any two nodes u and v

Labelled graph
    A graph is to be labelled if its edges are assigned data 

Weighted graph 
    A graph G is said to be weighted if each edge e in G is assigned a non-negative numerical value
    w(e) called the weight or length of e

Multiple edges
    distinct edges e and e1 are called multiple edge if they connect the same end points.that is
    if e=[u,v] and e1=[u,v]

loop
    An edge is called loop if it has identical end points e[u,u]

Directed graph 
    A directed graph G also called digraph is same as multigraph expect that each edge e assigned 
    a direction e=(u,v)

    u----->-----v

complete graph 
    A simple graph in which there exists an edge between every pair of vertices is called a complete graph

Representation of Graph
    1)Adjancency matrix representation 
        Suppose G is a simple graph with m nodes, and suppose the nodes og G have been ordered and are called
        v1,v2,v3....vm.Then the adjacency matrix A=(A i,j) of the graph G is the m*m Square matrix 

        if there is a edge between two nodes then write '1' if not then '0',,,if waighed graph then you can 
        write the waighed value at the place of one '1'

    2)Adjancency list representation 
        The adjancency list stores information about only those edges that exists
        The adjancency list contains a directory (dict) contains adjacency list for each vertex
        
        in this dict there is a vertex as a key and ,,a list of vertices of which this key is 
        connected as a values 
        v0:[v1,v2]

'''
