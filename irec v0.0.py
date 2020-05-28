# IREC - Importar Relatórios de Empresas via CVM

###############################################################################
# IMPORTS
###############################################################################

import requests
import os
import zipfile as zf

###############################################################################
# Funções
###############################################################################

# TODO: inserir tratamento de erro, caso não seja possível executar o download
def download_itr(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)


###############################################################################
# Variáveis
###############################################################################
# lista para armazenar a relação de endereços dos itrs
endereco_itrs = []



###############################################################################
# Rotina
###############################################################################

# Definições
# endereço dos arquivos ITRS no site da cvm
# TODO: elaborar forma de pesquisar quais ITRS estão diponíveis

print('\nObtendo relação de endereços dos ITRs no sitio da CVM')

# Obtendo a relação de endereços 
with open(os.path.join(os.getcwd(), 'src', 'enderecos_itrs.txt'), encoding="latin-1") as relacaoEnderecosItrs:
    for linhaArquivo in relacaoEnderecosItrs:
# armazenando n lista endereco_itrs
        endereco_itrs.append(linhaArquivo.strip())

print('Relação Obtida\n')

# Criando pasta do diretório onde estiver o programa para receber os arquivos com os ITRS
os.makedirs('itrs', exist_ok=True)

# TODO: evidenciar progresso dos downloads
# TODO melhorar forma como os downloads são feitos
for endereco in endereco_itrs:
    print('ANO [ ' + endereco[70:74] + ' ]')
    print('===> Download iniciado')
    download_itr(endereco, os.path.join(os.getcwd(), 'itrs', endereco[55:]))
    print('===> Download conclído\n')

