import requests
#print("Hello World!")

#"https://api.telegram.org/bot5725334288:AAF-Kd7nadnASAuMZWLY2ExVGWV1TiNzLvY/sendMessage?chat_id=-704631232&text="
message = input()

r = requests.post("https://api.telegram.org/bot5725334288:AAF-Kd7nadnASAuMZWLY2ExVGWV1TiNzLvY/sendMessage?chat_id=-704631232&text="+message)




