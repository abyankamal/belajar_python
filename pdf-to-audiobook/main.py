import PyPDF2
import pyttsx3

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_speech(text, audio_file_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, audio_file_path)
    engine.runAndWait()

def pdf_to_audiobook(pdf_path, audio_file_path):
    text = extract_text_from_pdf(pdf_path)
    text_to_speech(text, audio_file_path)

# Example usage
pdf_path = 'file.pdf'
audio_file_path = 'audiobook.mp3'
pdf_to_audiobook(pdf_path, audio_file_path)
