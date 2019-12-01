#coding: utf-8

from deputado import *
from vetor import *

matriculas = ["119110534", "119110256", "119110985"] #Preencham suas matrículas dentro desta variável
regioes = {
	'NORTE': ['AM', 'RR', 'AP', 'PA', 'PA', 'TO', 'RO', 'AC'],
	'NORDESTE': ['MA', 'PI', 'CE', 'RN', 'PE', 'PB', 'SE', 'AL', 'BA'], 
	'CENTRO-OESTE': ['MT', 'MS', 'GO'], 
	'SUDESTE': ['SP', 'RJ', 'ES', 'MG'],
	'SUL': ['PR', 'RS', 'SC']
	}

'''
Tarefa 02 - Comparar o alinhamento de dois deputados
A função abaixo recebe o nome de dois deputados e o
dicionário mapeando o nome do deputado com seu objeto
da classe Deputado, e retorna o produto interno representando
o grau de similaridade entre a política de voto dos dois deputados dados.
'''
def comparar(dep_a, dep_b, deputados):
	votosA = deputados[dep_a].votos;
	votosB = deputados[dep_b].votos;

	return votosA * votosB;

'''
Tarefa 03 - Encontrar o deputado mais similar com um deputado dado
A função deve receber o nome de um deputado e o dicionário mapeando
o nome do deputado com seu objeto da classe Deputado, e o nome do deputado 
mais similar ao que foi dado como entrada. No caso, de haver mais de um
deputado com o grau de similaridade máxima, todos os nomes devem ser retornados
em uma lista.
'''
def mais_similar(dep, deputados):
	res = []
	diff = -3000000 # Tem que mudar para uma variavel grande rsrsrs
	for deputado in deputados:
		if deputado != dep: # Remover essa linha depois
			similaridade = comparar(dep, deputado, deputados)
			if similaridade >= diff:
				if similaridade > diff:
					res = []
				res.append(deputado)
				diff = similaridade
	return res[0] if len(res) == 1 else res #Checar se há mais de um elemento na lista
			
		

'''
Tarefa 04 - Encontrar o deputado menos similar com um deputado dado
Similar a tarefa 03, porém deve retornar o nome do deputado menos similar
ou uma lista com todos os nomes, em caso de empate.
'''
def menos_similar(dep, deputados):
	res = []
	diff = 3000000 # Tem que mudar para uma variavel grande rsrsrs
	for deputado in deputados:
		if deputado != dep: # Remover essa linha depois
			similaridade = comparar(dep, deputado, deputados)
			if similaridade <= diff:
				if similaridade < diff:
					res = []
				res.append(deputado)
				diff = similaridade
	return res[0] if len(res) == 1 else res #Checar se há mais de um elemento na lista

'''
Tarefa 05 - Implementar a função encontra_similaridade_media(dep, dep_set, deputados)
que, dado o nome de um deputado, compara seu registro de votos com o registro de votos
com todos os deputados cujos nomes estão em dep_set, computando um produto interno para
cada, e então retornando o produto interno médio.
'''
def encontra_similaridade_media(dep, dep_set, deputados):
	soma = 0
	for deputado in dep_set:
		soma += comparar(dep, deputado, deputados)
	return soma / len(dep_set)

'''
Tarefa 06 - Implemente a função encontra_registro_medio(dep_set, voting_dict) que,
dado um conjunto com o nome dos deputados, encontre a média do registro de votação.
Isto é, realize adição vetorial na listas representando o registro de suas votações,
e então divida a soma pelo número de vetores. O resultado deve ser um vetor.
'''
def encontra_registro_medio(dep_set, deputados):
	res = Vetor([0 for i in range(len(deputados))]) # Cria um vetor nulo do tamanho do vetor dos deputados
	cont = 0
	for deputado in dep_set:
		res += deputados[deputado].votos;
		cont += 1
	return res * (1 / cont)

'''
Tarefa 07 - Implemente as funções a seguir
- registro_medio_partido(partido, deputados) que, dado o nome de um partido 
  encontra o registro médio de votação deste partido;
- registro_medio_estado(estado, deputados) que, dado o nome de um estado do
  Brasil encontra o registro médio de votação deste estado;
- registro_medio_regiao(regiao, deputados) que, dada o nome de uma região do
  Brasil encontra o registro médio de votação desta região.

  Considere os nomes da regiões brasileiras sendo NORTE, SUL, SUDESTE, NORDESTE e CENTRO-OESTE

O retorno de todas as funções descritas nesta tarefa deve ser um vetor.
'''

def registro_medio_partido(partido, deputados):
	dep_set = []
	for deputado in deputados:
		if deputados[deputado].partido == partido:
			dep_set.append(deputado)
	return encontra_registro_medio(dep_set, deputados)
    
def registro_medio_estado(estado, deputados):
	dep_set = []
	for deputado in deputados:
		if deputados[deputado].estado == estado:
			dep_set.append(deputado)
	return encontra_registro_medio(dep_set, deputados)
    
def registro_medio_regiao(regiao, deputados):
	dep_set = []
	for deputado in deputados:
		if deputados[deputado].estado in regioes[regiao]:
			dep_set.append(deputado)
	return encontra_registro_medio(dep_set, deputados) 

