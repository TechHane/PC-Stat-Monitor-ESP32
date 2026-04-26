import requests
import serial
import time

# --- AYARLAR ---
SERIAL_PORT = 'COM3' 
BAUD_RATE = 115200
LIBRE_URL = "http://localhost:8085/data.json"

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Bağlantı başarılı: {SERIAL_PORT}")
except Exception as e:
    print(f"Port hatası: {e}")
    input("Kapatmak için Enter'a bas...") # Hatayı görmen için hemen kapatmaz
    exit()

def get_val(data, cat, sensor):
    if data.get('Text') == cat:
        for child in data.get('Children', []):
            if child.get('Text') == sensor:
                return child.get('Value')
    if 'Children' in data:
        for child in data['Children']:
            res = get_val(child, cat, sensor)
            if res is not None: return res
    return None

def get_sensor_from_hardware(node, hardware_name, category_name, sensor_name):
    # Aranan donanımı bul
    if node.get('Text') == hardware_name:
        for category in node.get('Children', []):
            if category.get('Text') == category_name:
                for sensor in category.get('Children', []):
                    if sensor.get('Text') == sensor_name:
                        return sensor.get('Value')

    # Alt düğümlerde ara
    for child in node.get('Children', []):
        result = get_sensor_from_hardware(child, hardware_name, category_name, sensor_name)
        if result is not None:
            return result

    return None

def clean_one_decimal(val):
    if val is None or val == "": return "0.0 "
    try:
        num = val.split(' ')[0].replace(',', '.')
        return "{:.1f} ".format(float(num))
    except: return "0.0"

def clean_to_int(val):
    if val is None or val == "": return "0"
    try:
        # Önce boşluklara göre ayır, virgülü noktaya çevir, float yap, sonra int'e zorla
        num = val.split(' ')[0].replace(',', '.')
        return str(int(float(num))) # 2548.0 -> 2548 -> "2548"
    except:
        return "0"    

# --- ANA DÖNGÜ ---
while True:
    try:
        response = requests.get(LIBRE_URL)
        if response.status_code == 200:
            data = response.json()

            # CPU (Ryzen 9 9700X)
            c_temp = clean_one_decimal(get_val(data, "Temperatures", "Core (Tctl/Tdie)"))
            c_load = clean_one_decimal(get_val(data, "Load", "CPU Total"))
            c_freq = clean_to_int(get_val(data, "Clocks", "Cores (Average)")) 
            
            # GPU (RTX 5070)
            g_temp = clean_one_decimal(get_val(data, "Temperatures", "GPU Core"))
            g_load = clean_one_decimal(get_val(data, "Load", "GPU Core"))
            g_freq = clean_to_int(get_val(data, "Clocks", "GPU Core"))
            g_vram = clean_to_int(get_val(data, "Data", "GPU Memory Used"))
            g_fan  = clean_to_int(get_val(data, "Fans", "GPU Fan 1"))
            g_pwr  = clean_one_decimal(get_val(data, "Powers", "GPU Package"))
            
            # RAM
            r_used = clean_one_decimal(
                get_sensor_from_hardware(data, "Total Memory", "Data", "Memory Used")
            )
            
            # NETWORK 
            
            net_down = clean_one_decimal(
                get_sensor_from_hardware(data, "Wi-Fi", "Throughput", "Download Speed")
            )
            
            net_up   = clean_one_decimal(
                get_sensor_from_hardware(data, "Wi-Fi", "Throughput", "Upload Speed")
            )
            
            # DENEME 
            deneme   = clean_to_int(get_val(data, "Controls", "CPU Fan"))
            
            # PAKET OLUŞTURMA
            payload = f"{c_temp},{c_load},{c_freq},{g_temp},{g_load},{g_freq},{g_vram},{g_fan},{g_pwr},{r_used},{net_down},{net_up},{deneme}*"
            
            ser.write(payload.encode())
            print(f"Gönderildi: {payload}")
        else:
            print("LHM JSON çekilemedi!")

    except Exception as e:
        print(f"Döngü hatası: {e}")
    
    time.sleep(1)
