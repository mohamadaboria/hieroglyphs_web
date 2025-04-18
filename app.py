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
    result = ""
    if request.method == "POST":
        name = request.form.get("name", "")
        result = translate_to_hieroglyphs(name)
    return render_template("index.html", result=result)

@app.route("/image")
def image():
    text = request.args.get("text", "")
    img = Image.new("RGB", (600, 200), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("fonts/NotoSansEgyptianHieroglyphs-Regular.ttf", 48)
    except:
        font = ImageFont.load_default()
    draw.text((20, 70), text, font=font, fill=(0, 0, 0))
    img_io = io.BytesIO()
    img.save(img_io, "PNG")
    img_io.seek(0)
    return send_file(img_io, mimetype="image/png")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)