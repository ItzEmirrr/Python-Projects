import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot('6921560048:AAFHCkTFrYye7mnQM0D9DDdDThQ-5Dg8ub8')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}, if you want to order a project, please write /menu')


    # MARKETING DATABASE
    conn_marketing = sqlite3.connect('marketing_members.sql')
    cur_marketing = conn_marketing.cursor()
    cur_marketing.execute(
        'CREATE TABLE IF NOT EXISTS users_marketing(id int auto_increment primary key, name VARCHAR(50), pass VARCHAR(50), proj_name VARCHAR(50), details VARCHAR(50), deadline VARCHAR(50))')

    conn_marketing.commit()
    cur_marketing.close()
    conn_marketing.close()


    # COMMERCE DATABASE
    conn_commerce = sqlite3.connect('commerce_members.sql')
    cur_commerce = conn_commerce.cursor()
    cur_commerce.execute(
        'CREATE TABLE IF NOT EXISTS users_commerce(id int auto_increment primary key, name VARCHAR(50), pass VARCHAR(50), proj_name VARCHAR(50), details VARCHAR(50), deadline VARCHAR(50))')

    conn_commerce.commit()
    cur_commerce.close()
    conn_commerce.close()


    # EDUCATION DATABASE
    conn_education = sqlite3.connect('education_members.sql')
    cur_education = conn_education.cursor()
    cur_education.execute('CREATE TABLE IF NOT EXISTS users_education(id int auto_increment primary key, name VARCHAR(50), pass VARCHAR(50), proj_name VARCHAR(50), details VARCHAR(50), deadline VARCHAR(50))')

    conn_education.commit()
    cur_education.close()
    conn_education.close()


@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.InlineKeyboardMarkup()
    marketing_button = types.InlineKeyboardButton('ELIF Marketing', callback_data='marketing')
    commerce_button = types.InlineKeyboardButton('ELIF Commerce', callback_data='commerce')
    education_button = types.InlineKeyboardButton('ELIF Education', callback_data='education')

    markup.row(marketing_button, commerce_button, education_button)
    bot.reply_to(message, 'Please select the team from which you would like to order the project', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):


    if callback.data == 'marketing':
        markup = types.InlineKeyboardMarkup()
        order_marketing = types.InlineKeyboardButton('Order', callback_data='order_marketing')
        markup.row(order_marketing)
        bot.send_message(callback.message.chat.id, 'You have chosen <b>ELIF Marketing</b>', parse_mode='html',
                         reply_markup=markup)
    elif callback.data == 'commerce':
        markup = types.InlineKeyboardMarkup()
        order_commerce = types.InlineKeyboardButton('Order', callback_data='order_commerce')
        markup.row(order_commerce)
        bot.send_message(callback.message.chat.id, 'You have chosen <b>ELIF Commerce</b>', parse_mode='html',
                         reply_markup=markup)
    elif callback.data == 'education':
        markup = types.InlineKeyboardMarkup()
        order_education = types.InlineKeyboardButton('Order', callback_data='order_education')
        markup.row(order_education)
        bot.send_message(callback.message.chat.id, 'You have chosen <b>ELIF Education</b>', parse_mode='html', reply_markup=markup)



    elif callback.data == 'order_marketing':
        conn_marketing = sqlite3.connect('marketing_members.sql')
        cur_marketing = conn_marketing.cursor()
        cur_marketing.execute(
            'CREATE TABLE IF NOT EXISTS users_marketing(id int auto_increment primary key, name VARCHAR(50), pass VARCHAR(50), proj_name VARCHAR(50), details VARCHAR(50), deadline VARCHAR(50))')

        conn_marketing.commit()
        cur_marketing.close()
        conn_marketing.close()

        bot.send_message(callback.message.chat.id, "Let's start the ordering process. First, enter your name.")
        bot.register_next_step_handler(callback.message, process_order_marketing_name)

    elif callback.data == 'order_commerce':
        conn_commerce = sqlite3.connect('commerce_members.sql')
        cur_commerce = conn_commerce.cursor()
        cur_commerce.execute(
            'CREATE TABLE IF NOT EXISTS users_commerce(id int auto_increment primary key, name VARCHAR(50), pass VARCHAR(50), proj_name VARCHAR(50), details VARCHAR(50), deadline VARCHAR(50))')

        conn_commerce.commit()
        cur_commerce.close()
        conn_commerce.close()

        bot.send_message(callback.message.chat.id, "Let's start the ordering process. First, enter your name.")
        bot.register_next_step_handler(callback.message, process_order_commerce_name)

    elif callback.data == 'order_education':
        conn_education = sqlite3.connect('education_members.sql')
        cur_education = conn_education.cursor()
        cur_education.execute(
            'CREATE TABLE IF NOT EXISTS users_education(id int auto_increment primary key, name VARCHAR(50), pass VARCHAR(50), proj_name VARCHAR(50), details VARCHAR(50), deadline VARCHAR(50))')

        conn_education.commit()
        cur_education.close()
        conn_education.close()

        bot.send_message(callback.message.chat.id, "Let's start the ordering process. First, enter your name.")
        bot.register_next_step_handler(callback.message, process_order_education_name)

