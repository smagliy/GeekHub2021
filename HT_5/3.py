# На основі попередньої функції створити наступний кусок кода:
#    а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції)
#    - як валідні, так і ні;
#    б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором,
#    перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
#       Name: vasya
#       Password: wasd
#       Status: password must have at least one digit
#       -----
#       Name: vasya
#       Password: vasyapupkin2000
#       Status: OK



def verification(list_users):
    for elem in list_users:
        print(f'Name:{elem[0]}')
        print(f'Password: {elem[1]}')
        for elem1 in elem[1]:
            try:
                int(elem1)
                print('Status: OK')
                break
            except ValueError:
                print('Status: password must have at least one digit')


list_u = [['kate', '1254fdgh'], ['lkuy', 'kjxgyxjs'], ['anna_1', 'ag125412'], ['fish', 'rth101010']]
verification(list_u)