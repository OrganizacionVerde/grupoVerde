import entrada
import salida
from time import sleep
import schedule

schedule.every(3).seconds.do(entrada.main)

schedule.every(5).seconds.do(salida.main)

while True:
    schedule.run_pending()
    sleep(1)