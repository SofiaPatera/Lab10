from dataclasses import dataclass

@dataclass
class Tratta:
    hub1 : int
    hub2 : int
    valore_totale : float
    n_spedizioni : int #tot soedizioni riaguardo quella tratta

    def calcola_valore(self): #mettiamo anche self perché si trova all'interno della classe
        if self.n_spedizioni != 0:
            return float(self.valore_totale/self.n_spedizioni)
        else:
            return 0.0