def process_order_marketing_name(message):
    name = message.text
    bot.send_message(message.chat.id, "Great! Now, enter your password.")
    bot.register_next_step_handler(message, process_order_marketing_pass, name)

def process_order_marketing_pass(message, name):
    password = message.text
    bot.send_message(message.chat.id, "Awesome! Now, enter the name of the project.")
    bot.register_next_step_handler(message, process_order_marketing_proj_name, name, password)

def process_order_marketing_proj_name(message, name, password):
    project_name = message.text
    bot.send_message(message.chat.id, "Got it! Next, enter the details of the project.")
    bot.register_next_step_handler(message, process_order_marketing_details, name, password, project_name)


def process_order_marketing_details(message, name, password, project_name):
    details = message.text
    bot.send_message(message.chat.id, "Excellent! Finally, enter the deadline for the project")
    bot.register_next_step_handler(message, process_order_marketing_deadline, name, password, project_name, details)

def process_order_marketing_deadline(message, name, password, project_name, details):
    deadline = message.text

    conn_marketing = sqlite3.connect('marketing_members.sql')
    cur_marketing = conn_marketing.cursor()
    cur_marketing.execute("INSERT INTO users_marketing (name, pass, proj_name, details, deadline) VALUES (?, ?, ?, ?, ?)",
                          (name, password, project_name, details, deadline))
    conn_marketing.commit()
    cur_marketing.close()
    conn_marketing.close()

    bot.send_message(message.chat.id, "Registration complete! Your order has been placed.")


def process_order_commerce_name(message):
    name = message.text
    bot.send_message(message.chat.id, "Great! Now, enter your password.")
    bot.register_next_step_handler(message, process_order_commerce_pass, name)


def process_order_commerce_pass(message, name):
    password = message.text
    bot.send_message(message.chat.id, "Awesome! Now, enter the name of the project.")
    bot.register_next_step_handler(message, process_order_commerce_proj_name, name, password)


def process_order_commerce_proj_name(message, name, password):
    project_name = message.text
    bot.send_message(message.chat.id, "Got it! Next, enter the details of the project.")
    bot.register_next_step_handler(message, process_order_commerce_details, name, password, project_name)


def process_order_commerce_details(message, name, password, project_name):
    details = message.text
    bot.send_message(message.chat.id, "Excellent! Finally, enter the deadline for the project")
    bot.register_next_step_handler(message, process_order_commerce_deadline, name, password, project_name, details)



def process_order_commerce_deadline(message, name, password, project_name, details):
    deadline = message.text

    conn_commerce = sqlite3.connect('commerce_members.sql')
    cur_commerce = conn_commerce.cursor()
    cur_commerce.execute("INSERT INTO users_commerce (name, pass, proj_name, details, deadline) VALUES (?, ?, ?, ?, ?)",
                          (name, password, project_name, details, deadline))
    conn_commerce.commit()
    cur_commerce.close()
    conn_commerce.close()

    bot.send_message(message.chat.id, "Registration complete! Your order has been placed.")



def process_order_education_name(message):
    name = message.text
    bot.send_message(message.chat.id, "Great! Now, enter your password.")
    bot.register_next_step_handler(message, process_order_education_pass, name)


