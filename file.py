import time
import requests
from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from proxy_info import login, password

from selenium.webdriver.common.proxy import Proxy, ProxyType


headers = {
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}

proxies = {
	'https' : f'http://{login}:{password}@191.101.148.56:45785'
}


proxy_ip_port = '191.101.148.56:45785'

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

def get_location(url):
	response = requests.get(url=url, headers=headers, proxies=proxies)
	soup = BeautifulSoup(response.text, 'lxml')

	ip = soup.find('div', class_='ip').text.strip()
	location = soup.find('div', class_='value-country').text.strip()
	print(f'IP:{ip}\nLocation: {location}')

def get_data_with_selenium(url):
	options = webdriver.ChromeOptions()
	
	
	
	try:
		driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), desired_capabilities=capabilities,
			options=options,  
		)
			
		

		driver.get(url=url)
		time.sleep(500000)
	except Exception as ex:
		print(ex)

def main():
	get_location(url='https://2ip.ru')
	get_data_with_selenium('https://2ip.ru')

if __name__ == '__main__':
	main()

