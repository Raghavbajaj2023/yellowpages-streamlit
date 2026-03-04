import streamlit as st
import subprocess

st.title("YellowPages Lead Scraper")

st.write("Click the button to start scraping leads")

if st.button("Start Scraping"):
    subprocess.run(["python", "yellowpages_scrapper.py"])
    st.success("Scraping finished! Check CSV file.")
