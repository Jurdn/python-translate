from tkinter import *
from googletrans import Translator

global sentence
global selected_language
global result_translate

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'filipino',
    'he': 'hebrew'
}

window = Tk()
window.title("My translator")

window.geometry("600x300")

sentence_label = Label(window, text="Enter your sentence : ")

sentence = StringVar()
sentence.set("Enter a sentence")
entree = Entry(window, textvariable=sentence, width=30)

language_label = Label(window, text="Chose your language : ")

language_liste = Listbox(window)
i = 0
for lab, lang in LANGUAGES.items():
    language_liste.insert(i, lang)
    i += 1

selected_language = StringVar()

translate_bouton=Button(window, text="Translate", command=lambda : translate_func())
quit_button=Button(window, text="Quit", command=window.quit)
translate_label = Label(window, text="Translation", bg="yellow")

def updateLabel():
    line = language_liste.curselection()[0]
    item = language_liste.get(line)
    selected_language.set(item)


def translate(sent, country):
    translator = Translator()
    res = translator.translate(sent, dest=country)
    translate_label['text'] = "{} -> {}".format(sent, res.text)
    window.update()

def createall() :
    sentence_label.pack()
    entree.pack()
    language_label.pack()
    language_liste.pack()
    translate_bouton.pack()
    quit_button.pack()
    translate_label.pack()

def translate_func() :
    updateLabel()
    if (selected_language):
        translate(sentence.get(), selected_language.get())
    else:
        print("Please select a language.")

createall()
window.mainloop()