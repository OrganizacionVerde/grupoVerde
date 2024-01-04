from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hola_mundo():
    return {
            "codigo": 200,
            "message": "Hola Mundo"
            }

# @app.