import streamlit as st

# Page Configuration
st.set_page_config(page_title="Nishant Kumar | PhD Student", layout="centered")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About", "Academics", "Publications", "Projects", "Contact"])

# --- About Page ---
if page == "About":
    st.title("About Me")
    st.image("profile.jpeg", width=200)
    st.markdown("""
    👋 Hi! I'm **Nishant Kumar**, a PhD student in Civil Engineering at the University of Nebraska-Lincoln.  
    I work on **Rain-on-Snow**, **Non-Stationarity**, **Machine Learning in Hydrology**, **Droughts**, and **Land Surface Modeling** using **NASA-LIS** and **LIS/WRF-Hydro**.
    """)
    with open("Nishant-Kumar-Phd.pdf", "rb") as file:
        st.download_button("📄 Download CV", file, file_name="Nishant-Kumar-CV.pdf", mime="application/pdf")

# --- Academics Page ---
elif page == "Academics":
    st.title("Academics")
    st.markdown("""
    - 🎓 **Ph.D.** in Civil Engineering — *University of Nebraska-Lincoln, USA* (2022–2026)  
      Advisor: Prof. Tirthankar Roy  
    - 🎓 **M.Tech** in Civil Engineering — *Indian Institute of Science, India* (2020–2022)  
      Advisor: Prof. D. Nagesh Kumar  
    - 🎓 **B.E.** in Civil Engineering — *Jadavpur University, India* (2016–2020)
    """)

# --- Publications Page ---
elif page == "Publications":
    st.title("Publications")
    st.markdown("""
    - **A Machine Learning-based Probabilistic Approach for Irrigation Scheduling**  
      *Water Resources Management (2024)*
      
    - **Trends and Causal Structures of Rain-on-Snow Flooding**  
      *Journal of Hydrology (under review)*

    - **Spatiotemporal Analysis and Modeling of Non-Stationarity in Hydrological Time Series**  
      *EGU General Assembly, 2023*

    👉 More on [Google Scholar](https://scholar.google.com)
    """)

# --- Projects Page ---
elif page == "Projects":
    st.title("Current Project")
    st.markdown("""
    ### NASA-funded Project  
    **Enhancing the Hydrological Drought Monitoring Capability of the US Drought Monitor**  
    - Applying machine learning and remote sensing techniques to improve national drought resilience.
    - Collaborating with interdisciplinary teams on land surface modeling and data assimilation.
    """)

    st.markdown("#### GitHub")
    st.markdown("[nadriano (GitHub)](https://github.com/nadriano)")

# --- Contact Page ---
elif page == "Contact":
    st.title("Contact Me")
    st.markdown("""
    - 📧 Email: [nkumar4@huskers.unl.edu](mailto:nkumar4@huskers.unl.edu)  
    - 💼 GitHub: [github.com/nadriano](https://github.com/nadriano)  
    - 🔗 LinkedIn: [linkedin.com/in/nishant-kumar-2414601b8](https://www.linkedin.com/in/nishant-kumar-2414601b8)  
    - 📍 Lincoln, NE, USA  
    - ☎️ +1 402-301-5028
    """)

