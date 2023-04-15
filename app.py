import streamlit as st
import openai
from serpapi import GoogleSearch

# Set up your OpenAI API key
openai.api_key = "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"

# Define a function to search images using GoogleSearch API
def search_images(query):
    params = {
        "engine": "google",
        "tbm": "isch",
        "q": query,
        "api_key": "bebb5ff17b2faddf1eec1636ac6dc093d1892da946c28df6a41c3425f09bb4a3"
    }
    search = GoogleSearch(params)
    data = search.get_dict()
    if data.get('search_metadata').get('status') == 'Success':
        results = data.get('images_results')
        if results:
            images = []
            for result in results:
                images.append(result['original'])
            return images[:10]
        else:
            return "No results found."
    else:
        return "Search failed. Please try again later."

# Define a function to generate a response to a given question using OpenAI
def generate_response(question):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None,
    )

    message = response.choices[0].text.strip()
    return message

# Set up the Streamlit app
st.title("Welcome to Tourism AI Chatbot")
st.write("Please enter your tourism related query below:")

# Get user input and generate response
query = st.text_area("Your question here")
if st.button("Get Answer"):
    response = generate_response(query)
    st.write(response)

# Set up the Streamlit app for image search
st.title("Image Search using Google API")
st.write("Please enter your search query below:")

# Get user input and display image results
query = st.text_input("Search images here")
if st.button("Search"):
    images = search_images(query)
    if type(images) == str:
        st.write(images)
    else:
        for image in images:
            st.image(image, use_column_width=True)

