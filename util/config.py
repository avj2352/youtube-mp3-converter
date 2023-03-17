import time,os,sys
from dotenv import load_dotenv

load_dotenv()

OPEN_AI_API_KEY = os.environ.get('OPEN_AI_API_KEY') or None

'''
Generates typing effect
'''
def typing_print(text: str):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
