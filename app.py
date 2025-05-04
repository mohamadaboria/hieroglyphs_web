from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io
import os

app = Flask(__name__)


arabic_to_hieroglyphs = {
    'ا': '𓄿', 'ب': '𓃀', 'ت': '𓏏', 'ث': '𓍿',
    'ج': '𓎼', 'ح': '𓉔', 'خ': '𓐍', 'د': '𓂧',
    'ذ': '𓆓', 'ر': '𓂋', 'ز': '𓊃', 'س': '𓋴',
    'ش': '𓈙', 'ص': '𓍑', 'ض': '𓂞', 'ط': '𓏠',
    'ظ': '𓅱', 'ع': '𓂝', 'غ': '𓎼', 'ف': '𓆑',
    'ق': '𓎡', 'ك': '𓎢', 'ل': '𓃭', 'م': '𓅓',
    'ن': '𓈖', 'ه': '𓎛', 'و': '𓅱', 'ي': '𓇌',
    'ء': '𓀀', 'ى': '𓇌', 'ة': '𓏏'
}


def translate_to_hieroglyphs(text):
    return ''.join(arabic_to_hieroglyphs.get(c, c) for c in text)

@app.route("/", methods=["GET", "POST"])
def index():
    name = ""
    image_url = None
    if request.method == "POST":
        name = request.form.get("name", "")
        if name:
            image_url = f"/image?text={name}"
    return render_template("index.html", image_url=image_url, name=name)

@app.route("/image")
def image():
    arabic_text = request.args.get("text", "")
    hieroglyphic_text = translate_to_hieroglyphs(arabic_text)[::-1]

    img = Image.new("RGB", (800, 300), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    try:
        hiero_font = ImageFont.truetype("fonts/NotoSansEgyptianHieroglyphs-Regular.ttf", 64)
        arabic_font = ImageFont.truetype("fonts/Amiri-Regular.ttf", 48)
    except:
        hiero_font = ImageFont.load_default()
        arabic_font = ImageFont.load_default()

    
    arabic_bbox = draw.textbbox((0, 0), arabic_text, font=arabic_font)
    arabic_x = (img.width - (arabic_bbox[2] - arabic_bbox[0])) // 2
    draw.text((arabic_x, 30), arabic_text, font=arabic_font, fill=(0, 0, 0))

    
    hiero_bbox = draw.textbbox((0, 0), hieroglyphic_text, font=hiero_font)
    hiero_x = (img.width - (hiero_bbox[2] - hiero_bbox[0])) // 2
    draw.text((hiero_x, 150), hieroglyphic_text, font=hiero_font, fill=(0, 0, 0))

    img_io = io.BytesIO()
    img.save(img_io, "PNG")
    img_io.seek(0)
    return send_file(img_io, mimetype="image/png")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
