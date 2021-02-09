import pyodbc

# psycopg2 postgresql
# host = '127.0.0.1'
# port = "5432"
# database = "AnotherSnusFactory"
# username = "alex"
# password = "BeTilCat30K!"
# conn = psycopg2.connect(host=host, port=port, dbname=database, user=username, password=password)
# db_cursor = conn.cursor()

# pyodbc azure
server = "asfeaudit.database.windows.net"
database = "asfeaudit"
username = "alexanderfolstad"
password = "BeTilCat30K!"
driver = "{ODBC Driver 17 for SQL Server}"

conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
db_cursor = conn.cursor()


