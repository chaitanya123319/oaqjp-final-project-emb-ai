"""Emotion detection using the Watson NLP EmotionPredict service."""

import json

import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    """Analyze the emotions in a piece of text with the Watson NLP library.

    Args:
        text_to_analyze (str): The text whose emotions should be detected.

    Returns:
        dict: Scores for anger, disgust, fear, joy and sadness plus the
        'dominant_emotion' (the emotion with the highest score). When the
        service answers with status code 400 (for example blank input),
        every value in the dictionary is None.
    """
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=payload, headers=HEADERS, timeout=30)

    # Error handling: the service returns 400 for blank / invalid input.
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    dominant_emotion = max(emotions, key=emotions.get)
 # Handle blank input without calling the Watson API.
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
