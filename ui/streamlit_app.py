import streamlit as st
from ui.components.home_tab import show_home_tab
from ui.components.logs_tab import show_logs_tab
from ui.components.threats_tab import show_threats_tab
from ui.components.performance_tab import show_performance_tab
from ui.components.email_tab import show_email_tab  # <-- ✅ Add this line

# Apply custom styles
with open("ui/assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🔐 CyberGuard Dashboard")
page = st.sidebar.radio("Navigate", ["Home", "Logs", "Threats", "Performance", "Email"])  # <-- ✅ Add "Email"

# Display corresponding tab
if page == "Home":
    show_home_tab()
elif page == "Logs":
    show_logs_tab()
elif page == "Threats":
    show_threats_tab()
elif page == "Performance":
    show_performance_tab()
elif page == "Email":  # <-- ✅ Add this block
    show_email_tab()


        🔍 Features: