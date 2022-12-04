import re

with open('gastosCamaraMunicipalSP.csv', encoding="utf8") as csvfile:
    informacao_por_deputado: list = csvfile.read().split('Vereador(a)')
    ficha: list = []
    camara_inteira = []
    camara_inteira.append(informacao_por_deputado.pop(0))
    camara_inteira.append(informacao_por_deputado.pop(0))
    camara_inteira.append(informacao_por_deputado.pop(0))
    camara_inteira.append(informacao_por_deputado.pop(0))

    for dados_dos_gastos in informacao_por_deputado:
        informacoes = dados_dos_gastos.split('\n')
        gastos = []

        for informacao in informacoes:
            gasto = re.search('^\d{2}.\d{3}.\d{3}/\d{4}-\d{2}', informacao)

            if gasto is not None:
                index = informacoes.index(informacao) - 1
                tipo = informacoes[index]
                gastos.append((tipo, gasto.string))

        ficha.append(({'nome':informacoes[0].replace(': ', '')}, {'gastos': tuple(gastos)}))
        for dep in ficha:
            for item in dep[1]['gastos']:
                print(item)
                print('================================================================================================================================================')







class DataOrganization:
    def __init__(self: object, data: str):
        self._data: str = data




'''
: SILVIA DA BANCADA FEMINISTA
"Natureza da despesa Valor utilizado COMBUSTIVEL 20.190.819/0001-76 CENTRO AUTOMOTIVO THOMAS EDISON 706,52 TOTAL DO ITEM 706,52 CONTRATAÇAO DE PESSOA JURIDICA 44.121.715/0001-78 CH CONSULTORIA EM PLANEJAMENTO E GESTÃO URBANA 4.000,00 TOTAL DO ITEM 4.000,00 INTERMEDIADO - LOCAÇÃO DE VEÍCULOS 50.176.288/0001-28 CAMARA MUNICIPAL DE SÃO PAULO 1.432,67 TOTAL DO ITEM 1.432,67 LOCAÇÃO DE MOVEIS E EQUIPAMENTOS 40.721.413/0001-80 THIAGO ZAMBRANO MAHRENHOLZ 3.080,00 69.064.053/0001-72 SINALL COM E SERV DE MÁQUINAS LTDA 1.175,78 TOTAL DO ITEM 4.255,78 MATERIAL DE ESCRITORIO E OUTROS MATERIAIS DE CONSUMO 06.226.820/0001-82 CENTER PAPEIS COMERCIAL LTDA. 71,85 TOTAL DO ITEM 71,85 TELEFONE MOVEL 02.558.157/0001-62 TELEFONICA BRASIL S/A 78,99 TOTAL DO ITEM 78,99 TOTAL DO MÊS 10.545,81",Natureza da despesa,Valor utilizado,COMBUSTIVEL,20.190.819/0001-76,CENTRO AUTOMOTIVO THOMAS EDISON,"706,52",TOTAL DO ITEM,"706,52",CONTRATAÇAO DE PESSOA JURIDICA,44.121.715/0001-78,CH CONSULTORIA EM PLANEJAMENTO E GESTÃO URBANA,"4.000,00",TOTAL DO ITEM,"4.000,00",INTERMEDIADO - LOCAÇÃO DE VEÍCULOS,50.176.288/0001-28,CAMARA MUNICIPAL DE SÃO PAULO,"1.432,67",TOTAL DO ITEM,"1.432,67",LOCAÇÃO DE MOVEIS E EQUIPAMENTOS,40.721.413/0001-80,THIAGO ZAMBRANO MAHRENHOLZ,"3.080,00",69.064.053/0001-72,SINALL COM E SERV DE MÁQUINAS LTDA,"1.175,78",TOTAL DO ITEM,"4.255,78",MATERIAL DE ESCRITORIO E OUTROS MATERIAIS DE CONSUMO,06.226.820/0001-82,CENTER PAPEIS COMERCIAL LTDA.,"71,85",TOTAL DO ITEM,"71,85",TELEFONE MOVEL,02.558.157/0001-62,TELEFONICA BRASIL S/A,"78,99",TOTAL DO ITEM,"78,99",TOTAL DO MÊS,"10.545,81"
Natureza da despesa,Valor utilizado
COMBUSTIVEL
20.190.819/0001-76,CENTRO AUTOMOTIVO THOMAS EDISON,"706,52"
TOTAL DO ITEM,"706,52"
CONTRATAÇAO DE PESSOA JURIDICA
44.121.715/0001-78,CH CONSULTORIA EM PLANEJAMENTO E GESTÃO URBANA,"4.000,00"
TOTAL DO ITEM,"4.000,00"
INTERMEDIADO - LOCAÇÃO DE VEÍCULOS
50.176.288/0001-28,CAMARA MUNICIPAL DE SÃO PAULO,"1.432,67"
TOTAL DO ITEM,"1.432,67"
LOCAÇÃO DE MOVEIS E EQUIPAMENTOS
40.721.413/0001-80,THIAGO ZAMBRANO MAHRENHOLZ,"3.080,00"
69.064.053/0001-72,SINALL COM E SERV DE MÁQUINAS LTDA,"1.175,78"
TOTAL DO ITEM,"4.255,78"
MATERIAL DE ESCRITORIO E OUTROS MATERIAIS DE CONSUMO
06.226.820/0001-82,CENTER PAPEIS COMERCIAL LTDA.,"71,85"
TOTAL DO ITEM,"71,85"
TELEFONE MOVEL
02.558.157/0001-62,TELEFONICA BRASIL S/A,"78,99"
TOTAL DO ITEM,"78,99"
TOTAL DO MÊS,"10.545,81
'''