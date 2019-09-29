import random
class Person:
	def __init__(self, name, health):
		self.name = name
		self.health = health

	def __repr__(self):
		return f'У игрока {self.name} сейчас {self.health} здоровья'

	''' Расчитывается нанесение вида и размера ущерба/лечения. Переменная x 
	принимает случайное значение от 0 до 1 и это определяет какой вид воздействия сработает.
	Далее рандомно определяется значение внутри заданного интервала. Выводится инфа кто и сколько получил.'''
	def _rand_damage(self):
		otm1 = 0.33
		otm2 = 0.66
		x = random.random()
		if x< otm1:
			y = random.randrange(18, 26, 1)
			print (f"Игрок {self.name} получил повреждение 1 типа и теряет {y} процентов жизни")
			return y
		elif x < otm2:
			y = random.randrange(10, 36, 1)
			print (f"Игрок {self.name} получил повреждение 2 типа и теряет {y} процентов жизни")
			return y
		y = random.randrange(-25, -17, 1)
		print (f"Игрок {self.name} получил лечение 1 типа и приобретает {-y} процентов жизни")
		return y

	def hint(self):
		self.health -= self._rand_damage()
		

class Game:
	
	def __init__(self):
		self.person1 = Person("Computer",100)
		self.name2 = input("Введите имя человека: ")
		self.person2 = Person(self.name2,100)
		print('')
		print("Игра начинается! Представляем участников:")
		print(self.person1)
		print(self.person2)
		print('')

	#def set(self):
		while self.person1.health > 0 and self.person2.health > 0:
			z = random.choice([self.person1, self.person2])
			z.hint()
			print(z)
			print('')
		print(f"Игра закончена! Проиграл игрок {z.name} :(")


Game()
