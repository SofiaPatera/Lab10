from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()
        self._hub_list  = DAO.leggiHub()
        self._hub_dict = {}
        for h in self._hub_list:
            self._hub_dict[h.id] = h.nome

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        lista_hub = DAO.leggiHub()
        lista_tratte = DAO.leggitratte()
        #inserisco nodi
        for hub in lista_hub:
            self.G.add_node(hub.id)
        #inserisco tratte come archi
        for tratta in lista_tratte:
            valore= tratta.calcola_valore()
            if valore >= threshold:
                self.G.add_edge(tratta.hub1, tratta.hub2, weight = valore)


    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        return list(self.G.edges(data = True)) #data = True serve per dire a nx che mi deve restiruire anche il peso
