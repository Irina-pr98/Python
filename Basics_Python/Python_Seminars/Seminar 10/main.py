class Human:
    def __init__(self, name: str, age: int, is_work: bool):
        self.name = name
        self.age = age
        self.is_work = is_work
        
    def greetings(self):
        print(f'{self.name} говорит "Привет"')
        
    def goodbye(self, name: str):
        return f'{self.name} прощается с {name}'
    
    def __str__(self):
        return f'Это человек с именем {self.name}, возраста {self.age} лет'
        
stone = Human('Кирилл', 38, True)
rudolf = Human('Рудольф', 18, True)

print(stone.name)
print(stone.age)
print(stone.is_work)

stone.greetings()
rudolf.greetings()

stone.goodbye('Рудольфом')
rudolf.goodbye('Кириллом')

stone.name = 'Стоун'
print(stone.name)

# ----------- def __str__(self)

print(stone.goodbye('всем'))
print(rudolf)