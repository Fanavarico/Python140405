class Field:
    def __init__(self, name, category, score):
        self.name = name
        self.category = category
        self.score = score
        self.is_playing = False

    def play(self):
        self.is_playing = True
        print(f"{self.name} with category {self.category} and score {self.score} is being played on.")

    def stop(self):
        self.is_playing = False
        print(f"{self.name} with category {self.category} and score {self.score} has stopped.")

# Test Field
field1 = Field("Interstellar", "Science-Fiction", 10)
field1.play()
field1.stop()
print()