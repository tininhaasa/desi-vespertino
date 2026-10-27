# teste_produto.py — usa a classe Produto e mostra o resultado
from produto import Produto

p1 = Produto("P001", "Luva de vaqueta", 12, 20)
print(p1.listar_produtos())

p1.entrada(30)
print(p1.listar_produtos())

p1.saida(15)
print(p1.listar_produtos())

if p1.saida(100):
    print("Saída registrada")
else:
    print("Saída recusada")

print(p1.quantidade)