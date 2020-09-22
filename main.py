import requests


def stringparse():
		
	string = input('Please provide a shopify store to generate an account, format: [https://www.kith.com/] ')
		
	if string == 'https://www.cncpts.com/':
		print("We currently don't support Concepts account creation as they require a captcha.")

	try:
		start = string.find('www.') + len('www.')
		end = string.find('.com/')

		modified_string = string[start:end]

		print(f'Creating an account for {modified_string}..')

		url = f'https://{modified_string}.com/account'

		data = {
				'form_type': 'create_customer', 
			
				'utf8': '✓', 
			
				'customer[first_name]': '{your first name}', 
			
				'customer[last_name]': '{your last name}', 
			
				'customer[email]': '{your email}', 

				'customer[password]': '{your password}'
				}

	
		x = requests.post(url, data=data)

		
		if x.status_code == 200:
			print('Success!')
		else:
			print('We ran into an error, an account has not been generated. ')
	except:
		print('We seem to have run into an error. This could be due to a proxy issue, link issue, or connection issue.')

stringparse()
