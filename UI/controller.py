import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        self._view.lista_visualizzazione.controls.clear()
        valoreInserito = self._view.guadagno_medio_minimo.value
        if not valoreInserito:  #nel caso in cui il vlaore non viene inserito dall'utente => il programma manda un avviso per inserirlo
            self._view.show_alert("Inserisci un valore: ")
            self._view.update()
            return

        #controlliamo che sia un valore numerico
        try:
            valoreI = float(valoreInserito)
        except ValueError:
            self._view.show_alert("Valore inserito non valido, inserisci valore numerico: ")
            self._view.update()
            return

        try:
            self._model.costruisci_grafo(valoreI)
        except:
            self._view.show_alert("Errore nella costruzione del grafo")
            self._view.update()
            return

        numArchi = self._model.get_num_edges()
        numNodi = self._model.get_num_nodes()
        archi = self._model.get_all_edges()
        hub_dict = self._model._hub_dict
        #popolazione della listview
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Hubs: {numNodi}"))
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Tratte: {numArchi}"))
        self._view.lista_visualizzazione.controls.append(ft.Divider()) #

        count = 1
        for u,v, data in archi:
            peso = data['weight']
            nome_u = hub_dict.get(u, str(u))
            nome_v = hub_dict.get(v, str(v))
            self._view.lista_visualizzazione.controls.append(ft.Text(f"{count}) {nome_u} ->  {nome_v}: Guadagno medio per spedizione: € {peso:.2f}"))
            count += 1
        self._view.update()







