def showes(balance):
    print(f'💰 Ваш баланс: {balance} руб.')

def deposit(balance):
    amount = int(input('Сумма пополнения: '))
    if amount <= 0:
        print('❌ Сумма должна быть положительной!')
        return balance
    balance += amount
    print(f'✅ Счёт пополнен на {amount} руб.')
    return balance

def withdraw(balance):
    amount = int(input('Сумма снятия: '))
    if amount <= 0:
        print('❌ Сумма должна быть положительной!')
        return balance
    if amount > balance:
        print('❌ Недостаточно средств!')
        return balance
    balance -= amount
    print(f'✅ Снято {amount} руб.')
    return balance

def login(users):
    '''Вход пользователя'''
    login = input('👤 Введите логин: ')
    if login in users:
        print(f'✅ Добро пожаловать, {login}!')
        return login, users[login]
    else:
        print('❌ Пользователь не найден!')
        return None, None

def register(users):
    '''Регистрация нового пользователя'''
    login = input('📝 Придумайте логин: ')
    if login in users:
        print('❌ Такой логин уже существует!')
        return users
    users[login] = 0
    print(f'✅ Пользователь {login} создан!')
    return users

def bank_menu(username, balance):
    '''Меню банковских операций'''
    bonuses = 0  # отдельный счёт бонусов
    
    while True:
        print(f'\n🏦 Добро пожаловать, {username}!')
        print('1 - Баланс')
        print('2 - Пополнить')
        print('3 - Снять')
        print('4 - Выйти из аккаунта')
        print('5 - Бонусы')
        
        choice = input('Выберите действие: ')
        
        if choice == '1':
            print(f'Основной баланс: {balance} руб.')
            print(f'Бонусы: {bonuses:.2f} руб.')
        elif choice == '2':
            amount = int(input('Сумма пополнения: '))
            if amount <= 0:
                print('Сумма должна быть положительной!')
                continue
            bonus = amount * 0.01
            bonuses += bonus
            balance += amount
            print(f'Пополнено: {amount} руб.')
            print(f'Начислено бонусов: {bonus:.2f} руб.')
        elif choice == '3':
            amount = int(input('Сумма снятия: '))
            if amount <= 0:
                print('Сумма должна быть положительной!')
                continue
            if amount > balance:
                print('Недостаточно средств!')
                continue
            balance -= amount
            print(f'Снято: {amount} руб.')
        elif choice == '4':
            print(f'До свидания, {username}!')
            return balance
        
        elif choice == '5':
            if bonuses <= 0:
                print('У вас ещё нет бонусов!')
                continue
            print(f'У вас {bonuses:.2f} бонусных рублей.')
            use = input('Использовать ваши бонусы?(да/нет): ')
            if use.lower() == 'да':
                balance += bonuses
                print(f'Бонусы зачислены на ваш счёт, новый баланс составляет {balance:.2f} руб.')
                bonuses = 0
        else:
            print('Неверный выбор!')

def main():
    users = {'admin': 10000}  # начальный пользователь
    
    while True:
        print("\n🏦 Банк 'Ученик'")
        print('1 - Вход')
        print('2 - Регистрация')
        print('3 - Выход')
        
        choice = input('Выберите действие: ')
        
        if choice == '1':
            username, balance = login(users)
            if username:
                newes = bank_menu(username, balance)
                users[username] = newes
        elif choice == '2':
            users = register(users)
        elif choice == '3':
            print('👋 До свидания!')
            break
        else:
            print('❌ Неверный выбор!')

if __name__ == '__main__':
    main()