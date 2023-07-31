import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from flask import Flask, request, render_template
ps = PorterStemmer()

# Initialize the Flask app
app = Flask(__name__)

# Load the model and tf-idf vectorizer
tfidf = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

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

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['text']
    transformed_text = transform_text(input_text)
    vector_input = tfidf.transform([transformed_text])
    result = model.predict(vector_input)[0]
    prediction_result = "Spam" if result == 1 else "Not Spam"
    return render_template('index.html', result=prediction_result)


if __name__ == '__main__':
    app.run(debug=True)
