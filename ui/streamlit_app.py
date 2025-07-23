import streamlit as st
import numpy as np
from stable_baselines3 import DQN

# Load the trained RL model
try:
    model = DQN.load("rl_agent/model/cyberguard_agent.zip")
except FileNotFoundError:
    st.error("❌ Trained model not found. Please ensure 'cyberguard_agent.zip' exists in 'rl_agent/model/'.")
    st.stop()

# Define possible actions
actions = ["Allow", "Warn", "Block", "Educate"]

st.set_page_config(page_title="CyberGuard", page_icon="🛡️", layout="centered")
st.title("🛡️ CyberGuard: RL-Powered Safety Coach")
st.markdown("""
Welcome to **CyberGuard**, your AI-powered personal cybersecurity assistant. 
This tool uses a reinforcement learning (RL) model to help detect and prevent phishing or scam behaviors.
""")

st.subheader("🔍 Test a Suspicious Link")

# Input URL
test_url = st.text_input("Paste a URL you received (e.g. https://bit.ly/fake-login)", "")

if test_url:
    # Simulated feature extraction (replace with real features in production)
    test_features = {
        "reputation": 0.3,              # Simulated low reputation
        "clicked_similar": True,
        "attachment": False,
        "exe": False,
        "habit_score": 0.5
    }

    # Convert features to array for prediction
    state = np.array([
        test_features["reputation"],
        int(test_features["clicked_similar"]),
        int(test_features["attachment"]),
        int(test_features["exe"]),
        test_features["habit_score"]
    ])

    # Get action from model
    action, _ = model.predict(state)
    result = actions[action]

    # Show result
    st.markdown(f"### 🧠 CyberGuard Suggests: **{result}**")

    # Add interpretation
    if action == 0:
        st.success("✅ This link appears safe based on behavior and reputation.")
    elif action == 1:
        st.warning("⚠️ Caution: This resembles phishing attempts you've seen before.")
    elif action == 2:
        st.error("🛑 Blocked: This is very likely a scam. Do not click.")
    elif action == 3:
        st.info("📘 Educational: Learn why this link could be risky.")

# Optional: Future features like log viewer, real-time API checks, etc.
# st.subheader("📊 Activity Logs")
# st.write("Coming soon...")