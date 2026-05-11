# PC-Stat-Monitor-ESP32
🚀 Proje Özeti: TechHane PC Status Monitor
Bu proje; PC donanım verilerini Libre Hardware Monitor üzerinden çekip, bir Python scripti vasıtasıyla işleyen ve ESP32 kontrolcüsüne bağlı ILI9341 TFT ekrana aktaran bir sistemdir.

1. Donanım Hazırlığı ve Bağlantılar
Piyasada sıkça bulunan ESP32 Wroom 32D kartı ile ILI9341 2.8" TFT ekranı kullanıp, (VSPI hattı kullanarak) en yüksek performansı aldık:
MOSI 23,SCLK 18,CS 5 ,DC 2  

2. ESP32 & TFT_eSPI Kütüphane Ayarları
Arduino IDE üzerinde en kritik adım TFT_eSPI Kütüphanesinin User_Setup.h dosyasını düzenlemekti çünkü ekran ile ESP32 arasındaki pin tanımlamaları bu dosyalada yapılıyor.

3. PC Tarafı: Libre Hardware Monitor (LHM) (Versiyon 0.9.6)
Verilerin kaynağı olan yazılımı yapılandırdık:
Remote Web Server: Aktif edilerek verilerin localhost:8085/data.json adresinden yayınlanması sağlandı.

4. Python Yazılımı (Köprü Görevi)
PC ve ESP32 arasındaki iletişimi sağlayan kasa_monitor.py yazıldı:
Kütüphaneler: requests (JSON verisini çekmek için) ve pyserial (ESP32'ye göndermek için) kuruldu.

Veri İşleme: LHM'den gelen karmaşık JSON verisi ayıklandı, ondalık basamakları (clean_one_decimal) düzenlendi ve tek bir paket haline getirildi.

5. Otomasyon ve Arka Plan Çalışma
Sistemin PC açıldığında kendi kendine çalışması sağlandı:
Batch Dosyası (baslat.bat): Python kodunu doğru klasörde çalıştıran komut dosyası oluşturuldu.
VBS Script (baslat_gizli.vbs): Siyah terminal penceresini gizleyerek kodu "hayalet modunda" başlatan araç eklendi.
Başlangıç (Startup): Bu VBS dosyası shell:startup klasörüne atılarak sistemin her açılışta otomatik devreye girmesi sağlandı.

✅ Sonuç
Şu an kasanın içinde; işlemci sıcaklığından internet hızına kadar her şeyi anlık gösteren, TechHane yapımı, tamamen otomatik ve profesyonel bir panelin var.

🚀 Project Summary: TechHane PC Status Monitor
This project is a system that pulls PC hardware data via Libre Hardware Monitor, processes it through a Python script, and transmits it to an ILI9341 TFT display connected to an ESP32 controller.

1.Hardware Preparation and Connections
Using the widely available ESP32 Wroom 32D board and an ILI9341 2.8" TFT display, we achieved peak performance by utilizing the VSPI line:
MOSI: 23 SCLK: 18 CS: 5 DC: 2

2.ESP32 & TFT_eSPI Library Settings
The most critical step in the Arduino IDE was editing the User_Setup.h file of the TFT_eSPI library, as the pin definitions between the display and the ESP32 are configured within these files.

3.PC Side: Libre Hardware Monitor (LHM) (Version 0.9.6)
We configured the software that serves as the data source:
Remote Web Server: Activated to enable data broadcasting at localhost:8085/data.json.

4.Python Software (The Bridge)
The kasa_monitor.py script was developed to facilitate communication between the PC and the ESP32:
Libraries: requests (to pull JSON data) and pyserial (to send data to the ESP32) were installed.
Data Processing: The complex JSON data from LHM was parsed, decimal points were formatted (clean_one_decimal), and the data was compiled into a single packet.

5. Automation and Background Operation
The system was configured to run automatically upon PC startup:
Batch File (baslat.bat): A command file was created to run the Python code in the correct directory.
VBS Script (baslat_gizli.vbs): A tool was added to hide the black terminal window and launch the code in "ghost mode."
Startup: This VBS file was placed in the shell:startup folder to ensure the system activates automatically every time the computer boots up.

✅ Result
You now have a fully automated, professional, TechHane-made panel inside your case that displays everything from CPU temperature to internet speed in real-time.
