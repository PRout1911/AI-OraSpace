import streamlit as st
import pandas as pd

from db.oracle_conn import get_connection
from db.sql_queries import TABLESPACE_USAGE_SQL, DATAFILE_SQL
from db.command_parsar import parsar_command
from db.utils_alerts import tablespace_alerts

st.set_page_config(page_title="AI-Oraspace", layout="wide")