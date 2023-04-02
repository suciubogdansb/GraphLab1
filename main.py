from copy import deepcopy

from FileGraph import readFile, writeFile
from Graphs import Graph
from Vertex import Vertex


class Main():
    def __init__(self):
        self.__graph = Graph()
        self.__listGraphs = [deepcopy(self.__graph)]

    def menu(self):
        print("""
Commands:
    1. get the number of vertices
    2. get set of vertices
    3. get the number of edges
    4. get set of edges
    5. add vertex
    6. add edge
    7. remove vertex
    8. remove edge
    9. check if edge exists
    10. get in degree of a vertex
    11. get out degree of a vertex
    12. get outbound edges of a vertex
    13. get inbound edges of a vertex
    14. get cost of an edge
    15. modify cost of an edge
    16. copy graph
    17. go to last copy
    18. read from text file
    19. write to text file
    20. create random graph
    0. exit
            """)
        commands = {
            1: self.nrVertices,
            2: self.getVertices,
            3: self.nrEdges,
            4: self.getEdges,
            5: self.addVertex,
            6: self.addEdge,
            7: self.removeVertex,
            8: self.removeEgde,
            9: self.checkEdge,
            10: self.printInDegree,
            11: self.printOutDegree,
            12: self.printOutbound,
            13: self.printInbound,
            14: self.printCost,
            15: self.modifyCost,
            16: self.copyGraph,
            17: self.goLastCopy,
            18: self.readFrom,
            19: self.writeTo,
            20: self.generateGraph

        }
        while True:
            inputCommand = int(input(">>"))
            try:
                if inputCommand == 0:
                    break
                elif inputCommand in range(1, 21):
                    commands[inputCommand]()
                else:
                    raise ValueError("Invalid Input")
            except Exception as e:
                print(e)

    def nrVertices(self):
        print(self.__graph.getNumberVertexes())

    def getVertices(self):
        print(self.__graph.parseVertices())

    def nrEdges(self):
        print(self.__graph.getNumberEgdes())

    def getEdges(self):
        print(self.__graph.parseEdges())

    def addVertex(self):
        id = int(input("id>>"))
        self.__graph.addVertex(Vertex(id))

    def addEdge(self):
        inId = int(input("inId>>"))
        outId = int(input("outId>>"))
        cost = int(input("cost>>"))
        self.__graph.addEdge(Vertex(inId), Vertex(outId), cost)

    def removeVertex(self):
        id = int(input("id>>"))
        self.__graph.removeVertex(Vertex(id))

    def removeEgde(self):
        inId = int(input("inId>>"))
        outId = int(input("outId>>"))
        self.__graph.removeEdge(Vertex(inId), Vertex(outId))

    def checkEdge(self):
        inId = int(input("inId>>"))
        outId = int(input("outId>>"))
        print(self.__graph.checkIfEdge(Vertex(inId), Vertex(outId)))

    def printInDegree(self):
        id = int(input("id>>"))
        print(self.__graph.getInDegree(Vertex(id)))

    def printOutDegree(self):
        id = int(input("id>>"))
        print(self.__graph.getOutDegree(Vertex(id)))

    def printOutbound(self):
        id = int(input("id>>"))
        print(self.__graph.parseOutboundEdges(Vertex(id)))

    def printInbound(self):
        id = int(input("id>>"))
        print(self.__graph.parseInboundEdges(Vertex(id)))

    def printCost(self):
        inId = int(input("inId>>"))
        outId = int(input("outId>>"))
        print(self.__graph.getCost(Vertex(inId), Vertex(outId)))

    def modifyCost(self):
        inId = int(input("inId>>"))
        outId = int(input("outId>>"))
        newCost = int(input("cost>>"))
        self.__graph.updateEdge(Vertex(inId), Vertex(outId), newCost)

    def copyGraph(self):
        self.__listGraphs.append(deepcopy(self.__graph))

    def goLastCopy(self):
        self.__graph = self.__listGraphs.pop(-1)

    def readFrom(self):
        fileName = input("fileName>>")
        self.__graph = readFile(fileName)

    def writeTo(self):
        fileName = input("fileName>>")
        writeFile(fileName, self.__graph)

    def generateGraph(self):
        nrVertices = int(input("nrVertices>>"))
        nrEdges = int(input("nrEdges>>"))
        self.__graph.generateRandom(nrVertices, nrEdges)


if __name__ == "__main__":
    main = Main()
    main.menu()