def process_order_education_pass(message, name):
    password = message.text
    bot.send_message(message.chat.id, "Awesome! Now, enter the name of the project.")
    bot.register_next_step_handler(message, process_order_education_proj_name, name, password)


def process_order_education_proj_name(message, name, password):
    project_name = message.text
    bot.send_message(message.chat.id, "Got it! Next, enter the details of the project.")
    bot.register_next_step_handler(message, process_order_education_details, name, password, project_name)


def process_order_education_details(message, name, password, project_name):
    details = message.text
    bot.send_message(message.chat.id, "Excellent! Finally, enter the deadline for the project")
    bot.register_next_step_handler(message, process_order_education_deadline, name, password, project_name, details)


def process_order_education_deadline(message, name, password, project_name, details):
    deadline = message.text

    conn_education = sqlite3.connect('education_members.sql')
    cur_education = conn_education.cursor()
    cur_education.execute("INSERT INTO users_education (name, pass, proj_name, details, deadline) VALUES (?, ?, ?, ?, ?)",
                          (name, password, project_name, details, deadline))
    conn_education.commit()
    cur_education.close()
    conn_education.close()

    bot.send_message(message.chat.id, "Registration complete! Your order has been placed.")


def is_admin_user(user_id):
    return user_id == 1373109311

@bot.message_handler(commands=['admin_init'])
def admin_init(message):
    conn_stuff = sqlite3.connect('stuff.sql')
    cur_stuff = conn_stuff.cursor()
    cur_stuff.execute('''
        CREATE TABLE IF NOT EXISTS stuff (
            id INTEGER PRIMARY KEY,
            name VARCHAR(50),
            surname VARCHAR(50),
            password VARCHAR(50),
            customer_name VARCHAR(50),
            project_name VARCHAR(50),
            project_details VARCHAR(50),
            deadline VARCHAR(50),
            department VARCHAR(50)
        )
    ''')
    conn_stuff.commit()
    cur_stuff.close()
    conn_stuff.close()
    user_id = message.from_user.id

    if is_admin_user(user_id):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1)
        marketing_button = types.KeyboardButton('ELIF Marketing')
        commerce_button = types.KeyboardButton('ELIF Commerce')
        education_button = types.KeyboardButton('ELIF Education')
        markup.add(marketing_button, commerce_button, education_button)
        bot.send_message(message.chat.id, 'Please choose a company:', reply_markup=markup)

        bot.register_next_step_handler(message, admin_choose_company)
    else:
        bot.send_message(message.chat.id, 'You are not authorized to perform this action.')



def admin_choose_company(message):
    company_name = message.text

    if company_name == 'ELIF Marketing':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add(types.KeyboardButton('Show customers'))
        markup.add(types.KeyboardButton('Stuff'))
        bot.send_message(message.chat.id, 'Choose action:', reply_markup=markup)
        bot.register_next_step_handler(message, admin_mark_action)

    elif company_name == 'ELIF Commerce':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add(types.KeyboardButton('Show customers'))
        markup.add(types.KeyboardButton('Stuff'))
        bot.send_message(message.chat.id, 'Choose action:', reply_markup=markup)
        bot.register_next_step_handler(message, admin_comm_action)

    elif company_name == 'ELIF Education':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add(types.KeyboardButton('Show customers'))
        markup.add(types.KeyboardButton('Stuff'))
        bot.send_message(message.chat.id, 'Choose action:', reply_markup=markup)
        bot.register_next_step_handler(message, admin_edu_action)






def admin_mark_action(message):
    action = message.text

    if action == 'Show customers':
        conn_marketing = sqlite3.connect('marketing_members.sql')
        cur_marketing = conn_marketing.cursor()
        cur_marketing.execute("SELECT name FROM users_marketing")
        users = cur_marketing.fetchall()

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        buttons = [types.KeyboardButton(row[0]) for row in users]
        markup.add(*buttons)

        bot.send_message(message.chat.id, 'Choose customer', reply_markup=markup)

        conn_marketing.close()
        bot.register_next_step_handler(message, admin_mark_customer_details)

    elif action == 'Stuff':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,row_width=3)
        markup.add(types.KeyboardButton("Add stuff"))
        markup.add(types.KeyboardButton("Fire stuff"))
        markup.add(types.KeyboardButton("Show stuff"))
        bot.send_message(message.chat.id, "Choose action", reply_markup=markup)

        bot.register_next_step_handler(message, admin_choose_mark_action_stuff)


