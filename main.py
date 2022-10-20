import os

import xml.etree.ElementTree as ET
from googletrans import Translator
import pandas as pd

# look for a request with `.xml` ending

def run(fn: str):
    mytree = ET.parse(f'{fn}.xml')
    myroot = mytree.getroot()
    res = mytree.findall('.//{http://www.w3.org/ns/ttml}span')
    texts = [x.text for x in res]

    translator = Translator()
    trans = [translator.translate(text, src='de', dest='en').text for text in texts]

    miehahah = pd.DataFrame(
        {'de': texts,
         'en': trans
         })

    miehahah.to_csv(f"{fn}.csv", index=False)


if __name__ == '__main__':
    run(fn="heidi_15")