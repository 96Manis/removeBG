from rembg import remove
import easygui
from PIL import Image

inputPath = easygui.fileopenbox(title='Select the image file')
outputPath = easygui.filesavebox(title='Save the file to..')

input = Image.open(inputPath)
output = remove(input)

output.save(outputPath)