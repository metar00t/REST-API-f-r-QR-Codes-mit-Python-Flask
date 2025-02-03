from flask import Flask
import qrcode
import qrcode.image.svg

app = Flask(__name__)

@app.route("/api/v1/qr/generate/<string:text>")
def generateQrCode(text):

    method = ""

    if method == 'basic':
        # Simple factory, just a set of rects.
        factory = qrcode.image.svg.SvgImage
    elif method == 'fragment':
        # Fragment factory (also just a set of rects)
        factory = qrcode.image.svg.SvgFragmentImage
    else:
        # Combined path factory, fixes white space that may occur when zooming
        factory = qrcode.image.svg.SvgPathImage

    img = qrcode.make(text, image_factory=factory)
    text = img.to_string(encoding='unicode')
    return f'{text}'