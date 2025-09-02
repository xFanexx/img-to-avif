import sys
import os
from PIL import Image

SUPPORTED_FORMATS = ['.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff', '.tif']
AVIF_QUALITY = 90

def convert_to_avif(image_path):
    """Convert an image to AVIF format"""
    ext = os.path.splitext(image_path)[1].lower()
    if ext not in SUPPORTED_FORMATS:
        print(f"❌ Unsupported format: {ext} - {os.path.basename(image_path)}")
        return False
    
    try:
        # Open image
        img = Image.open(image_path)
        avif_path = os.path.splitext(image_path)[0] + '.avif'
        
        # Save as AVIF
        img.save(avif_path, format='AVIF', quality=AVIF_QUALITY)
        
        # Compare file sizes
        original_size = os.path.getsize(image_path)
        new_size = os.path.getsize(avif_path)
        reduction = ((original_size - new_size) / original_size) * 100
        
        print(f"✅ {os.path.basename(image_path)} -> {os.path.basename(avif_path)} ({reduction:.1f}% smaller)")
        return True
        
    except Exception as e:
        print(f"❌ Error processing {os.path.basename(image_path)}: {e}")
        return False

def main():
    print("=== AVIF Converter ===")
    print(f"Supported formats: {', '.join(SUPPORTED_FORMATS)}")
    print(f"Quality: {AVIF_QUALITY}")
    print("-" * 50)
    
    if len(sys.argv) < 2:
        print("💡 Usage:")
        print("   - Drag & drop files onto the EXE")
        print("   - Or: avif_converter.exe image1.jpg image2.png ...")
        print("\n⏳ Waiting for input or press Enter to exit...")
        input()
        return
    
    # Process all provided files
    files = sys.argv[1:]
    converted_count = 0
    total_files = len(files)
    
    print(f"📂 Processing {total_files} file(s)...\n")
    
    for image_path in files:
        if os.path.isfile(image_path):
            if convert_to_avif(image_path):
                converted_count += 1
        else:
            print(f"❌ File not found: {image_path}")
    
    print("\n" + "="*50)
    print(f"🎉 Done! {converted_count} of {total_files} files converted.")
    
    # Wait for input so window doesn't close immediately
    print("\n⏳ Press Enter to exit...")
    input()

if __name__ == "__main__":
    main()
