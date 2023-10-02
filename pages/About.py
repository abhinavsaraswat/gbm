import streamlit as st
st.title('GBM Journal Abstract Explorer')

info_text = """
The dataset is from https://www.kaggle.com/datasets/rtwillett/glioblastoma-journal-abstracts which is published under CC0: Public Domain license.

**Context**
Glioblastoma is one of the most insidious and pernicious human cancers with a very poor prognosis. Thought to arise from an astrocyte cell of origin, glioblastoma (also known as glioblastoma multiforme or GBM) is an extremely rapidly growing brain tumor with few treatment options.

**Acknowledgements**
These are abstracts of journal publications in the field of glioblastoma research from the last 70 years. These represent the fruits of the efforts of thousands of researchers throughout the decades and are collected here for easy reference by others.

"""
st.write(info_text)