import telebot

bot = telebot.TeleBot('1021427945:AAHmr-U5_EkQZ9O3lKRtOJrl3QFvG2pcbiM')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
					# # # KEYBOARDS # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	### ГЛАВНОЕ МЕНЮ ###
keymain = telebot.types.ReplyKeyboardMarkup(True)
keymain.row('🎁Готовые клады🎁')
keymain.row('💰Прайс💰', '♨️Конкурсы♨️')
keymain.row('👥Оператор👥')
keymain.row('📢Канал📢', '💬Чат💬')


	### ПРАЙСЛИСТ ###
keypr = telebot.types.ReplyKeyboardMarkup(True, True)
keypr.row('⚜️Амф⚜️')
keypr.row('⚜️Шиш⚜️')
keypr.row('🔙 Назад', '🏠В начало')

	### ВОЗВРАТ ###
keyback = telebot.types.ReplyKeyboardMarkup(True, True)
keyback.row('🔙 Назад', '🏠В начало')


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, '🇺🇦🇺🇦🇺🇦', reply_markup=keymain)
    bot.send_message(message.chat.id, 'Добро пожаловать ✋✋✋‼️')        
    bot.send_message(message.chat.id, 'Здесь ты можешь увидить: ▪️Актуальный прайс ▪️Нужную информацию ▪️Ссылки ▪️Конкурсы ‼️')
    bot.send_message(message.chat.id, '💠 ГЛАВНОЕ МЕНЮ 💠')



@bot.message_handler(content_types=['text'])
def menu(message):
    if message.text.lower() == '👥оператор👥':
    	bot.send_message(message.chat.id, '🔻 🔻 🔻 🔻 🔻', reply_markup=keyback)
    	bot.send_message(message.chat.id, '@MarihuanichVN', reply_markup=keyback)
    	bot.send_message(message.chat.id, '🔺 🔺 🔺 🔺 🔺', reply_markup=keyback)
    elif message.text.lower() == '🏠в начало':
    	welcome(message)
    elif message.text.lower() == '🔙 назад':
    	welcome(message)
    elif message.text.lower() == '🎁готовые клады🎁':
    	bot.send_message(message.chat.id, 'В разработке...', reply_markup=keyback)
    elif message.text.lower() == '📢канал📢':
    	bot.send_message(message.chat.id, '🔻 📢 🔻 📢 🔻', reply_markup=keyback)
    	bot.send_message(message.chat.id, 'https://t.me/joinchat/AAAAAFRjHu7EK534BY23RQ', reply_markup=keyback)
    	bot.send_message(message.chat.id, '📢 🔺 📢 🔺 📢', reply_markup=keyback)
    elif message.text.lower() == '💬чат💬':
    	bot.send_message(message.chat.id, '🔻 💬 🔻 💬 🔻', reply_markup=keyback)
    	bot.send_message(message.chat.id, 'https://t.me/joinchat/MniU9hWuby3gQK25ngMj1w', reply_markup=keyback)
    	bot.send_message(message.chat.id, '💬 🔺 💬 🔺 💬', reply_markup=keyback)
    elif message.text.lower() == '♨️конкурсы♨️':
    	bot.send_message(message.chat.id, '❌', reply_markup=keyback)
    elif message.text.lower() == '💰прайс💰':
    	bot.send_message(message.chat.id, 'Актуальный прайс: ', reply_markup=keypr)
    elif message.text.lower() == '⚜️амф⚜️':
    	bot.send_message(message.chat.id, '💠0.25 - 💠0.5 - 💠1 - 💠3 - 💠5 - 💠10 -', reply_markup=keyback)
    elif message.text.lower() == '⚜️шиш⚜️':
    	bot.send_message(message.chat.id, '💠0.5 - 💠1 - 💠3 - 💠5 - 💠10 -', reply_markup=keyback)
bot.polling()