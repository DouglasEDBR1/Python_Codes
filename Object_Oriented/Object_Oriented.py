class Triangulo:
    def __init__(self, lado1, lado2, lado3, base , altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2

    def tipo(self):
        if self.lado1 > self.lado2 + self.lado3:
            return 'Não é um triangulo'
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado1 == self.lado2:
            return 'triângulo isósceles'
        else:
            return 'outro tipo de triângulo'


t1 = Triangulo(2, 1, 3, 4, 3 )
t1.area()
print(f'LADO 1: {t1.lado1}, LADO 2: {t1.lado2}, LADO 3: {t1.lado3}, BASE: {t1.base} , ALTURA: {t1.altura}')
print('ÁREA:', t1.area())
print('TIPO:', t1.tipo())

t2 = Triangulo(5, 1, 3, 4, 3 )
print(f'LADO 1: {t2.lado1}, LADO 2: {t2.lado2}, LADO 3: {t2.lado3}, BASE: {t2.base} , ALTURA: {t2.altura}')
print('ÁREA:', t2.area())
print('TIPO:', t2.tipo())

t3 = Triangulo(8, 8, 8, 16, 9)
print(f'LADO 1: {t3.lado1}, LADO 2: {t3.lado2}, LADO 3: {t3.lado3}, BASE: {t3.base} , ALTURA: {t3.altura}')
print('ÁREA:', t3.area())
print('TIPO:', t3.tipo())

