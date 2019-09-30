import random
class Person:
	#mark1 = 1/3
	#mark2 = 2/3
	def __init__(self, name, health):
		self.name = name
		self.health = health
		self.mark1 = 1/3
		self.mark2 = 2/3

	def __repr__(self):
		return f'У игрока {self.name} сейчас {self.health} здоровья'

	''' Расчитывается нанесение вида и размера ущерба/лечения. Переменная x 
	принимает случайное значение от 0 до 1 и это определяет какой вид воздействия сработает.
	Далее рандомно определяется значение внутри заданного интервала. Выводится инфа кто и сколько получил.'''
	def _rand_damage(self):
		x = random.random()
		if x< self.mark1:
			y = random.randrange(18, 26, 1)
			print (f"Игрок {self.name} получил повреждение 1 типа и теряет {y} процентов жизни")
			return y
		elif x < self.mark2:
			y = random.randrange(10, 36, 1)
			print (f"Игрок {self.name} получил повреждение 2 типа и теряет {y} процентов жизни")
			return y
		y = random.randrange(-25, -17, 1)
		print (f"Игрок {self.name} получил лечение 1 типа и приобретает {-y} процентов жизни")
		return y

	def hint(self):
		self.health -= self._rand_damage()

class AltPerson(Person):

	def special_abilities(self):
		if self.health < 35:
			print("Для игрока Компьютер вводятся в силу новые условия!")
			print("Вероятность его излечения возрастает на 20%!!!")
			self.mark2 = 1 - (1/3)*1.2
			self.mark1 = (1-self.mark2)/2
			return self._rand_damage()
		return self._rand_damage()

	def hint(self):
		self.health -= self.special_abilities()
		

class Game:
	
	def __init__(self):
		self.person1 = AltPerson("Computer", 100)
		self.name2 = input("Введите имя человека: ")
		self.person2 = Person(self.name2, 100)
		print('')
		print("Игра начинается! Представляем участников:")
		print(self.person1)
		print(self.person2)
		print('')

	def set(self):
		while self.person1.health > 0 and self.person2.health > 0:
			player = random.choice([self.person1, self.person2])
			player.hint()
			print(player)
			print('')
		print(f"Игра закончена! Проиграл игрок {player.name} :(")

if __name__ == '__main__':
	Game()
