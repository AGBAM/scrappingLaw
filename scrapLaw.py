import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

st.title('Scrapping de Leis Municipais')

link=st.text_input('Digite o link da lei que deseja scrappear')

if link is not None:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    nav=webdriver.Chrome(options=options)
    time.sleep(0.5)
    nav.get(link)
    time.sleep(0.5)
    l=nav.find_elements(By.CLASS_NAME,"tooltips")
    leis=[]
    for i in l:
        leis.append(i.text)
    xpath='//*[@id="conteudo_diploma"]/div/div[1]/center/font'
    texto=nav.find_element(By.XPATH,xpath).text
    df=pd.DataFrame({'Lei':[texto]*len(leis),'Conecta':leis})
    st.dataframe(df)
    nav.quit()
