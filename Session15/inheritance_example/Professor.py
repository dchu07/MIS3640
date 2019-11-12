from BabsonPerson import BabsonPerson

class Professor(BabsonPerson):

    def __init__(self, name, course):
        BabsonPerson.__init__(self, name)
        self.course = course

    def speak(self, utterance):
        new_utterance = f"In course {self.course}, we say that {utterance}."
        return BabsonPerson.speak(self, new_utterance)
    
    
def main():
    prof = Professor("Zhi Li", "MI 3640")
    print(prof.speak("Python is awesome"))


if __name__ == "__main__":
    main()