import fitz
from PIL import Image, ImageGrab
import os
import subprocess


class image_manager:
    def __init__(self):
        pass

    def converts_pdf2jpg(self, file):

        file = fitz.open(file)
        images = []             
        for page_num in range(len(file)):
            page = file.load_page(page_num)

            #renderiza la pagina a un mapa de pixeles

            pixmap = page.get_pixmap(dpi=150)

            output_image_file = os.path.join('temp_files', f'page_{page_num+1}.jpg')

            images.append(output_image_file)

            pixmap.save(output_image_file,'jpeg' )


        file.close()
        
        images_to_merge = [Image.open(img) for img in images]

        max_width = max(img.width for img in images_to_merge)
        total_height = sum(img.height for img in images_to_merge)

        merged_image = Image.new('RGB', (max_width, total_height))


        y_offset = 0
        for img in images_to_merge:
            merged_image.paste(img, (0, y_offset))
            y_offset += img.height

        # Save the result
        merged_image_name = 'temp_files/merged_cs.jpg'
        merged_image.save(merged_image_name, 'jpeg', quality=200)


        return os.path.abspath(merged_image_name)
    

    def copy_image_2_clipboard(self, image_path):
        # img = ImageGrab.grabclipboard()  # This gets the image from clipboard

        # img.save(image_path, 'PNG')  

        # if img is None:
        #     print("No image found in clipboard.")
        
        subprocess.run([ 'xclip', '-selection', 'clipboard', '-target', 'image/png', '-i', image_path])  #it works

        return


if __name__=='__main__':
    import sys

    file = sys.argv[1]
    print(file)
    mrg = image_manager()
    returned  = mrg.converts_pdf2jpg(file)
    print(returned)