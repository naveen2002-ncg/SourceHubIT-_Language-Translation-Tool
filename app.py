from flask import Flask, render_template, request
from mintrans import GoogleTranslator
from gtts import gTTS
from email.message import EmailMessage
import smtplib
import os

app = Flask(__name__)
translator = GoogleTranslator()

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
                translation_result = translator.translate(source_text, source_lang, target_lang)
                # Extract the translated text from the response
                if isinstance(translation_result, dict) and 'sentences' in translation_result:
                    translated_text = translation_result['sentences'][0]['trans']
                else:
                    translated_text = str(translation_result)
                
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
