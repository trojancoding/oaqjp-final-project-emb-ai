import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    payload = { "raw_document": { "text": text_to_analyze } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 400:
        return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }

    response_json = json.loads(response.text)

    anger_score = response_json['emotionPredictions'][0]['emotion']['anger']
    disgust_score = response_json['emotionPredictions'][0]['emotion']['disgust']
    fear_score = response_json['emotionPredictions'][0]['emotion']['fear']
    joy_score = response_json['emotionPredictions'][0]['emotion']['joy']
    sadness_score = response_json['emotionPredictions'][0]['emotion']['sadness']

    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(emotions, key=lambda k: emotions[k])

    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    return result