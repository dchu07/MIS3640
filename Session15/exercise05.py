class BMI:
    """
    represents one's bmi

    attributes: weight, height
    """
    def __init__(self, weight = 0, height = 0):
        self.weight = weight
        self.height = height
                
    def __str__(self):
        return f'(Your BMI is: {(self.weight/self.height**2)*703}).'

demi = BMI(weight = 130, height = 67)
print(demi)