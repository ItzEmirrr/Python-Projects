        marketing_button = types.KeyboardButton('ELIF Marketing')
        commerce_button = types.KeyboardButton('ELIF Commerce')
        education_button = types.KeyboardButton('ELIF Education')
        markup.add(marketing_button, commerce_button, education_button)
        bot.send_message(message.chat.id, 'Please choose a company:', reply_markup=markup)

        bot.register_next_step_handler(message, admin_choose_mark_action)
    else:
        bot.send_message(message.chat.id, 'You are not authorized to perform this action.')

def admin_choose_mark_action(message):
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
            f"The full infomation:ID: {customer_details[0]}\nNAME: {customer_details[1]}\nPASSWORD: {customer_details[2]}\nPROJECT NAME: {customer_details[3]}\nPROJECT DETAILS: {customer_details[4]}\nDEADLINE OF THE PROLECT: {customer_details[5]}")

        bot.send_message(message.chat.id, info, parse_mode='Markdown')


def admin_comm_customer_details(message):
    conn_commerce = sqlite3.connect('commerce_members.sql')
    cur_commerce = conn_commerce.cursor()
    cur_commerce.execute("SELECT * FROM users_commerce WHERE name=?", (message.text,))
    customer_details = cur_commerce.fetchone()

    if customer_details:
        info = (
            f"The full infomation:ID: {customer_details[0]}\nNAME: {customer_details[1]}\nPASSWORD: {customer_details[2]}\nPROJECT NAME: {customer_details[3]}\nPROJECT DETAILS: {customer_details[4]}\nDEADLINE OF THE PROLECT: {customer_details[5]}")

        bot.send_message(message.chat.id, info, parse_mode='Markdown')



def admin_edu_customer_details(message):
    conn_education = sqlite3.connect('education_members.sql')
    cur_education = conn_education.cursor()
    cur_education.execute("SELECT * FROM users_education WHERE name=?", (message.text,))
    customer_details = cur_education.fetchone()

    if customer_details:
        info = (f"The full infomation:ID: {customer_details[0]}\nNAME: {customer_details[1]}\nPASSWORD: {customer_details[2]}\nPROJECT NAME: {customer_details[3]}\nPROJECT DETAILS: {customer_details[4]}\nDEADLINE OF THE PROLECT: {customer_details[5]}")

        bot.send_message(message.chat.id, info, parse_mode='Markdown')