import requests
from bs4 import BeautifulSoup
import urllib
import os
from WMOCR import Recognizer

ProductUrl = []
BaseUrl = 'http://www.wi-mobile.com/'
Folders = []
def main():

	search_products_url()
	search_product()
	print(len(Folders))
	extractor = Recognizer(Folders)	
	extractor.extract_pictures_text()

#search for the category of each product in WM products website and gets the URL
def search_products_url():

	response = requests.get(BaseUrl+'{}'.format('es/productos'))
	soup = BeautifulSoup(response.content, 'html.parser')
	product_container = soup.findAll('div',{"class": "leer_mas"})
	
	
	for idx,product in enumerate(product_container):
		
		ProductUrl.append(product.find('a')['href'])
		print('*-----*------*---------**-----*------*---------*')
		print(' ')
		print(ProductUrl[idx])

	

#search for every product in the category
def search_product():
	
	for idx,product in enumerate(ProductUrl):
		response = requests.get(BaseUrl+'{}'.format(ProductUrl[idx]))
		soup = BeautifulSoup(response.content, 'html.parser')
		product_container = soup.find('h2')
		title = product_container.find()['title']
		Folders.append(title)
		print(title)
		product_container = soup.find('div',{'class': 'story_body'})
		print(product_container)
		images_tag = product_container.findAll('img')
		try:
			os.mkdir(title)
		except FileExistsError as e:
			pass

		print('*-----*------*---------**-----*------*---------*')
		print(' ')
		# for idx,url in enumerate(images_tag):
		# 	print(url['src'])
		# 	print(idx)
		# 	fullfilename = os.path.join(title, title+str(idx)+'.jpg')
		# 	urllib.request.urlretrieve(url['src'],fullfilename)

	# for name in folders:
	# 	print(name)
	
		


	
	
	# print('*-----*------*---------**-----*------*---------*')
	# print(' ')
	# for idx,url in enumerate(images_tag):
	# 	print(url['src'])
	# 	print(idx)
	# 	fullfilename = os.path.join(title, title+str(idx)+'.jpg')
	# 	urllib.request.urlretrieve(url['src'],fullfilename)
	
		
	
	

		
	

	# for i in range(1,3):
	# 	response = requests.get('https://xkcd.com/{}'.format(i))
		
	# 	soup = BeautifulSoup(response.content, 'html.parser')
	# 	image_container = soup.find(id='comic')
	# 	image_url = image_container.find('img')['src']
	# 	image_name = image_url.split('/')[-1]
	# 	urllib.request.urlretrieve('https:{}'.format(image_url),image_name)
	# 	print(type(image_url))

if __name__ == '__main__':
	main()