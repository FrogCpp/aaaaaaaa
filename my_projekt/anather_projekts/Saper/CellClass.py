class Cell():
    def __init__(self, _poz, _isMine=False, _dangerLevel=0):
        self._pozition = _poz
        self._status = True
        self._isMine = _isMine
        self._supports = []
        self._dangerLevel = _dangerLevel

    def Click(self, _mousClick=False):
        if self._isMine and _mousClick:
            return
        if self._dangerLevel < 1:
            for i in self._supports:
                for j in i:
                    try:
                        if j._status:
                            j.Click()
                    except:
                        pass
        self._status = False

    def __str__(self):
        return "[ ]" if self._status else f"[{self._dangerLevel}]"

    def __repr__(self):
        return self.__str__()

    def Draw(self):
        print(self._pozition)
        print()
        for i in range(3):
            for j in range(3):
                try:
                    print(self._supports[i][j]._pozition, end='')
                except:
                    print("(-, -)", end='')
            print()

    def complited(self):
        self._supports[1][1] = None
        for i in self._supports:
            for j in i:
                try:
                    self._dangerLevel += 1 if j._isMine else 0
                except:
                    pass