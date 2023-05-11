from selenium import webdriver 
from selenium.webdriver.common.by import By
import time  
from selenium.webdriver.common.keys import Keys  


driver = webdriver.Chrome()  

#maximize the window size  
driver.maximize_window()  
#navigate to the url  
driver.get("http://informacoesbmp.aneel.gov.br/ConsultarBMPAberto.aspx")  
print('Connected')

#click todas empresas  
driver.find_element(By.XPATH,'/html/body/form/div[3]/div[5]/div[3]/div[1]/fieldset/table/tbody/tr[3]/td[2]/input').click()

#click Geração
driver.find_element(By.XPATH,'/html/body/form/div[3]/div[5]/div[3]/div[1]/fieldset/table/tbody/tr[4]/td[2]/input[3]').click()

#choose dates
driver.find_element(By.XPATH,"//input[@id='Conteudo_txtDataInicioPesquisa']").clear()
driver.find_element(By.XPATH,"//input[@id='Conteudo_txtDataInicioPesquisa']").click()
driver.find_element(By.XPATH,"//input[@id='Conteudo_txtDataInicioPesquisa']").send_keys("012020")
driver.find_element(By.XPATH,"//input[@id='Conteudo_txtDataFimPesquisa']").clear()
driver.find_element(By.XPATH,"//input[@id='Conteudo_txtDataFimPesquisa']").click()
driver.find_element(By.XPATH,"//input[@id='Conteudo_txtDataFimPesquisa']").send_keys("012020")

#clicks Confirmar
driver.find_element(By.XPATH,'/html/body/form/div[3]/div[5]/div[3]/div[1]/div/input[1]').click()
time.sleep(3)  

#clicks all page options
driver.find_element(By.XPATH,'/html/body/form/div[3]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr[1]/th[1]/span/input').click()

#clicks Gerar toodos
driver.find_element(By.XPATH,'/html/body/form/div[3]/div[5]/div[3]/div[2]/div[1]/table/tbody/tr/td/input').click()
time.sleep(3)  

#clicks Confirma on the pop-up
driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div[3]/input[1]').click()