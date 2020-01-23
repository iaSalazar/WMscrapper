import pytesseract as tess
tess.pytesseract.tesseract_cmd =r'C:\Users\isalazar\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image
import cv2
import numpy as np
import os

Folders = []

class Recognizer:


	"""docstring for recognizer"""
	def __init__(self, data):
		print('Entro carpeta')
		self.Folders = data
		print(len(self.Folders))
		
	def extract_pictures_text(self):
		
		for name in self.Folders:
			print(name)
		for folder in self.Folders:
			i = 0
			for file in os.listdir(folder):
				if file.endswith('jpg'):
					print(file)
					print(i)
					print('ENTROO')
					img = Image.open('{}/{}'.format(folder,file)).convert('L')
					ret,img = cv2.threshold(np.array(img), 237, 255, cv2.THRESH_BINARY)
					print(type(ret))
					print(type(img))
					cv2.imshow("after", img)
					cv2.waitKey(5000)
					text = tess.image_to_string(img)
					text = text.split(' ')
					print(text)
					i+=1
		
		

		# print('ENTROO')
		# img = Image.open('Terminales portátiles para operaciones en campo/Terminales portátiles para operaciones en campo1.jpg').convert('L')
		# ret,img = cv2.threshold(np.array(img), 237, 255, cv2.THRESH_BINARY)
		# print(type(ret))
		# print(type(img))
		# cv2.imshow("after", img)
		# cv2.waitKey(0)
		# text = tess.image_to_string(img)
		# text = text.split(' ')
		# print(text)
		

def main(img):
	print('main program')

if __name__ == '__main__':
	
	main()
