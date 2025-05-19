from PIL import Image
image = Image.new("RGB", (300, 300), "red")
image.save("image_rouge.png")
print("image cree avec succes")
