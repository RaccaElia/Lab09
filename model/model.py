from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._aeroporti = DAO.getAeroporti()
        self._grafo = nx.Graph()
        self._idMap = {}
        for aeroporto in self._aeroporti:
            self._idMap[aeroporto[0]] = f"{aeroporto[1]} ({aeroporto[2]})"

    def buildGraph(self, distanza):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._idMap.values())
        self.analizza(distanza)

    def analizza(self, distanza):
        voli = DAO.getFlightsDistance(distanza)
        for volo in voli:
            self._grafo.add_edge(self._idMap[volo.aeroportoPartenza], self._idMap[volo.aeroportoArrivo], distanza=volo.distanza)

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def getArchi(self):
        return self._grafo.edges