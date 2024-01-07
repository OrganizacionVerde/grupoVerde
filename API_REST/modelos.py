from pydantic import BaseModel


class Referencia(BaseModel):
    Nombre: str
    Tipo: str
    Estacion: str
    Eficiencia_energetica: str
    Capacidad_frenado: str
    Ruido_ambiental_dB: int
    Ruido_ambiental_ondas: int
    Dimension: str
