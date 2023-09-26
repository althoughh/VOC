import streamlit as st
import pandas as pd

# Read CSV files from URLs
industry_url = 'https://github.com/althoughh/VOC/blob/main/industry.csv'
individual_url = 'https://github.com/althoughh/VOC/blob/main/individual.csv'
jobs_url = 'https://github.com/althoughh/VOC/blob/main/jobs.csv'

industry_df = pd.read_csv(industry_url)
individual_df = pd.read_csv(individual_url)
jobs_df = pd.read_csv(jobs_url)

# Streamlit app starts here
st.title("Industry Information Dashboard")

# Filters
st.sidebar.title("Filters")

selected_industry = st.sidebar.multiselect("Select Industry", industry_df['Industry Name'].unique())
selected_role = st.sidebar.multiselect("Select Role", individual_df['Role Name'].unique())
selected_job = st.sidebar.multiselect("Select Jobs to be Done", jobs_df['Job Name'].unique())

# Button to confirm selection and show tables
if st.sidebar.button('Show Data'):
    
    # Filter and display tables only if filters are selected
    if selected_industry or selected_role or selected_job:
        st.header("Filtered Data")

        if selected_industry:
            st.subheader("Industry")
            st.write(industry_df[industry_df['Industry Name'].isin(selected_industry)].drop(columns=['Industry ID']))

        if selected_role:
            st.subheader("Individual")
            filtered_individual_df = individual_df[individual_df['Role Name'].isin(selected_role)]
            st.write(filtered_individual_df.drop(columns=['Individual ID', 'Industry ID']))

        if selected_job:
            st.subheader("Jobs to be Done")
            filtered_jobs_df = jobs_df[jobs_df['Job Name'].isin(selected_job)]
            st.write(filtered_jobs_df.drop(columns=['Job ID', 'Industry ID', 'Individual ID']))

    else:
        st.write("No filters selected. Please choose options from the sidebar.")
