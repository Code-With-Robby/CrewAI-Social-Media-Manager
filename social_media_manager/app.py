# app.py - Render deployment entry point
from flask import Flask, request, render_template_string
from social_media_manager.crew import SocialMediaManager
import os

app = Flask(__name__)

# Simple HTML form (no separate templates folder needed)
INDEX_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>BJJ/MMA DM Generator</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #111; color: #eee; }
        h1 { color: #c8102e; }
        input { padding: 10px; width: 100%; max-width: 400px; margin: 10px 0; }
        button { padding: 12px 20px; background: #c8102e; color: white; border: none; cursor: pointer; }
        pre { background: #222; padding: 15px; border-radius: 8px; white-space: pre-wrap; }
    </style>
</head>
<body>
    <h1>BJJ/MMA Personalized DM Generator</h1>
    <form method="POST">
        <input type="text" name="athlete_name" placeholder="Enter athlete name (e.g. Ilia Topuria)" required>
        <br>
        <button type="submit">Generate DM</button>
    </form>
    {% if result %}
    <h3>Generated DM:</h3>
    <pre>{{ result }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        athlete_name = request.form.get('athlete_name', '').strip()
        if athlete_name:
            inputs = {
                "athlete_name": athlete_name,
                "current_year": "2026"
            }
            try:
                crew_result = SocialMediaManager().crew().kickoff(inputs=inputs)
                result = str(crew_result)
            except Exception as e:
                result = f"Error: {str(e)}"
    return render_template_string(INDEX_HTML, result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
