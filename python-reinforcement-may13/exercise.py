class Person:
  def __init__(self, emotions):
    self.mood = emotions

  def __str__(self):
    return f"Emotions: {self.mood}"

  def get_mood(self):
    results = []
    for emotion, level in self.mood.items():
      if level == 1:
        results.append(f"I am feeling a low amount of {emotion}")
      elif level == 2:
        results.append(f"I am feeling a moderate amount of {emotion}")
      elif level == 3:
        results.append(f"I am feeling a high amount of {emotion}")
      
    return results

emotions = {
  'happiness': 3,
  'sadness': 1,
  'stress': 2
}

person1 = Person(emotions)
# print(person1)
# print(person1.mood)
# person1.get_mood()

print(person1.get_mood())

