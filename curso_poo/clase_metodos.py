class Matematica:
    def suma(self):
        self.n1 = 2
        self.n2 = 3
    def suma2(self):
        self.n1 = 5
        self.n2 = 7

s = Matematica()
s.suma()
print(s.n1 + s.n2)


objeto = Matematica()
objeto.suma2()
print(objeto.n1 *  objeto.n2)