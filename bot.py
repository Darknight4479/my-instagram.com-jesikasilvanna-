notepad bot.py
from instagrapi import Client

username = "ritt.aerina_IG"
password = "akukamu2020_IG"

cl = Client()
cl.login(username, password)

caption = """
LOWONGAN PEKERJAAN

Posisi: Admin Online
Lokasi: Remote
Gaji: 3-5 juta

Kirim CV via DM
#lowongankerja #loker
"""

cl.photo_upload("loker.jpg", caption)

print("Posting berhasil")
