
import streamlit as st
import pandas as pd
import collections

# The URL of the raw data file on GitHub
url = "https://raw.githubusercontent.com/althoughh/VOC/main/data.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(url)


def main():
    st.title("Product Analysis Dashboard")

    st.header("Choose a question to answer")

    question_option = st.selectbox(
        "",
        (
            "Most common phrases for Users with a [sentiment] experience when talking about [category]",
            "Most common [categories] amongst [industry]",
            "Most common phrases for people with a [score] rating",
            "For [product/slug], [sentiment] reviews contained the following phrases",
            "Negative reviews common phrases of [product/slug] compared to [product/slug]",
            "For [product/slug] the following categories were most prominent when the experience was [sentiment]"
        ),
    )

    if question_option == "Most common phrases for Users with a [sentiment] experience when talking about [category]":
        sentiment_option = st.selectbox("Choose sentiment", df['sentiment'].unique())
        category_option = st.selectbox("Choose category", df['category'].unique())
        # Perform your analysis here based on the selected sentiment and category

    elif question_option == "Most common [categories] amongst [industry]":
        industry_option = st.selectbox("Choose industry", df['industry'].unique())
        # Perform your analysis here based on the selected industry

    elif question_option == "Most common phrases for people with a [score] rating":
        score_option = st.selectbox("Choose score", df['score'].unique())
        # Perform your analysis here based on the selected score
        filtered_df = df[df['score'] == score_option]
        common_phrases = collections.Counter(" ".join(filtered_df["review_processed"]).split()).most_common(5)
        st.write("Most common phrases:", common_phrases)

    # Add other questions and their corresponding dropdowns and analysis
    
    st.write("Your selected options will be used for analysis here.")

if __name__ == "__main__":
    main()
