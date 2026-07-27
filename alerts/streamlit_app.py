import streamlit as st
import pandas as pd

from db.conn import get_connection
from db.queries import TABLESPACE_USAGE_SQL, DATAFILE_SQL
from db.parser import comm_parse
from alerts.alert import tablespace_alerts

st.set_page_config(page_title="AI-Oraspace", layout="wide")
st.title("AI-OraSpace - Oracle DBA Command Console")

command = st.text_input(
    "Enter Command", 
    placeholder = "check ts | check files USERS | add df"
)

if st.button("Run"):
    parsed = comm_parse(command)

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

                    if not warn.empty:
                        st.error("Tablespaces crossing threshold ⚠️")
                        st.dataframe(warn)

                if parsed["action"] == "DATAFILES":
                    df = pd.read_sql(DATAFILE_SQL, conn, params={"tbls": parsed["tablespace"]}
                    )
                    st.subheader(f"📁 Datafiles for {parsed['tablespace']}")
                    st.dataframe(df)

        if parsed["type"] == "DDL_PREVIEW":
            st.warning("DDL execution disabled (Preview mode) ⚠️")
            st.code(parsed["sql"], language= "sql")