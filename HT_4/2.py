# Написати функцію < bank > , яка працює за наступною логікою:
# користувач робить вклад у розмірі < a > одиниць строком на < years > років
# під < percents > відсотків (кожен рік сума вкладу збільшується на цей відсоток,
# ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки).
# Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%).
# Функція повинна принтануть і вернуть суму, яка буде на рахунку.
def bank(a, years, percents=10):
    result = int(a)*(1+(percents/100))**int(years)
    return result


money = input('How much do you invest money? ')
years_money = input('How many years do you want to invest in a bank? ')
print(bank(money, years_money))
