# -- coding: latin-1 --

class Deque:
    """Classe que representa uma lista duplamente ligada com sentinelas."""

    class __No:
        """Subclasse privada que representa um n� da lista."""

        def __init__(self, dado=None):
            self.dado = dado  # Armazena o dado do n�.
            self.proximo = None  # Aponta para o pr�ximo n�.
            self.anterior = None  # Aponta para o n� anterior.

    def __init__(self):
        self.__cabeca = self.__No()  # Cria o n� sentinela de cabe�a.
        self.__cauda = self.__No()  # Cria o n� sentinela de cauda.
        self.__cabeca.proximo = self.__cauda  # Liga cabe�a ao n� sentinela de cauda.
        self.__cauda.anterior = self.__cabeca  # Liga cauda ao n� sentinela de cabe�a.
        self.__tamanho = 0  # Inicializa o tamanho da lista como 0.

    def addFirst(self, dado):
        """Insere um novo n� no in�cio da lista."""
        novo_no = self.__No(dado)  # Cria um novo n� com o dado fornecido.
        primeiro = self.__cabeca.proximo  # O primeiro n� real.
        novo_no.proximo = primeiro  # Aponta para o antigo primeiro n�.
        novo_no.anterior = self.__cabeca  # Aponta para o n� sentinela de cabe�a.
        primeiro.anterior = novo_no  # Atualiza o anterior do antigo primeiro.
        self.__cabeca.proximo = novo_no  # Atualiza o pr�ximo da cabe�a.
        self.__tamanho += 1  # Incrementa o tamanho da lista.

    def addLast(self, dado):
        """Insere um novo n� no final da lista."""
        novo_no = self.__No(dado)  # Cria um novo n� com o dado fornecido.
        ultimo = self.__cauda.anterior  # O �ltimo n� real.
        novo_no.proximo = self.__cauda  # O novo n� aponta para o n� sentinela de cauda.
        novo_no.anterior = ultimo  # Aponta para o antigo �ltimo n�.
        ultimo.proximo = novo_no  # O antigo �ltimo n� aponta para o novo n�.
        self.__cauda.anterior = novo_no  # O n� sentinela de cauda aponta para o novo n�.
        self.__tamanho += 1  # Incrementa o tamanho da lista.

    def inserir_posicao(self, dado, posicao):
        """Insere um novo n� na posi��o especificada."""
        if posicao < 0 or posicao > self.__tamanho:
            print("Posi��o inv�lida.")
            return
        atual = self.__cabeca.proximo  # Come�a no primeiro n� real.
        for _ in range(posicao):
            atual = atual.proximo  # Avan�a at� a posi��o.
        novo_no = self.__No(dado)  # Cria o novo n�.
        novo_no.proximo = atual  # O novo n� aponta para o n� atual.
        novo_no.anterior = atual.anterior  # O novo n� aponta para o n� anterior.
        atual.anterior.proximo = novo_no  # O anterior aponta para o novo n�.
        atual.anterior = novo_no  # O n� atual aponta para o novo n�.
        self.__tamanho += 1  # Incrementa o tamanho da lista.

    def deleteFirst(self):
        """Remove o n� do in�cio da lista e retorna seu dado."""
        if self.__tamanho == 0:  # Lista vazia.
            print("Erro: N�o � poss�vel remover de um deque vazio.")
            return None
        removido = self.__cabeca.proximo  # O primeiro n� real.
        self.__cabeca.proximo = removido.proximo  # Cabe�a aponta para o segundo n�.
        removido.proximo.anterior = self.__cabeca  # O segundo n� aponta para a cabe�a.
        self.__tamanho -= 1  # Decrementa o tamanho.
        return removido.dado  # Retorna o dado removido.

    def deleteLast(self):
        """Remove o n� do final da lista e retorna seu dado."""
        if self.__tamanho == 0:  # Lista vazia.
            print("Erro: N�o � poss�vel remover de um deque vazio.")
            return None
        removido = self.__cauda.anterior  # O �ltimo n� real.
        self.__cauda.anterior = removido.anterior  # Cauda aponta para o pen�ltimo n�.
        removido.anterior.proximo = self.__cauda  # O pen�ltimo n� aponta para a cauda.
        self.__tamanho -= 1  # Decrementa o tamanho.
        return removido.dado  # Retorna o dado removido.

    def remover_posicao(self, posicao):
        """Remove o n� na posi��o especificada e retorna seu dado."""
        if posicao < 0 or posicao >= self.__tamanho:
            print("Posi��o inv�lida.")
            return None
        atual = self.__cabeca.proximo
        for _ in range(posicao):
            atual = atual.proximo  # Avan�a at� a posi��o.
        removido = atual  # N� a ser removido.
        removido.anterior.proximo = removido.proximo  # Conecta anterior ao pr�ximo.
        removido.proximo.anterior = removido.anterior  # Conecta pr�ximo ao anterior.
        self.__tamanho -= 1  # Decrementa o tamanho.
        return removido.dado  # Retorna o dado removido.

    def remover_dado(self, dado):
        """Remove o primeiro n� que cont�m o dado especificado."""
        atual = self.__cabeca.proximo
        for _ in range(self.__tamanho):
            if atual.dado == dado:  # Verifica se o dado corresponde.
                atual.anterior.proximo = atual.proximo  # Conecta anterior ao pr�ximo.
                atual.proximo.anterior = atual.anterior  # Conecta pr�ximo ao anterior.
                self.__tamanho -= 1  # Decrementa o tamanho.
                return atual.dado  # Retorna o dado removido.
            atual = atual.proximo
        print("Dado n�o encontrado.")  # Se o dado n�o estiver na lista.
        return None

    def peek(self):
        """Recupera o dado do n� no in�cio da lista."""
        if self.__tamanho == 0:  # Lista vazia.
            return None
        return self.__cabeca.proximo.dado  # Retorna o dado do primeiro n� real.

    def top(self):
        """Recupera o dado do n� no final da lista."""
        if self.__tamanho == 0:  # Lista vazia.
            return None
        return self.__cauda.anterior.dado  # Retorna o dado do �ltimo n� real.

    def recuperar_posicao(self, posicao):
        """Recupera o dado do n� na posi��o especificada."""
        if posicao < 0 or posicao >= self.__tamanho:
            print("Posi��o inv�lida.")
            return None
        atual = self.__cabeca.proximo
        for _ in range(posicao):
            atual = atual.proximo  # Avan�a at� a posi��o desejada.
        return atual.dado  # Retorna o dado do n� da posi��o.

    def imprimir_lista(self):
        """Imprime os dados de todos os n�s da lista."""
        atual = self.__cabeca.proximo
        for _ in range(self.__tamanho):
            print(atual.dado, end=" <-> ")  # Imprime o dado do n� atual.
            atual = atual.proximo  # Avan�a para o pr�ximo n�.
        print("None")  # Indica o fim da lista.

    def getSize(self):
        """Retorna o tamanho da lista."""
        return self.__tamanho  # Retorna o n�mero de n�s na lista.

    def obter_cabeca(self):
        """Retorna o n� sentinela da cabe�a."""
        return self.__cabeca

    def obter_cauda(self):
        """Retorna o n� sentinela da cauda."""
        return self.__cauda

    def isEmpty(self):
        if self.__tamanho == 0:
            return True
        else:
            return False

    def __str__(self):
        # """Retorna uma string representando os elementos da fila."""
        elementos = []  # Cria uma lista para armazenar os elementos.
        atual = self.obter_cabeca().proximo  # Come�a no primeiro n� da lista.
        while atual != self.__cauda:  # Percorre todos os n�s da lista.
            elementos.append(str(atual.dado))  # Adiciona o dado � lista.
            atual = atual.proximo  # Move para o pr�ximo n�.
        return " ".join(elementos)  #


