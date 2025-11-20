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
