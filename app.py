import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import re

# Set a consistent style for plots
plt.style.use('seaborn-v0_8-whitegrid')

# Configure Streamlit page layout
st.set_page_config(
    page_title="CORD-19 Data Explorer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("CORD-19 Data Explorer 🔬")
st.markdown("### Simple exploration of COVID-19 research papers")

# --- Data Loading and Caching ---
# Use st.cache_data to load the data once and cache it for performance
@st.cache_data
def load_and_clean_data(file_path):
    """
    Loads, cleans, and prepares the CORD-19 metadata.csv file.
    Returns a cleaned pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path)

        # 1. Data Cleaning
        # Drop rows with missing titles or abstracts as they are crucial for this analysis
        cleaned_df = df.dropna(subset=['title', 'abstract'])

        # 2. Data Preparation
        # Convert publish_time to datetime and extract the year
        cleaned_df['publish_time'] = pd.to_datetime(cleaned_df['publish_time'], errors='coerce')
        cleaned_df['publication_year'] = cleaned_df['publish_time'].dt.year

        # Drop rows where year could not be parsed
        cleaned_df.dropna(subset=['publication_year'], inplace=True)
        cleaned_df['publication_year'] = cleaned_df['publication_year'].astype(int)

        # Create a new column for abstract word count
        cleaned_df['abstract_word_count'] = cleaned_df['abstract'].apply(lambda x: len(str(x).split()))

        # Clean up journal names (basic)
        cleaned_df['journal'] = cleaned_df['journal'].str.lower().str.strip()
        cleaned_df['journal'].fillna('Unknown', inplace=True)

        return cleaned_df

    except FileNotFoundError:
        st.error(f"Error: The file '{file_path}' was not found.")
        st.stop()
    except Exception as e:
        st.error(f"An error occurred during data loading: {e}")
        st.stop()

# --- Main Application Logic ---
# Load the data with caching
file_path = 'metadata.csv'
data = load_and_clean_data(file_path)

# Add an expandable section for data info
with st.expander("ℹ️ Data Overview"):
    st.write(f"The dataset contains **{data.shape[0]:,}** cleaned research papers across **{data.shape[1]}** columns.")
    st.dataframe(data.head())
    
# --- Interactive Widgets (Sidebar) ---
st.sidebar.header("Explore the Data")

# Publication year slider
min_year = int(data['publication_year'].min())
max_year = int(data['publication_year'].max())
selected_year_range = st.sidebar.slider(
    "Select Publication Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Filter the data based on user selection
filtered_data = data[
    (data['publication_year'] >= selected_year_range[0]) &
    (data['publication_year'] <= selected_year_range[1])
]

# Check if filtered data is empty
if filtered_data.empty:
    st.warning("No data available for the selected year range. Please adjust the slider.")
else:
    # --- Visualization Section ---
    st.markdown("---")
    st.header("Key Findings & Visualizations")
    st.info(f"Analysis based on **{len(filtered_data):,}** papers from **{selected_year_range[0]}** to **{selected_year_range[1]}**.")

    # 1. Publications Over Time
    st.subheader("1. Publications Over Time 📈")
    fig, ax = plt.subplots(figsize=(10, 6))
    papers_by_year = filtered_data.groupby('publication_year').size()
    papers_by_year.plot(kind='bar', ax=ax, color=sns.color_palette("rocket")[0])
    ax.set_title('Number of Publications Per Year')
    ax.set_xlabel('Publication Year')
    ax.set_ylabel('Number of Papers')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # 2. Top Journals
    st.subheader("2. Top 10 Publishing Journals 📰")
    top_journals = filtered_data['journal'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax, palette='viridis')
    ax.set_title('Top 10 Publishing Journals')
    ax.set_xlabel('Number of Papers')
    ax.set_ylabel('Journal Name')
    st.pyplot(fig)

    # 3. Word Cloud of Titles
    st.subheader("3. Word Cloud of Paper Titles ☁️")
    all_titles = ' '.join(filtered_data['title'].dropna().tolist())
    
    # Simple function to clean text for the word cloud
    def clean_text(text):
        # Remove common stopwords and numbers
        stopwords = set(['a', 'an', 'the', 'and', 'or', 'in', 'of', 'for', 'to', 'from', 'with', 'on', 'is', 'are', 'was', 'were', 'as'])
        text = text.lower()
        text = re.sub(r'[^a-z\s]', '', text) # Keep only letters and spaces
        words = text.split()
        return ' '.join([word for word in words if word not in stopwords and len(word) > 2])

    cleaned_titles = clean_text(all_titles)

    if cleaned_titles:
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(cleaned_titles)
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)
    else:
        st.warning("Not enough text data to generate a word cloud for the selected filters.")

    # 4. Abstract Word Count Distribution
    st.subheader("4. Abstract Word Count Distribution 📊")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(filtered_data['abstract_word_count'], bins=50, kde=True, ax=ax, color='purple')
    ax.set_title('Distribution of Abstract Word Counts')
    ax.set_xlabel('Abstract Word Count')
    ax.set_ylabel('Number of Papers')
    st.pyplot(fig)

    st.markdown("---")
    st.markdown("Created with ❤️ using Python, pandas, and Streamlit.")