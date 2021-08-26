from PIL import Image
s = input("Enter the path of the image to be rotated : ")
d = int(input("Enter the degree of rotation of the image : "))
img = Image.open(s)
rotated_img = img.rotate(d)
s1 = input("Enter the path where the image needs to be saved : ")
rotated_img.save(s1)
print("The image is saved in the path")
