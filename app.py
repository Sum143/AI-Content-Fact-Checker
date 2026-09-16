import streamlit as st
import requests

# --- Paste your n8n webhook URL here ---
N8N_WEBHOOK_URL = "https://suman4429391.app.n8n.cloud/webhook-test/ebb17f76-95f6-41bd-9793-f24753ed8516"

st.title(":mag: AI Content Fact Checker")
st.write("Paste an article or post below. n8n runs the fact-checking workflow and sends back a report.")

text = st.text_area("Enter the article/post text here:", height=250)

if st.button("Check Facts", key="check_btn"):
    if text:
        with st.spinner("Sending to n8n workflow..."):
            try:
                response = requests.post(
                    url=N8N_WEBHOOK_URL,
                    json={"text": text},
                    timeout=60,
                )
            except requests.exceptions.RequestException as e:
                st.error(f"Could not reach the n8n webhook: {e}")
                response = None

        if response is not None:
            if response.status_code == 200:
                data = response.json()

                st.subheader("Summary")
                st.write(data.get("summary", "No summary returned."))

                col1, col2 = st.columns(2)
                col1.metric("Claims checked", data.get("claims_checked", 0))
                col2.metric("Claims flagged", data.get("claims_flagged", 0))

                claims = data.get("claims", [])
                if claims:
                    st.subheader("All Claims")
                    for c in claims:
                        verdict = c.get("verdict", "unknown")
                        icon = {
                            "likely true": "✅",
                            "likely false": "❌",
                            "needs context": "⚠️",
                            "unverifiable": "❔",
                        }.get(verdict, "❔")
                        with st.expander(f"{icon} {c.get('claim', '')}"):
                            st.write(f"**Verdict:** {verdict}")
                            st.write(f"**Confidence:** {c.get('confidence', 'N/A')}")
                            st.write(f"**Reasoning:** {c.get('reasoning', '')}")

                flagged = data.get("flagged_claims", [])
                if flagged:
                    st.subheader("⚠️ Needs Your Attention")
                    for c in flagged:
                        st.warning(f"{c.get('claim', '')} — {c.get('verdict', '')}")
            else:
                st.error(f"n8n returned an error (status {response.status_code}): {response.text}")
    else:
        st.warning("Please enter some text first.")