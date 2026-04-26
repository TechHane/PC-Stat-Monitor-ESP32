@echo off
:: Türkçe karakter desteği için
chcp 65001 > nul

:: Klasöre git (Daha güvenli tırnak kullanımı)
cd /d "F:\ELEKTRİK ELEKTRONİK\01.ARDUINO\3D Yazıcı İle Arduino\PC Kasa Yardımcı Ekran\Arduino yazılım"

:: Python scriptini çalıştır
:: Eğer 'python' komutu çalışmazsa bunu 'py' olarak değiştirmeyi dene
python kasa_monitor.py

::pause