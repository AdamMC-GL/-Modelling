import psycopg2

c = psycopg2.connect("dbname=postgres user=postgres password=!@#$%^&*()")  # edit this.
cur = c.cursor()
"""
    Toon de verschillende filialen (toon filiaalnummer, adres en plaats) waar een 
    klant met bonuskaartnummer 65472335 boodschappen heeft gedaan en op welke datum.
"""
cur.execute("SELECT DISTINCT transactie.filiaal_nummer, adres, plaats, datum"
            " FROM transactie, filiaal"
            " WHERE bonus_kaart_nummer = 65472335"
            " AND transactie.filiaal_nummer = filiaal.filiaal_nummer;")
results = cur.fetchall()
print(results)

"""
    Toon het totaalbedrag dat de klant met bonuskaartnummer 65472335 heeft besteed aan boodschappen. 
    Je hoeft dus alleen het totaalbedrag (1 waarde) te tonen, niet wat of wie of wanneer.
"""
cur.execute("SELECT SUM(prijs)"
            " FROM Product, aankoop, transactie"
            " WHERE bonus_kaart_nummer = 65472335"
            " AND aankoop.product = Product.product_nummer"
            " AND transactie.transactie_nummer = aankoop.transactie_nummer;")
results = cur.fetchone()[0]
print(results)

"""
    Toon het aantal maal dat de 'AH halfvolle melk' is verkocht in de maand december 2019 bij 
    een filiaal in Utrecht. Toon dus ook weer 1 waarde (niet in welk filiaal dat was of welk product etc.).
"""
cur.execute("SELECT SUM(aantal)"  # COUNT(omschrijving)
            " FROM Product, aankoop, transactie, filiaal"
            " WHERE omschrijving = 'AH halfvolle melk'"
            " AND filiaal.plaats = 'Utrecht'"
            " AND EXTRACT(MONTH FROM datum) = 12"
            " AND aankoop.product = Product.product_nummer"
            " AND transactie.filiaal_nummer = filiaal.filiaal_nummer"
            " AND transactie.transactie_nummer = aankoop.transactie_nummer;")

results = cur.fetchone()[0]
print(results)

c.commit()
cur.close()
c.close()
