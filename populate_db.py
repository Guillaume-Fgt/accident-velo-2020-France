import sqlite3
import csv

connection = sqlite3.connect("app.db")

cursor = connection.cursor()

# with open("Accidents_velos/caracteristiques-2020.csv", encoding="UTF-8") as csv_file:
#     reading = csv.DictReader(csv_file, delimiter=";")
#     for row in reading:
#         cursor.execute(
#             "INSERT INTO caracteristique (num_accident, jour, mois, an, hrmn, lum, dep, com, agg, inter, atm, lat, long) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
#             (
#                 row["Num_Acc"],
#                 row["jour"],
#                 row["mois"],
#                 row["an"],
#                 row["hrmn"],
#                 row["lum"],
#                 row["dep"],
#                 row["com"],
#                 row["agg"],
#                 row["int"],
#                 row["atm"],
#                 row["lat"],
#                 row["long"],
#             ),
#         )

# with open("Accidents_velos/vehicules-2020.csv", encoding="UTF-8") as csv_file:
#     reading = csv.DictReader(csv_file, delimiter=";")
#     for row in reading:
#         cursor.execute(
#             "INSERT INTO vehicule (num_accident, id_veh, catv, obs, obsm, choc, manv, motor) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
#             (
#                 row["Num_Acc"],
#                 row["id_vehicule"],
#                 row["catv"],
#                 row["obs"],
#                 row["obsm"],
#                 row["choc"],
#                 row["manv"],
#                 row["motor"],
#             ),
#         )

# ######
# motor_dict = {
#     -1: "Non renseigné",
#     0: "Inconnue",
#     1: "Hydrocarbures",
#     2: "hybride électrique",
#     3: "Electrique",
#     4: "Hydrogène",
#     5: "Humaine",
#     6: "Autre",
# }

# for key, value in motor_dict.items():
#     cursor.execute("INSERT INTO type_motor (motor, type) VALUES (?, ?)", (key, value))
# ######

# #####
# luminosite_dict = {
#     1: "Plein jour",
#     2: "Crépuscule ou aube",
#     3: "Nuit sans éclairage public",
#     4: "Nuit avec éclairage public non allumé",
#     5: "Nuit avec éclairage public allumé",
# }

# for key, value in luminosite_dict.items():
#     cursor.execute("INSERT INTO luminosite (lum, cond) VALUES (?, ?)", (key, value))
# ######

# #####
# agglomeration_dict = {
#     1: "Hors agglomération",
#     2: "En agglomération",
# }

# for key, value in agglomeration_dict.items():
#     cursor.execute("INSERT INTO agglomeration (agg, cond) VALUES (?, ?)", (key, value))
# ######

# #####
# atmospherique_dict = {
#     -1: "Non renseigné",
#     1: "Normale",
#     2: "Pluie légère",
#     3: "Pluie forte",
#     4: "Neige - grêle",
#     5: "Brouillard - fumée",
#     6: "Vent fort - tempête",
#     7: "Temps éblouissant",
#     8: "Temps couvert",
#     9: "Autre",
# }

# for key, value in atmospherique_dict.items():
#     cursor.execute("INSERT INTO atmospherique (atm, cond) VALUES (?, ?)", (key, value))
# ######

with open("Accidents_velos/usagers-2020.csv", encoding="UTF-8") as csv_file:
    reading = csv.DictReader(csv_file, delimiter=";")
    for row in reading:
        cursor.execute(
            "INSERT INTO usager (num_accident, id_veh, grav, sexe, an_nais, trajet) VALUES (?, ?, ?, ?, ?, ?)",
            (
                row["Num_Acc"],
                row["id_vehicule"],
                row["grav"],
                row["sexe"],
                row["an_nais"],
                row["trajet"],
            ),
        )

# #####
# gravite_dict = {
#     1: "Indemne",
#     2: "Tué",
#     3: "Blessé hospitalisé",
#     4: "Blessé léger",
# }

# for key, value in gravite_dict.items():
#     cursor.execute("INSERT INTO gravite (grav, cond) VALUES (?, ?)", (key, value))
# # ######

connection.commit()
