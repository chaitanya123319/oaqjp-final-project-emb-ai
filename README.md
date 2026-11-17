# Final project

Emotion Detector: a Flask web application built on the Watson NLP library that
analyses a statement and reports scores for **anger, disgust, fear, joy and
sadness**, plus the **dominant emotion**.

## Project layout

```
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py            # makes EmotionDetection a package
│   └── emotion_detection.py   # emotion_detector() using Watson NLP
├── static/mywebscript.js      # front-end script
├── templates/index.html       # web interface
├── server.py                  # Flask deployment
├── test_emotion_detection.py  # unit tests
└── requirements.txt
```

## Run the application

```bash
pip install -r requirements.txt
python3 server.py            # then open http://localhost:5000
```

## Use the function directly

```python
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> emotion_detector("I love this new technology.")
```

## Run the unit tests

```bash
python3 -m unittest test_emotion_detection.py
```

## Static code analysis

```bash
pylint server.py
```

## Error handling

Blank or invalid input makes the Watson service respond with status code 400.
`emotion_detector` then returns `None` for every value and the web app shows
**"Invalid text! Please try again!"**.

> The Watson endpoint (`sn-watson-emotion.labs.skills.network`) is reachable
> from inside the IBM Skills Network Cloud IDE lab environment.
