from random import random
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import random
import time
import string
import nltk
from replicas import eng1, liza, l1, l11, l2, l21, l3, l31, l4, l41, l5, l51, l6, l61, l7, l71, l8, l81, welcome,welcome1, artemy, artemy1


main_token = 'd67f83db79197faed7c707a243fa66e7e8b02c7d3de626ff29b83eb816396983cac11adb5b7d6b576a1d6'
vk_session = vk_api.VkApi(token = main_token)
longpoll = VkBotLongPoll(vk_session, '198179927')
vk = vk_session.get_api()

def sms(id, msg):
		vk.messages.send(peer_id = id, message = msg, random_id = 0)

def res(response, id, eng1):
	for i in response:
		resul = list(i)
		if 'блины' == i:
			sms(id,'ИНГРЕДИЕНТЫ\nМолоко - 1 стакан\nКуриное яйцо - 1 штука\nСоль - щепотка\nСахар - 1,5 столовые ложки\nПшеничная мука - 8 столовых ложек\nРастительное масло - 1,5 чайные ложки\nРазрыхлитель - на кончике ножа')
			sms(id,'ИНСТРУКЦИЯ ПРИГОТОВЛЕНИЯ\n1. Налить в подходящую емкость молоко комнатной температуры, вбить туда яйца, добавить соль и сахар.\n2. Постепенно подсыпать муку, при этом помешивая, чтобы не получалось комочков. Они все равно будут получаться, так что помешивать надо качественно. Довести до консистенции нежирной сметаны. Добавить разрыхлитель.\n3. Все размешать, оставить на 15–20 минут и потом добавить растительное масло. Кстати, тесто для блинов можно оставить в холодильнике и приготовить блины позже. С ним ничего не случится.\n4. На сильно раскаленную сковороду налить немного масла и жарить блины.')
		if i in welcome:
			sms(id, random.choice(welcome1))
			break
		elif i in artemy:
			sms(id, random.choice(artemy1))
			break
		elif i == 'лиза' or i == 'савина' or i == 'лизка':
			sms(id, random.choice(liza))
			break
		elif i in l1:
			sms(id, random.choice(l11))
			break
		elif i in l2:
			sms(id, random.choice(l21))
			break
		elif i in l3:
			sms(id, random.choice(l31))
			break
		elif i in l4:
			sms(id, random.choice(l41))
			break
		elif i in l5:
			sms(id, random.choice(l51))
			break
		elif i in l6:
			sms(id, random.choice(l61))
			break
		elif i in l7:
			sms(id, random.choice(l71))
			break
		elif i in l8:
			if ('на' in response) or ('в' in response):
				sms(id, random.choice(l81))
				break
	s = 0
	for a in eng1:
		if a in resul:
			s += 1
		else:
			s -= 1
	print(s)
	if s > -25:
		engchance = random.randint(1, 2)
		if engchance == 1:
			vk.messages.send(peer_id=event.obj['peer_id'], message='по русски', random_id=0)
			vk.messages.send(peer_id=event.obj['peer_id'], message='ебат', random_id=0)
			vk.messages.send(peer_id=event.obj['peer_id'], message='пиши', random_id=0)
		else:
			vk.messages.send(peer_id=event.obj['peer_id'], message='человеческим языком можна', random_id=0)




for event in longpoll.listen():
	if (event.type == VkBotEventType.MESSAGE_NEW):
		if event.from_user:
			t = 0
		else:
			t = 4
		response = event.object['text']
		sentences = nltk.sent_tokenize(response)
		for sentence in sentences:
			response = nltk.word_tokenize(sentence)
			print(response)
		id = event.obj['peer_id']
		if random.randint(1, 9) > t:
			time.sleep(random.randint(1, 5))
			res(response, id, eng1)
		print(t)
		
