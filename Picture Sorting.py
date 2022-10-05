import os,sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

##############################CHANGE_ACCORDINGLY###################################################
path = f'{os.path.dirname(os.path.abspath(__file__))}\pictures'
path_from_code_to_pics = "pictures/"
common_name = "pictures_"
################################################################################


def comparison(picture1,picture2):
	err = np.sum((picture1.astype("float") - picture2.astype("float")) ** 2)
	err /= float(picture1.shape[0] * picture1.shape[1])
	if err < 275 :
		return "same"
	else:
		return "not same"

def remove_dups(array):
	output = []
	for i in array:
		if i not in output:
			output.append(i)
	return output

pictures = os.listdir(path)

number_of_pics = len(pictures)
pictures_array = []

for i in range(number_of_pics):
	picture_name = pictures[i]
	
	picture = cv2.imread(path_from_code_to_pics + picture_name)[:,:,::-1]
	pic_resize = cv2.resize(picture, dsize=(270,270), fx=5, fy=5, interpolation=cv2.INTER_LINEAR)
	gray_picture = np.mean(pic_resize,2)
	picture = []
	pictures_array.append(gray_picture)
#output: picture array
#--------------------------------------------------------
array_length = len(pictures_array)
i = 0

while i < array_length:
	current_pic = pictures_array[i]
	comparison_pictures = len(pictures_array) - i - 1
	j = i+1
	
	removal = []
	if comparison_pictures > 0:
		for k in range(comparison_pictures):
			comparison_pic = pictures_array[j + k]
			if comparison(current_pic,comparison_pic) == "same":
				removal.append(j + k)
	
	removal = remove_dups(removal)
	for n in range(len(removal)):
		if removal[n] == i:
			i -= 1
		pictures_array.pop(removal[n])
		os.remove(path_from_code_to_pics + pictures[removal[n]])
		pictures.pop(removal[n])
		array_length -= 1
	i += 1

pictures = os.listdir(path)
j = 0
for i in pictures:
	j += 1
	os.rename(path + '/' + i, path + '/' + common_name + str(j) + 'temp.jpg')

pictures = os.listdir(path)
j = 0
for i in pictures:
	j += 1
	os.rename(path + '/' + i, path + '/' + common_name + str(j) + '.jpg')