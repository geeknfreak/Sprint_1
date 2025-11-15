# ==================== ЗАДАНИЕ 1: Конвертация времени ====================

# example string '1h 45m,360s,25m,30m 120s,2h 60s'
def time_change(time_string):
    total_min = 0
    
    # Заменяем пробелы на запятые и разделяем по запятым
    time_string = time_string.replace(' ', ',')
    parts = time_string.split(',')
    
    for time in parts:
        time = time.strip()  # Убираем лишние пробелы
        
        if time.endswith('h'):
            hours = int(time[:-1])  # Убираем 'h' и преобразуем в число
            total_min += hours * 60
            
        elif time.endswith('m'):
            minutes = int(time[:-1])  # Убираем 'm' и преобразуем в число
            total_min += minutes
            
        elif time.endswith('s'):
            seconds = int(time[:-1])  # Убираем 's' и преобразуем в число
            total_min += seconds / 60

    print(int(total_min))

time_change('1h 45m,360s,25m,30m 120s,2h 60s')




# ==================== ЗАДАНИЕ 2: Исправление класса ====================

class Tester:

    def __init__(self, name):
        self.name = name
        self.deadline = True

    def work_hard(self, deadline=True):
        if deadline: 
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester('tester_1')
tester_1.work_hard(False)  # 'tester_1 Можно отдыхать'
tester_2 = Tester('tester_2')
tester_2.work_hard(True)   # 'tester_2 Что ж, ещё часок поработаю!' 




# ==================== ЗАДАНИЕ 3: Работа со словарем ====================

world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

country = 'Италия'

world_champions[2022] = 'Аргентина' # Добавил в словарь 2022 год и чемпиона Аргентину
for year,cntry in world_champions.items(): # Тут как будто покрасивше можно второе вэлью было написать, country занят переменной
    print(year, '-', cntry)
if country in cntry:
    print('Италия становилась чемпионом мира по футболу в 21 веке!')
else: print('Италия не становилась чемпионом мира по футболу в 21 веке!')





# ==================== ЗАДАНИЕ 4: Работа со списками ====================

new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006'] 

# Перенос задачи task_005 из новых в завершенные (В одно действие)
completed_tasks.append(new_tasks.pop(-1))

# Удаление task_007 из новых
new_tasks.remove('task_007')

# Вывести на экран последнюю задачу из новых
last_task = new_tasks[-1]
print(last_task)





# ==================== ЗАДАНИЕ 5:  ====================

class TestCase:
    
    def __init__(self, result=None):
        self.steps = {}
        self.result = result
    
    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text
    
    def delete_step(self, step_number):
        if step_number in self.steps:
            del self.steps[step_number]
        
    def set_result(self, result):
        self.result = result
    
    def get_test_case(self):
        print({'Шаги': self.steps, 'Ожидаемый результат': self.result})


test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case() 
        