import fitz, os, pathlib, pyttsx3


def read_pdf(file_path):
    with fitz.open(file_path) as doc:
        text = chr(12).join([page.get_text() for page in doc])
    
    return text

def convert_to_audio(text, book_title):
    current_dir = os.path.dirname(__file__)
    path = os.path.join(current_dir, 'audiobooks')
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    save_path = f'{path}/{book_title}.mp3'

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    choosen_voice = None
    for voice in voices:
        print(voice)
        if 'English' in voice.name:
            choosen_voice = voice
    
    engine.setProperty('voice', choosen_voice.id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.save_to_file(text, save_path)
    engine.runAndWait()


# testing
test_file = r"C:\Users\kubas\Desktop\100 day python coding\Day 91 - PDF to Audiobook converter\testing_pdf\test english.pdf"
text = read_pdf(test_file)
convert_to_audio(text, 'test')
