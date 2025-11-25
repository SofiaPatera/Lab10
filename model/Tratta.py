
#somma di tutti i valore delle merci / spedizioni
class Tratta:
    hub1: int
    hub2: int
    valore_tot : float
    n_spedizioni : int #tot soedizioni riaguardo quella tratta

    def calcola_valore(valore_tot, n_spedizioni):
        valore = float(valore_tot/n_spedizioni)
