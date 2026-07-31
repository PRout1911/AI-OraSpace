import pandas as pd

from db.conn import get_connection
from db.queries import GET_TABLESPACES_SQL

def load_tablespaces():

    with get_connection() as conn:

        df = pd.read_sql(GET_TABLESPACES_SQL, conn)

    return df["TABLESPACE_NAME"].tolist()