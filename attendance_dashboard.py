# streamlit/attendance_dashboard.py
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Attendance Dashboard", layout="wide")
st.title("📊 Student Attendance Dashboard")

uploaded = st.file_uploader("Upload students CSV", type=["csv"])
if uploaded is not None:
    df = pd.read_csv(uploaded)
else:
    df = pd.read_csv("../data/students.csv")

required = {"StudentID","Name","TotalClasses","ClassesAttended"}
if not required.issubset(df.columns):
    st.error("CSV is missing required columns: StudentID, Name, TotalClasses, ClassesAttended")
else:
    df["Attendance%"] = round((df["ClassesAttended"]/df["TotalClasses"])*100,2)
    df["Category"] = pd.cut(df["Attendance%"], bins=[-1,40,75,100],
                            labels=["Low (<40%)","Medium (40-75%)","High (>75%)"])
    st.subheader("Attendance Table")
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Bar chart")
        fig, ax = plt.subplots(figsize=(8,4))
        ax.bar(df["Name"], df["Attendance%"])
        ax.set_ylim(0,100)
        st.pyplot(fig)
    with col2:
        st.subheader("Category distribution")
        counts = df["Category"].value_counts().reindex(["Low (<40%)","Medium (40-75%)","High (>75%)"]).fillna(0)
        fig2, ax2 = plt.subplots(figsize=(5,5))
        ax2.pie(counts, labels=counts.index, autopct="%1.1f%%", startangle=90)
        ax2.axis("equal")
        st.pyplot(fig2)

    st.markdown("---")
    st.subheader("Quick Insights")
    low = df[df["Category"]=="Low (<40%)"].shape[0]
    med = df[df["Category"]=="Medium (40-75%)"].shape[0]
    high = df[df["Category"]=="High (>75%)"].shape[0]
    st.write(f"Low: {low}, Medium: {med}, High: {high}")
