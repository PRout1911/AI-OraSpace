import streamlit as st
import pandas as pd

from db.oracle_conn import get_connection
from db.sql_queries import TABLESPACE_USAGE_SQL, DATAFILE_SQL
from db.command_parsar import parsar_command
from db.utils_alerts import tablespace_alerts

st.set_page_config(page_title="AI-Oraspace", layout="wide")
st.title("AI-OraSpace – Oracle DBA Command Console")

command = st.text_input(
    "Enter Command", 
    placeholder = "check ts | check files USERS | add df"
)

if st.button("Run"):
    parsed = comm_parse(comm)

    if not parsed:
        st.error("Unknown command ❌")

    else:
        if parsed["type"] == "QUERY":
            with get_connection() as conn:
                if parsed["action"] == "TABLESPACE":
                    df = pd.read_sql(TABLESPACE_USAGE_SQL, conn)

                    st.subheader("Tablespace Usage 📊")
                    st.dataframe(df)

                    warn, crit = tablespace_alerts(df)

                    if not crit.empty:
                        st.error("Critical tablespaces detected 🚨")
                        st.dataframe(crit)