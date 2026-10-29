"""
SESSION 6 - Task 1: Simple PDF Chatbot & Text Extractor using PyPDF2 & Streamlit
Upload a PDF (e.g. IRCTC ticket, college timetable) and extract/search text in the browser.
"""

import streamlit as st
import PyPDF2
import io

st.set_page_config(page_title="PDF Chatbot & Reader", page_icon="📄")
st.title("📄 PDF Text Extractor & Assistant")
st.write("Upload any PDF document (e.g., College Timetable, IRCTC Ticket, Syllabus) to extract and view its text.")

uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    extracted_text = ""
    for page_idx, page in enumerate(reader.pages):
        page_text = page.extract_text()
        if page_text:
            extracted_text += f"\n--- Page {page_idx + 1} ---\n" + page_text
    return extracted_text

if uploaded_file is not None:
    with st.spinner("Extracting text with PyPDF2..."):
        try:
            pdf_text = extract_text_from_pdf(uploaded_file)
            st.success(f"Successfully extracted text from '{uploaded_file.name}'!")
            
            # Display Extracted Text
            st.subheader("📑 Extracted Text Content:")
            st.text_area("Full Document Text", pdf_text, height=350)
            
            # Simple interactive query / keyword finder
            st.subheader("🔍 Quick Search inside Document:")
            query = st.text_input("Ask a question or enter keyword (e.g., 'Seat', 'Room', 'Date', 'Time'):")
            if query:
                matches = [line.strip() for line in pdf_text.splitlines() if query.lower() in line.lower()]
                if matches:
                    st.write(f"**Found {len(matches)} relevant line(s):**")
                    for m in matches[:5]:
                        st.info(f"👉 {m}")
                else:
                    st.warning(f"No mentions of '{query}' found in this document.")
        except Exception as e:
            st.error(f"Failed to process PDF: {e}")

