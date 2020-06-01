from selenium import webdriver
import time
import pickle
from alise_bot import dialog

driver = webdriver.Chrome()

#try:
	#cookies = pickle.load(open("cookies.pkl", "rb"))
	#driver.get('https://vk.com')
	#for cookie in cookies:
		#if 'expiry' in cookie:
			#cookie['expiry'] = int(cookie['expiry'])
		#driver.add_cookie(cookie)
	#driver.get('https://vk.com')


#except:
	#driver.get('https://vk.com')
	#phone = driver.find_element_by_id('index_email')
	#phone.clear()
	#phone.send_keys('79959718311')
	#time.sleep(5)

	#password = driver.find_element_by_id('index_pass')
	#password.clear()
	#password.send_keys('CHKryu50zh')
	#time.sleep(6)

	#logining = driver.find_element_by_id('index_login_button')
	#logining.click()

	#pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

driver.get('https://vk.com')

phone = '79959718311'
password = 'CHKryu50zh'

def autorization(phon,passw):
	phone = driver.find_element_by_id('index_email')
	phone.clear()
	phone.send_keys(phon)
	time.sleep(5)

	password = driver.find_element_by_id('index_pass')
	password.clear()
	password.send_keys(passw)
	time.sleep(6)

	logining = driver.find_element_by_id('index_login_button')
	logining.click()




def send_massage(resp):
	input_mas = driver.find_element_by_id('im_editable0')
	input_mas.clear()
	input_mas.send_keys(resp)
	time.sleep(6)
	mas_send = driver.find_element_by_class_name('im-send-btn_send')
	mas_send.click()




#pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))



def click_mass():
	msg = driver.find_element_by_id('l_msg')
	msg.click()
	time.sleep(10)

def resp_mass():
	while True:
		for i in driver.find_elements_by_class_name('nim-dialog_unread'):
			i.click()
			time.sleep(5)
			unread_msg = driver.find_elements_by_class_name('_im_mess_stack')[-1].find_elements_by_class_name('im-mess')
			for i in unread_msg:
				print(i.text)
				resp = dialog(i.text)
				time.sleep(5)
				print(resp)
				send_massage(resp)
				time.sleep(5)

		click_mass()

if __name__ == '__main__':

	autorization(phone,password)
	time.sleep(5)

	click_mass()
	time.sleep(5)

	resp_mass()
	time.sleep(5)













	






    	



