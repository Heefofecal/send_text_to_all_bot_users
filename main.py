import telebot
bot = telebot.TeleBot("API TOKEN")
text = input(">>Enter text to send to all bot users>>")
with open("database.txt", "r") as file: 
    for line in file: 
        print("Sending text to " + line.replace("\n", ""))
        bot.send_message(line.replace("\n", ""), text)
