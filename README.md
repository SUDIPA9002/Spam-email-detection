# Spam Email Detection

This is a GitHub repository for a spam email detection project. The project aims to detect whether an email is spam or not using machine learning techniques. The code is implemented in Python and uses popular libraries like NumPy, Pandas, NLTK, Matplotlib, Seaborn, and Scikit-learn.

## Data
The dataset used in this project is loaded from a CSV file named "Spam Email Detection - spam.csv". The dataset contains email messages labeled as spam (Type 1) or not spam (Type 0).

## Contents
The repository is organized into the following sections:

### 1. Data Cleaning
In this section, the data is cleaned to prepare it for analysis and modeling. The following steps are performed:
- Dropping unnecessary columns from the dataset.
- Encoding the target variable.
- Checking for missing values and duplicates and handling them.

### 2. Exploratory Data Analysis (EDA)
EDA is performed to gain insights into the data. The following visualizations are created:
- Pie chart to show the distribution of spam and non-spam emails.
- Histograms and pair plots to analyze the distribution of character count, word count, and sentence count in both spam and non-spam emails.

### 3. Text Preprocessing
In this section, the text data in the emails is preprocessed before feeding it into the machine learning models. The following steps are performed:
- Converting the text to lowercase.
- Tokenizing the sentences.
- Removing special characters, stopwords, and punctuation.
- Applying stemming to reduce words to their root form.

### 4. Model Building
Two different approaches are used for feature extraction: CountVectorizer and TfidfVectorizer. Then, the following machine learning models are trained and evaluated on the dataset using the two feature extraction methods:
- Gaussian Naive Bayes
- Multinomial Naive Bayes
- Bernoulli Naive Bayes
- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree
- K-Nearest Neighbors (KNN)
- Random Forest
- AdaBoost
- Bagging
- Extra Trees
- Gradient Boosting
- XGBoost

### 5. Model Evaluation
The accuracy and precision scores of each model are calculated and compared to select the best performing model.

### 6. Model Improvement
In this section, an attempt is made to improve the model's performance by:
- Changing the max_feature parameter of TfidfVectorizer.
- Including additional features like character count in the dataset.

## Deployment
The final selected model is saved using the `pickle` library and deployed through a Flask web application. The user can input an email text, and the web application will predict whether the email is spam or not.

## How to Use
To run the code and Flask web application, follow these steps:
1. Clone the repository to your local machine.
2. Install the required Python libraries mentioned in the code.
3. Run the Jupyter notebook or Python script to train the models and save the selected model and TfidfVectorizer.
4. Run the Flask application and access it through your web browser.

Please note that this README provides a summary of the project. For detailed information and code execution, refer to the respective notebooks and scripts in the repository.
If you want to know more about this you can go through this -
https://medium.com/@sudipakoner492/building-a-spam-email-detection-model-a-step-by-step-guide-aa44e7ff9b21
