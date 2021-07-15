#09) Faça um programa que cadastre em uma pilha encadeada vários números. A entrada deles será finalizada com a digitação de um número menor ou igual a zero. 
#Posteriormente, o programa deve gerar duas filas encadeadas, a primeira com os números pares e a segunda com os números ímpares. 
#A saída do programa deve apresentar a pilha digitada e as filas geradas. Caso alguma das filas seja vazia, deve-se imprimir “Fila vazia”.
#ENTREGAR NO MOODLE o exercício 09 em UM ARQUIVO no formato pdf ou doc. Não precisa ser manuscrito. 
#Esta entrega será utilizada para computar a nota média dos exercícios ao final do semestre, conforme previsto no plano de ensino.

class NodePilha:
    __num = None
    __proximo = None

    def __init__(self):
        self.__num = None
        self.__proximo = None

    def getProximo(self):
        return self.__proximo

    def setProximo(self, proximo):
        self.__proximo = proximo

    def getNum(self):
        return self.__num
    
    def setNum(self):
        self.__num = int(input('Digite um numero para entrar na pilha: '))       

class Pilha: 
    __topo = None

    def __init__(self):
        self.__topo = None
        temp_node = None
    
    def push(self):
        temp_node = NodePilha()          

        if temp_node:
            temp_node.setNum()
            if self.__topo:
                temp_node.setProximo(self.__topo) 
            self.__topo = temp_node 
        

    def popPilha(self):
        if self.__topo:
            self.__topo = self.__topo.getProximo()

        else:
            print("Pilha vazia...")

    def printall(self):
        if not self.__topo: # None
            print("Pilha vazia...")
            return
        temp = self.__topo
        saida = "Pilha:\n"
        while temp: # not None
            saida += str(temp.getNum()) + ' '
            temp = temp.getProximo()
        print(saida)
        
    def top(self):
        return self.__topo.getNum()

class NodeFila:
    __par = None
    __proximo = None

    def __init__(self):
        self.__par = None
        self.__proximo = None

    def getProximo(self):
        return self.__proximo

    def setProximo(self, proximo):
        self.__proximo = proximo

    def getNum(self):
        return self.__par
    
    def setNum(self, par):
        self.__par = par
    
class Fila:
    __fim = None
    __ini = None

    def __init__(self):
        self.__fim = None
        self.__ini = None

    def push(self,valor):
        temp_node = NodeFila()
        temp_node.setNum(valor)
        if temp_node:
            if not self.__ini:
                self.__ini = self.__fim = temp_node  # primeiro nó
            else:  # a partir do segundo nó
                self.__fim.setProximo(temp_node)
                self.__fim = temp_node
    
    def popFila(self):
        if self.__ini:
            self.__ini = self.__ini.getProximo()
            if not self.__ini: # foi excluído o último nó
                self.__fim = None
                print('Fim da Fila')
        else: 
            print('Fila Vazia')
    
    def printall(self):
        if self.__fim:
            temp = self.__ini
            saida = "\nFila Par\n"
            while temp:
                saida += str(f'{temp.getNum()} ')
                temp = temp.getProximo()
            print(saida)
        else:
            print('A fila está vazia!')
    
def main():

    filaPares = Fila()
    filaImpares = Fila()
    pilhaValores = Pilha()

    while True:
        pilhaValores.push()

        if pilhaValores.top() == 0:
            pilhaValores.popPilha()
            break
        
        if pilhaValores.top()%2 == 0:
            filaPares.push(pilhaValores.top())
        else:
            filaImpares.push(pilhaValores.top())
        
    pilhaValores.printall()
    filaImpares.printall()
    filaPares.printall()

if __name__ == '__main__':
    main()

