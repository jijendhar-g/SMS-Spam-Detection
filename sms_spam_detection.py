import nltk
nltk.download('punkt')
nltk.download('stopwords')
import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

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

vectorizer = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))

if 'input_sms' not in st.session_state:
    st.session_state.input_sms = ""
if 'prediction_result' not in st.session_state:
    st.session_state.prediction_result = ""

st.set_page_config(page_title="SMS Spam Detection", page_icon="📩", layout="centered")

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

st.markdown("<h1 class='main-heading'>📩 SMS Spam Detection App</h1>", unsafe_allow_html=True)
st.write("**Detect whether an SMS is Spam or Not in just seconds!**")
st.write("---")

st.header("Enter the SMS Below:")

input_sms = st.text_area("💬 Your SMS Message", value=st.session_state.input_sms, placeholder="Type your message here...", height=150)

col1, col2 = st.columns([1, 1])
with col1:
    predict_button = st.button('🔍 Predict')
with col2:
    clear_button = st.button('🧹 Clear')

if predict_button:
    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message to classify!")
    else:
        st.session_state.input_sms = input_sms
        
        transformed_sms = transform_text(input_sms)
        vector_input = vectorizer.transform([transformed_sms])
        result = model.predict(vector_input)[0]

        st.session_state.prediction_result = result

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

if clear_button:
    st.session_state.input_sms = ""
    st.session_state.prediction_result = ""

st.markdown("---")
st.markdown(
    """
    <div class='footer'>
    👨‍💻 Developed by <strong>GJ Technologies </strong><br>
    📚 Powered by Natural Language Processing
    </div>
    """,
    unsafe_allow_html=True,
)
