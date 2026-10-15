from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>News Detection Using NLP</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial;
            background: #eef2f7;
            margin: 30px auto;
            padding: 20px;
            max-width: 650px;
        }
        .card {
            background: white;
            padding: 25px;
            border-radius: 12px;
        }
        textarea {
            width: 100%;
            height: 120px;
            box-sizing: border-box;
            padding: 10px;
        }
        button {
            padding: 12px 20px;
            background: #155eef;
            color: white;
            border: 0;
            border-radius: 6px;
        }
    </style>
</head>
<body>
<div class="card">
    <h1>News Detection Using NLP</h1>
    <p>Enter news text for a basic keyword-based check.</p>
    <form method="POST">
        <textarea name="news" required
          placeholder="Paste news text here..."></textarea>
        <p><button type="submit">Analyze News</button></p>
    </form>
    {% if result %}
        <h3>Analysis Result</h3>
        <p>{{ result }}</p>
        <small>This demo is not a reliable fake-news detector.</small>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        news = request.form.get("news", "").strip().lower()
        if news:
            suspicious_words = [
                "shocking", "secret cure",
                "you won't believe", "miracle",
                "100% guaranteed"
            ]
            if any(word in news for word in suspicious_words):
                result = (
                    "Suspicious wording detected. "
                    "Please verify with trusted sources."
                )
            else:
                result = (
                    "No listed suspicious phrases found. "
                    "This does not prove the news is true."
                )
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)