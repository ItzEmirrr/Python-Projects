import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot('6806298603:AAENzni2nCPxqkX2-h8SdixghMKyT_qw8Zg')
name = ''
password = ''


@bot.message_handler(commands=['start', 'main'])
def start(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')
    conn = sqlite3.connect('hello_world_members.sql')
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users(id int auto_increment primary key, name VARCHAR(50), pass VARCHAR(50), proj VARCHAR(50))')

    conn.commit()
    cur.close()
    conn.close()


@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.InlineKeyboardMarkup()
    hw_button = types.InlineKeyboardButton('Hello World Team', callback_data='hw')
    ps_button = types.InlineKeyboardButton('Python Snakes Team', callback_data='ps')
    markup.row(hw_button, ps_button)
    bot.reply_to(message, 'Choose which team would you like to join?', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'hw':
        markup = types.InlineKeyboardMarkup()
        join_hw_button = types.InlineKeyboardButton('Join', callback_data='join_hw')
        show_hw_button = types.InlineKeyboardButton('Show members', callback_data='users')
        markup.row(join_hw_button, show_hw_button)
        bot.send_message(callback.message.chat.id, 'It is <b>Hello World Team</b>', parse_mode='html',
                         reply_markup=markup)
    elif callback.data == 'ps':
        markup = types.InlineKeyboardMarkup()
        join_ps_button = types.InlineKeyboardButton('Join', callback_data='join_ps')
        show_ps_button = types.InlineKeyboardButton('Show members', callback_data='users')
        markup.row(join_ps_button, show_ps_button)
        bot.send_message(callback.message.chat.id, 'It is <b>Python Snakes Team</b>', parse_mode='html',
                         reply_markup=markup)
    elif callback.data == 'users':
        conn = sqlite3.connect('hello_world_members.sql')
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()

        info = ''
        for el in users:
            info += f'Name: {el[1]}, password: {el[2]}, project name: {el[3]}\n'

        cur.close()
        conn.close()

        bot.send_message(callback.message.chat.id, info)

    elif callback.data == 'join_hw' or 'join_ps':
        bot.send_message(callback.message.chat.id,
                         "Conditions for joining our team: you must have your own project. If you have, please write /register")


@bot.message_handler(commands=['register'])
def start_registration(message):
    conn = sqlite3.connect('hello_world_members.sql')
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users(id int auto_increment primary key, name VARCHAR(50), pass VARCHAR(50), proj VARCHAR(50))')

    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, "Let's start our registration process. First, enter your name")
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Write your password')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    global password
    password = message.text.strip()
    bot.send_message(message.chat.id, 'Write the name of your project')
    bot.register_next_step_handler(message, user_project)


def user_project(message):
    project = message.text.strip()

    conn = sqlite3.connect('hello_world_members.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users(name, pass, proj) VALUES ('%s', '%s', '%s')" % (name, password, project))
    conn.commit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Member list', callback_data='users'))
    bot.send_message(message.chat.id, 'User have been registered', reply_markup=markup)


bot.polling(none_stop=True)
