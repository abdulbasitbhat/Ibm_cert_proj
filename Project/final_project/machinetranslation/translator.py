'''Translator'''
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey=os.environ['apikey']
url=os.environ['url']

authenticator=IAMAuthenticator('4AdbSkRICbhx7kjfjxICxKZqukXHAE6eGmdZaEuDQCEL')
language_translator=LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url(
    'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/9e38fcbd-71ce-48ff-b0fd-730ef7f403ab'
    )

ENGLISH_TEXT="Hello"
FRENCH_TEXT="Salut frere comment vas-tu"

'''Eng to French'''
def english_to_french(englishText):
    french_text=language_translator.translate(text=englishText, model_id='en-fr').get_result()
    print(french_text)
    return french_text

'''French to eng'''
def french_to_english(frenchText):
    english_text=language_translator.translate(text=frenchText, model_id='fr-en').get_result()
    print(english_text)
    return english_text

print('eng to french')
english_to_french(ENGLISH_TEXT)
print('french to eng')
french_to_english(FRENCH_TEXT)
