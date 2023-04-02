from Graphs import Graph
from Vertex import Vertex


def readFile(fileName):
    graph = Graph()
    with open(fileName, "r") as file:
        numberVertices, numberEdges = map(int, file.readline().split())
        for i in range(numberVertices):
            graph.addVertex(Vertex(i))
        for _ in range(numberEdges):
            startVertex, endVertex, cost = map(int, file.readline().split())
            graph.addEdge(Vertex(startVertex), Vertex(endVertex), cost)
        file.close()
    return graph


def writeFile(fileName, graph: Graph):
    with open(fileName, "w") as file:
        file.write(str(graph.getNumberVertexes()) + ' ' + str(graph.getNumberEgdes()) + '\n')
        edges = graph.parseEdges()
        for edge in list(edges.keys()):
            file.write(str(edge[0].id)+' '+str(edge[1].id)+' '+str(edges[edge])+'\n')
        file.close()