from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3
from create_map import create_map

app = FastAPI()

app.mount("/templates", StaticFiles(directory="templates"), name="templates")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    data_filter = request.query_params.get("filter", False)
    connection = sqlite3.connect("app.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT lum.cond, COUNT(car.num_accident) AS num_accident
        FROM caracteristique AS car JOIN vehicule AS veh ON car.num_accident=veh.num_accident 
                                    JOIN usager AS us ON us.id_veh=veh.id_veh
                                    JOIN luminosite as lum ON lum.lum=car.lum
                                    JOIN agglomeration as agg ON agg.agg=car.agg
                                    JOIN atmospherique as atm ON atm.atm=car.atm
                                    JOIN gravite as grav ON grav.grav=us.grav
        WHERE veh.catv=1 AND grav.cond LIKE ?
        GROUP BY lum.cond
        ORDER BY num_accident DESC
    """,
        (data_filter,),
    )
    rows_luminosite = cursor.fetchall()

    cursor.execute(
        """
        SELECT agg.cond, COUNT(car.num_accident) AS num_accident
        FROM caracteristique AS car JOIN vehicule AS veh ON car.num_accident=veh.num_accident 
                                    JOIN usager AS us ON us.id_veh=veh.id_veh
                                    JOIN luminosite as lum ON lum.lum=car.lum
                                    JOIN agglomeration as agg ON agg.agg=car.agg
                                    JOIN atmospherique as atm ON atm.atm=car.atm
                                    JOIN gravite as grav ON grav.grav=us.grav
        WHERE veh.catv=1 AND grav.cond LIKE ?
        GROUP BY agg.cond
        ORDER BY num_accident DESC
    """,
        (data_filter,),
    )
    rows_agglomeration = cursor.fetchall()

    cursor.execute(
        """
        SELECT atm.cond, COUNT(car.num_accident) AS num_accident
        FROM caracteristique AS car JOIN vehicule AS veh ON car.num_accident=veh.num_accident 
                                    JOIN usager AS us ON us.id_veh=veh.id_veh
                                    JOIN luminosite as lum ON lum.lum=car.lum
                                    JOIN agglomeration as agg ON agg.agg=car.agg
                                    JOIN atmospherique as atm ON atm.atm=car.atm
                                    JOIN gravite as grav ON grav.grav=us.grav
        WHERE veh.catv=1 AND grav.cond LIKE ?
        GROUP BY atm.cond
        ORDER BY num_accident DESC
    """,
        (data_filter,),
    )
    rows_atmospherique = cursor.fetchall()
    create_map(data_filter)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "luminosite": rows_luminosite,
            "agglomeration": rows_agglomeration,
            "atmospherique": rows_atmospherique,
        },
    )
