# ui/components/threats_tab.py

import streamlit as st
import json
import os

def show_threats_tab():
    st.title("🚨 Detected Threats")

    threats_path = "data/phishing_urls.json"
    if os.path.exists(threats_path):
        with open(threats_path, "r") as f:
            data = json.load(f)

        if data:
            for i, threat in enumerate(data):
                with st.expander(f"🔗 {threat['url']}"):
                    st.write(f"**Detected On:** {threat['timestamp']}")
                    st.write(f"**Threat Score:** {threat['score']}")
                    st.write(f"**Explained:** {threat.get('explanation', 'No explanation available.')}")
        else:
            st.info("No threats recorded yet.")
    else:
        st.warning("Threats data not found.")
