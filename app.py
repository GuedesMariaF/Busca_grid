from flask import Flask, render_template, request
import numpy as np
from random import randrange
from buscaGridNP import buscaGridNP

app = Flask(__name__)

def Gera_Problema(nx, ny, qtd):
    mapa = np.zeros((nx, ny), int)
    
    k = 0
    while k < qtd:
        i = randrange(0, nx)
        j = randrange(0, ny)
        if mapa[i][j] == 0:
            mapa[i][j] = 9
            k += 1
    return mapa

nx = 10
ny = 10
qtd_obstaculos = 10
mapa = Gera_Problema(nx, ny, qtd_obstaculos)
sol = buscaGridNP()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        origem_x = int(request.form['origem_x'])
        origem_y = int(request.form['origem_y'])
        destino_x = int(request.form['destino_x'])
        destino_y = int(request.form['destino_y'])
        algoritmo = request.form['algoritmo']
        
        
        limite_profundidade = 10  
        if algoritmo == 'prof_limitada':
            limite_profundidade = int(request.form.get('limite_profundidade', 10))
            print(f"Limite de profundidade: {limite_profundidade}")

        print("Mapa atual:")
        print(mapa)
        print(f"Origem: ({origem_x}, {origem_y}) -> {mapa[origem_x][origem_y]}")
        print(f"Destino: ({destino_x}, {destino_y}) -> {mapa[destino_x][destino_y]}")

        if (mapa[origem_x][origem_y] != 0 or 
            mapa[destino_x][destino_y] != 0 or
            origem_x < 0 or origem_x >= nx or
            origem_y < 0 or origem_y >= ny or
            destino_x < 0 or destino_x >= nx or
            destino_y < 0 or destino_y >= ny):
            return render_template('index.html', 
                                 erro="Coordenadas inválidas! Por favor, tente novamente.",
                                 mapa=mapa.tolist())
        
        origem = [origem_x, origem_y]
        destino = [destino_x, destino_y]

        resultado = executar_busca(algoritmo, origem, destino, limite_profundidade)

        return render_template('resultado.html', 
                              origem=origem, 
                              destino=destino,
                              resultado=resultado,
                              algoritmo=algoritmo,
                              mapa=mapa.tolist(),
                              limite_profundidade=limite_profundidade if algoritmo == 'prof_limitada' else None)
    
    return render_template('index.html', mapa=mapa.tolist())

def executar_busca(algoritmo, origem, destino, limite_profundidade=10):
    if algoritmo == 'amplitude':
        caminho = sol.amplitude(origem, destino, nx, ny, mapa)
    elif algoritmo == 'profundidade':
        caminho = sol.profundidade(origem, destino, nx, ny, mapa)
    elif algoritmo == 'prof_limitada':
        caminho = sol.prof_limitada(origem, destino, nx, ny, mapa, limite_profundidade)
    elif algoritmo == 'aprof_iterativo':
        caminho = sol.aprof_iterativo(origem, destino, nx, ny, mapa, nx*ny)
    elif algoritmo == 'bidirecional':
        caminho = sol.bidirecional(origem, destino, nx, ny, mapa)

    return {
        'caminho': caminho if caminho is not None else [],
        'custo': len(caminho) - 1 if caminho is not None else None,
        'encontrado': caminho is not None
    }

if __name__ == '__main__':
    app.run(debug=True)