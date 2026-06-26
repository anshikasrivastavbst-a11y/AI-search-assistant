import streamlit as st
from dotenv import load_dotenv
import os
import time

from agents.search_agent import search_web
from agents.report_agent import build_web_content
from agents.research_agent import generate_research_report
from agents.image_agent import search_images
from utils.pdf_utils import create_pdf

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Safety check
if not TAVILY_API_KEY or not GEMINI_API_KEY:
    st.error("API keys missing! Check your .env file")
    st.stop()

# -----------------------------
# Streamlit Config
# -----------------------------
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔍",
    layout="wide"
)

# -----------------------------
# Session State
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("📚 Research History")

    st.divider()

    st.subheader("⚙️ Research Options")

    report_length = st.radio(
        "Report Length",
        ["Short", "Medium", "Detailed"],
        index=1
    )

    st.divider()

    if len(st.session_state.history) == 0:
        st.info("No searches yet")

    for item in reversed(st.session_state.history):
        st.write("•", item)

    st.divider()

    if st.button("🗑 Clear History"):
        st.session_state.history = []
        st.rerun()

# -----------------------------
# MAIN UI
# -----------------------------
st.title("🔍 AI Research Assistant")

st.markdown("""
### AI-powered research system:

- 🌐 Web Search (Tavily)
- 🧠 AI Analysis (Gemini)
- 📄 Structured Report
- 📥 PDF Download
""")

topic = st.text_input("Enter a research topic")

# -----------------------------
# PIPELINE
# -----------------------------
def run_pipeline(topic, tavily_key, gemini_key):

    search_results = search_web(topic, tavily_key)

    if not search_results or "results" not in search_results:
        return {}, "", "No search results found."

    web_content = build_web_content(search_results)

    if not web_content:
        web_content = "No web content generated."

    report = generate_research_report(
        topic,
        web_content,
        gemini_key,
        report_length
    )

    if not report:
        report = "No report generated."

    return search_results, web_content, report

# -----------------------------
# BUTTON ACTION
# -----------------------------
if st.button("🚀 Research"):

    if not topic.strip():
        st.warning("Please enter a topic")
        st.stop()

    if topic not in st.session_state.history:
        st.session_state.history.append(topic)

    start_time = time.time()
    with st.spinner("🌐 Collecting web intelligence..."):


        search_results, web_content, report = run_pipeline(
            topic,
            TAVILY_API_KEY,
            GEMINI_API_KEY
        )

        # -----------------------------
        # Fetch Related Images
        # -----------------------------
        image_results = search_images(
            topic,
            TAVILY_API_KEY
        ) 

        end_time = time.time()
        generation_time = round(end_time - start_time, 2)

        st.success("Research Complete ✅")
        st.info(f"⏱️ Report generated in {generation_time} seconds")
    # -----------------------------
    # REPORT OUTPUT (FIXED - NO STREAMING ISSUES)
    # -----------------------------

    st.subheader("📊 Research Statistics")

    st.write(f"📚 Sources Used: {len(search_results)}")
    st.write(f"📝 Report Words: {len(report.split())}")
    st.write(f"⏱️ Generation Time: {generation_time} sec")

    st.divider()

    st.subheader("📄 Research Report")

    st.markdown(report)

    # -----------------------------
    # PDF
    # -----------------------------
    try:
        pdf_file = create_pdf(report)

        with open(pdf_file, "rb") as file:
            st.download_button(
                label="📥 Download PDF Report",
                data=file,
                file_name="research_report.pdf",
                mime="application/pdf"
            )
    except Exception as e:
        st.error(f"PDF Error: {e}")

    # -----------------------------
    # SOURCES
    # -----------------------------
    st.divider()
    st.subheader("🔗 Sources")

    if search_results and "results" in search_results:
        for result in search_results["results"]:
            st.markdown(f"- [{result['title']}]({result['url']})")
    else:
        st.warning("No sources available")