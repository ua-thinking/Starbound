import os
import json

# шлях до папки зі скриптом
script_dir = os.path.dirname(__file__)

# шлях до папки зі всіма перекладами
translations_dir = os.path.join(script_dir, "..", "translations")

# перевіряємо чи існує папка з перекладами
if not os.path.exists(translations_dir):
    os.mkdir(translations_dir)

# створюємо пусті файли
with open(os.path.join(translations_dir, "totallabels.json"), "w") as f:
    json.dump({}, f)

with open(os.path.join(translations_dir, "translatedlabels.json"), "w") as f:
    json.dump({}, f)
    
print("Файли totallabels.json та translatedlabels.json створено в папці translations")    