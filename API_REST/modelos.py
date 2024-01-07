from pydantic import BaseModel
from datetime import datetime

class Referencia(BaseModel):
    Nombre: str
    Tipo: str
    Estacion: str
    Eficiencia_energetica: str
    Capacidad_frenado: str
    Ruido_ambiental_dB: int
    Ruido_ambiental_ondas: int
    Dimension: str

class Lote(Referencia):
    ID_lote: int
    Cantidad_neumaticos: int
    fecha_entrada: datetime
    fecha_salida: datetime = None
    Nombre: str
    Tipo: str
    Estacion: str
    Eficiencia_energetica: str
    Capacidad_frenado: str
    Ruido_ambiental_dB: int
    Ruido_ambiental_ondas: int
    Dimension: str
