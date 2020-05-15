from FlowNetwork import Edge as Edge
from FlowNetwork import Residual_Edge as Residual_Edge
from FlowNetwork import Vertex as Vertex
from FlowNetwork import FlowNetwork as FlowNetwork


def isEliminated(standings: str):
    teams =[]

    for t in  standings.split("-"):
        teams.append(t.split(" "))
    Q = []
    network = FlowNetwork()

    vo = network.insert_vertex("O", source=True)
    vt = network.insert_vertex("T", sink=True)
    v= None
    for i in range(0, len(teams)):
        for j in range(i, len(teams)):
            Q.add((teams[i], teams[j]))

            v = network.insert_vertex( str(teams[i][0][0])+ ", "+ str(teams[j][0][0]))
            network.insert_edge(teams[i][len(teams)-(3-i)] *2, vo, v)

        for t in teams:
            v2 = network.insert_vertex(t[0][0])
            network.insert_edge(teams[i][len(teams)-(3-i)] *2, v, v2)