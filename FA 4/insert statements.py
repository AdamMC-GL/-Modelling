import psycopg2

c = psycopg2.connect("dbname=postgres user=postgres password=!@#$%^&*()")  # edit this.
cur = c.cursor()

'''2. Voer in deze database de volgende gegevens in (door middel van insert statements):'''
cur.execute("INSERT INTO Product VALUES (250, 'AH halfvolle melk', 0.99);")
cur.execute("INSERT INTO Product VALUES (251, 'AH pindakaas', 2.39);")
cur.execute("INSERT INTO Product VALUES (252, 'tandelborstel', 1.35);")

"""- Anonieme bonuskaart met nummer 65472335"""
sql = "INSERT INTO bonus_kaart VALUES (65472335);"
cur.execute(sql)

"""- Bonuskaarthouder Annette, woont op Vredenburg 12 in Utrecht en heeft bonuskaartnummer 12345678"""
cur.execute("INSERT INTO bonus_kaart"
            " VALUES (12345678, 'Annette', 'Vredenburg 12', 'Utrecht');")

"""- Filiaal van Albert Heijn: Utrecht, Stationsplein. Filiaalnummer 35."""
cur.execute("INSERT INTO filiaal"
            " VALUES (35, 'Utrecht', 'Stationsplein');")

"""Filiaal van Albert Heijn: Utrecht, Roelantdreef 41. Filiaalnummer 48."""
cur.execute("INSERT INTO filiaal"
            " VALUES (48, 'Utrecht', 'Roelantdreef 41');")

"""
- De anomieme bonuskaarthouder heeft bij het filiaal op het Stationsplein op 1 december 2019 
om 17:35 uur de volgende aankopen gedaan:

            2 maal pak AH halfvolle melk à 0,99
            1 maal pot AH pindakaas à 2,39
            1 maal tandelborstel à 1,35
"""
cur.execute("SELECT bonus_kaart_nummer FROM bonus_kaart WHERE naam IS NULL;")
bonus_kaart_nr = cur.fetchone()[0]
cur.execute("SELECT filiaal_nummer FROM filiaal WHERE adres = 'Stationsplein';")
filiaal_nr = cur.fetchone()[0]

cur.execute("INSERT INTO transactie"
            f" VALUES (90, '01-12-2019', '17:35', {bonus_kaart_nr}, {filiaal_nr});")

cur.execute("INSERT INTO aankoop VALUES (90, 250, 2);")
cur.execute("INSERT INTO aankoop VALUES (90, 251, 1);")
cur.execute("INSERT INTO aankoop VALUES (90, 252, 1);")

"""
- Op 3 december 2019 om 12:25 heeft deze anonieme bonuskaarthouder bij het filiaal op de Roelantdreef het volgende gekocht:

            1 maal pak AH halfvolle melk à 0,99
"""
cur.execute("SELECT bonus_kaart_nummer FROM bonus_kaart WHERE naam IS NULL;")
bonus_kaart_nr = cur.fetchone()[0]
cur.execute("SELECT filiaal_nummer FROM filiaal WHERE adres = 'Roelantdreef 41';")
filiaal_nr = cur.fetchone()[0]

cur.execute("INSERT INTO transactie"
            f" VALUES (91, '03-12-2019', '12:25', {bonus_kaart_nr}, {filiaal_nr});")

cur.execute(f"INSERT INTO aankoop VALUES (91, 250, 1);")

"""
- Bonuskaarthouder Annette heeft bij het filiaal op het stationsplein op 1 december 2019 om 08:30 het volgende gekocht:

            2 maal pak AH halfvolle melk à 0,99
"""
cur.execute("SELECT bonus_kaart_nummer FROM bonus_kaart WHERE naam = 'Annette';")
bonus_kaart_nr = cur.fetchone()[0]
cur.execute("SELECT filiaal_nummer FROM filiaal WHERE adres = 'Stationsplein';")
filiaal_nr = cur.fetchone()[0]
cur.execute("INSERT INTO transactie"
            f" VALUES (92, '01-12-2019', '08:30', {bonus_kaart_nr}, {filiaal_nr});")

cur.execute(f"INSERT INTO aankoop VALUES (92, 250, 2);")

c.commit()
cur.close()
c.close()
