import streamlit as st
import google.generativeai as genai
import os
import pypdf as pdf
from dotenv import load_dotenv

st.set_page_config(page_title="AI ATS Resume Analyzer",
                   page_icon="🛸", layout="wide")

# CSS file ko alag se padhne ka function


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css("style.css")  # Yahan hum CSS design ko app mein link kar rahe hain


# 1. Tijori se API key nikalna


load_dotenv()
my_api_key = os.getenv("GOOGLE_API_KEY")

# google AI  ko apni API key dena
genai.configure(api_key=my_api_key)


def input_pdf_text(uploaded_file):
    text = ""
    reader = pdf.PdfReader(uploaded_file)
    for page in range(len(reader.pages)):
        page_obj = reader.pages[page]
        text += str(page_obj.extract_text())
    return text


# -----------------------------------------------------
# 3. AI ko Command dena aur Result nikalna
# -----------------------------------------------------
input_prompt = """
Act like a strict and highly experienced ATS (Applicant Tracking System) with a deep understanding of the tech industry. 
Your task is to evaluate the candidate's resume based on the provided Job Description (JD). 
Keep in mind this is typically for entry-level or fresher IT engineering roles, so focus heavily on foundational technical skills, tools, and academic projects, rather than expecting years of professional work experience.

First, strictly calculate an overall ATS Score out of 100 based on how well the resume aligns with the JD requirements. Be realistic and critical.

Output your response strictly in the following structure:
**🏆 ATS Score:** [Your Score Here]/100
**📊 Match Percentage:** [Your Percentage Here]%
**🔍 Missing Keywords:** [List of skills/keywords missing from the resume]
**💡 Profile Summary:** [Provide a brief, constructive summary of the candidate's suitability for this role]
"""


def get_gemini_response(prompt, resume_text, jd_text):
    # Gemini 3.5 Flash use kar rahe hain
    model = genai.GenerativeModel('gemini-3.5-flash')
    combined_input = f"{prompt}\n\nResume Text:\n{resume_text}\n\nJob Description:\n{jd_text}"
    response = model.generate_content(combined_input)
    return response.text


# # 4. UI Design
st.title("AI ATS Resume Analyzer")
st.text("ATS Analyzer")
uploaded_file = st.file_uploader(
    "Apna Resume Upload Karo (PDF format me)", type=["pdf"])
if uploaded_file is not None:
    st.success("Resume uploaded successfully!")

st.write("---")
st.subheader("Job Description:")
jd_text = st.text_area("Apna Job Description Yahan Paste Karo")

# Submit button for Job Description

if st.button("Resume ko JD se Match Karo"):
    if uploaded_file is not None and jd_text != "":
        st.info("Resume aur Job Description ko match kar rahe hain...")
        try:
            # Text nikalna aur AI ko bhejna
            resume_text = input_pdf_text(uploaded_file)
            ai_result = get_gemini_response(input_prompt, resume_text, jd_text)

            # Result dikhana
            st.success("Analysis Complete! 🎯")
            st.write("---")
            st.write(ai_result)
        except Exception as e:
            st.error(f"Kuch gadbad hui: {e}")
    else:
        st.warning(
            "Please dono cheezein dein: Resume upload karein AUR JD paste karein.")

# if uploaded_file is not None:

#     st.success("Resume is uploaded successfully!")

    # if st.button("Resume ka Text Check Karein"):
    #     extracted_text = input_pdf_text(uploaded_file)
    #     st.write("### Pdf ke andar ka text:")
    #     st.write(extracted_text)

    #     st.write("---")
    #     if st.button("AI se Hellow Bulwao"):

    #         model = genai.GenerativeModel("gemini-3.5-flash")
    #         response = model.generate_content(
    #             "Say a short motivating hellow in english to a new software debeloper")

    #         st.info(response.text)


# # 4. AI se pehla sawal (TEST_1)
# st.write("---")
# st.subheader("AI Testing:")

if st.button("AI se ATS check Karo"):
    # Google ke sabse fast model (Gemini 3.5 Flash) ko call karna

    model = genai.GenerativeModel("gemini-3.5-flash")
    response = model.generate_content(
        "Say a short motivating hellow in english to a new software debeloper")

    st.info(response.text)
