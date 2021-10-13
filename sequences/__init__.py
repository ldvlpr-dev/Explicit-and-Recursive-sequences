import matplotlib.pyplot as plt
__version__ = '0.1.0'


class _Sequence:
    def __init__(self, formula: str):
        self.formula = formula
        self.calculated_terms = {}

    def __repr__(self):
        return f"Sequence of {self.type} form defined by '{self.formula}'"

    def display_graph(self):
        plt.plot(self.calculated_terms.keys(),
                 self.calculated_terms.values(), 'bo')
        plt.grid()
        plt.show()

    def exec(self):
        raise RuntimeError(
            "No execution process definded: you're using the model Sequence class, please not do that")


class ExplicitSequence(_Sequence):
    def __init__(self, formula: str):
        super().__init__(formula)
        self.type = "explicit"
        self.variablechar = "n"

    def exec(self, max_range: int, diplay_graph=False):
        self.calculated_terms = {}
        for i in range(max_range+1):
            try:
                self.calculated_terms[i] = float(
                    eval(self.formula.replace(self.variablechar, str(i))))
            except ZeroDivisionError:
                pass
        if diplay_graph:
            self.display_graph()
        return self.calculated_terms


class RecursiveSequence(_Sequence):
    def __init__(self, formula: str):
        super().__init__(formula)
        self.type = "recursive"
        self.variablechar = "an"

    def exec(self, first_term: float, max_range: int, diplay_graph=False):
        self.calculated_terms = {0: first_term}
        for i in range(1, max_range+1):
            try:
                self.calculated_terms[i] = float(eval(self.formula.replace(
                    self.variablechar, str(self.calculated_terms[i-1]))))
            except ZeroDivisionError:
                pass
        if diplay_graph:
            self.display_graph()
        return self.calculated_terms
