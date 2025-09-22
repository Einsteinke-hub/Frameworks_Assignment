CORD-19 Data Explorer
This project is a simple data analysis and visualization application built with Python and Streamlit. The goal is to explore a subset of the COVID-19 Open Research Dataset (CORD-19), specifically the metadata.csv file, to uncover basic insights about scientific publications related to the pandemic.

This project was created as an assignment to demonstrate fundamental data analysis skills, including data loading, cleaning, manipulation, and visualization, all presented through an interactive web application.

Table of Contents
Project Overview

Project Structure

How to Run the Application

Key Findings

Reflection

Project Overview
The application processes the CORD-19 metadata.csv file to provide a quick look at the research landscape. Users can interact with a slider to filter the data by publication year and see real-time updates to the visualizations.

The application includes:

Data Cleaning and Preparation: Handling missing values and converting data types.

Data Analysis: Counting papers by year, identifying top journals, and analyzing paper titles.

Visualizations: Interactive charts showing publication trends, a list of top journals, and a word cloud of common title words.

Project Structure
app.py: The main Python script that contains all the code for the Streamlit application, including data loading, cleaning, analysis, and visualization.

metadata.csv: The primary dataset file used for the analysis. Note: This is a large file and is tracked using Git Large File Storage (LFS).

How to Run the Application
1. Prerequisites
Ensure you have Python 3.7+ installed. You also need the required libraries.

pip install pandas matplotlib seaborn streamlit wordcloud

2. Download the Dataset
The metadata.csv file is required to run the application. You can download it directly from the Kaggle CORD-19 dataset page. Place this file in the same directory as the app.py script.

3. Run the App
Navigate to the project directory in your terminal and run the following command:

streamlit run app.py

This will start a local web server and open the application in your browser.

Key Findings
Based on the analysis, here are some of the key insights from the dataset:

Publication Trends: There was a significant spike in COVID-19-related publications in the year 2020, reflecting the global focus on the pandemic.

Top Journals: Journals like medRxiv and bioRxiv were among the most active publishers, likely due to their role as pre-print servers, which allows for rapid sharing of research.

Common Terminology: The word cloud reveals that terms such as "COVID-19," "SARS-CoV-2," "pandemic," and "risk" are most prevalent in paper titles, which aligns with the core topics of the research.

Reflection
The biggest challenge in this project was handling the large metadata.csv file. Loading and processing it efficiently required a careful approach, and using Git LFS was essential for managing the project on GitHub.

Working with Streamlit was a great introduction to building interactive data applications. It was surprising how quickly a functional and visually appealing dashboard could be created with a few lines of code. The combination of pandas for data manipulation and Streamlit for presentation provides a powerful and accessible toolkit for anyone starting in data science.
