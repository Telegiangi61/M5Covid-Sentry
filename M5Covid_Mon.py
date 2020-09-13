# 2020-AUG-01 M5 Covid-Sentry ver 1.3 by Telegiangi61 https://github.com/Telegiangi61/M5Covid-Mon under GNU General Public License v3.0
# A simple project to monitor Covid-19 disease, based on M5Stack Core Grey, remotely connect to Italian Civil Protection Department github repository.
# Download and parse json official data and show them in rolling mode the relevant informations for each Italy regions. 
# Coding with a bounce of umicropython
# Press btn A to light OFF LCD and save battery when unnecessary
# Press btn C to light ON LCD
# Still search how put on deep sleep mode for > 30 secs caused by an issue on power management,
# after about 32secs  the IP5306 chip onboard M5Stack cores falls itself in idle mode if power load is < 45mA till next press of Power btn

# For a correct use load first the M5 Burner firmware at https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/software/M5Burner.zip
# Do not forget to load background image italy4.jpg to res path of M5Stack with a tool like UI Flow (https://flow.m5stack.com/)
# Load code and execute to test by using the gui Mu  https://codewith.mu/ (set USB as M5 access)


from m5stack import *
from m5ui import *
from uiflow import *
import wifiCfg
import urequests
import machine
import ujson


i = 0  # start from 0 index region on json data (ABRUZZO)

lcd.setBrightness(10)

label0 = M5TextBox(0, 0, "", lcd.FONT_Default, 0xFF0000, rotate=0)
image0 = M5Img(1, -21, "res/italy4.jpg", True)
title0 = M5Title(title="M5 COVID-Sentry", x=70 , fgcolor=0xff0000, bgcolor=0xffffff)
lcd.print("CONNECTING....",80,120)

# detect if A or C button has been pressed to ON / OFF LCD and save battery
def buttonA_wasPressed():
  lcd.setBrightness(0)
#  speaker.tone(1800, 20)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonC_wasPressed():
  lcd.setBrightness(10)
#  speaker.tone(1000, 20)
  pass
btnC.wasPressed(buttonC_wasPressed)

# connect to your wifi 
wifiCfg.doConnect("YOUR SSID", "YOUR PASSWD")

# retrieve json data from official github of Italian Protezione Civile DPT. Data were updates daily after 17:00 
req = urequests.get(
        "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni-latest.json"
    )
while True:

    totpos = (ujson.loads((req.text)))[i]["totale_positivi"]
    time = (ujson.loads((req.text)))[i]["data"]
    nuovipos = (ujson.loads((req.text)))[i]["nuovi_positivi"]
    guariti = (ujson.loads((req.text)))[i]["dimessi_guariti"]
    decessi = (ujson.loads((req.text)))[i]["deceduti"]
    regione = (ujson.loads((req.text)))[i]["denominazione_regione"]
	
    lcd.clear()
    image0 = M5Img(1, -21, "res/italy4.jpg", True)
    title0 = M5Title(
        title="M5 COVID-Sentry", x=70, fgcolor=0xFF0000, bgcolor=0xFFFFFF
    )
    lcd.print(str(time), 70, 25)
    lcd.print("Tot Pos:", 4, 60)
    lcd.print(str(totpos), 140, 60)
    lcd.print("Nuovi Pos:", 4, 80)
    lcd.print(str(nuovipos), 140, 80)
    lcd.print("Decessi:", 4, 100)
    lcd.print(str(decessi), 140, 100)
    lcd.print("Guariti:", 4, 120)
    lcd.print(str(guariti), 140, 120)
    lcd.print("Regione:", 4, 180)
    lcd.print(str(regione), 140, 180)
    lcd.print("Stato:                  ITALIA", 4, 200)
    lcd.print("Battery Status:", 4, 220)
    lcd.print(power.getBatteryLevel(), 120, 220)

#    req.close()
    i = i + 1
    if i == 21:
        i = 0
# wait 10 seconds before load next region
    wait_ms(10000)
