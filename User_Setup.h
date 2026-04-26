#define USER_SETUP_LOADED

#define ILI9341_DRIVER

#define TFT_MISO -1  // Ekrandan veri okumayacağız o yüzden -1 yapabilirsin
#define TFT_MOSI 23
#define TFT_SCLK 18
#define TFT_CS    5  // Chip select control pin
#define TFT_DC    2  // Data/Command control pin
#define TFT_RST   -1  //  Reset ekranın 3.3V'a bağla ve -1 kalsın

#define LOAD_GLCD
#define LOAD_FONT2
#define LOAD_FONT4
#define LOAD_FONT6
#define LOAD_FONT7
#define LOAD_FONT8

#define SPI_FREQUENCY  27000000 // WT32-ETH01 için daha stabil bir hız