# Cria��o de um deque.
deque = Deque()
# Inserindo e exibindo elementos no in�cio.
print("Inserindo 10 no in�cio do deque:")
deque.addFirst(10)
print(deque)  # Deve imprimir: 10.
print("Inserindo 5 no in�cio do deque:")
deque.addFirst(5)
print(deque)  # Deve imprimir: 5 10.
# Inserindo e exibindo elementos no final.
print("Inserindo 20 no final do deque:")
deque.addLast(20)
print(deque)  # Deve imprimir: 5 10 20.
print("Inserindo 30 no final do deque:")
deque.addLast(30)
print(deque)  # Deve imprimir: 5 10 20 30.
# Removendo e exibindo elemento do in�cio.
print("\nRemovendo elemento do in�cio do deque:")
deque.deleteFirst()
print(deque)  # Deve imprimir: 10 20 30.
print("Removendo outro elemento do in�cio do deque:")
deque.deleteFirst()
print(deque)  # Deve imprimir: 20 30.
# Removendo e exibindo elemento do final.
print("Removendo elemento do final do deque:")
deque.deleteLast()
print(deque)  # Deve imprimir: 20.
print("Removendo outro elemento do final do deque:")
deque.deleteLast()
print(deque)  # Deve imprimir: None.
# Verificando se o deque est� vazio e tentando remover de um deque vazio.
print("\nO deque est� vazio?", deque.isEmpty())  # Deve imprimir: True.
print("Tentando remover de um deque vazio:")
deque.deleteFirst()  # Deve imprimir mensagem de erro.