import streamlit as st

def show_email_tab():
    st.title("📧 Email Threat Detector")

    st.markdown("Upload a file or paste raw email content to extract and analyze potentially dangerous emails.")

    # Input method
    option = st.radio("Choose input method", ["Upload File", "Paste Email"])

    if option == "Upload File":
        uploaded_file = st.file_uploader("Upload .txt or .eml email file", type=["txt", "eml"])
        if uploaded_file is not None:
            email_content = uploaded_file.read().decode("utf-8")
    else:
        email_content = st.text_area("Paste email content below")

    if st.button("Analyze Email"):
        if not email_content.strip():
            st.warning("Please provide email content.")
            return

        st.subheader("🔍 Extracted Email Features")
        st.code(email_content[:1000] + "\n\n... (truncated)")

        # Here you can later plug in phishing detection
        st.success("✅ Email processed. No phishing indicators found. (Dummy output)")

