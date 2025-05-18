import random as rd
import funcoes_auxiliares1 as fa
from listaDencPeso import listaDuplaEncadeadaPeso as lista

class buscaGridPeso(object):
    
    def custo_uniforme(self,origem,destino,mapa,nx,ny):  
        print("CUSTO UNIFORME")
        print("Origem:", origem)    
        print("Destino:", destino)
        print("Mapa:", mapa)
        l1 = lista()
        l2 = lista()
        visitado = []
        l1.insereUltimo(origem,0,0,None)
        l2.insereUltimo(origem,0,0,None)
        linha = []
        linha.append(origem)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == destino:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                print("Cópia da árvore:\n",l2.exibeLista())
                print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                return caminho, atual.valor2
        
            filhos = fa.sucessores(atual.estado,mapa,nx,ny)
            print(filhos)
            for novo in filhos:
                valor = []
                valor.append(novo[0])
                valor.append(novo[1])
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[2]  # custo do caminho
                v1 = v2 # f1(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==valor:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(valor, v1, v2, atual)
                    l2.insereUltimo(valor, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(valor)
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado", None      
    
    def greedy(self,origem,destino,mapa,nx,ny):  
        l1 = lista()
        l2 = lista()
        visitado = []
        l1.insereUltimo(origem,0,0,None)
        l2.insereUltimo(origem,0,0,None)
        linha = []
        linha.append(origem)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == destino:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                return caminho, atual.valor2
        
            filhos = fa.sucessores(atual.estado,mapa,nx,ny)
            for novo in filhos:
                valor = []
                valor.append(novo[0])
                valor.append(novo[1])
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[2]  # custo do caminho
                v1 = fa.h(valor,destino) # f2(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==valor:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(valor, v1, v2, atual)
                    l2.insereUltimo(valor, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(valor)
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado", None
    
    def a_estrela(self,origem,destino,mapa,nx,ny):  
        l1 = lista()
        l2 = lista()
        visitado = []
        l1.insereUltimo(origem,0,0,None)
        l2.insereUltimo(origem,0,0,None)
        linha = []
        linha.append(origem)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == destino:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                print("Cópia da árvore:\n",l2.exibeLista())
                print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                return caminho, atual.valor2
        
            filhos = fa.sucessores(atual.estado,mapa,nx,ny)
            for novo in filhos:
                valor = []
                valor.append(novo[0])
                valor.append(novo[1])
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[2]  # custo do caminho
                v1 = v2 + fa.h(valor,destino) # f3(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==valor:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(valor, v1, v2, atual)
                    l2.insereUltimo(valor, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(valor)
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado", None

    def aia_estrela(self,origem,destino,mapa,nx,ny,limite):  
        
        while True:
            lim_exc = []
            l1 = lista()
            l2 = lista()
            visitado = []
            l1.insereUltimo(origem,0,0,None)
            l2.insereUltimo(origem,0,0,None)
            linha = []
            linha.append(origem)
            linha.append(0)
            visitado.append(linha)
            
            while l1.vazio() == False:
                atual = l1.deletaPrimeiro()
                
                if atual.estado == destino:
                    caminho = []
                    caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                    #print("Cópia da árvore:\n",l2.exibeLista())
                    #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                    return caminho, atual.valor2
            
                filhos = fa.sucessores(atual.estado,mapa,nx,ny)
                
                for novo in filhos:
                    valor = []
                    valor.append(novo[0])
                    valor.append(novo[1])
                    # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                    v2 = atual.valor2 + novo[2]  # custo do caminho
                    v1 = v2 + fa.h(valor,destino) # f3(n)
                    if v1<=limite:
                        flag1 = True
                        flag2 = True
                        for j in range(len(visitado)):
                            if visitado[j][0]==valor:
                                if visitado[j][1]<=v2:
                                    flag1 = False
                                else:
                                    visitado[j][1]=v2
                                    flag2 = False
                                break
        
                        if flag1:
                            l1.inserePos_X(valor, v1, v2, atual)
                            l2.insereUltimo(valor, v1, v2, atual)
                            if flag2:
                                linha = []
                                linha.append(valor)
                                linha.append(v2)
                                visitado.append(linha)
                    else:
                        lim_exc.append(v1)
            limite = float(sum(lim_exc)/len(lim_exc))
            
        return "Caminho não encontrado", None
