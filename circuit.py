"""More practice with classes and inheritance."""

class LogicGate(object):

    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n):
        # super().__init__(n)

        self.pinA = None
        self.pinB = None
        return super(BinaryGate, self).__init__(n)

    def getPinA(self):
        return int(raw_input("Enter Pin A input for gate " + \
            self.get_label()+"-->"))

    def getPinB(self):
        return int(raw_input("Enter Pin B input for gate " + \
            self.get_label()+"-->"))


class UnaryGate(LogicGate):
    def __init__(self, n):
        # super().__init__(n)

        self.pin = None
        return super(UnaryGate, self).__init__(n)

    def getPin(self):
        return int(raw_input("Enter Pin input for gate " + \
            self.get_label()+"-->"))


class AndGate(BinaryGate):
    def __init__(self, n):
        return super(AndGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n):
        return super(AndGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0
