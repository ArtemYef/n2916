class Grandparent:
    def about_myself(self):
        print("I am a grandfather")
class Parent(Grandparent):
    def about_myself(self):
        print("Im a father")
class Child(Parent):
    def about_myself(self):
        print("I am a son")
Alex = Child()
