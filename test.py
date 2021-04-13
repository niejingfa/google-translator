from google_trans_new import google_translator
translator = google_translator()

text = 'test'
translate_text = translator.translate(text, lang_tgt='zh-CN')
print(translate_text)