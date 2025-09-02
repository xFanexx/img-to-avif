# img-to-avif

Simple CLI tool to convert images to AVIF format with drag & drop support.

## Installation

```bash
pip install -r requirements.txt
```
or
```bash
pip install pillow pillow-avif-plugin pyinstaller
```

## Build EXE

```bash
pyinstaller --onefile --console img_to_avif.py
```

## Usage

**Drag & Drop:** Drag images onto the EXE file, it will output the .avif into the same folder where the original is stored.

**Command Line:** 
```bash
img_to_avif.exe image1.jpg image2.png
```

## Supported Formats
- JPG/JPEG
- PNG  
- WebP
- BMP
- TIFF

## Output
- Creates `.avif` files next to originals
- Shows file size reduction
- Quality: 90 (hardcoded, u can change the code for less or more quality tho)
