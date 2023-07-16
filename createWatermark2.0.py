from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

# Definiere den Pfad zum Ordner mit den Bildern
folder_path = r'E:\2016\Brand Sägewerk Wawern'

# Definiere das Wasserzeichen
watermark_text = "©Feuerwehr Kanzem"
opacity = 0.25
font_size = 50

# Definiere die Schriftart und die Größe des Wasserzeichens
font = ImageFont.truetype("arial.ttf", font_size)

# Definiere die Schrittweite des Rasters
step_size = 500

# Gehe durch alle Dateien im Ordner
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        
        # Öffne das Bild und das Wasserzeichen
        image_path = os.path.join(folder_path, filename)
        image = Image.open(image_path)

        # Erstelle eine Kopie des Bildes
        output_image = image.copy()

        # Erstelle ein neues Bild für das Wasserzeichen
        watermark_image = Image.new('RGBA', image.size, (0,0,0,0))
        draw = ImageDraw.Draw(watermark_image)

        # Durchlaufe alle Rasterpositionen
        for x in range(0, image.width, step_size):
            for y in range(0, image.height, step_size):

                # Schreibe das Wasserzeichen auf das Bild
                watermark_width, watermark_height = draw.textsize(watermark_text, font=font)
                if x + watermark_width <= image.width and y + watermark_height <= image.height:
                    draw.text((x, y), watermark_text, fill=(255,255,255,int(255*opacity)), font=font)

        # Füge das Wasserzeichen hinzu
        output_image.paste(watermark_image, (0,0), watermark_image)

        # Speichere das Bild mit dem Wasserzeichen
        output_filename = os.path.splitext(filename)[0] + '_mit_wasserzeichen.jpg'
        output_path = os.path.join(folder_path, output_filename)
        output_image.save(output_path)