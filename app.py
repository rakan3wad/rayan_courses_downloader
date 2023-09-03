from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def extract_first_url(code):
    url_pattern = r"https:\/\/vod-progressive\.akamaized\.net\/exp=[^~]+~acl=[^~]+~hmac=[^\/]+\/[^\s\"]+\.mp4"
    matches = re.findall(url_pattern, code)

    if matches:
        return matches[0]
    else:
        return "URL not found"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code_input = request.json['code_input']
        extracted_url = extract_first_url(code_input)
        return jsonify({'url': extracted_url})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
