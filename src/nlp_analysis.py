import re
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

def clean_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#', '', text)
    text = text.lower()
    return text

def analyze_sentiment(comments, model_name):
    sentiment_analyzer = pipeline('sentiment-analysis', model=model_name)
    comments['cleaned_comment'] = comments['comment'].apply(clean_text)
    comments['sentiment'] = comments['cleaned_comment'].apply(
        lambda x: sentiment_analyzer(x[:512])[0]['label'] if x else 'NEUTRAL'
    )
    comments['sentiment_score'] = comments['cleaned_comment'].apply(
        lambda x: sentiment_analyzer(x[:512])[0]['score'] if x else 0.5
    )
    return comments

def extract_keywords(comments, max_features):
    tfidf = TfidfVectorizer(max_features=max_features, stop_words='english')
    tfidf_matrix = tfidf.fit_transform(comments['cleaned_comment'])
    return tfidf.get_feature_names_out()
