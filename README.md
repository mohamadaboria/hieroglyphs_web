# Hieroglyph Name Converter (Arabic to Ancient Egyptian)

This web app allows users to type their name in Arabic and see it written in Ancient Egyptian hieroglyphs. It also generates an image of the hieroglyphs.

## How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Then open: http://localhost:5000

## Deploy on Render

1. Upload this folder to GitHub
2. Create new "Web Service" on [https://render.com](https://render.com)
3. Set:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py`
   - Port: 5000

Make sure the file `fonts/NotoSansEgyptianHieroglyphs-Regular.ttf` exists and is valid.

## License

Free to use for educational and personal projects.# hieroglyphs_web
