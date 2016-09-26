import utils

class Proposal(object):

    def reader(self, url):
        m = 0

        proposals = utils.load_url(url, 'propostas')
        for item in proposals:
            print item['data_envio_proposta']
            print item['valor_contra_partida']
            print item['valor_repasse']
            print item['fim_execucao']
            print item['data_cadastramento_proposta']
            print item['valor_global']

            print '\n###Proponente'
            proponent_url = '%s.json' % (item['proponente']['Proponente']['href'])
            self.read_proponente(proponent_url)

            print item['inicio_execucao']

            print '\n###Situacao'
            situation_url = '%s.json' % (item['situacao']['SituacaoProposta']['href'])
            self.read_situation(situation_url)

            print '\n###Proposta'
            proposal_url = '%s.json' % (item['href'])
            self.read_proposal(proposal_url)

            print item['objeto_resumido']
            print item['justificativa_resumida']

            if m > 0:
                break

            m = m + 1

    def read_proponente(self, url):
        proponents = utils.load_url(url, 'proponentes')
        for item in proponents:
            print item['cnpj']
            print item['cpf_responsavel']
            print item['nome']
            print item['inscricao_estadual']
            print item['esfera_administrativa']['EsferaAdministrativa']['href']
            print item['nome_responsavel']
            print item['natureza_juridica']['NaturezaJuridica']['href']
            print item['pessoa_responsavel']['PessoaResponsavel']['href']
            print item['municipio']['Municipio']['href']

    def read_situation(self, url):
        situation = utils.load_url(url, 'situacaopropostas')
        for item in situation:
            print item['nome']

    def read_proposal(self, url):
        proposals = utils.load_url(url, 'propostas')
        for item in proposals:
            print item['data_envio_proposta']
            print item['valor_contra_partida']
            print item['valor_repasse']
            print item['fim_execucao']
            print item['objeto']
            print item['justificativa']
            print item['valor_global']

            print '\n###Programas'
            for i in item['programas']:
                print i['associacao'][0]['Programa']['href']
                values = i['associacao'][1]['valores']
                values['contrapartida_financeira']
                values['global']
                values['contrapartida']
                values['repasse']
                values['contrapartida_bens_servicos']

prop = Proposal()
prop.reader('http://api.convenios.gov.br/siconv/v1/consulta/propostas.json')
