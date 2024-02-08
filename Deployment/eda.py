import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MultipleLocator

def run():
    st.title("Flight Passenger Satisfaction Prediction")

    st.subheader("Analysis Data for Flight Passenger")

    st.write("This page made by Dicky Gabriel")
    st.markdown("---")

    df = pd.read_csv("Fligh_satification.csv")
    st.dataframe(df)
    df.columns = df.columns.str.lower()

    st.write("## Passenger Satisfaction")
    sns.set_style("whitegrid")
    fig_pie, ax_pie = plt.subplots(figsize=(6, 6))
    ax_pie.pie(df.satisfaction.value_counts(), labels=["Neutral or dissatisfied", "Satisfied"], autopct='%1.1f%%')
    ax_pie.set_title('Perbandingan kolom satisfied dan neutral or disastified')
    st.pyplot(fig_pie)

    st.write("## Age Histogram")
    fig_hist, ax_hist = plt.subplots(figsize=(20, 20))
    ax_hist.minorticks_on()
    ax_hist.xaxis.set_minor_locator(MultipleLocator(5))
    ax_hist.yaxis.set_minor_locator(MultipleLocator(100))
    ax_hist.set_title('Ages Histogram', size=20, fontweight='bold', y=1.04)

    sns.histplot(x='age', data=df, edgecolor='black', kde=True, line_kws={'lw': 1, 'linestyle': '--'}, ax=ax_hist)

    ax_hist.set_xlabel('Age', size=15)
    ax_hist.set_ylabel('Count', size=15)
    st.pyplot(fig_hist)

    st.write("## Scatterplot of age and satisfaction")
    fig_scatter, ax_scatter = plt.subplots(figsize=(20, 20))
    ax_scatter.minorticks_on()
    ax_scatter.xaxis.set_minor_locator(MultipleLocator(5))
    ax_scatter.yaxis.set_minor_locator(MultipleLocator(100))
    ax_scatter.set_title('Ages Histogram with Satisfaction', size=20, fontweight='bold', y=1.04)

    sns.histplot(x='age', data=df, edgecolor='black', hue="satisfaction", kde=True,
                 line_kws={'lw': 1, 'linestyle': '--'}, ax=ax_scatter)

    ax_scatter.set_xlabel('Age', size=15)
    ax_scatter.set_ylabel('Count', size=15)
    st.pyplot(fig_scatter)

    st.write("## plane type")
    fig_plane_type = plt.figure(figsize=(10, 5), dpi=200)

    ax_plane_type = sns.countplot(x='type of travel', hue='satisfaction', data=df)
    ax_plane_type.set_title('type of travel', size=15)
    ax_plane_type.legend(fontsize='10')
    plt.xlabel('')
    plt.ylabel('Count', size=15)

    st.write("## plane type")
    fig_plane_type = plt.figure(figsize=(10, 5), dpi=200)

    ax_plane_type = sns.countplot(x='type of travel', hue='satisfaction', data=df)
    ax_plane_type.set_title('type of travel', size=15)
    ax_plane_type.legend(fontsize='10')
    plt.xlabel('')
    plt.ylabel('Count', size=15)


    for p in ax_plane_type.patches:
        ax_plane_type.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                                ha='center', va='center', fontsize=8, color='black', xytext=(0, 5),
                                textcoords='offset points')

    st.pyplot(fig_plane_type)

    st.write("## Class type")
    fig_class_type = plt.figure(figsize=(10,5),dpi=200)

    ax=sns.countplot(x='class',hue='satisfaction',data=df)
    ax.set_title('class',size=15)
    ax.legend(fontsize='10')
    plt.xlabel('')
    plt.ylabel('Count',size=15)

    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=8, color='black', xytext=(0, 5),
                    textcoords='offset points')
        
    plt.show()

    st.pyplot(fig_class_type)

if __name__ == "__main__":
    run()
