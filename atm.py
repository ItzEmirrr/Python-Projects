def input_taker(typ, text):
    inp = input(text)
    if typ == 'int':
        return int(inp)
    else:
        return inp

def action_picker():
    print('choose action: 1- check balance 2- withdraw 3- deposit 4- close')
    action = input_taker(typ='', text='>>> ')
    return action


def check_user(users):
    login = input_taker('', 'write your login of q to quit: ')
    if login == 'q':
        return (False, 'done')
    while True:
        for i,v in enumerate(users):
            if login == v['login']:
                password = input_taker('', 'write your password: ')
                if password == v['password']:
                    return (True, i)
            else:
                print('login or password incorrect')
                return (False, 'done')

def main():
    print('Hello from Alatoo bank')
    done = True
    user_data = [
        {'login': 'johnny', 'password': '1234', 'name': 'John', 'surname': 'Smith', 'age': 20, 'balance_kg': 5000},
        {'login': 'mary1990', 'password': '4332', 'name': 'Mary', 'surname': 'Jackson', 'age': 19, 'balance_kg': 6150},
        {'login': 'son44', 'password': '8796', 'name': 'Son', 'surname': 'Lee', 'age': 22, 'balance_kg': 3540}
    ]
    current_user = {}
    while done:
        ch = check_user(user_data)
        if ch[1] == 'done':
            done = False
        if ch[0]:
            current_user = user_data[ch[1]]
            action = action_picker()
        else:
            continue
        if action == '1':
            print(f"you have {current_user['balance_kg']}c in your balance")
            done = func()

        elif action == '2':
            print(f'your latest balance is {current_user["balance_kg"]}')
            money2with = int(input('write amount: '))
            current_user["balance_kg"] = current_user["balance_kg"] - money2with
            print(f'your latest balance is {current_user["balance_kg"]}')
            done = func()

        elif action == '3':
            add = int(input('Write amount: '))
            current_user["balance_kg"] = current_user["balance_kg"] + add
            print(f'your latest balance is {current_user["balance_kg"]}')
            done = func()
        else:
            done = False

def func():
    ask = input('Do you want to continue? yes/no: ')
    if ask == 'yes':
        return True
    else:
        return False

if __name__ == '__main__':
    main()