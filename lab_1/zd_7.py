from PIL import Image
import os


def jpg_to_png(directory):
    for jpg in directory:
        try:
            image = Image.open(jpg)
            jpg = jpg.replace('.jpg', '.png')
            image.save(jpg)
        except Exception as e:
            print(e)


dir_path = os.path.dirname(os.path.realpath(__file__))
directory = [dir_path + '/pic' + str(f) + '.jpg' for f in range(1, 5)]
jpg_to_png(directory)



