# Advanced Mini SIEM Logic - Developed by Umutcan Korkmaz
import time

THREAT_SIGNATURES = ["UNION SELECT", "<script>", "admin'--", "/etc/passwd", "os.system("]
ALERT_THRESHOLD = 5 # 5 saniyede 5 şüpheli işlem gelirse alarm ver

def process_log_stream(log_line):
    for signature in THREAT_SIGNATURES:
        if signature in log_line:
            return True, signature
    return False, None

def start_monitor():
    print("[*] SIEM Core Engine is active and monitoring...")
    # Simüle edilmiş log akışı
    log_sample = "192.168.1.1 - GET /index.php?id=1 UNION SELECT 1,2,3"
    
    is_threat, pattern = process_log_stream(log_sample)
    if is_threat:
        print(f"[ALERT] Malicious pattern '{pattern}' detected in traffic!")

if __name__ == "__main__":
    start_monitor()
