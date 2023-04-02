from random import randint

from Vertex import *


class Graph:
    def __init__(self):
        self.__predecessors = {}
        self.__successors = {}
        self.__edges = {}

    def getNumberVertexes(self):
        return len(list(self.__predecessors.keys()))

    def getNumberEgdes(self):
        return len(self.__edges)

    def parseVertices(self):
        return list(self.__predecessors.keys())

    def __checkIfVertex(self, vertex: Vertex):
        if vertex not in self.__predecessors.keys():
            return False
        return True

    def checkIfEdge(self, first: Vertex, second: Vertex):
        if not (self.__checkIfVertex(first) and self.__checkIfVertex(second)):
            raise ValueError("No vertex with such id")
        if first in self.__predecessors[second] or second in self.__successors[first]:
            return True
        else:
            return False

    def parseEdges(self):
        return self.__edges

    def getDegrees(self, vertex: Vertex):
        inDegree = self.getInDegree(vertex)
        outDegree = self.getOutDegree(vertex)
        return inDegree, outDegree

    def getInDegree(self, vertex: Vertex):
        if not self.__checkIfVertex(vertex):
            raise ValueError("No vertex with such id")
        inDegree = len(self.__predecessors[vertex])
        return inDegree

    def getOutDegree(self, vertex: Vertex):
        if not self.__checkIfVertex(vertex):
            raise ValueError("No vertex with such id")
        outDegree = len(self.__successors[vertex])
        return outDegree

    def parseOutboundEdges(self, vertex: Vertex):
        if not self.__checkIfVertex(vertex):
            raise ValueError("No vertex with such id")
        outboundEdges = {}
        for outVertex in self.__successors[vertex]:
            outboundEdges[(vertex, outVertex)] = self.__edges[(vertex, outVertex)]
        return outboundEdges

    def parseInboundEdges(self, vertex: Vertex):
        if not self.__checkIfVertex(vertex):
            raise ValueError("No vertex with such id")
        inboundEdges = {}
        for inVertex in self.__predecessors[vertex]:
            inboundEdges[(inVertex, vertex)] = self.__edges[(inVertex, vertex)]
        return inboundEdges

    def addVertex(self, vertex: Vertex):
        if self.__checkIfVertex(vertex):
            raise ValueError("Vertex with id already exists")
        self.__predecessors[vertex] = set()
        self.__successors[vertex] = set()

    def addEdge(self, startVertex: Vertex, endVertex: Vertex, cost: int):
        if not (self.__checkIfVertex(startVertex) and self.__checkIfVertex(endVertex)):
            raise ValueError("No vertex with such id")
        if self.checkIfEdge(startVertex, endVertex):
            raise ValueError("Edge already exists")
        self.__edges[(startVertex, endVertex)] = cost
        self.__successors[startVertex].add(endVertex)
        self.__predecessors[endVertex].add(startVertex)

    def removeVertex(self, vertex: Vertex):
        if not self.__checkIfVertex(vertex):
            raise ValueError("No vertex with such id")
        for outVertex in self.__successors[vertex]:
            self.__predecessors[outVertex].discard(vertex)
            if self.checkIfEdge(vertex, outVertex):
                del self.__edges[(vertex, outVertex)]
        for inVertex in self.__predecessors[vertex]:
            self.__successors[inVertex].discard(vertex)
            if self.checkIfEdge(inVertex, vertex):
                del self.__edges[(inVertex, vertex)]
        del self.__predecessors[vertex]
        del self.__successors[vertex]

    def removeEdge(self, inVertex: Vertex, outVertex: Vertex):
        if not self.checkIfEdge(inVertex, outVertex):
            raise ValueError("No such edge")
        del self.__edges[(inVertex, outVertex)]
        self.__predecessors[outVertex].discard(inVertex)
        self.__successors[inVertex].discard(outVertex)

    def updateEdge(self, inVertex: Vertex, outVertex: Vertex, newCost: int):
        if not self.checkIfEdge(inVertex, outVertex):
            raise ValueError("No such egde")
        self.__edges[(inVertex, outVertex)] = newCost

    def getCost(self, inVertex: Vertex, outVertex: Vertex):
        if not self.checkIfEdge(inVertex, outVertex):
            raise ValueError("No such edge")
        return self.__edges[(inVertex, outVertex)]

    def generateRandom(self, nrVertices: int, nrEgdes: int):
        self.__predecessors.clear()
        self.__successors.clear()
        self.__edges.clear()
        for i in range(nrVertices):
            self.addVertex(Vertex(i))
        nrEgdes = min(nrVertices**2, nrEgdes)
        for _ in range(nrEgdes):
            inId = randint(0,nrVertices-1)
            outId = randint(0,nrVertices-1)
            while self.checkIfEdge(Vertex(inId), Vertex(outId)):
                inId = randint(0, nrVertices - 1)
                outId = randint(0, nrVertices - 1)
            self.addEdge(Vertex(inId),Vertex(outId), randint(0, 3*nrVertices))

