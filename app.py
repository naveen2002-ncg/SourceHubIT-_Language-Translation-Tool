from flask import Flask, render_template, request
from googletrans import Translator
from gtts import gTTS
from email.message import EmailMessage
import smtplib
import os

app = Flask(__name__)
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    error_message = ""
    
    if request.method == 'POST':
        source_text = request.form['source_text']
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']

        if source_text:
            try:
                translated = translator.translate(source_text, src=source_lang, dest=target_lang)
                translated_text = translated.text
            
                # Send the email
                msg = EmailMessage()
                msg['Subject'] = 'Translated Text'
                msg['From'] = os.environ.get('EMAIL_USER')
                msg['To'] = 'recipient@example.com'
                msg.set_content(translated_text)

                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login(os.environ.get('EMAIL_USER'), os.environ.get('EMAIL_PASS'))
                    server.send_message(msg)
                
            except Exception as e:
                error_message = "An error occurred: " + str(e)

    return render_template('index.html', translated_text=translated_text, error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
