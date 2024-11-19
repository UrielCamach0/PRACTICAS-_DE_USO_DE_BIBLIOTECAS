import datetime

#obtener fecha y hora actuales 
ahora=datetime.datetime.now()
print("fecha y hora actuales: ", ahora)

#obtener solo la fecha
fecha=ahora.date()
print("Fecha actual: ",fecha)

#obtener solo la hora
hora=ahora.time()
print("Hora actual: ", hora)

#crear dos fechas
fecha1=datetime.datetime(2024, 10, 20)
fecha2=datetime.datetime(2023, 10, 20)

#calcular la diferencia
diferencia= fecha1-fecha2
print("Diferencia entre fechas: ", diferencia.days, "dias")