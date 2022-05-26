class Livro:
    
    def __init__(self, autorDoLivro: str, tituloDoLivro: str, nPaginas: int, vezesEmprestado: int, numReferenciaDoLivro: str=None):
        self.__autor =autorDoLivro
        self.__titulo =tituloDoLivro
        self.__paginas =nPaginas
        self.__nReferencia =numReferenciaDoLivro
        self.__emprestado =vezesEmprestado

    def getAutor(self):
        return self.__autor
    
    def getTitulo(self):
        return self.__titulo
    
    def getPaginas(self, paginas):
        return self.__paginas

    def getNumReferencia(self):
        return self.__nReferencia
    
    def setNumReferencia(self, nReferencia):
        self.__nReferencia =(" ")

    def getEmprestado(self, emprestado):
        return self.__emprestado

    def emprestar(self):
        self.__emprestado = self.__emprestado + 1

    def exibirAutor(self):
        print('Autor: ', self.__autor)
        
    def exibirTitulo(self):
        print('Título: ', self.__titulo)
        
    def exibirPaginas(self):
        print('Páginas: ', self.__paginas)
        
    def exibirNumReferencia(self):
        print('Número de Referência: ', self.__nReferencia)

    def exibirnEmprestado(self):
        print('Emprestado ', self.__emprestado, 'vezes')
        
    def exibirDetalhes(self):
        self.exibirTitulo()
        self.exibirAutor()
        self.exibirPaginas()

        if self.__nReferencia == None:
            print('Número de Referência: ZZZ')
        else:
            self.exibirNumReferencia()
        
        self.emprestar()
        self.emprestar()
        self.exibirnEmprestado()

livro1 = Livro('Robinson Crusoe', 'Daniel Defoe', '232', 0)
livro1.exibirDetalhes()
