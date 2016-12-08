
class LogicGate:
    def __init__(self, n):
        # The label identifies the logic gate
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def set_label(self, n):
        self.label = n

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a == None:
            return(int(input("Enter Pin A input for gate " \
                + self.get_label() + " --> ")))
        else:
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        if self.pin_b == None:
            return(int(input("Enter Pin B input for gate " \
                + self.get_label() + " --> ")))
        else:
            return self.pin_b.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                # raise RuntimeError("Error: No empty pins.")
                print("Cannot connect: No empty pins on this gate.")

class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 1 or b == 1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def get_pin(self):
        return(int(input("Enter Pin input for gate " \
            + self.get_label() + " --> ")))

class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1

class Connector:
    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate
        to_gate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate

g1 = AndGate("g1")
print(g1.perform_gate_logic())

g2 = OrGate("g2")
print(g2.perform_gate_logic())

g3 = UnaryGate("g3")
print(g3.get_pin())

g4 = NotGate("g4")
print(g4.perform_gate_logic())
