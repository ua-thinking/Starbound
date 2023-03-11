import json
import os

# переконуємося, що поточна робоча директорія - головна директорія проєкту
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# створюємо папку translations, якщо її ще немає
if not os.path.exists('translations'):
    os.makedirs('translations')

# створюємо порожні файли з відповідними іменами у папці translations
with open('translations/totallabels.json', 'w') as f:
    json.dump({}, f)

with open('translations/translation_en.json', 'w') as f:
    json.dump({}, f)
