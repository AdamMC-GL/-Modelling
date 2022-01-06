import psycopg2

c = psycopg2.connect("dbname=postgres user=postgres password=!@#$%^&*()")  # edit this.
cur = c.cursor()

"""
1. Schrijf voor deze database een DDL-script om een database met de tabellen, keys en
 constraints aan te maken. Voer het script uit op je eigen omgeving.
"""
# eliminates all existing tables with the same name in order to start fresh:
cur.execute("DROP TABLE IF EXISTS Product CASCADE")
cur.execute("DROP TABLE IF EXISTS aankoop CASCADE")
cur.execute("DROP TABLE IF EXISTS transactie CASCADE")
cur.execute("DROP TABLE IF EXISTS filiaal CASCADE")
cur.execute("DROP TABLE IF EXISTS bonus_kaart CASCADE")

# Make all tables
cur.execute("""CREATE TABLE bonus_kaart
                (bonus_kaart_nummer INTEGER NOT NULL,
                 naam VARCHAR,
                 adres VARCHAR,
                 woonplaats VARCHAR,
                 PRIMARY KEY (bonus_kaart_nummer)  
                 );""")

cur.execute("""CREATE TABLE filiaal
                (filiaal_nummer INTEGER NOT NULL,
                 plaats VARCHAR NOT NULL,
                 adres VARCHAR NOT NULL,
                 PRIMARY KEY (filiaal_nummer)  
                 );""")

cur.execute("""CREATE TABLE transactie
                (transactie_nummer INTEGER NOT NULL,
                 datum DATE NOT NULL,
                 tijd TIME NOT NULL,
                 bonus_kaart_nummer INTEGER NOT NULL,
                 filiaal_nummer INTEGER NOT NULL,
                 PRIMARY KEY (transactie_nummer),
                 FOREIGN KEY (bonus_kaart_nummer) REFERENCES bonus_kaart(bonus_kaart_nummer),
                 FOREIGN KEY (filiaal_nummer) REFERENCES filiaal(filiaal_nummer)
                 );""")

cur.execute("""CREATE TABLE Product
                (product_nummer INTEGER NOT NULL,
                 omschrijving VARCHAR NOT NULL,
                 prijs DECIMAL NOT NULL,
                 PRIMARY KEY (product_nummer)  
                 );""")

cur.execute("""CREATE TABLE aankoop
                (transactie_nummer INTEGER NOT NULL,
                 product INTEGER NOT NULL,
                 aantal INTEGER NOT NULL,
                 PRIMARY KEY (transactie_nummer, product),
                 FOREIGN KEY (transactie_nummer) REFERENCES transactie(transactie_nummer),
                 FOREIGN KEY (product) REFERENCES Product(product_nummer)
                 );""")

c.commit()
cur.close()
c.close()
