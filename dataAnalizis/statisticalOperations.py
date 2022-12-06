import re
import json
from typing import List,Dict,Tuple

"""

#-------------------------limpa os dados do arquivo gastosCamaraMunicipalSP-------------------------

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

                nome = re.search('^[A-Z]',informacoes[index])
                if nome != None:
                    tipo = informacoes[index]
                    gastos.append((tipo, gasto.string))
                else:
                    tipo = informacao.split(',')[1]
                    gastos.append((tipo, gasto.string))


        ficha.append({'nome': informacoes[0].replace(': ', ''),  'gastos': gastos})
    json_object = json.dumps(ficha, indent=4,ensure_ascii=False)

    with open("gastosCamaraMunicipalSP_emJson.json", "w", encoding='utf8') as outfile:
        outfile.write(json_object)


"""

ARQUIVO = List[Dict[str, List]]

class OrganizacaoGastosCamara:
    def __init__(self: object, arquivo_nome: str):
        with open(arquivo_nome, encoding='utf8') as data:
            arquivo:ARQUIVO = json.load(data)

        self._arquivo: list = arquivo

    @property
    def arquivo(self: object):
        return self._arquivo

    def juntarValoresIguais(self: object, dataToBeCombined: List) -> List:
        final_data: List = []

        for info in dataToBeCombined:
            same_info: List = []
            single_info: List = []
            to_be_combined = info[0]
            single_info.append({'info': info[0], 'dadosValores': {'valores': info[-1].split('"')[-2],'howManyTimes': 1}})
            valores = []

            for second_info in dataToBeCombined:
                del single_info[:-1]
                name = second_info[0]

                if to_be_combined == name:
                    valor = second_info[-1].split('"')[-2]
                    valores.append(valor)
                    same_info.append(second_info)

            final_data.append({'info': info[0], 'dadosValores':{'valores': valores,'quantasVezes': len(same_info)}})
            for info in single_info:
                final_data.append(info)
        print(final_data)

        return final_data





gastos_camara = OrganizacaoGastosCamara('gastosCamaraMunicipalSP_emJson.json')


for data in gastos_camara.arquivo:
    #print(data['nome'])
    gastos_camara.juntarValoresIguais(dataToBeCombined=data['gastos'])

