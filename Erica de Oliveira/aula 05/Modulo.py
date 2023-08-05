


def calcular_area_quadrado(lado):
    area = lado ** 2
    return area

def calcular_perimetro_quadrado(lado):
    perimetro = 4 * lado
    return perimetro

def calcular_area_triangulo(base, altura):
    area = 0.5 * base * altura
    return area

def calcular_area_retangulo(largura, altura):
    area = largura * altura
    return area

lado_quadrado = 5
area_quadrado = calcular_area_quadrado(lado_quadrado)
perimetro_quadrado = calcular_perimetro_quadrado(lado_quadrado)

base_triangulo = 4
altura_triangulo = 3
area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)

largura_retangulo = 6
altura_retangulo = 4
area_retangulo = calcular_area_retangulo(largura_retangulo, altura_retangulo)

print("Área do quadrado:", area_quadrado)
print("Perímetro do quadrado:", perimetro_quadrado)
print("Área do triângulo:", area_triangulo)
print("Área do retângulo:", area_retangulo)

