# ==================== ЗАДАНИЕ 2: Исправление класса ====================

class Tester:

    def __init__(self, name):
        self.name = name

    def work_hard(self, deadline=True):
        if deadline: 
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester('tester_1')
tester_1.work_hard(False)  # 'tester_1 Можно отдыхать'
tester_2 = Tester('tester_2')
tester_2.work_hard(True)   # 'tester_2 Что ж, ещё часок поработаю!' 
