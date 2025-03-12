import psycopg2
from config import settings

conn = psycopg2.connect(user = settings.databases['default']['user'], password = settings.databases['default']['password'], host = settings.databases['default']['host'], database = settings.databases['default']['name'], port = settings.databases['default']['port'])

cursor = conn.cursor()

cursor.execute("SELECT * FROM mxmedspasch.appointment_status")

#conn.commit()

rows = cursor.fetchall()

for row in rows:
    print(row)