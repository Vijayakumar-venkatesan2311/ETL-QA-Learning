#  Cricket OOP Concepts in Python
# You're a Coach. You manage a team with Batsmen, Bowlers, and AllRounders.

# Let’s see how each OOP concept fits in Python style.

# Inheritance
# “Every player is a Cricketer, but adds their own skills.”

# 📖 Story:
# You define a base class Cricketer. Batsman and Bowler inherit from it.

class Cricketer:
    def warm_up(self):
        print("Doing basic warm-up")

class Batsman(Cricketer):
    def bat(self):
        print("Practicing cover drives")

#  Polymorphism
# “One call from the coach — everyone plays in their own way.”

# 📖 Story:
# Coach calls play(). A Batsman bats, a Bowler bowls — same method, different actions.

class Cricketer:
    def play(self):
        print("Generic play")

class Batsman(Cricketer):
    def play(self):
        print("Batsman playing shots")

class Bowler(Cricketer):
    def play(self):
        print("Bowler delivering overs")

# Coach commands:
team = [Batsman(), Bowler()]
for player in team:
    player.play()  # Polymorphism in action


# Encapsulation
# “Fitness reports stay with the physio, not the media.”

# 📖 Story:
# Player’s health data is private. Coach accesses it through proper methods only.

class Cricketer:
    def __init__(self):
        self.__fitness_score = 100  # private

    def get_fitness(self):
        return self.__fitness_score

    def set_fitness(self, score):
        if 0 <= score <= 100:
            self.__fitness_score = score

#  Abstraction
# “Every player must prepare — no excuses.”

# 📖 Story:
# Coach defines that all players must implement prepare(). How they do it is up to them.

from abc import ABC, abstractmethod

class Cricketer(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Batsman(Cricketer):
    def prepare(self):
        print("Batsman: Practicing in nets")

class Bowler(Cricketer):
    def prepare(self):
        print("Bowler: Practicing line and length")
