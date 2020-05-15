from dfs import dfs_iterator
from edge_list_graph import Edge
from edge_list_graph import Graph
from edge_list_graph import Vertex


class Node:
    
    def __init__(self):
        super().__init__()
        Right= 0
        Left = 0
        Up = 0
        Down = 0

def RobotOnAGrid(num, maze):
    graph = Graph()
    graph.setEnd(str(len(maze)-1)+ " " +maze[len(maze)-1])
    graph.setStart(str(0)+ " " + maze[0])
    v1 = None
    v3 = None
    v2 = None
    dfs = dfs_iterator()

#Laver knuder for alle "," tegene i mazeen
    for i in range(len(maze)):
        #Skifter linje
        if i%4 == 0 and i != 0:
            pass
        #Tilføjer knuder til højre 
        elif maze[i] != '#' and maze[i+1] != '#':
            v1 = graph.insert_vertex(str(i) +" " + str(maze[i]))
            v2 = graph.insert_vertex(str(i) +" " +str( maze[i+1]))
            
            graph.insert_edge("R", v1, v2)
        #Tilføj knuder ned af 
        elif maze[i+5] != '#' and maze[i+num] != None:
            v3 = graph.insert_vertex(str(i) +" " + str(maze[i+num]))
            
            graph.insert_edge("D",v1, v3 )
        #tilføj knuder til venstre
        elif maze[i] != '#' and maze[i-1] != '#' and maze[i-1] != None:
            v1 = graph.insert_vertex(str(i) +" " + str(maze[i]))
            v2 = graph.insert_vertex(str(i) +" " + str(maze[i+1]))
            graph.insert_edge("L", v2, v1)
        #tilføj knuder op af
        elif maze[i] != '#' and maze[i-num] != None:
            v3 = graph.insert_vertex(str(i) +" " +str( maze[i-num]))
            graph.insert_edge("U",v3, v1 )


    return dfs.DFS(graph)



print(RobotOnAGrid(5, ".....#..#.#..#....#......"))