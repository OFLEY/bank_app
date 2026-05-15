def show_balance(balance):
    '''Показывает текущий баланс'''
    print(f'💰 Ваш баланс: {balance} руб.')
'''</code></pre></div><div style="display:contents" dir="auto"><p id="32df5022-cde3-804b-9e74-d571f896d624" class=""><strong>Почему это круто:</strong></p></div><div style="display:contents" dir="auto"><ul id="32df5022-cde3-80fe-85d9-ea71fd595f83" class="bulleted-list"><li style="list-style-type:disc">✅ Один раз написали — много раз используем</li></ul></div><div style="display:contents" dir="auto"><ul id="32df5022-cde3-80ff-8d52-dfcf6af50168" class="bulleted-list"><li style="list-style-type:disc">✅ Легко исправлять ошибки</li></ul></div><div style="display:contents" dir="auto"><ul id="32df5022-cde3-8094-9245-e7aa40a54022" class="bulleted-list"><li style="list-style-type:disc">✅ Код становится читаемым'</li></ul></div><div style="display:contents" dir="auto"><hr id="32df5022-cde3-8000-8fb6-dfd0da5bf49e"/></div><div style="display:contents" dir="auto"><p id="32df5022-cde3-80e6-8174-e638caa26a1c" class="">
</p></div><div style="display:contents" dir="auto"><h3 id="32df5022-cde3-803c-8104-eb94a3d88d0a" class="">👨‍💻 Практика 1 (я показываю) </h3></div><div style="display:contents" dir="auto"><p id="32df5022-cde3-80af-9807-ddc3d606ee42" class=""><strong>Задача:</strong> Переписать меню банка с использованием функций.</p></div><div style="display:contents" dir="auto"><pre id="32df5022-cde3-80e7-8e75-e61f3fc61ff5" class="code code-wrap"><code class="language-python" style="white-space:pre-wrap;word-break:break-all"># bank-python-app - версия 3 (с функциями)
''' 

def show_balance(balance):
    '''Показывает баланс'''
    print(f'💰 Ваш баланс: {balance} руб.')

def deposit(balance):
    '''Пополнение счёта'''
    amount = int(input('Сумма пополнения: '))
    if amount <= 0:
        print('❌ Сумма должна быть положительной!')
        return balance
    new_balance = balance + amount
    print(f'✅ Счёт пополнен на {amount} руб.')
    return new_balance

def withdraw(balance):
    '''Снятие денег'''
    amount = int(input('Сумма снятия: '))
    if amount <= 0:
        print('❌ Сумма должна быть положительной!')
        return balance
    if amount > balance:
        print('❌ Недостаточно средств!')
        return balance
    new_balance = balance - amount
    print(f'✅ Снято {amount} руб.')
    return new_balance

def main():
    '''Главная функция программы'''
    balance = 5000
    
    while True:
        print('\n1 - Баланс')
        print('2 - Пополнить')
        print('3 - Снять')
        print('4 - Выход')
        
        choice = input('Выберите действие: ')
        
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance = deposit(balance)
        elif choice == '3':
            balance = withdraw(balance)
        elif choice == '4':
            print('👋 До свидания!')
            break
        else:
            print('❌ Неверный выбор!')

if __name__ == '__main__':
    main()