from datetime import datetime
import pytz

bogota_timezone = pytz.timezone('America/Bogota')

# Así obtengo el now de bogotá
bogota_date = datetime.now(bogota_timezone)
print(f"Bogotá: {bogota_date.strftime('%d/%m/%Y, %H:%M:%S')}")

