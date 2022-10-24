import xml.etree.ElementTree as ET

root = ET.Element("Configuration", typical="CAPA_NP")
arq = ET.ElementTree(root)
pai = ET.SubElement(root, 'ConfigurationVariables')

nome = ['DDESCR', 'CLIENTE', 'OBRA', 'END_OBRA', 'ENC_OBRA', 'DOC_REF', 'NUM_CLIENTE', 'NUMERO', 'DATA', 'DESCRICAO', 'ELABORADOR', 'EXECUCAO',
        'VERIFICADOR', 'GESTOR', 'PROCESSO', 'OP', 'TAG_PAINEL', 'CONCESSIONARIA', 'COD_PROT', 'ENTRADA', 'USO', 'ESCALA', 'DADOS_AUTO', 'NOME_PAG',
        'LM_DESCRICAO', 'LM_EXECUCAO', 'LM_ITEM', 'LM_NUM_G', 'LM_NUM_REV', 'LM_PROCESSO']

texto = ['TESTE-2', 'CLIENTE', 'OBRA', 'ENDEREÇO', 'ENCARREGADO', 'TESTE-DOC', 'S/N', '00', '19/10/2022', 'INICIAL', 'BRUNO', 'BRR', 'MIKE',
         'ANDRÉ', 'E-20554', '20554-1', 'TAG PAINEL', 'ENEL-SP', 'CBMT ENEL-AES03A', 'DIREITA', 'ABRIGADO', 'S/E', 'OCULTAR', '1', 'TESTE DESC', 'BRR',
         '1', 'G-00235/2022-REV.01', '5', '20558']

for posicao in nome:

    filho = ET.SubElement(pai, 'ConfigurationVariable', name=posicao)
    filho.text = texto[nome.index(posicao)]
    arq.write('teste-xml.xml')