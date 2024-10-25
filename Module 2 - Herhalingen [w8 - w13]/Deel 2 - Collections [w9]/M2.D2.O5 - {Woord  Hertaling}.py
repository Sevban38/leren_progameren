translation_dict = {
    "hart": "teennagels",
    "grot": "geit",
    "Draganthor": "Rurik",
    "schubben": "waterende",
    "vurige": "golf van water",
    "draak": "geit",
    "brulde": "spuwde",
    "vlammenzee": "golf van water",
    "bedreigde": "bedreigde",
    "krachtig": "krachtig",
    "schild": "zwemvest",
    "magie": "plastic",
    "hart." : "teennagels.",
    "grot.": "geit.",
    "Draganthor.": "Rurik.",
    "schubben.": "waterende.",
    "vurige.": "golf van water.",
    "draak.": "geit.",
    "brulde.": "spuwde.",
    "vlammenzee.": "golf van water.",
    "bedreigde.": "bedreigde.",
    "krachtig.": "krachtig.",
    "schild.": "zwemvest.",
    "magie.": "plastic."
}

def translate_text(text):
    translated_text = ""
    words = text.split()
    for word in words:
        translated_word = translation_dict.get(word, word)
        translated_text += translated_word + " "
    return translated_text.strip()

input_text = input("Enter a piece of text: ")
output_text = translate_text(input_text)
print("Translated text:")
print(output_text)