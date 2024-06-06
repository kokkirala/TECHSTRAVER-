from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load pre-trained NLP model
qa_pipeline = pipeline("question-answering")

# Dummy data for medical information and appointment scheduling
medical_info = {
    "headache": "A headache is pain or discomfort in the head or face area. It can be caused by various factors including stress, dehydration, or medical conditions.",
    "fever": "A fever is a temporary increase in body temperature, often due to an illness. It is a part of the body's immune response."
}

appointments = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['question']
    response = qa_pipeline({
        'question': user_input,
        'context': ' '.join(medical_info.values())
    })
    answer = response['answer']
    return render_template('index.html', answer=answer)

@app.route('/schedule', methods=['POST'])
def schedule():
    appointment_details = request.form['appointment']
    appointments.append(appointment_details)
    return render_template('index.html', message="Appointment scheduled successfully!")

if __name__ == '__main__':
    app.run(debug=True)
