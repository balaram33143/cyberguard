# ui/components/performance_tab.py

import streamlit as st
import os
import json

def show_performance_tab():
    st.title("📈 RL Agent Performance")

    log_file = "data/reward_logs.json"

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            reward_logs = json.load(f)

        if reward_logs:
            rewards = [entry["reward"] for entry in reward_logs]
            episodes = [entry["episode"] for entry in reward_logs]

            st.line_chart({
                "Episode": episodes,
                "Reward": rewards
            })

        else:
            st.info("No performance data yet.")
    else:
        st.warning("Reward logs not found.")