def admin_choose_mark_action_stuff(message):
    action = message.text

    if action == 'Add stuff':
        conn_stuff = sqlite3.connect('stuff.sql')
        cur_stuff = conn_stuff.cursor()
        cur_stuff.execute('''
            CREATE TABLE IF NOT EXISTS stuff (
                id INTEGER PRIMARY KEY,
                name VARCHAR(50),
                surname VARCHAR(50),
                password VARCHAR(50),
                customer_name VARCHAR(50),
                project_name VARCHAR(50),
                project_details VARCHAR(50),
                deadline VARCHAR(50),
                department VARCHAR(50)
            )
        ''')
        conn_stuff.commit()
        cur_stuff.close()
        conn_stuff.close()

        bot.send_message(message.chat.id, "Let's start stuff adding process. First, employee's id")
        bot.register_next_step_handler(message, add_marketing_stuff_id)

    elif action == 'Fire stuff':
        conn_stuff = sqlite3.connect('stuff.sql')
        cur_stuff = conn_stuff.cursor()
        cur_stuff.execute("SELECT name FROM stuff")

        selected_stuff = cur_stuff.fetchall()
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        buttons = [types.KeyboardButton(f"{row[0]}") for row in selected_stuff]
        markup.add(*buttons)

        bot.send_message(message.chat.id, 'Choose employee', reply_markup=markup)

        conn_stuff.close()
        bot.register_next_step_handler(message, admin_delete_stuff)

    elif action == 'Show stuff':
        conn_stuff = sqlite3.connect('stuff.sql')
        cur_stuff = conn_stuff.cursor()
        cur_stuff.execute("SELECT name FROM stuff")

        selected_stuff = cur_stuff.fetchall()
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        buttons = [types.KeyboardButton(f"{row[0]}") for row in selected_stuff]
        markup.add(*buttons)

        bot.send_message(message.chat.id, 'Choose employee', reply_markup=markup)

        conn_stuff.close()
        bot.register_next_step_handler(message, stuff_details)


def stuff_details(message):
    conn_stuff = sqlite3.connect('stuff.sql')
    cur_stuff = conn_stuff.cursor()
    cur_stuff.execute("SELECT * FROM stuff WHERE name=?", (message.text,))
    customer_details = cur_stuff.fetchone()

    if customer_details:
        info = (
            f"The full information:\nID: {customer_details[0]}\nNAME: {customer_details[1]}\nSURNAME: {customer_details[2]}\nPASSWORD: {customer_details[3]}\nPROJECT NAME: {customer_details[4]}\nPROJECT DETAILS: {customer_details[5]}\nDEADLINE OF THE PROJECT: {customer_details[6]}")

        bot.send_message(message.chat.id, info, parse_mode='Markdown')




def admin_delete_stuff(message):
    selected_employee = message.text

    conn_stuff = sqlite3.connect('stuff.sql')
    cur_stuff = conn_stuff.cursor()

    cur_stuff.execute("DELETE FROM stuff WHERE name=?", (selected_employee,))

    conn_stuff.commit()
    conn_stuff.close()

    bot.send_message(message.chat.id, f'{selected_employee} has been deleted from the database.')



def add_marketing_stuff_id(message):
    id_stuff = message.text
    bot.send_message(message.chat.id, "Enter employee's name")
    bot.register_next_step_handler(message, add_marketing_stuff_name, id_stuff)


def add_marketing_stuff_name(message, id_stuff):
    name = message.text.capitalize()
    bot.send_message(message.chat.id, "Great! Now, enter employee's surname.")
    bot.register_next_step_handler(message, add_marketing_stuff_surname, id_stuff, name)


def add_marketing_stuff_surname(message, id_stuff, name):
    surname = message.text.capitalize()
    bot.send_message(message.chat.id, "Now, enter your password")
    bot.register_next_step_handler(message, add_marketing_stuff_pass, id_stuff, name, surname)


