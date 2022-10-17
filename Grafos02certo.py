class Grafo:
    def __init__(self, vertice):
        self.v = vertice
        self.adjacentMatriz = [[0 for i in range(self.v)] for j in range(self.v)]

    def AddDirectedEdges(self, src, dest, custo):
        if src == dest:
            print("Mesma origem e destino")
        else:
            self.adjacentMatriz[src][dest] = custo

    def GetDirectedNeighbours(self, src):
        lst = []
        for i in range(len(self.adjacentMatriz[src])):
            if self.adjacentMatriz[src][i] > 0:
                lst.append(i)
        return lst
    
    def DijkstraShortestPath(self,src,dest):
        dct = {}
        for i in range(len(self.adjacentMatriz)):
            temp = {}
            x = self.GetDirectedNeighbours(i)
            for j in x:
                temp[j] = self.adjacentMatriz[i][j]
            dct[i] = temp
        
        inicio = src
        fim = dest
        menor_dist = {}
        pred = {}
        nos_nao_vistos = dct
        infinito = 9999999
        path = []
        maiores = 0
        for node in nos_nao_vistos:
            menor_dist[node] = infinito
        menor_dist[inicio] = 0

        while nos_nao_vistos:
            minNode = None
            for node in nos_nao_vistos:
                if minNode is None:
                    minNode = node
                elif menor_dist[node] < menor_dist[minNode]:
                    minNode = node

            for filho, peso in dct[minNode].items():
                if peso + menor_dist[minNode] < menor_dist[filho]:
                    menor_dist[filho] = peso + menor_dist[minNode]
                    pred[filho] = minNode
            nos_nao_vistos.pop(minNode)

        no_atual = fim
        while no_atual != inicio:
            try:
                path.insert(0,no_atual+1)
                no_atual = pred[no_atual]
            except KeyError:
                print('Caminho nao alcançável')
                break
        path.insert(0,inicio+1)
        if menor_dist[fim] != infinito:
            maiores += menor_dist[fim]
            print('Menor distancia é', str(menor_dist[fim]))
            print('E o caminho é', str(path))
            print('\n')
            return maiores
        

g = Grafo(10)
g.AddDirectedEdges(0,1,10)
g.AddDirectedEdges(0,4,3)
g.AddDirectedEdges(0,6,5)
g.AddDirectedEdges(1,3,3)
g.AddDirectedEdges(1,5,3)
g.AddDirectedEdges(2,0,6)
g.AddDirectedEdges(2,3,8)
g.AddDirectedEdges(2,5,8)
g.AddDirectedEdges(3,4,10)
g.AddDirectedEdges(3,5,1)
g.AddDirectedEdges(3,1,5)
g.AddDirectedEdges(4,5,20)
g.AddDirectedEdges(4,9,8)
g.AddDirectedEdges(4,8,11)
g.AddDirectedEdges(5,6,20)
g.AddDirectedEdges(5,9,12)
g.AddDirectedEdges(5,7,5)
g.AddDirectedEdges(5,1,2)
g.AddDirectedEdges(6,4,7)
g.AddDirectedEdges(7,6,2)
g.AddDirectedEdges(7,8,12)
g.AddDirectedEdges(7,9,3)
g.AddDirectedEdges(8,4,2)
g.AddDirectedEdges(8,5,20)
g.AddDirectedEdges(8,7,4)
g.AddDirectedEdges(9,0,5)
g.AddDirectedEdges(9,2,7)
g.AddDirectedEdges(9,4,4)
g.AddDirectedEdges(9,7,20)
g.AddDirectedEdges(9,8,6)

list_maiores = []

for i in range(10):
    maiores2=0
    for j in range(10):
        print('DO GRAFO', i+1,'AO GRAFO', j+1)
        maiores = g.DijkstraShortestPath(i,j)
        maiores2 += maiores
    list_maiores.append(maiores2)
    print('---------------------------------------')

print('lista de distancias totais', list_maiores)
index = list_maiores.index(min(list_maiores))
print('O elemento central é:',index+1)