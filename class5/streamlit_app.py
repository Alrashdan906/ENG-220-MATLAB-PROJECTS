# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(page_title="Dataset Visualizer", page_icon="📊", layout="wide")

# Title of the app
st.title("Dataset Visualizer")

# Upload the dataset
st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the dataset
    df = pd.read_csv(uploaded_file)

    # Show the dataset
    st.subheader("Dataset Preview")
    st.write(df.head())  # Display the first few rows of the dataset

    # Show dataset statistics
    st.subheader("Dataset Statistics")
    st.write(df.describe())

    # Select columns for plotting
    st.sidebar.header("Visualization Settings")
    plot_type = st.sidebar.selectbox("Choose Plot Type", ["Line Chart", "Bar Chart", "Scatter Plot"])

    # Select columns for x and y axes
    x_col = st.sidebar.selectbox("Select X-axis column", df.columns)
    y_col = st.sidebar.selectbox("Select Y-axis column", df.columns)

    # Plotting
    st.subheader(f"{plot_type} of {y_col} vs {x_col}")

    if plot_type == "Line Chart":
        fig, ax = plt.subplots()
        sns.lineplot(data=df, x=x_col, y=y_col, ax=ax)
        st.pyplot(fig)

    elif plot_type == "Bar Chart":
        fig, ax = plt.subplots()
        sns.barplot(data=df, x=x_col, y=y_col, ax=ax)
        st.pyplot(fig)

    elif plot_type == "Scatter Plot":
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
        st.pyplot(fig)
else:
    st.info("Please upload a CSV file to visualize.")

# Add footer
st.sidebar.markdown("## About")
st.sidebar.info("This is a simple dataset visualization app built with Streamlit. Upload a CSV file to get started!")