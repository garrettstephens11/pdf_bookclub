import os
import openai
import fitz
import re
import nltk
from flask import Flask, render_template, request, session, jsonify
import logging

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')

openai.organization = os.getenv('OPENAI_ORG_ID')
openai.api_key = os.getenv('OPENAI_API_KEY')

logging.basicConfig(level=logging.INFO)

def clean_text(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = re.sub(r' \.', '.', cleaned_text)
    cleaned_text = re.sub(r' ,', ',', cleaned_text)
    cleaned_text = re.sub(r' !', '!', cleaned_text)
    cleaned_text = re.sub(r' \?', '?', cleaned_text)
    cleaned_text = re.sub(r' ;', ';', cleaned_text)
    cleaned_text = re.sub(r' :', ':', cleaned_text)
    return cleaned_text

def extract_pdf_text(pdf_data):
    doc = fitz.open(stream=pdf_data, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    sentences = nltk.sent_tokenize(text)
    paragraphs = [' '.join(sentences[i:i+5]) for i in range(0, len(sentences), 5)]
    text = '\n\n'.join(paragraphs)
    text = text.replace(' .', '.')
    return clean_text(text)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pdf_data = request.files['pdf_file'].read()
        text = extract_pdf_text(pdf_data)
        tokens = nltk.word_tokenize(text)
        segments = [' '.join(tokens[i:i+2000]) for i in range(0, len(tokens), 2000)]
        segments = [clean_text(segment) for segment in segments]
        enumerated_segments = list(enumerate(segments))
        return render_template('result.html', segments=enumerated_segments, discussions=session.get('discussions'))
    session.pop('discussions', None)
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    index = request.form.get('index')
    segment = request.form.get('segment')
    relation_text = request.form.get('relation_text')
    
    prompt = """
    Can you generate for me a short book club discussion between three people about the following section of a book: {}.
    The discussion should be formatted as follows:
    Person A: [Person A's comment]
    Person B: [Person B's comment]
    Person C: [Person C's comment]
    This discussion should involve at least two "turns" per discussion participant in this discussion. The discussion should address the book club question: 'What is a random word or phrase that stood out to you in reading this text? What does that word or phrase bring to mind for you? Then, relate your thought back to the passage's message.'
    """.format(segment)
    
    if relation_text:
        prompt += " Next, have the group participants relate the reading to {}.".format(relation_text)

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    
    discussion = response.choices[0].message['content']
    logging.info(f"Raw discussion output: {discussion}")
    
    if 'discussions' not in session:
        session['discussions'] = {}
    if str(index) not in session['discussions']:
        session['discussions'][str(index)] = []
    session['discussions'][str(index)].append(discussion)
    logging.info(f'Sessions after generation:  {session["discussions"]}')
    return jsonify(discussion=discussion)

@app.route('/format_rough', methods=['POST'])
def format_text_rough():
    segment = request.form.get('segment')
    
    sentences = segment.split('.')
    rough_formatted_text = ''
    
    for i in range(len(sentences)):
        rough_formatted_text += sentences[i].strip() + '.'
        if (i + 1) % 3 == 0 and i < len(sentences) - 1:  # every third sentence
            rough_formatted_text += '<br>'
    
    logging.info(f"Rough formatted text output: {rough_formatted_text}")
    return jsonify(formatted_text=rough_formatted_text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 4000)))
