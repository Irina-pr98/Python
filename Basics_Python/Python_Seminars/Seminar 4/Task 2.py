# Пользователь вводит текст(строка). Словом считается последовательность 
# непробельных символов идущих подряд, слова разделены одним или 
# большим числом пробелов или символами конца строки.Определите, 
# сколько различных слов содержится в этом тексте.

string = """Мармелад мышка ящерица ящерица мышка мышка"""

list_string = string.lower().split()
print(string)
print(list_string)

# Через словарь
catalog = {}

for word in list_string:
    catalog[word] = catalog.get(word, 0) + 1
count = 0
for _ in catalog:
    count += 1
print(count)

# Через метод
key = catalog.keys()
print(len(key))

# Через множество
print(len(set(list_string)))