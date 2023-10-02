import streamlit as st
import pandas as pd
import spacy
from annotated_text import annotated_text
# Load SpaCy model
nlp = spacy.load("en_core_web_sm")


st.title('GBM Journal Abstract Explorer')
st.write('A tool to explore abstracts from the PubMed abstracts for the keyword "Glioblastoma" from 1951-2020.')
# load data 
file_path = 'data/gbm_abstracts.tsv.zip'

@st.cache_data 
def load_data(file_path):
    df = pd.read_csv(file_path, sep='\t', header=None, names=['PubMed ID', 'Abstract'], skiprows=2)
    # remove duplicates from Abstract column
    df.drop_duplicates(subset='Abstract', inplace=True)
    return df

def get_annotated_data(text):
    doc = nlp(text)
    annotated_data = []

    for token in doc:
        annotated_data.append((token.text, token.pos_))
        annotated_data.append(" ")

    return tuple(annotated_data)

raw_data = load_data(file_path)
raw_article_count = len(raw_data)



# show article explorer 
st.success(f'{raw_article_count} unique abstracts available')
st.header('Article Explorer')
st.info('Double click on abstract to view full text')
st.dataframe(raw_data, use_container_width=True)


# sidebar
st.sidebar.header('Search Abstracts')
# add search term
st.sidebar.write(f"Search for a single word (e.g. *'overexpression'*) or multiple words (e.g. *'TMZ-mediated cytotoxicity'*) or even DOI e.g. *'10.1159/000495920'*.")
search_term = st.sidebar.text_input('Search abstract')

def filter_data(raw_data, search_term):
    filtered_data = raw_data[raw_data['Abstract'].str.contains(search_term)]
    return filtered_data

filtered_data = filter_data(raw_data, search_term)

if search_term:
    st.sidebar.subheader('Filter to specific article')
    filtered_abstracts = filtered_data['Abstract'].values.tolist()
    count_filtered_abstracts = len(filtered_abstracts)
    st.sidebar.write(f'{count_filtered_abstracts} abstracts found')
    selected_abstract = st.sidebar.selectbox('Select abstract', filtered_abstracts)

if search_term:
    st.header('Filtered Data')
    st.write(f'{len(filtered_data)} articles found')
    # show abstracts
    st.write(filtered_data)


try: 
    if selected_abstract:
        st.header('Selected Abstract')
        st.write(selected_abstract)
except:
    pass 