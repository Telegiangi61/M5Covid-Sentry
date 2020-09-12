# M5Covid-Mon

2020-AUG-01
M5 Covid-Mon ver 1.3 by Telegiangi61 https://github.com/Telegiangi61/M5Covid-Mon under GNU General Public License v3.0

A simple project to monitor Covid-19 disease, based on M5Stack Core Grey, remotely connect to Italian Civil Protection Department github repository.
Download and parse json official data and show them in rolling mode the relevant informations for each Italy regions. 
Coding with a bounce of umicropython
Press btn A to light OFF LCD and save battery when unnecessary
Press btn C to light ON LCD
Still search how put on deep sleep mode for > 30 secs caused by an issue on power management,
after about 32secs  the IP5306 chip onboard M5Stack cores falls itself in idle mode if power load is < 45mA till next press of Power btn

For a correct use load first the M5 Burner firmware at https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/software/M5Burner.zip
Do not forget to load background image italy4.jpg to res path of M5Stack with a tool like UI Flow (https://flow.m5stack.com/)
Load code and execute to test by using the gui Mu  https://codewith.mu/ (set USB as M5 access)
