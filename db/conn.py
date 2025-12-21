import oracledb
import os

def get_connection():
    
    return oracledb.connect(
        user=os.getenv("ORA_USER", "system"),
        password=os.getenv("ORA_PWD", "oracle"),
        dsn=os.getenv("ORA_DSN", "localhost/XEPDB1")
    )
