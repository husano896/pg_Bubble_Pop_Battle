import json
_translations = {}
_languages = ['zh-Hant', 'en']
_useLang = 'zh-Hant'

def _load_langfiles():
    global _translations, _languages
    for langName in _languages:
        filepath = 'Languages/' + langName+'.json'
        with open(filepath, encoding='utf-8') as data_file:
            _translations[langName] = json.loads(data_file.read())

_load_langfiles()

def setLang(lang):
    global _useLang
    _useLang = lang

def l(key, lang=None):
    global _translations,_useLang
    return _translations[lang or _useLang][key]

