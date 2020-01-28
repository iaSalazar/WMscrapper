import pytesseract as tess
tess.pytesseract.tesseract_cmd =r'C:\Users\isalazar\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image
import cv2
import numpy as np
import os
import csv
import pandas as pd
import pathlib

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
					#after_path = str(folder)+'/after-'+str(i)+str(file)
					after_path = 'afterPics/'+str(i)+str(file)
					print(after_path)
					cv2.imwrite(after_path,img)
					cv2.imshow("after", img)
					cv2.waitKey(2000)
					text = tess.image_to_string(img)
					text = text.split(' ')
					print('TEXTOOOOOOOO')
					print(text)
					i+=1
					self.save_info(folder,text)
		#self.unify_csv(folder)

	def unify_csv(self,folder):
		csv_files = []
		for folder in self.Folders:
			i = 0
			for file in os.listdir(folder):
				if file.endswith('csv'):
					print('ARCHIVOOOO')
					print(file)
					csv_files.append(pathlib.PurePath(folder, file))
		combined_csv = pd.concat([pd.read_csv(f) for f in csv_files])
		combined_csv.to_csv( "combined_csv.csv", index=False )
			
	def save_info(self,folder,text):
		with open('{}/productos.csv'.format(folder),'w') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=',',quotechar='|')
			filewriter.writerow([folder])
			filewriter.writerow(text)

def main(img):
	print('main program')

if __name__ == '__main__':
	
	main()
