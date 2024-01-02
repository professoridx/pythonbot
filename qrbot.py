import qrcode
import os 
import io
from urllib.request import urlopen
import sengo

def create_qrcode(text):
    if os.path.exists("pythonbot/output") is False:
        os.mkdir("pythonbot/output")
        
    output_folder=f"pythonbot/output/image.png"
     
    img=qrcode.make(text)
    img.save(output_folder)
    
def animator_gif(text):
    output_folder=f"pythonbot/output/imagegif.png"
    qrcode = sengo.make(text, error='h')
    
    url="https://img.icons8.com/color/48/telegram-app--v1.png"
    bg=urlopen(url)
    out = io.BytesIO()
    qrcode.to_artistic(background=bg, target=out, scale=5, kind='png')
    qrcode.save(output_folder)
    
text="fuckuou"
animator_gif(text)