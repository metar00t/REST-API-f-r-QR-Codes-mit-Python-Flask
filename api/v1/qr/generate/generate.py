from flask import Flask
import qrcode
from qrcode.image.styles.moduledrawers.svg import SvgCircleDrawer
import qrcode.image.svg

app = Flask(__name__)

# Klasse QrCode wird erstellt
class QrCode:
    def __init__(self, text):
        # Hier wird der übergebene Wert als Variable deklariert
        self.text = text
    # Methode generate() definiert
    def generate(self):

        # TODO Code zum Styling der QR-Codes anpassen
        img = qrcode.make(self.text, image_factory=qrcode.image.svg.SvgPathImage)
        self.text = img.to_string(encoding='unicode')
        # Gibt die SVG (Vektorgrafik) als String zurück
        return f'{self.text}'
    
    @app.route("/api/v1/qr/generate/<string:text>")
    def generateQrCode(text):
        # Erstellung des Objektes
        qr = QrCode(text)
        # Aufruf der Methode zur Generierung des Codes mit der Rückgabe von der Methodenausgabe
        return qr.generate()