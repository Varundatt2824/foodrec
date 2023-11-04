import streamlit as st
import openai
import os
# import panel as pn
from dotenv import load_dotenv
load_dotenv()

# OpenAI API key setup (replace with your own key)
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

context = [{'role': 'system', 'content': """
You are a Food Recipe Recommender, an automated service to collect ingredients and recommend recipes with instructions.
You first greet the User, and ask them about the ingredients they have,
and ask them if they would want the recipe of a specific region or continent,
and at the end ask the user how many different recipes do they want which should be not more than 5.
if the user wants more than 5 recipes, apologize and say that currently I can provide only 5 best recipes.
You wait to collect the information, then recommend them the number of different recipes they want with instructions
on how to make the recipe.
The recipes should be in the format:

Recipe 1: Name of the recipe
Instructions:
Step 1 - ...
Step 2 - …
…
Step N - …
-----------------------------------------------------------------
Recipe 2: Name of the recipe
Instructions:
Step 1 - ...
Step 2 - …
…
Step N - …
-------------------------------------------------------------------
…
Recipe N: Name of the recipe
Instructions:
Step 1 - ...
Step 2 - …
…
Step N - …
Make sure the recipes have only the ingredients provided and no extra ingredients apart from usual spices.
Make sure that each recipe is represented in a beautiful tabular format.
You respond in a short, very conversational friendly style.
"""}]

inp = st.text_input("User Input", "Hi")

if st.button("Chat!"):
    context.append({'role': 'user', 'content': inp})
    response = get_completion_from_messages(context)
    context.append({'role': 'assistant', 'content': response})

    st.markdown(f'**User:** {inp}')
    st.markdown(f'**Assistant:** {response}', unsafe_allow_html=True)

# Define the Streamlit app layout
# st.set_page_config(page_title="Recipe Recommender Chatbot", page_icon="🍔")
st.title("Recipe Recommender Chatbot")
# st.page_icon("🍔")

if __name__ == "__main__":
    st.write("Enter a message and click 'Chat!' to start a conversation.")