import xml.etree.ElementTree as ET

arquivo = "EXP-COG-2.xml"
tree = ET.parse(arquivo)
root = tree.getroot()
descricao = './/ConfigurationVariables/ConfigurationVariable[@name="DDESCR"]'

# Escreve o atributo do XML
print(root.attrib)

# Faz a leitura do conteudo de uma determinada variável do xml
conteudo = tree.find(descricao).text
print(conteudo)