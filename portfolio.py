import streamlit as st


st.set_page_config(page_title="Student Portfolio", page_icon=":mortar_board:", layout="wide")


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Skills", "Projects", "Education", "Contact"])




if page == "Home":
    st.title("Keerthivarman")
    st.write("**Student | Major in Python**")
    st.write("📍 Coimbatore")

    st.write(
        """
        Welcome to my portfolio! I'm a student at Kgisl Institute Of Technology majoring in Python, passionate about 
        fields like data science, software development, and artificial intelligence. Feel free to explore my 
        skills, projects, education, and ways to get in touch!
        """
    )


elif page == "About Me":
    st.header("About Me")
    st.write(
        """
        I am currently a B.Tech IT student at Kgisl Institute Of Technology. I have a strong interest in Full Stack Development. My goal is to leverage my skills in a professional setting to make an impact 
        and continue growing my knowledge in the field.
        """
    )


elif page == "Skills":
    st.header("Skills")
    st.write("Here are some of the skills I have developed through my studies and projects:")


    st.subheader("Technical Skills")
    st.write("- **Programming Languages:** Python, SQL")
    st.write("- **Tools & Technologies:** Git, Streamlit, Excel")


    st.subheader("Soft Skills")
    st.write("- Teamwork")
    st.write("- Problem-solving")
    st.write("- Time management")

elif page == "Projects":
    st.header("Academic Projects")
    
    st.write("### Project 1: ATM")
    st.write(
        """
        - **Description:** Created a online bank management to create account and manage accounts using text files as a database.
        - **Tools:** Python
        - **Skills Developed:** Logical Thinking
        """
    )
    
    st.write("### Project 2: Personal Portfolio Website")
    st.write(
        """
        - **Description:** Created a personal portfolio website using Streamlit.
        - **Tools:** Streamlit, Python
        - **Skills Developed:** Web development, UI design
        """
    )
    
elif page == "Education":
    st.header("Education")
    st.write("### B.Tech IT")
    st.write("Kgisl Institute Of Technology ")

    st.subheader("Relevant Coursework")
    courses = ["Introduction to Programming", "Data Structures and Algorithms", "Database Systems"]
    for course in courses:
        st.write(f"- {course}")


elif page == "Contact":
    st.header("Contact Information")
    st.write(
        """
        If you'd like to get in touch, feel free to reach out via the channels below:
        """
    )
    st.write("📧 **Email:** keerthivarman010@gmail.com")
    st.write("🔗 **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/keerthi-varman-3000b2315)")