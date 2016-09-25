import utils

class Proposal(object):

    def reader(self, url):
        proposals = utils.load_url(url, 'propostas')

        for item in proposals:
            print item['data_envio_proposta']
            print item['valor_contra_partida']
            print item['valor_repasse']
            print item['fim_execucao']
            print item['data_cadastramento_proposta']
            print item['valor_global']
            print '%s.json' % (item['proponente']['Proponente']['href'])
            print item['inicio_execucao']
            print '%s.json' % (item['situacao']['SituacaoProposta']['href'])
            print item['href']
            print item['objeto_resumido']
            print item['justificativa_resumida']
            break

prop = Proposal()
prop.reader('http://api.convenios.gov.br/siconv/v1/consulta/propostas.json')
