import folium
from folium.plugins import FastMarkerCluster
import sqlite3


def create_map(data_filter):

    m = folium.Map(location=[47.070, 2.681], zoom_start=5)

    tooltip = "Détails"

    connection = sqlite3.connect("app.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT car.lat, car.long, grav.cond as grav, atm.cond as atm, lum.cond as lum, car.hrmn as heur
        FROM caracteristique AS car JOIN vehicule AS veh ON car.num_accident=veh.num_accident 
                                    JOIN usager AS us ON us.id_veh=veh.id_veh
                                    JOIN luminosite as lum ON lum.lum=car.lum
                                    JOIN agglomeration as agg ON agg.agg=car.agg
                                    JOIN atmospherique as atm ON atm.atm=car.atm
                                    JOIN gravite as grav ON grav.grav=us.grav
        WHERE veh.catv=1 AND grav.cond LIKE ?
    """,
        (data_filter,),
    )
    rows_coor = cursor.fetchall()

    locations = []

    for row in rows_coor:
        lat_num = row["lat"].replace(",", ".")
        long_num = row["long"].replace(",", ".")
        gravite_dict = {
            "Indemne": "darkgreen",
            "Blessé léger": "lightgreen",
            "Blessé hospitalisé": "orange",
            "Tué": "red",
        }
        color_icon = gravite_dict[row["grav"]]
        locations.append(
            [
                lat_num,
                long_num,
                color_icon,
                row["grav"],
                row["atm"],
                row["lum"],
                row["heur"],
            ]
        )

    callback = (
        "function (row) {"
        'var marker = L.marker(new L.LatLng(row[0], row[1]), {color: "red"});'
        "var icon = L.AwesomeMarkers.icon({"
        "icon: 'plus-sign',"
        "markerColor: row[2],"
        "prefix: 'glyphicon',"
        "extraClasses: 'fa-rotate-0'"
        "});"
        "marker.setIcon(icon);"
        "var popup = L.popup({maxWidth: '300'});"
        "const display_text = {text: row[3]};"
        "const display_text2 = {text: row[5]};"
        "const display_text3 = {text: row[4]};"
        "const display_text4 = {text: row[6]};"
        "var mytext = $(`<div id='mytext' class='display_text' style='width: 100.0%; height: 100.0%;'> Gravité: ${display_text.text}<br>Luminosité: ${display_text2.text}<br>Météo: ${display_text3.text}<br>Heure: ${display_text4.text}<br></div>`)[0];"
        "popup.setContent(mytext);"
        "marker.bindPopup(popup);"
        "return marker};"
    )

    FastMarkerCluster(data=locations, callback=callback).add_to(m)

    m.save("templates/map.html")

    # return folium_map._repr_html_()
