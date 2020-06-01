import requests





def dialog(text):
	url = 'https://api.dialogflow.com/v1/query?v=20150910'
	headers = {'Authorization':'Bearer a1df2bf1addf414cb2ab798bad96a8ff'}
	params = {'lang':'ru','sessionId':'12345','timezone':'Russia/Moscow','query':text}


	r = requests.get(url,headers = headers, params = params)
	

	responce = r.json()['result']['fulfillment']['speech']


	return responce
    
   

if __name__ == '__main__':

	while True:
		c = dialog(input())
		if c:
			print(c)
		else:
			print('Я тебя не понял')


