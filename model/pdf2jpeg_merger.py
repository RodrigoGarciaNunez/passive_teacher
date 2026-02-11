import fitz
from PIL import Image
import os



class merger:
    def __init__(self, file):
        self.file  = file

    def converts_pdf2jpg(self):

        file = fitz.open(self.file)
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
        merged_image.save(merged_image_name)


        return os.path.abspath(merged_image_name)


if __name__=='__main__':
    import sys

    file = sys.argv[1]
    print(file)
    mrg = merger(file)
    returned  = mrg.converts_pdf2jpg()
    print(returned)