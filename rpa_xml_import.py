from datetime import date
import requests
import pyautogui as pag

actual_day = str(date.today())
xml_source = "C:/Users/mandz/Dysk Google/KetoBazar/bioU/xml/2020/service"+actual_day+".xml"

URL = 'https://www.biou.pl/modules/pricewars2/service.php?alias=hurtownia-biou'

response = requests.get(URL)
with open(xml_source, 'wb') as file:
    file.write(response.content)
    print('Download successful!')

## open website ketobazar from desktop shortcut
pag.moveTo(900,1050,)
pag.click(button='right')
pag.moveTo(915,888,)
pag.click(button='left')
pag.moveTo(1830,30,)
pag.doubleClick()
pag.moveTo(80,660,5) ##Page loading
pag.scroll(-400)
pag.moveTo(80,955,1)
pag.click(button='left')
pag.moveTo(530,450,3)
pag.click(button='left')
pag.moveTo(550,65,3)

## import xml using pyautogui
pag.click(button='left') ##Upload file
pag.write('C:/Users/mandz/Dysk Google/KetoBazar/bioU/xml/2020')
pag.press('enter')
pag.moveTo(500,175)
pag.doubleClick()
pag.moveTo(1190,720,11)
pag.click(button='left') #Existing items
pag.moveTo(1040,840)
pag.click(button='left')
pag.press('down', presses=7, interval=0.5)
pag.moveTo(900,960)
pag.moveTo(900,790) 
pag.click(button='left') ##Continue to step 2
