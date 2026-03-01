"""
Server module for Emotion Detection application.
This file creates the Flask server, exposes the
/emotionDetector route, and deploys the application
on localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flask app
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Receives text input, calls emotion_detector function,
    and formats output as required.
    """
    # Get text from query parameter
    text_to_analyze = request.args.get('textToAnalyze')

    # Call emotion detector function
    response = emotion_detector(text_to_analyze)
    # Handle invalid or blank input case
    if response  is None or response .get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    # Format output exactly as required
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return response_text

@app.route("/")
def render_index_page():
    """
    his function initiates the rendering of the main application
        page over the Flask channel.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
