import RPi.GPIO as GPIO #GPIO KÜTÜPHANESİNİ TANIMLADIM
import spidev #SPI İLE ANALOG VERİ OKUMAK İçİN SPİDEV KÜTÜPHANESİ ÇAğRILDI
import time # BEKLEME SÜRELERİ KULLANMAK İÇİN TİME KÜTÜPHANESİNİ KULLANILDI
 

vrx_channel = 0 #İLK X KANALINA SONRASINDA FONKSİYONDA KULLANMAK İÇİN 0 DEĞERİ ATANDI
vry_channel = 1 #İLK Y KANALINA SONRASINDA FONKSİYONDA KULLANMAK İÇİN 1 DEĞERİ ATANDI
vrx1_channel = 2 #İKİNCİ X KANALINA SONRASINDA FONKSİYONDA KULLANMAK İÇİN 2 DEĞERİ ATANDI 
vry1_channel = 3 #İKİNCİ Y KANALINA SONRASINDA FONKSİYONDA KULLANMAK İÇİN 3 DEĞERİ ATANDI

GPIO.setmode(GPIO.BOARD9) #GPIO NUMARALANDIRMALARININ BOARD TÜRÜNE GöRE OLMASI AYARLANDI
GPIO.setup(29, GPIO.OUT) # 29 , 31 , 33 , 35  NUMARALI GPIO PİNLERİ PWM SİNYALİ UYGULAMLARI İÇİN ÇIKIŞ OLARAK AYARLANDI
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)

servo1=GPIO.PWM(29,50) # 29 , 31 , 33 , 35 NUMARALI GPIO PİNLERİ 50 HZ PWM SİNYALİ UYGULAMALARI İÇİN AYARLANDI VE SERVO DEĞİŞKENLERİNE ATANDI
servo2=GPIO.PWM(31,50)
servo3=GPIO.PWM(33,50)
servo4=GPIO.PWM(35,50)
servo1.start(7.5) # 29 , 31,33,35 NUMARALI GPIO PİNLERİNDEN %7.5 DUTY CYCLE UYGULANARAK PWM SİNYALLERİ UYGULANMAYA BAŞLANDI
servo2.start(7.5)
servo3.start(7.5)
servo4.start(7.5)


delay = 0.5 # 5 MS BEKLEME KOYULDU
 
# Spidevin okuma fonksiyonu çağrılarak spi değişkenine atandı ve değişken sıfır değerinden başlatıldı
spi = spidev.SpiDev()
spi.open(0,0)
 
#  MCP 3008 ÇİPİNDEN ALINAN ANALOG SİNYALLERİN YANLIŞ OKUNMAMASI VE 8 BİTE AKTARILMASI İÇİN OKUMA FONKSİYONU TANIMLANDI
def readChannel(channel):
  val = spi.xfer2([1,(8+channel)<<4,0])
  data = ((val[1]&3) << 8) + val[2]
  return data
 
 
# endless loop
while True:
 
  # OKUNAN DEĞERLER HER EKSEN İÇİN FARKLI BİR DEĞİŞKENE ATANDI
  vrx_pos = readChannel(vrx_channel)
  vry_pos = readChannel(vry_channel)
  vrx1_pos = readChannel(vrx1_channel)
  vry1_pos = readChannel(vry1_channel)
 #0 İLE 1024 DEĞERLERİ ARASINDA OKUNAN ANALOG SİNYALLER 3 İLE 12 ARASINDA Kİ DUTY CYCLE DEĞERLERİNE DÖNÜŞTÜRDÜM  
  donme1=((vrx_pos*0.008789)+3)
  donme2=((vrx_pos*0.008789)+3)
  donme3=((vrx_pos*0.008789)+3)  
  donme4=((vrx_pos*0.008789)+3) 
#ELDE ETTİĞİMİZ DÖNME DEĞİŞKEN DEĞERLERİNİ CHANGE FONKSİYONU İLE SERVO MOTORLARA UYGULADIM  
  servo1.ChangeDutyCycle(donme1)
  servo2.ChangeDutyCycle(donme2)
  servo3.ChangeDutyCycle(donme3)
  servo4.ChangeDutyCycle(donme4)
	
#DÖNMENİN GERÇEKLEŞMESİ İÇİN BEKLEME SÜRESİ KOYDUM 
  time.sleep(delay)  
 
#PROGRAMDAN ÇIKILDIKTAN SONRA GPIO PİNLERİNİN TEMİZLENMESİ İÇİB PROGRAM SONU FONKSİYONU OLUŞTURDUM
def endprogram():
    GPIO.cleanup()
#PROGRAMIN GÜVENLİ ÇALIŞMASI İÇİN TRY VE EXCEPT FONKSİYONLARINI KULLANDIM 
if TRUE== :

    try:
        loop()

    except KeyboardInterrupt:
        endprogram()
