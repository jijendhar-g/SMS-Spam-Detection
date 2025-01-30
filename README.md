# SMS-Spam-Detection
The SMS Spam Detection project is a machine learning application designed to classify SMS messages as either spam or not spam. Using a dataset of labeled SMS messages, the project leverages various machine learning algorithms to build a model capable of identifying spam messages with high accuracy.
This project implements an SMS spam detection system using machine learning techniques. The model classifies SMS messages as either spam or not spam. Built using Python, the model is deployed as a web application using Streamlit.
________________________________________
Technologies Used
•	Python
•	Scikit-learn
•	Pandas
•	NumPy
•	Streamlit
________________________________________
Features
•	SMS Data Collection
•	Data Preprocessing and Cleaning
•	Exploratory Data Analysis (EDA)
•	Model Training and Selection
•	Web Deployment via Streamlit
________________________________________
Data Collection
The dataset used for training this model is the SMS Spam Collection dataset, available from Kaggle. This dataset contains over 5,500 labeled SMS messages (spam and not spam).
________________________________________
Data Preprocessing
The dataset underwent several preprocessing steps to prepare it for machine learning:
•	Removed any null or duplicate values.
•	Label encoded the target variable: spam messages as 1 and non-spam messages as 0.
•	Text was tokenized, stop words and punctuations were removed.
•	Stemming was applied to reduce words to their base form.
•	All text was converted to lowercase for consistency.
________________________________________
Exploratory Data Analysis (EDA)
Exploratory data analysis was conducted to better understand the dataset and identify patterns:
•	Counted the number of characters, words, and sentences in each message.
•	Investigated correlations between variables using visualizations (e.g., bar charts, pie charts, heatmaps).
•	Generated word clouds to visualize the most frequent words in both spam and non-spam messages.
________________________________________
Model Building and Evaluation
Several classification models were evaluated for spam detection:
•	Naive Bayes
•	Random Forest
•	K-Nearest Neighbors (KNN)
•	Decision Tree
•	Logistic Regression
•	Extra Trees Classifier
•	Support Vector Machine (SVC)
The Naive Bayes classifier performed the best, achieving 100% precision.
________________________________________
Web Deployment
The trained model is deployed as a web application using Streamlit, allowing users to interact with the model directly:
•	Input box: Users can input an SMS message.
•	Classification result: The model predicts whether the message is spam or not spam.
You can try out the live demo here.
________________________________________
How to Use
To run the SMS Spam Detection app on your local machine, follow these steps:
1.	Clone the repository:
bash
Copy
git clone  https://github.com/jijendhar-g/SMS-Spam-Detection
2.	Install required dependencies:
bash
Copy
pip install -r requirements.txt
3.	Run the Streamlit app:
bash
Copy
streamlit run app.py
4.	Open your browser and go to localhost:8501 to access the app.
________________________________________
Contributions
Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or create a pull request.
________________________________________
License
This project is open-source and available under the MIT License.

