'''
aça um programa que leia a largura e altura de uma parede, em seguida calcule:  a área (m2)
  a quantidade em litros (L) de tinta necessária para pintar, sabendo que:  100 ml consegue pintar 2 m2
'''


altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
area = altura * largura
tinta_necessaria = (area/2) * 0.1
print(f'A área da parede é de {area} m²')
print(f'A quantidade de tinta necessária para pintar a parede será de {tinta_necessaria} litros')
