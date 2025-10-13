import re

def count_special_groups_regex(text):
    # Ищем последовательности, которые начинаются с A,
    # содержат от 8 до ... символов (не A и не B),
    # и заканчиваются на A
    pattern = r'A[^AB]{8,}A'
    matches = re.findall(pattern, text)
    return len(matches)

# Чтение файла
with open('24 (1).txt', 'r') as file:
    text = file.read().strip()

# Подсчет групп
result = count_special_groups_regex(text)
print(f"Количество групп: {result}")