import nltk
import streamlit as st
import pickle 
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Initialize Porter Stemmer
ps = PorterStemmer()

# Preprocessing function
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load pre-trained vectorizer and model
vectorizer = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))

# Streamlit App Interface
st.set_page_config(page_title="SMS Spam Detection", page_icon="📩", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .spam-result {
        background-color: #ffcccc;
        color: black;
        font-size: 24px;
        text-align: center;
        padding: 20px;
        border-radius: 8px;
    }
    .not-spam-result {
        background-color: #ccffcc;
        color: black;
        font-size: 24px;
        text-align: center;
        padding: 20px;
        border-radius: 8px;
    }
    .main-heading {
        color: #4CAF50;
        text-align: center;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: gray;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Section
st.markdown("<h1 class='main-heading'>📩 SMS Spam Detection App</h1>", unsafe_allow_html=True)
st.write("**Detect whether an SMS is Spam or Not in just seconds!**")
st.write("---")

# Input Section
st.header("Enter the SMS Below:")
input_sms = st.text_area("💬 Your SMS Message", placeholder="Type your message here...", height=150)

if st.button('🔍 Predict'):
    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message to classify!")
    else:
        # 1. Preprocess
        transformed_sms = transform_text(input_sms)
        # 2. Vectorize
        vector_input = vectorizer.transform([transformed_sms])
        # 3. Predict
        result = model.predict(vector_input)[0]

        # 4. Display Result
        st.write("---")
        if result == 1:
            st.markdown(
                "<div class='spam-result'>🚨 This message is classified as <strong>Spam</strong>!</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<div class='not-spam-result'>✅ This message is classified as <strong>Not Spam</strong>!</div>",
                unsafe_allow_html=True,
            )

# Footer Section
st.markdown("---")
st.markdown(
    """
    <div class='footer'>
    👨‍💻 Developed by <strong>Edunet Foundation</strong><br>
    📚 Powered by Natural Language Processing
    </div>
    """,
    unsafe_allow_html=True,
)
