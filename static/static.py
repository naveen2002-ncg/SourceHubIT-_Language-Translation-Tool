import os
@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    if request.method == 'POST':
        source_text = request.form['source_text']
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']
        if source_text:
            translated = translator.translate(source_text, src=source_lang, dest=target_lang)
            translated_text = translated.text
            # Check if the static directory exists
            if not os.path.exists("static"):
                print("Static directory does not exist.")
                os.makedirs("static")  # Create the directory if it doesn't exist
            # Optional: Convert translated text to speech
            audio_file_path = "static/translated.mp3"
            if os.path.exists(audio_file_path):
                os.remove(audio_file_path)  # Remove the old file if it exists
            tts.save(audio_file_path)  # Save the new audio file
    return render_template('index.html', translated_text=translated_text)