from PIL import Image

#define colors
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

#access to tuples
im = Image.open("old_image3.jpg")
data = im.getdata()
data_list = list(data)

data_list

#changing tuples by color
picture_list = []
for tuple in data_list:
	total = tuple[0] + tuple[1] + tuple[2]
	if total < 182:
		picture_list.append(darkBlue)
	elif total > 182 and total <= 364:
		picture_list.append(red)
	elif total > 364 and total <= 546:
		picture_list.append(lightBlue)
	else:
		picture_list.append(yellow)

#actually creating new image with data from appended tuples
new_image = Image.new("RGB", (960, 720), "white")
new_image.putdata(picture_list)

new_image.show()