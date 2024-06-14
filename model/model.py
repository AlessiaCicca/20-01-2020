import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.ruoli=DAO.getRuoli()
        self.grafo=nx.Graph()
        self._idMap = {}
        self.dict = {}
        self._solBest = []
        self._costBest = 0


    def creaGrafo(self, ruolo):
        self.nodi = DAO.getNodi(ruolo)
        self.grafo.add_nodes_from(DAO.getNodi(ruolo))
        for v in self.nodi:
            self._idMap[v.artist_id] = v
        self.addEdges(ruolo)
        return self.grafo

    def addEdges(self,ruolo):
         self.grafo.clear_edges()
         allEdges = DAO.getConnessioni(ruolo)
         for connessione in allEdges:
             nodo1 = self._idMap[connessione.v1]
             nodo2 = self._idMap[connessione.v2]
             if nodo1 in self.grafo.nodes and nodo2 in self.grafo.nodes:
                 if self.grafo.has_edge(nodo1, nodo2) == False:
                     #peso = DAO.getPeso(forma, anno, connessione.v1, connessione.v2)
                     self.grafo.add_edge(nodo1, nodo2, weight=connessione.peso)

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def bestPath(self,v0id):
        v0=self._idMap[v0id]
        self._solBest = []
        self._costBest = 0
        parziale = [v0]
        self.ricorsione(parziale)
        return self._solBest, self._costBest

    def ricorsione(self, parziale):
        # Controllo se parziale è una sol valida, ed in caso se è migliore del best
        if len(parziale) > self._costBest:
            self._costBest = len(parziale)
            self._solBest = copy.deepcopy(parziale)

        for v in self.grafo.neighbors(parziale[-1]):
            if v not in parziale:
                parziale.append(v)
                if self.ammissibile(parziale):
                    self.ricorsione(parziale)
                    parziale.pop()
                else:
                    parziale.pop()

    def ammissibile(self,listanodi):
        okay=True
        for i in range(len(listanodi)-2):
            if (self.grafo[listanodi[i]][listanodi[i+1]]["weight"]!=self.grafo[listanodi[i+1]][listanodi[i+2]]["weight"]):
                okay=False
        return okay





