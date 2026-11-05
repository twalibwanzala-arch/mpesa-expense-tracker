"""Streamlit dashboard for the M-Pesa Expense Tracker.

Run it with:  streamlit run app.py
"""

import pandas as pd
import streamlit as st

from categorizer import categorize_all
from parser import parse_message

# --- Page setup -----------------------------------------------------------
st.set_page_config(page_title="M-Pesa Expense Tracker", page_icon="💸")
st.title("💸 M-Pesa Expense Tracker")
st.write("Upload a text file of M-Pesa messages (one per line) to see where your money goes.")
st.caption("Privacy: your file is processed in this session only. The demo uses fake data.")

# --- Load the messages ----------------------------------------------------
uploaded = st.file_uploader("Upload your messages (.txt)", type="txt")

if uploaded is not None:
    text = uploaded.getvalue().decode("utf-8")
else:
    st.info("No file uploaded, so you're seeing the fake sample data.")
    with open("sample_messages.txt", encoding="utf-8") as f:
        text = f.read()

# --- Parse and categorize -------------------------------------------------
parsed = [parse_message(line) for line in text.splitlines() if line.strip()]
transactions = categorize_all([t for t in parsed if t is not None])

if not transactions:
    st.warning("No M-Pesa transactions were found in that file.")
    st.stop()

df = pd.DataFrame(transactions)

# --- Summary numbers ------------------------------------------------------
income = df.loc[df["category"] == "Income", "amount"].sum()
spending = df.loc[df["category"] != "Income", "amount"].sum()

col1, col2 = st.columns(2)
col1.metric("Money in", f"Ksh {income:,.2f}")
col2.metric("Money out", f"Ksh {spending:,.2f}")

# --- Chart: spending by category -----------------------------------------
st.subheader("Spending by category")
by_category = (
    df[df["category"] != "Income"]
    .groupby("category")["amount"]
    .sum()
    .sort_values(ascending=False)
)
st.bar_chart(by_category)

# --- Table of all transactions -------------------------------------------
st.subheader("All transactions")
st.dataframe(df[["date", "time", "type", "party", "category", "amount"]])
