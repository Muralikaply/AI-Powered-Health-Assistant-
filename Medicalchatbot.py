import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nltk.download('punkt')
nltk.download('stopwords')


# Load a pre-trained Hugging Face model
chatbot = pipeline("text-generation", model="distilgpt2")



def healthcare_chatbot(user_input):
    # Simple rule-based keywords to respond
    if "symptom" in user_input:
        return "It looks like you're experiencing certain symptoms. To ensure accurate advice and proper care, it's best to consult a qualified doctor. A medical professional can provide a precise diagnosis and the right treatment for your condition. Don’t rely solely on assumptions—seek expert guidance for your health and well-being."
    elif "appointment" in user_input:
        return "Would you like me to arrange a doctor's appointment for you? Consulting a medical professional ensures you receive accurate advice and proper treatment. It's important to address health concerns with expert guidance rather than assumptions. Let me know if you'd like assistance in scheduling an appointment for you."
    elif "medication" in user_input:
        return "Taking your prescribed medications regularly is essential for effective treatment and recovery. Skipping doses or stopping early may affect your health. If you have any concerns about your medication, side effects, or dosage, consult your doctor immediately. A medical professional can provide the best guidance for your well-being."
    elif "headache" in user_input:
        return "Headaches can often be relieved through simple remedies. Staying hydrated is crucial, as dehydration can trigger headaches. Resting in a quiet, dark room helps reduce discomfort, especially for migraines. Applying a cold or warm compress can provide relief by numbing pain or relaxing tense muscles. Managing stress through deep breathing, meditation, or gentle massages can prevent tension headaches. Limiting screen time reduces eye strain, a common trigger. Over-the-counter pain relievers may help, but avoid overuse. Maintaining a healthy sleep schedule is essential for prevention. If headaches persist or worsen, consulting a doctor ensures proper diagnosis and treatment."
    elif "fever" in user_input: 
        return "Fever is the body's natural response to infections and can often be managed at home. Staying hydrated is essential, as fever can cause dehydration. Resting in a cool, comfortable environment helps the body recover faster. Wearing light clothing and using a damp cloth on the forehead can provide relief. Drinking warm fluids like herbal tea or soup soothes the body. Over-the-counter medications like paracetamol or ibuprofen can reduce fever if needed. A lukewarm sponge bath may also help. However, if the fever persists, is very high, or comes with severe symptoms, consult a doctor for proper diagnosis and treatment."
    else:
      
        response = chatbot(user_input, max_length=300, num_return_sequences=1)
       
        return response[0]['generated_text']


# Streamlit web app interface
def main():
    st.title("Medical Healthcare Assistant Chatbot")
    

    user_input = st.text_input("How can I help you Today ?", "")

    
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
           
            with st.spinner("Processing please wait..."):
                response = healthcare_chatbot(user_input)
            print("response ",response)
            print("=======================================================")
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Enter your query.")
if __name__ == "__main__":
    main()
