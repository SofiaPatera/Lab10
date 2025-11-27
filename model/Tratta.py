

from dataclasses import dataclass


@dataclass
class Tratta:
    hub1 : int
    hub2 : int
    valore_totalw : float
    n_spedizioni = int #tot soedizioni riaguardo quella tratta

    def calcola_valore(self, valore_totale, n_spedizioni): #mettiamo anche self perché si trova all'interno della classe
        valore = float(valore_totale/n_spedizioni)
        return valore
