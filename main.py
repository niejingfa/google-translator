import json
from google_trans_new import google_translator
translator = google_translator()

text = "{\"17049\":{\"name\":\"Total 0% Fat Free Greek Strained Yoghurt\"},\"18051\":{\"name\":\"nutri_cookies\"}}"

data = json.loads(text)
for key, value in data.items():
  sres = translator.translate(value['name'], lang_tgt='zh-CN')
  value['alias'] = sres
  print(sres)

print(data)