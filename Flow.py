import streamlit as st
from crewai.flow.flow import Flow,start, listen
from src.project11.agent1_main import outline_writer
from src.project11.agent2_main import writer
from fpdf import FPDF

class ExampleFlow(Flow):

    @start()

    def writer_crew(self, topic):
        st.write("### First Agent is Running...")
        result = outline_writer(topic=topic)
        st.write("**Outline:**",result.raw)
        self.state["outline"] = result.raw

    @listen("writer_crew")   

    def writer_crew_listener(self):
        st.write("### Second Agent is Running...")
        result = writer(data=self.state["outline"])
        st.write("**Final Output:**", result.raw)
        self.state["output"]=result.raw


    



        # Save the output to a PDF file
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, result.raw)
        pdf_filename = "generated_content.pdf"
        pdf.output(pdf_filename)
        
        # Provide a download link
        with open(pdf_filename, "rb") as file:
            st.download_button(label="Download Output as PDF", data=file, file_name=pdf_filename, mime="application/pdf")

# Streamlit UI
col1, col2 = st.columns([1,6])
with col1:
    st.image("https://framerusercontent.com/images/3WJHjDd67EoRo8mYwfdFPmzwLJo.png", width=90)
with col2:
    st.title("AI Book Writer")

# Input field for topic
topic = st.text_input("Enter a topic:", "Artificial Intelligence in 2025")

if st.button("Generate Content"):
    with st.spinner("Processing..."):
        poem_flow = ExampleFlow()
        poem_flow.writer_crew(topic)
        poem_flow.writer_crew_listener()
