class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):       
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score) 
    def profile(self):
        print("His name is", self.name, "He is", self.age, "He's studying the", self.tracks, "and has a score of", self.score)
        pass
    def change_name(self, rename):
        self.name = rename
        rename = "Peter"
        print(f"His name is {rename}")
    def change_age(self, new_age):
        self.age = new_age
        new_age  = 34
        print(f"he is {new_age}")
    def add_track(self, new_tracks):
        self.tracks = new_tracks
        new_tracks = ["UI/UX"]
        print(f"he's studying the {new_tracks}")
    def get_score(self):
        return self.score 
        


Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)
Bob.profile()
print("For the change: ")
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print("and has a score of", Bob.get_score())