'''
Tarefa 08 - Implemente as funções a seguir:
- similaridade_no_partido(dep, deputados) que,
  dado o nome de um deputado encontra o grau de similaridade dele com seu partido.
- similaridade_no_estado(dep, deputados) que,
  dado o nome de um deputado encontra o grau de similaridade dele com seu estado.
- similaridade_na_regiao(dep, deputados) que,
  dado o nome de um deputado encontra o grau de similaridade dele com sua regiao.

Para as funções acima o retorno deve ser o respectivo grau de similaridade.

- encontra_mais_alinhado_partido(partido, deputados) que,
  dado o nome de um partido encontra o deputado mais similar ao partido.
  
Para a função acima o retorno deve ser uma lista contendo o nome do deputado e seu respectivo
grau de similaridade.
'''

def similaridade_no_partido(dep, deputados):
	dep_set = []
	for deputado in deputados:
		if deputados[deputado].partido == deputados[dep].partido:
			dep_set.append(deputado)
	return encontra_similaridade_media(dep, dep_set, deputados)

def similaridade_no_estado(dep, deputados):
	dep_set = []
	for deputado in deputados:
		if deputados[deputado].estado == deputados[dep].estado:
			dep_set.append(deputado)
	return encontra_similaridade_media(dep, dep_set, deputados)

def similaridade_na_regiao(dep, deputados):
	regiao_deputado = ""
	for regiao in regioes:
		if deputados[dep].estado in regioes[regiao]:
			regiao_deputado = regiao
	
	dep_set = []
	for deputado in deputados:
		if deputados[deputado].estado in regioes[regiao_deputado]:
			dep_set.append(deputado)
	return encontra_similaridade_media(dep, dep_set, deputados)

def encontra_mais_alinhado_partido(partido, deputados):
	# Obtendo os deputados do partido
	dep_set = []
	for deputado in deputados:
		if deputados[deputado].partido == partido:
			dep_set.append(deputado)

	# Varrendo os deputados do partido e selecionando aquele que tem a maior similaridade
	maior_similaridade = 0
	deputado_similar = ''
	for deputado in dep_set:
		similaridade = encontra_similaridade_media(deputado, dep_set, deputados)
		if similaridade >= maior_similaridade:
			maior_similaridade = similaridade
			deputado_similar = deputado

	return [deputado_similar, maior_similaridade]



'''
Tarefa 09 - Implemente as funções a seguir:
- rivais_amargos(deputados) que encontra os dois deputados menos similares do conjunto inteiro.
- amigos_adocicados(deputados) que encontra os dois deputados mais similares do conjunto inteiro.

O retorno deve ser uma lista contendo os nomes dos dois deputados.
'''

def rivais_amargos(deputados):
	# Varrendo os deputados e selecionando os que são menos similares
	menor_similaridade = 0
	rivais = []
	lista_deputados = list(deputados.keys())
	for i in range(len(lista_deputados)):
		for j in range(i + 1, len(lista_deputados)):
			dep1 = lista_deputados[i]
			dep2 = lista_deputados[j]
			similaridade = comparar(dep1, dep2, deputados) if dep1 != dep2 else 0
			if similaridade <= menor_similaridade:
				menor_similaridade = similaridade
				rivais = [dep1, dep2]
	return rivais


def amigos_adocicados(deputados):
	maior_similaridade = 0
	amigos = []
	lista_deputados = list(deputados.keys())
	for i in range(len(lista_deputados)):
		for j in range(i + 1, len(lista_deputados)):
			dep1 = lista_deputados[i]
			dep2 = lista_deputados[j]
			similaridade = comparar(dep1, dep2, deputados) if dep1 != dep2 else 0
			if similaridade >= maior_similaridade:
				maior_similaridade = similaridade
				amigos = [dep1, dep2]
	return amigos

'''
Tarefa 10 - Implemente as funções a seguir:
- encontra_partido_mais_coerente(deputados) que encontra o partido
  cujos congressistas são mais similares entre si, ou seja, cuja média das
  similaridades entre cada deputado é a maior.
- encontra_partido_menos_coerente(deputados) que encontra o partido
  cujos congressistas são menos similares entre si, ou seja, cuja média das
  similaridades entre cada deputado é a menor.
  
O retorno, para ambas, deve ser o nome do partido.
'''

def encontra_partido_mais_coerente(deputados):
	# Obtendo os partidos e colocando os candidatos em uma lista dentro
	partidos = dict()
	for deputado in deputados:
		partido = deputados[deputado].partido
		if partido not in partidos:
			partidos[partido] = []
		partidos[partido].append(deputado)
	
	# Obtendo a similaridade e comparando
	mais_similar = 0
	partido_mais_coerente = ""

	for partido in partidos:
		similaridade = 0
		for deputado in partidos[partido]:
			similaridade += similaridade_no_partido(deputado, deputados)
		similaridadePartido = similaridade / len(partidos[partido])
		if similaridadePartido >= mais_similar:
			mais_similar = similaridadePartido
			partido_mais_coerente = partido
	
	return partido_mais_coerente

def encontra_partido_menos_coerente(deputados):
	# Obtendo os partidos e colocando os candidatos em uma lista dentro
	partidos = dict()
	for deputado in deputados:
		partido = deputados[deputado].partido
		if partido not in partidos:
			partidos[partido] = []
		partidos[partido].append(deputado)

	# Obtendo a similaridade e comparando
	menos_similar = 300000
	partido_menos_coerente = ""
	
	for partido in partidos:
		similaridade = 0
		for deputado in partidos[partido]:
			similaridade += similaridade_no_partido(deputado, deputados)
		similaridadePartido = similaridade / len(partidos[partido])
		if similaridadePartido <= menos_similar:
			menos_similar = similaridadePartido
			partido_menos_coerente = partido
	
	return partido_menos_coerente
	
