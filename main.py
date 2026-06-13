from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# Configuration CORS pour permettre au frontend de discuter avec l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ta connexion (remplace par tes vrais identifiants)
def get_db_connection():
    return psycopg2.connect(dbname="ymmo_db", user="app_user", password="Azerty123!", host="localhost", port="5432")

@app.get("/biens")
def get_biens():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM immo_schema.biens;")
    biens = cur.fetchall()
    cur.close()
    conn.close()
    return {"biens": biens}

@app.get("/estimer")
def estimer_bien(surface: int):
    # Prix au m2 moyen pour l'exercice (tu pourras le rendre dynamique plus tard)
    prix_m2 = 4000 
    estimation = surface * prix_m2
    return {"surface": surface, "prix_estime": estimation}