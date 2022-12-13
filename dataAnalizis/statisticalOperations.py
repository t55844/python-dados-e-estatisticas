import copy
import re
from typing import List,Dict,Tuple,AnyStr

FLOAT_LIST = List[float]
INTERVALO_CLASSES = List[Dict]
class calculosEstatisticos:
    def __init__(self: object, dados: list):
        self._dados: FLOAT_LIST = self.convercao_dados_float(dados)
        self._quantidade: int = len(dados)
    @property
    def dados(self: object) -> FLOAT_LIST:
        return self._dados

    @property
    def quantidade(self:object) -> int:
        return self._quantidade

    @property
    def ordem_crecente(self:object) -> FLOAT_LIST:
        return sorted(self.dados)
    def convercao_dados_float(self:object, dados:list) ->FLOAT_LIST:
        if(type(dados[0]) == str):
            valores: list = [float(valor.replace(',', '.')) for valor in [dado_com_ponto.replace('.', '') for dado_com_ponto in dados]]
            return valores
        elif(type(dados[0]) == float):
            valores: list = [float(valor) for valor in dados]
            return valores
        elif(type(dados[0]) == int):
            valores: list = [float(valor) for valor in dados]
            return valores
        else:
            raise ValueError('O dos dados da lista tem que ser int, float ou str')

    @property
    def media(self: object ) -> float:
        total = sum(self.dados)
        media = total/self.quantidade
        return media

    @property
    def amplitude_total(self:object) -> int:
        menor_numero = self.ordem_crecente[0]
        maior_numero = self.ordem_crecente[-1]
        amplitude = maior_numero - menor_numero
        return amplitude

    @property
    def intervalo_de_classes(self:object) -> INTERVALO_CLASSES:
        quantidade_intervalos = self.quantidade / 2
        valor_intervalo = self.amplitude_total / quantidade_intervalos
        valores: list = copy.deepcopy(self.ordem_crecente)
        intervalo_classes: INTERVALO_CLASSES =[]
        valores_verificados: list = []
        for valor in valores:
            if(valor not in valores_verificados):
                limite_inferior: int = valor
                limite_superior: int = valor + valor_intervalo
                valores_no_intervalo: List = []
                for segundo_valor in valores:
                    if(segundo_valor <= limite_superior and segundo_valor >= limite_inferior):
                        valores_no_intervalo.append(segundo_valor)
                        valores_verificados.append(segundo_valor)
                intervalo_classes.append({
                    'intervalo_classes': f'Entre {limite_inferior} e {limite_superior} : {len(valores_no_intervalo)}',
                    'frequencia': len(valores_no_intervalo),
                    'intervalos': [limite_superior,limite_inferior]
                })

        return intervalo_classes

    @property
    def media_aritimetica(self: object):
        frequencias: list = []
        intervalos_frequencia_multiplicacao:list = []
        for intervalo in self.intervalo_de_classes:
            media = sum(intervalo['intervalos']) / 2
            mutiplicacao = media * intervalo['frequencia']
            intervalos_frequencia_multiplicacao.append(mutiplicacao)
            frequencias.append(intervalo['frequencia'])
        media_aritimetica = sum(intervalos_frequencia_multiplicacao)/sum(frequencias)
        return media_aritimetica

    def calcula_percentil(self: object, porcentagem:int) -> str:
        porcentagem = float(f'0.{porcentagem}')
        total_itens = self.quantidade + 1
        posicao_percentil = total_itens * (porcentagem/100)
        posicao_anterior = int(str(posicao_percentil).split('.')[0])
        print('num')
        porcentagem_ate_proxima = float('0.'+ str(posicao_percentil).split('.')[1])
        percentil = self.ordem_crecente[posicao_anterior] + porcentagem_ate_proxima * (self.ordem_crecente[posicao_anterior] - self.ordem_crecente[posicao_anterior + 1])
        return f'{porcentagem * 100}% dos valores são menores que {percentil} e {100 - (porcentagem * 100)}% dos valores estão acima de {percentil}'

dados_testes: list = ['800,00', '800,00', '6.000,00', '6.000,00', '3.000,00', '3.000,00', '2.500,00', '2.500,00', '7.000,00', '7.000,00', '500,00', '500,00', '900,00', '900,00', '1.415,00', '1.415,00', '6.000,00', '6.000,00', '8.000,00', '8.000,00']
calc1_test = calculosEstatisticos(dados_testes)
print(calc1_test.ordem_crecente)
print(calc1_test.amplitude_total)
print(calc1_test.intervalo_de_classes)
print('medias')
print(calc1_test.media)
print(calc1_test.media_aritimetica)
print(calc1_test.calcula_percentil(50))

calc2_test = calculosEstatisticos([4.0, 8])
print(calc2_test.ordem_crecente)
print(calc2_test.amplitude_total)
print(calc2_test.intervalo_de_classes)
print('medias')
print(calc2_test.media)
print(calc2_test.media_aritimetica)
print(calc2_test.calcula_percentil(50))