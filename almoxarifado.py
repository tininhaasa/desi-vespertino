class Almoxarifado:
    def __init__(self, unidade):
        self.unidade = unidade
        self.produtos = []

    # Conta quantos produtos estão com quantidade zero
    def contar_em_falta(self):
        total = 0                       # começa o contador
        for p in self.produtos:         # cada p é um objeto Produto
            if p.situacao() == "Em falta":
                total = total + 1
        return total                    

    def listar_produtos(self):
        lista = []
        for p in self.produtos:
            lista.append(p.listar_produtos())
        return lista

    