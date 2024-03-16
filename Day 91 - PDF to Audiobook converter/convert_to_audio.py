import fitz, os, pyttsx3


def read_pdf(file_path):
    with fitz.open(file_path) as doc:
        text = chr(12).join([page.get_text() for page in doc])
    
    return text

def convert_to_audio(text, language, file_name):
    save_path = f'{file_name}'

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    choosen_voice = None
    for voice in voices:
        if language in voice.name:
            choosen_voice = voice
            print(voice)
    
    engine.setProperty('voice', choosen_voice.id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.save_to_file(text, save_path)
    engine.runAndWait()

