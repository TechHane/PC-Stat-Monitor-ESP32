# PC-Stat-Monitor-ESP32
🚀 Proje Özeti: TechHane PC Status Monitor
Bu proje; PC donanım verilerini Libre Hardware Monitor üzerinden çekip, bir Python scripti vasıtasıyla işleyen ve ESP32 kontrolcüsüne bağlı ILI9341 TFT ekrana aktaran bir sistemdir.

1. Donanım Hazırlığı ve Bağlantılar
Piyasada sıkça bulunan ESP32 Wroom 32D kartınla (VSPI hattı kullanarak) en yüksek performansı aldık:

VCC: 3.3V / GND: GND.
SCK: GPIO 18 / MOSI: GPIO 23.
CS: GPIO 5 / DC: GPIO 2 / RST: GPIO 4.

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

