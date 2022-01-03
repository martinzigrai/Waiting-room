# bpc-bds-cakaren

3. projekt predmetu Bezpečnosť databázových systémov

## 1. krok
V prvom kroku je nutné stiahnuť si projekt z gitlabu.

## 2. krok
V tomto kroku treba vytvoriť a inicializovať databázu, príkazy potrebné k tomuto kroku nájdete v zložke POSTGRESQL.
Príkazy sa nachádzajú v súboroch a treba ich kopírovať v nasledujúcom poradí: create.sql, insert.sql, roles.sql, view.sql a injection.sql  

## 3. krok
Doinštalovanie knihovien:   -pip install Flask
                            -pip install bcrypt
                            -pip install Flask-WTF
                            -pip install Flask-SQLAlchemy
                            -pip install psycopg2

## 4. krok
Spustenie aplikácie pomocou príkazu python app.py (je potrebné nachádzať sa v danej zložke). Ak bude problém s pripojením k databáze, tak je potrebné zmeniť svoje prihlasovacie údaje a parametre v zložke connection.py

## 5. krok
Prihlásenie sa do aplikácie alebo vytvorenie nového účtu s vlastným heslom. 
Pre prihlásenie odporúčam použiť účet admin s heslom root. 
