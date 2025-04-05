class father:
    def __init__(self):
        print("hi father!")

class mother:
    def __init__(self):
        print("hi mother!")

class sister:
    def __init__(self):
        print("hi sister!")

class brother(father,mother,sister):
    def __init__(self):
        super().__init__()
        print("hi brother!")
ahmed=brother()
