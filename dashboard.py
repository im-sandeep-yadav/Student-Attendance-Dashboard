# src/dashboard.py
import os
import pandas as pd
import matplotlib.pyplot as plt

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PATH = os.path.join(BASE, "data", "students.csv")
OUT_DIR = os.path.join(BASE, "output")
IMG_DIR = os.path.join(OUT_DIR, "images")
os.makedirs(IMG_DIR, exist_ok=True)

def load_data(path=DATA_PATH):
    df = pd.read_csv(path)
    return df

def process(df):
    df["Attendance%"] = round((df["ClassesAttended"] / df["TotalClasses"]) * 100, 2)
    df["Category"] = pd.cut(df["Attendance%"], bins=[-1, 40, 75, 100],
                            labels=["Low (<40%)", "Medium (40-75%)", "High (>75%)"])
    return df

def save_processed(df):
    out_csv = os.path.join(OUT_DIR, "processed_students.csv")
    os.makedirs(OUT_DIR, exist_ok=True)
    df.to_csv(out_csv, index=False)
    print("Saved processed CSV:", out_csv)
    return out_csv

def plot_bar(df):
    fig_path = os.path.join(IMG_DIR, "bar_chart.png")
    plt.figure(figsize=(8,4))
    plt.bar(df["Name"], df["Attendance%"])
    plt.ylim(0,100)
    plt.title("Attendance % per Student")
    plt.xlabel("Student")
    plt.ylabel("Attendance %")
    plt.tight_layout()
    plt.savefig(fig_path)
    plt.close()
    print("Saved bar chart:", fig_path)
    return fig_path

def plot_pie(df):
    fig_path = os.path.join(IMG_DIR, "pie_chart.png")
    counts = df["Category"].value_counts().reindex(["Low (<40%)","Medium (40-75%)","High (>75%)"]).fillna(0)
    plt.figure(figsize=(6,6))
    plt.pie(counts, labels=counts.index, autopct="%1.1f%%", startangle=90)
    plt.title("Attendance Category Distribution")
    plt.tight_layout()
    plt.savefig(fig_path)
    plt.close()
    print("Saved pie chart:", fig_path)
    return fig_path

def generate_insights(df):
    total = len(df)
    low = df[df["Category"]=="Low (<40%)"].shape[0]
    med = df[df["Category"]=="Medium (40-75%)"].shape[0]
    high = df[df["Category"]=="High (>75%)"].shape[0]
    top = df.sort_values("Attendance%", ascending=False).head(3)
    ins_text = f"Total students: {total}\nLow: {low}\nMedium: {med}\nHigh: {high}\nTop performers:\n{top[['StudentID','Name','Attendance%']].to_string(index=False)}"
    print("\n=== INSIGHTS ===\n", ins_text)
    out_path = os.path.join(OUT_DIR, "insights.txt")
    with open(out_path, "w") as f:
        f.write(ins_text)
    print("Saved insights:", out_path)
    return ins_text

def main():
    df = load_data()
    df = process(df)
    save_processed(df)
    plot_bar(df)
    plot_pie(df)
    generate_insights(df)
    print("\nAll outputs are in the 'output' folder (processed CSV, images, insights.txt)")

if __name__ == "__main__":
    main()
