from database.DB_connect import DBConnect
from model.compagnia import Compagnia
from model.hub import Hub
from model.spedizione import Spedizione
from model.Tratta import Tratta


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    @staticmethod
    def leggiCompagnia():
        conn= DBConnect.get_connection()
        results = []
        query = """SELECT * from compagnie"""
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            compagnia = Compagnia(row['id'], row['codice'], row['nome'])
            results.append(compagnia)
        cursor.close()
        conn.closs()
        return results

    @staticmethod
    def leggiHub():
        conn = DBConnect.get_connection()
        results = []
        query = """ SELECT * from hub"""
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            hub = Hub(row['id'], row['codice'], row['nome'], row['citta'],
                      row['stato'], row['latitudine'], row['longitudine'])
            results.append(hub)
        cursor.close()
        conn.close()
        return results

    @staticmethod
    def leggispedizione():
        conn= DBConnect.get_connection()
        results = []
        query = """ SELECT * from spedizione"""
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            spedizione = Spedizione(row['id'], row['id_compagnia'], row['numero_tracking'],
                                    row['id_hub_origine'], row['id_hub_destinazione'],
                                    row['data_ritiro_programmata'], row['distanza'],
                                    row['data_consegna'], row['valore_merce'])
            results.append(spedizione)
        cursor.close()
        conn.close()
        return results


    @staticmethod
    def LeggiTratta():
        conn = DBConnect.get_connection()
        results = []
        query = """ SELECT 
                    LEAST (id_hub_destinazione, id_hub_origine) AS hub1
                    GREATEST(id_hub_destinazione, id_hub_origine) AS hub2
                    SUM(valore_merce)  AS valore_totale
                    count(*)  AS n_spedizione
                    from spedizione  AS s
                    GROUP BY hub1, hub2"""
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            tratta = Tratta(row['hub1'], row['hub2'], row['valore_tot'], row['n_spedizioni'])


   """ select h1 
            h2 
    sum(vlaore merce) as valore totale 
count(*)
from pspedi<ione 
gruop by 
#non clacola la direzione => 

#least => prende valore piu piccolo tra una serie 
#gratesst => prende valore più grande tra una serie di valori """