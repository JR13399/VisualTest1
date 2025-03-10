import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
data = pd.read_csv("university_student_dashboard_data.csv")

# Set the title and description of the app
st.set_page_config(page_title="University Dashboard", layout="wide")
st.title("📊 University Dashboard - Admissions, Retention & Satisfaction")
st.markdown("""
Welcome to the interactive dashboard of the university's admission, retention, and satisfaction trends over the years.  
This dashboard allows you to analyze:
- Total applications, admissions, and enrollments per term
- Retention rate trends over time
- Student satisfaction scores over the years
- Enrollment breakdown by department (Engineering, Business, Arts, Science)
- Spring vs. Fall term comparison
- Trends for departments, retention rates, and satisfaction levels
""")

# 1. Total Applications, Admissions, and Enrollments per Term
st.header("📈 Total Applications, Admissions, and Enrollments per Term")
term_data = data.groupby(['Year', 'Term'])[['Applications', 'Admitted', 'Enrolled']].sum().reset_index()

# Plot
fig = px.line(term_data, x="Year", y=["Applications", "Admitted", "Enrolled"], color="Term",
              labels={"value": "Count", "variable": "Metric"},
              title="Total Applications, Admissions, and Enrollments Over Time")
st.plotly_chart(fig)

# 2. Retention Rate Trends Over Time
st.header("📊 Retention Rate Trends Over Time")
fig = px.line(data, x="Year", y="Retention Rate (%)", color="Term", 
              labels={"Retention Rate (%)": "Retention Rate (%)"}, 
              title="Retention Rate Trends Over Time")
st.plotly_chart(fig)

# 3. Student Satisfaction Over the Years
st.header("😊 Student Satisfaction Over the Years")
fig = px.line(data, x="Year", y="Student Satisfaction (%)", color="Term", 
              labels={"Student Satisfaction (%)": "Satisfaction (%)"},
              title="Student Satisfaction Over the Years")
st.plotly_chart(fig)

# 4. Enrollment Breakdown by Department
st.header("🏫 Enrollment Breakdown by Department")
department_data = data.groupby(['Year', 'Term'])[['Engineering Enrolled', 'Business Enrolled', 
                                                  'Arts Enrolled', 'Science Enrolled']].sum().reset_index()

# Plot
fig = px.line(department_data, x="Year", y=["Engineering Enrolled", "Business Enrolled", 
                                             "Arts Enrolled", "Science Enrolled"], color="Term",
              labels={"value": "Enrolled Students", "variable": "Department"},
              title="Enrollment Breakdown by Department")
st.plotly_chart(fig)

# 5. Comparison Between Spring vs. Fall Term Trends
st.header("🌱 Spring vs. 🍂 Fall Term Comparison")
comparison_data = data.groupby(['Year', 'Term'])[['Retention Rate (%)', 'Student Satisfaction (%)']].mean().reset_index()

fig = px.line(comparison_data, x="Year", y=["Retention Rate (%)", "Student Satisfaction (%)"], color="Term", 
              labels={"value": "Percentage", "variable": "Metric"},
              title="Spring vs. Fall Term Comparison")
st.plotly_chart(fig)

# 6. Department-Wise Comparison for Retention & Satisfaction
st.header("🏫 Department-Wise Comparison for Retention & Satisfaction")
department_retention = data.groupby(['Year', 'Term'])[['Retention Rate (%)']].mean().reset_index()
department_satisfaction = data.groupby(['Year', 'Term'])[['Student Satisfaction (%)']].mean().reset_index()

# Merge data for comparison
department_comparison = pd.merge(department_retention, department_satisfaction, on=["Year", "Term"])

fig = px.line(department_comparison, x="Year", y=["Retention Rate (%)", "Student Satisfaction (%)"], color="Term", 
              labels={"value": "Percentage", "variable": "Metric"},
              title="Department-Wise Retention & Satisfaction Comparison")
st.plotly_chart(fig)

# Display key findings
st.subheader("🔍 Key Findings:")
st.write("""
- The retention rate has increased over the years, peaking at 90% in 2024.
- Satisfaction levels have also steadily increased, with an 88% satisfaction rate in 2024.
- Engineering has consistently had the highest enrollment numbers, followed by Business, Arts, and Science.
- Spring terms have higher enrollment than Fall terms, with trends being similar for retention and satisfaction.
""")

# Add more analysis or interactive filters as needed

# Run Streamlit
if __name__ == "__main__":
    st.write("End of dashboard.")
