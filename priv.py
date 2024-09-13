class y:
    __privatevar=9
    def __privmeth(self):
        print("it is a protected function")
    def hello():
        print("private variable",y.__privatevar)

obj =y()
y.hello()
y.__privmeth()