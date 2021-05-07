#モジュールを読み込む
import RPi.GPIO as GPIO
import time
 
#GPIO番号の指定モードを設定(BCM:役割ピン番号、BOARD:PIN番号)
GPIO.setmode(GPIO.BCM)    #BCMの方がプログラムの互換性がある
 
#23番ピンを出力として使用するように設定
GPIO.setup(23, GPIO.OUT)
 
try:
    while True:    #無限ループ
     #23番ピンにHIGHを出力(LEDをON)
        GPIO.output(23, GPIO.HIGH)
 
        time.sleep(2.0)     #0.5秒スリープ
 
     #23番ピンにLOWを出力(LEDをOFF)
        GPIO.output(23, GPIO.LOW)
 
        time.sleep(2.0)     #0.5秒スリープ
 
#キーボードからCtrl+C割込みが入ったら
except KeyboardInterrupt:
    pass #何もせずに次の行へ
 
#GPIOの設定をリセット
GPIO.cleanup()