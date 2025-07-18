import streamlit as st
import numpy as np
import pandas as pd
import joblib 
import toml

# Load your trained model
model = joblib.load('model1.pkl') 
config = toml.load(".streamlit/config.toml")
# Streamlit app
st.title("Salary Prediction App")

# Categorical inputs (example with selectbox, you can adjust options)
qualifications = st.selectbox("Qualifications", options=['M.Tech', 'BCA', 'PhD', 'MBA', 'MCA', 'M.Com', 'BBA', 'B.Tech', 'B.Com', 'BA'])
work_type = st.selectbox("Work Type", options=['Intern', 'Temporary', 'Full-Time', 'Contract', 'Part-Time'])
company_size = st.selectbox("Company size", options=['Small', 'Large', 'Medium'])
job_options = ['Sales, Marketing, and Supply Chain Management',
               'Front-End Developer', 'Operations and Management',
               'Engineering and Technical Development', 'Quality and Analytics',
               'Healthcare, Counseling, and Education', 'Design and Architecture',
               'Financial and Event Planning', 'Testing and Analytical Research',
               'Legal and Corporate Law', 'IT, Sales, and Administrative Support',
               'Support, Security, and Digital Communications']

role_options = ['Social Media & Brand Strategist',
               'Web and Application Development Specialists',
               'Quality Management and Customer Success',
               'Engineering and Technical Development Specialists',
               'Operations & Facilities Management Specialist',
               'Healthcare and Administrative Support Specialist',
               'Design and User Experience Specialist',
               'Event Coordination, Urban Planning, and Demand Forecasting',
               'Software Testing and Automation Specialists',
               'Legal Professionals and Support Staff',
               'Cybersecurity & Network Defense Specialist',
               'Account and Client Relationship Management',
               'Marketing, Brand Management, and Market Research Specialists',
               'Healthcare, Counseling, and Social Support Specialists',
               'Content Creation and Digital Communications',
               'Data, Analytics, and Operations Support',
               'Human Resources, Operations, and Administrative Support',
               'Supply Chain and Procurement Manager',
               'Sales and Sales Management',
               'Tax & Financial Advisory Specialist',
               'Technical Support and Customer Service',
               'Database and Data Integration Developer',
               'Data Science, Analytics, and Research Specialists',
               'Financial and Risk Analyst',
               'Project and Program Management Specialists',
               'Sustainability and Environmental Design',
               'IT Infrastructure, Systems Integration, and Network Administration',
               'SEO and Search Engine Marketing Specialists',
               'Cloud Architecture, Cloud Systems Engineering, and NoSQL Database Management',
               'Medical & Executive Support Professionals']

# Numerical inputs
avg_experience = st.number_input("Average Experience (years)", min_value=0.0, max_value=10.0, value=5.0)
job = st.selectbox("Job Area", options=job_options)
role = st.selectbox("Role cluster", options=role_options)
bonuses = st.checkbox("Bonuses and Incentive Programs")
casual_dress = st.checkbox("Casual Dress Code")
childcare = st.checkbox("Childcare Assistance")
eap = st.checkbox("Employee Assistance Programs (EAP)")
employee_discounts = st.checkbox("Employee Discounts")
employee_recognition = st.checkbox("Employee Recognition Programs")
employee_referral = st.checkbox("Employee Referral Programs")
financial_counseling = st.checkbox("Financial Counseling")
fsas = st.checkbox("Flexible Spending Accounts (FSAs)")
flexible_work = st.checkbox("Flexible Work Arrangements")
health_insurance = st.checkbox("Health Insurance")
wellness_facilities = st.checkbox("Health and Wellness Facilities")
legal_assistance = st.checkbox("Legal Assistance")
life_disability = st.checkbox("Life and Disability Insurance")
pto = st.checkbox("Paid Time Off (PTO)")
parental_leave = st.checkbox("Parental Leave")
professional_dev = st.checkbox("Professional Development")
profit_sharing = st.checkbox("Profit-Sharing")
relocation = st.checkbox("Relocation Assistance")
retirement_plans = st.checkbox("Retirement Plans")
social_recreational = st.checkbox("Social and Recreational Activities")
stock_options = st.checkbox("Stock Options or Equity Grants")
transportation_benefits = st.checkbox("Transportation Benefits")
tuition_reimbursement = st.checkbox("Tuition Reimbursement")
wellness_programs = st.checkbox("Wellness Programs")

jobs = job_options.index(job) 
roles = role_options.index(role)

input_dict = {
    "Qualifications": qualifications,
    "Work Type": work_type,
    "Average_experience": avg_experience,
    "Company size": company_size,
    "Job Area": jobs,    
    "Role cluster": roles,
    "Bonuses and Incentive Programs": int(bonuses),
    "Casual Dress Code": int(casual_dress),
    "Childcare Assistance": int(childcare),
    "Employee Assistance Programs (EAP)": int(eap),
    "Employee Discounts": int(employee_discounts),
    "Employee Recognition Programs": int(employee_recognition),
    "Employee Referral Programs": int(employee_referral),
    "Financial Counseling": int(financial_counseling),
    "Flexible Spending Accounts (FSAs)": int(fsas),
    "Flexible Work Arrangements": int(flexible_work),
    "Health Insurance": int(health_insurance),
    "Health and Wellness Facilities": int(wellness_facilities),
    "Legal Assistance": int(legal_assistance),
    "Life and Disability Insurance": int(life_disability),
    "Paid Time Off (PTO)": int(pto),
    "Parental Leave": int(parental_leave),
    "Professional Development": int(professional_dev),
    "Profit-Sharing": int(profit_sharing),
    "Relocation Assistance": int(relocation),
    "Retirement Plans": int(retirement_plans),
    "Social and Recreational Activities": int(social_recreational),
    "Stock Options or Equity Grants": int(stock_options),
    "Transportation Benefits": int(transportation_benefits),
    "Tuition Reimbursement": int(tuition_reimbursement),
    "Wellness Programs": int(wellness_programs),
}

input_df = pd.DataFrame([input_dict])

if st.button("Predict Salary"):
    
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Salary: {prediction}")