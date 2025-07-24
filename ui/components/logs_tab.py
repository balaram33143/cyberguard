# ui/components/logs_tab.py

import streamlit as st
import pandas as pd
import os

def load_logs():
    log_path = "data/user_logs.csv"
    if os.path.exists(log_path):
        return pd.read_csv(log_path)
    else:
        return pd.DataFrame(columns=["Timestamp", "Action", "URL", "ThreatScore"])

def show_logs_tab():
    st.title("📜 Activity Logs")

    logs_df = load_logs()
    if logs_df.empty:
        st.info("No logs found.")
    else:
        st.dataframe(logs_df, use_container_width=True)