def add_marketing_stuff_pass(message, id_stuff, name, surname):
    password = message.text
    bot.send_message(message.chat.id, "Enter employee's department")
    bot.register_next_step_handler(message, add_marketing_stuff_department, id_stuff, name, surname, password)


def add_marketing_stuff_department(message, id_stuff, name, surname, password):
    department = message.text.capitalize()

    conn_stuff = sqlite3.connect('stuff.sql')
    cur_stuff = conn_stuff.cursor()
    cur_stuff.execute("INSERT INTO stuff(id, name, surname, password, department) VALUES (?, ?, ?, ?, ?)", (id_stuff, name, surname, password, department))

    conn_stuff.commit()
    cur_stuff.close()
    conn_stuff.close()

    bot.send_message(message.chat.id, "Employee has been added")

def admin_comm_action(message):
    conn_commerce = sqlite3.connect('commerce_members.sql')
    cur_commerce = conn_commerce.cursor()
    cur_commerce.execute("SELECT name FROM users_commerce")
    users = cur_commerce.fetchall()

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    buttons = [types.KeyboardButton(row[0]) for row in users]
    markup.add(*buttons)

    bot.send_message(message.chat.id, 'Choose customer', reply_markup=markup)

    conn_commerce.close()
    bot.register_next_step_handler(message, admin_comm_customer_details)

def admin_edu_action(message):
    action = message.text

    if action == 'Show customers':
        conn_education = sqlite3.connect('education_members.sql')
        cur_education = conn_education.cursor()
        cur_education.execute("SELECT name FROM users_education")
        users = cur_education.fetchall()

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        buttons = [types.KeyboardButton(row[0]) for row in users]
        markup.add(*buttons)

        bot.send_message(message.chat.id, 'Choose customer', reply_markup=markup)

        conn_education.close()
        bot.register_next_step_handler(message, admin_edu_customer_details)

def admin_mark_customer_details(message):
    conn_marketing = sqlite3.connect('marketing_members.sql')
    cur_marketing = conn_marketing.cursor()
    cur_marketing.execute("SELECT * FROM users_marketing WHERE name=?", (message.text,))
    customer_details = cur_marketing.fetchone()

    if customer_details:
        info = (
            f"The full information:\nID: {customer_details[0]}\nNAME: {customer_details[1]}\nPASSWORD: {customer_details[2]}\nPROJECT NAME: {customer_details[3]}\nPROJECT DETAILS: {customer_details[4]}\nDEADLINE OF THE PROJECT: {customer_details[5]}")

        bot.send_message(message.chat.id, info, parse_mode='Markdown')

def admin_comm_customer_details(message):
    conn_commerce = sqlite3.connect('commerce_members.sql')
    cur_commerce = conn_commerce.cursor()
    cur_commerce.execute("SELECT * FROM users_commerce WHERE name=?", (message.text,))
    customer_details = cur_commerce.fetchone()

    if customer_details:
        info = (
            f"The full information:\nID: {customer_details[0]}\nNAME: {customer_details[1]}\nPASSWORD: {customer_details[2]}\nPROJECT NAME: {customer_details[3]}\nPROJECT DETAILS: {customer_details[4]}\nDEADLINE OF THE PROJECT: {customer_details[5]}")

        bot.send_message(message.chat.id, info, parse_mode='Markdown')

def admin_edu_customer_details(message):
    conn_education = sqlite3.connect('education_members.sql')
    cur_education = conn_education.cursor()
    cur_education.execute("SELECT * FROM users_education WHERE name=?", (message.text,))
    customer_details = cur_education.fetchone()

    if customer_details:
        info = (
            f"The full information:\nID: {customer_details[0]}\nNAME: {customer_details[1]}\nPASSWORD: {customer_details[2]}\nPROJECT NAME: {customer_details[3]}\nPROJECT DETAILS: {customer_details[4]}\nDEADLINE OF THE PROJECT: {customer_details[5]}")

        bot.send_message(message.chat.id, info, parse_mode='Markdown')



bot.polling(none_stop=True)
