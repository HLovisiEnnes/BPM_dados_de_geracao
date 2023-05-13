from bs4 import UnicodeDammit
import codecs
import webbrowser
from bs4 import BeautifulSoup
import time
import pandas as pd
import os

#hides annoying pandas's warn
pd.options.mode.chained_assignment = None
def make_csv(empresa, folder, save = None):
    #makes a list of all xls files in the folder
    files = os.listdir(folder)
    files_xls = []
    for el in files:
        if el.split('.')[-1] == 'xls':
            files_xls.append(el)
    
    #makes empty dataframe to be iterated over
    data = pd.DataFrame(columns = ['Conta', 'Descrição', 'Saldo Anterior (R$)', 'Débito (R$)',
       'Crédito (R$)', 'Variação (R$)', 'Variação (%)', 'Saldo (R$)', 'Mês'])

    #iterates over all xsl files
    for f in files_xls:
        #open xls as html
        file = codecs.open(f, "r", 'iso-8859-1')
        soup = BeautifulSoup(file, 'html.parser')
        #finds all table information
        tbs = soup.find_all("table")
        #selects current month
        month = str(tbs[1].find_all("td")[5]).split('>')[1].split('<')[0]
        
        #list of companies so that, for each of them, we save only the last submission
        empresas = {}
        for i in range(0,int(len(tbs)/3)):
            p_tag = tbs[3*i+1].find_all("td")
            html = str(p_tag[1])
            empresas[(html.split('>')[1].split('<')[0])] = i
        
        #uses only the company wanted
        if empresa in list(empresas.keys()):
            dfs = pd.read_html(str(tbs[3*empresas[empresa]+2]),decimal=",", thousands=".")[0]
            dfs.columns = dfs.iloc[0]
            dfs = d.iloc[1:]
            dfs['Mês'] = [month for i in range(len(dfs))]
            data = pd.concat([data, dfs])
    
    #saves as excel
    if save != None:
        data.to_excel(save, index = False)
  
    return data.reset_index(drop=True)    
