# Sentiment & Emotion Analysis Web App

A Django web application that performs sentiment analysis and emotion detection on text reviews using TextBlob and Text2Emotion libraries.

![image](https://github.com/user-attachments/assets/84a26c7d-fe9f-4d31-b7e9-c6238e1437ca)

## Features

- Real-time sentiment analysis (Positive, Negative, Neutral)
- Detailed emotion detection (Happy, Sad, Angry, Fear, Surprise)
- User-friendly interface with example reviews
- Responsive design using Tailwind CSS
- Visual feedback with color-coded results

![image](https://github.com/user-attachments/assets/2bce83e3-2098-4c1a-9984-e8313d69e323)


## Technologies Used

- Python 3.x
- Django 5.1.4
- TextBlob 0.17.1
- Text2Emotion 0.0.5
- Tailwind CSS (via CDN)
- NLTK

## Installation

1. Clone the repository:

```sh
git clone https://github.com/HasanAbdelhady/Sentiment-Analysis-And-Emotions-Detection.git
cd sentiment_analysis
```

2. Create and activate a virtual environment:

On Windows:
```sh
python -m venv venv
venv\Scripts\activate
```
On Mac & Linux:
```sh
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages:

```sh
pip install -r requirements.txt
```

4. Run migrations:

```sh
python manage.py migrate
```

5. Start the development server:

```sh
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

1. Open the application in your web browser
2. Enter your text review in the textarea or use one of the example reviews
3. Click "Analyze" to get sentiment and emotion analysis results
4. View the color-coded sentiment result and emotion breakdown

## Project Structure

```
sentiment_analysis/
├── manage.py
├── requirements.txt
├── reviews/
│   ├── templates/
│   │   └── reviews/
│   │       └── classify_review.html
│   ├── views.py
│   ├── urls.py
│   └── models.py
└── sentiment_analysis/
    ├── settings.py
    └── urls.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

# **Live Demo**: https://1sentimentanalysis990.pythonanywhere.com/
