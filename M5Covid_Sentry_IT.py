# 2020-AUG-01 M5 Covid-Sentry ver 1.0 by Telegiangi61 https://github.com/Telegiangi61/M5Covid-Mon under GNU General Public License v3.0
# A simple project to monitor Covid-19 disease, based on M5Stack Core Grey, remotely connect to Italian Civil Protection Department github repository.
# Download and parse json official data and show the relevant informations for Italy country. 

# Still search how put on deep sleep mode for > 30 secs caused by an issue on power management,
# after about 32secs  the IP5306 chip onboard M5Stack cores falls itself in idle mode if power load is < 45mA till next press of Power btn

# For a correct use load first the M5 Burner firmware at https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/software/M5Burner.zip
# Load code and execute to test by using the gui Mu  https://codewith.mu/ (set USB as M5 access)

from m5stack import *
from m5ui import *
from uiflow import *
import wifiCfg
import urequests
import ujson

setScreenColor(0x443322)

while True:
  lcd.clear()
  wifiCfg.doConnect('YOUR SSID', 'YOUR PASSWD')
  req = urequests.get('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale-latest.json')
  totpos = (ujson.loads((req.text)))[0]["totale_positivi"]
  time = (ujson.loads((req.text)))[0]["data"]
  nuovipos = (ujson.loads((req.text)))[0]["nuovi_positivi"]

  guariti = (ujson.loads((req.text)))[0]["dimessi_guariti"]
  decessi = (ujson.loads((req.text)))[0]["deceduti"]
  lcd.print("M5 COVID-Sentry",80,0)

  lcd.print(str(time),60,30)
  lcd.print("Tot Pos:",0,60)
  lcd.print(str(totpos),140,60)
  lcd.print("Nuovi Pos:",0,80)
  lcd.print(str(nuovipos),140,80)
  lcd.print("Decessi:",0,100)
  lcd.print(str(decessi),140,100)
  lcd.print("Guariti:",0,120)
  lcd.print(str(guariti),140,120)
  lcd.print("Stato:       ITALIA",0,200)



  req.close()
  wait_ms(180000)# 2020-AUG-01 M5 Covid-Sentry ver 1.0 by Telegiangi61 https://github.com/Telegiangi61/M5Covid-Mon under GNU General Public License v3.0
# A simple project to monitor Covid-19 disease, based on M5Stack Core Grey, remotely connect to Italian Civil Protection Department github repository.
# Download and parse json official data and show the relevant informations for Italy country. 

# Still search how put on deep sleep mode for > 30 secs caused by an issue on power management,
# after about 32secs  the IP5306 chip onboard M5Stack cores falls itself in idle mode if power load is < 45mA till next press of Power btn

# For a correct use load first the M5 Burner firmware at https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/software/M5Burner.zip
# Load code and execute to test by using the gui Mu  https://codewith.mu/ (set USB as M5 access)

from m5stack import *
from m5ui import *
from uiflow import *
import wifiCfg
import urequests
import ujson

setScreenColor(0xFF2222)

while True:
  lcd.clear()
  wifiCfg.doConnect('YOUR SSID', 'YOUR PASSWD')
  req = urequests.get('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale-latest.json')
  totpos = (ujson.loads((req.text)))[0]["totale_positivi"]
  time = (ujson.loads((req.text)))[0]["data"]
  nuovipos = (ujson.loads((req.text)))[0]["nuovi_positivi"]

  guariti = (ujson.loads((req.text)))[0]["dimessi_guariti"]
  decessi = (ujson.loads((req.text)))[0]["deceduti"]
  lcd.print("M5 COVID-Sentry",20,0)

  lcd.print(str(time),20,30)
  lcd.print("Tot Pos:",0,60)
  lcd.print(str(totpos),140,60)
  lcd.print("Nuovi Pos:",0,80)
  lcd.print(str(nuovipos),140,80)
  lcd.print("Decessi:",0,100)
  lcd.print(str(decessi),140,100)
  lcd.print("Guariti:",0,120)
  lcd.print(str(guariti),140,120)
  lcd.print("Stato:       ITALIA",0,200)



  req.close()
  wait_ms(180000)
