import streamlit as st
from utils import categorize_post, calculate_engagement

st.title("Influencer Promo Analyzer")

text = st.text_area("Paste influencer caption or description")

if text:
    category = categorize_post(text)
    st.success(f"Detected Category: {category}")

    likes = st.number_input("Likes", min_value=0)
    views = st.number_input("Views", min_value=0)

    if views > 0:
        engagement = calculate_engagement(likes, views)
        st.metric("Engagement Rate (%)", round(engagement, 2))
