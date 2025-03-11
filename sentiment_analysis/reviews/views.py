from django.shortcuts import render
import nltk
import os
import text2emotion as te
from textblob import TextBlob
import logging

# Setting up logging
logger = logging.getLogger(__name__)

# Set NLTK data path to use the virtual environment's nltk_data
nltk_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'venv/nltk_data')
nltk.data.path.append(nltk_data_path)

def get_sentiment(polarity):
    """
    Classify sentiment based on polarity.
    """
    if polarity > 0:
        return 'Positive', 'text-green-500 font-bold'
    elif polarity < 0:
        return 'Negative', 'text-red-500 font-bold'
    else:
        return 'Neutral', 'text-yellow-500 font-bold'

def get_emotions(review_text):
    """
    Use text2emotion to extract emotions from the review.
    """
    emotions = te.get_emotion(review_text)
    # Filter emotions to only show the ones with a score greater than 0, and sort by score
    filtered_emotions = {emotion: score for emotion, score in emotions.items() if score > 0}
    sorted_emotions = dict(sorted(filtered_emotions.items(), key=lambda item: item[1], reverse=True))
    # Capitalize the emotion names
    return {emotion.capitalize(): score for emotion, score in sorted_emotions.items()}

def classify_review(request):
    sentiment = None
    sentiment_class = ''
    emotions = {}
    error_message = None
    review_text = None

    if request.method == 'POST':
        review_text = request.POST.get('review_text', '').strip()

        # Handle empty review text
        if not review_text:
            error_message = 'Review text cannot be empty.'
        else:
            try:
                # Sentiment Analysis using TextBlob
                blob = TextBlob(review_text)
                polarity = blob.sentiment.polarity
                sentiment, sentiment_class = get_sentiment(polarity)

                # Emotion Detection using text2emotion
                emotions = get_emotions(review_text)

            except Exception as e:
                error_message = f"An error occurred while processing the review: {str(e)}"
                logger.error(f"Error processing review: {str(e)}")

    return render(request, 'reviews/classify_review.html', {
        'sentiment': sentiment,
        'sentiment_class': sentiment_class,
        'emotions': emotions,
        'error_message': error_message,
        'review_text': review_text  # Pass review_text to template
    })
