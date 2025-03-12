import psycopg2
from config import settings

conn = psycopg2.connect(user = settings.databases['default']['user'], password = settings.databases['default']['password'], host = settings.databases['default']['host'], database = settings.databases['default']['name'], port = settings.databases['default']['port'])

cursor = conn.cursor()

#cursor.execute("SELECT * FROM mxmedspasch.appointment_status")
#cursor.execute("SELECT * FROM mxmedspasch.service_product")
#cursor.execute("SELECT * FROM mxmedspasch.service_category")
#cursor.execute("SELECT * FROM mxmedspasch.supplier_service_product")
#cursor.execute("SELECT * FROM mxmedspasch.service_type")
cursor.execute("SELECT sc.name, st.name, sp.name, ssp.name FROM mxmedspasch.service_product AS sp LEFT JOIN mxmedspasch.service_category AS sc ON sp.service_category_id = sc.id LEFT JOIN mxmedspasch.service_type AS st ON st.id = sp.service_type_id LEFT JOIN mxmedspasch.supplier_service_product AS ssp ON ssp.id = sp.supplier_service_pdt_id")

#conn.commit()

rows = cursor.fetchall()

for row in rows:
    print(row)