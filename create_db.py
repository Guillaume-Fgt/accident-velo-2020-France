import sqlite3

connection = sqlite3.connect("app.db")

cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS caracteristique (
        id INTEGER PRIMARY KEY,
        num_accident INTEGER NOT NULL UNIQUE,
        jour INTEGER NOT NULL,
        mois INTEGER NOT NULL,
        an INTEGER NOT NULL,
        hrmn DATETIME NOT NULL,
        lum INTEGER NOT NULL,
        dep INTEGER NOT NULL,
        com INTEGER NOT NULL,
        agg INTEGER NOT NULL,
        inter INTEGER NOT NULL,
        atm INTEGER NOT NULL,
        lat DECIMAL NOT NULL,
        long DECIMAL NOT NULL
    )              
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS vehicule (
        id INTEGER PRIMARY KEY,
        num_accident INTEGER NOT NULL,
        id_veh INTEGER NOT NULL,
        catv INTEGER NOT NULL,
        obs INTEGER NOT NULL,
        obsm INTEGER NOT NULL,
        choc DATETIME NOT NULL,
        manv INTEGER NOT NULL,
        motor INTEGER NOT NULL,
        FOREIGN KEY (num_accident) REFERENCES caracteristique (num_accident)
    )              
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS type_motor (
        id INTEGER PRIMARY KEY,
        motor INTEGER NOT NULL UNIQUE,
        type TEXT NOT NULL,
        FOREIGN KEY (motor) REFERENCES vehicule (motor)
    )              
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS luminosite (
        id INTEGER PRIMARY KEY,
        lum INTEGER NOT NULL UNIQUE,
        cond TEXT NOT NULL,
        FOREIGN KEY (lum) REFERENCES caracteristique (lum)
    )              
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS agglomeration (
        id INTEGER PRIMARY KEY,
        agg INTEGER NOT NULL UNIQUE,
        cond TEXT NOT NULL,
        FOREIGN KEY (agg) REFERENCES caracteristique (agg)
    )              
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS atmospherique (
        id INTEGER PRIMARY KEY,
        atm INTEGER NOT NULL UNIQUE,
        cond TEXT NOT NULL,
        FOREIGN KEY (atm) REFERENCES caracteristique (atm)
    )              
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usager (
        id INTEGER PRIMARY KEY,
        num_accident INTEGER NOT NULL,
        id_veh INTEGER NOT NULL,
        grav INTEGER NOT NULL,
        sexe INTEGER NOT NULL,
        an_nais INTEGER NOT NULL,
        trajet DATETIME NOT NULL,
        FOREIGN KEY (num_accident) REFERENCES caracteristique (num_accident)
    )              
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS gravite (
        id INTEGER PRIMARY KEY,
        grav INTEGER NOT NULL UNIQUE,
        cond TEXT NOT NULL,
        FOREIGN KEY (grav) REFERENCES usager (grav)
    )              
"""
)

connection.commit()
