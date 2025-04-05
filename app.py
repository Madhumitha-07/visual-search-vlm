import streamlit as st
from vlm_search import VLMSearch
from PIL import Image

st.title("🔍 Visual Search using VLM (CLIP)")
query = st.text_input("Enter a text query (e.g., 'a beach with palm trees'):")

if 'vlm' not in st.session_state:
    st.session_state.vlm = VLMSearch()
    with st.spinner("Encoding dataset..."):
        st.session_state.vlm.encode_images()

if query:
    with st.spinner("Searching..."):
        results = st.session_state.vlm.search(query, top_k=5)
    st.success("Top results:")
    for path in results:
        st.image(Image.open(path), caption=path, use_column_width=True)
