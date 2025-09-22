# CORD-19 Data Explorer

This project is a simple data analysis and visualization application built with Python and Streamlit. Its goal is to explore a subset of the COVID-19 Open Research Dataset (CORD-19)—specifically the `metadata.csv` file—to uncover basic insights about scientific publications related to the pandemic.

Created as an assignment, this project demonstrates core data analysis skills: data loading, cleaning, manipulation, and visualization, all presented through an interactive web application.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [How to Run the Application](#how-to-run-the-application)
- [Key Findings](#key-findings)
- [Reflection](#reflection)

---

## Project Overview

The application processes the CORD-19 `metadata.csv` file and provides an interactive exploration of the research landscape. Users can filter data by publication year using a slider and see real-time updates in the visualizations.

**The application includes:**
- **Data Cleaning and Preparation:** Handles missing values and converts data types as needed.
- **Data Analysis:** Counts papers by year, identifies top journals, and analyzes paper titles.
- **Visualizations:** Interactive charts display publication trends, a list of top journals, and a word cloud of common words in paper titles.

---

## Project Structure

- **`app.py`**: Main Python script containing all code for the Streamlit application, including data loading, cleaning, analysis, and visualization.
- **`metadata.csv`**: Primary dataset used for analysis. _Note: This is a large file and is tracked using Git Large File Storage (LFS)._

---

## How to Run the Application

### 1. Prerequisites

Make sure you have Python 3.7+ installed. Install the required libraries:

```bash
pip install pandas matplotlib seaborn streamlit wordcloud
```

### 2. Download the Dataset

Download `metadata.csv` from the [Kaggle CORD-19 dataset page](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge). Place this file in the same directory as `app.py`.

### 3. Run the App

Navigate to the project directory in your terminal and run:

```bash
streamlit run app.py
```

This will start a local web server and open the application in your browser.

---

## Key Findings

Based on the analysis, here are some key insights from the dataset:

- **Publication Trends:** There was a dramatic spike in COVID-19-related publications in 2020, reflecting the global focus on the pandemic.
- **Top Journals:** Journals like _medRxiv_ and _bioRxiv_ were among the most active publishers, likely due to their pre-print nature, allowing rapid sharing of research.
- **Common Terminology:** The word cloud reveals that terms such as "COVID-19," "SARS-CoV-2," "pandemic," and "risk" are most prevalent in paper titles, aligning with core research topics.

---

## Reflection

The biggest challenge was efficiently handling the large `metadata.csv` file. Loading and processing it required careful attention, and using Git LFS was essential for managing the file on GitHub.

Working with Streamlit offered a great introduction to building interactive data applications. It was surprising how quickly a functional, visually appealing dashboard could be created. The combination of pandas for data manipulation and Streamlit for presentation provides a powerful, accessible toolkit for anyone starting in data science.
