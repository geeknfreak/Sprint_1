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
