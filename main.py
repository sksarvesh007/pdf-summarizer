from flask import Flask, render_template, request
from transformers import pipeline
import PyPDF2
import gunicorn
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/summary', methods=['POST'])
def get_summary():
    pdf_file = request.files['pdf']
    page_number = int(request.form['page'])
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    page_text = pdf_reader.pages[page_number - 1].extract_text()
    summarizer = pipeline("summarization")
    summary = summarizer(page_text, max_length=600, min_length=30, do_sample=False)
    
    return render_template('summary.html', summary=summary[0]['summary_text'])

if __name__ == '__main__':
    app.run(debug=True)
