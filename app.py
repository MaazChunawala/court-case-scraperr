import streamlit as st
from scrapers.high_court import fetch_high_court_case
from scrapers.district_court import fetch_district_court_case
from services.database import init_db, save_query, get_all_queries
from services.pdf_generator import generate_pdf

# --- Load custom CSS ---
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Initialize Database ---
init_db()

# --- Streamlit Layout ---
st.title("⚖️ Court Case Lookup & Cause List Checker")
st.markdown("Enter case details below to fetch case status & judgments.")

# Input Form
with st.form("case_form"):
    court_type = st.selectbox("Court Type", ["High Court", "District Court"])
    case_type = st.text_input("Case Type", placeholder="e.g. WP")
    case_number = st.text_input("Case Number", placeholder="e.g. 1234")
    case_year = st.text_input("Year", placeholder="e.g. 2023")
    submit = st.form_submit_button("🔍 Search Case")

if submit:
    if not case_type or not case_number or not case_year:
        st.error("Please fill all fields!")
    else:
        with st.spinner("Fetching case details..."):
            if court_type == "High Court":
                result = fetch_high_court_case(case_type, case_number, case_year)
            else:
                result = fetch_district_court_case(case_type, case_number, case_year)

            if result:
                save_query(court_type, case_type, case_number, case_year, result)
                st.success("✅ Case details fetched successfully!")

                st.subheader("📄 Case Details")
                st.json(result)

                if st.button("📥 Download as PDF"):
                    pdf_path = generate_pdf(result)
                    st.download_button("Download PDF", data=open(pdf_path, "rb"), file_name="case_details.pdf")
            else:
                st.warning("No data found for the given details.")

st.markdown("---")
st.subheader("📜 Search History")
queries = get_all_queries()
if queries:
    for q in queries:
        st.markdown(f"- **{q['court_type']}** | {q['case_type']} {q['case_number']}/{q['case_year']}")
else:
    st.info("No previous searches yet.")