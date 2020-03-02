from datetime import date
import requests
import pyautogui as pag
import sys
from tqdm import tqdm

actual_day = str(date.today())
xml_source = "C:/Users/mandz/Dysk Google/KetoBazar/bioU/xml/2020/service"+actual_day+".xml"

URL = 'https://www.biou.pl/modules/pricewars2/service.php?alias=hurtownia-biou'

response = requests.get(URL)

with open(xml_source, 'wb') as file:
    file.write(response.content)
    print('Download successful!')

sys.exit()

