from selenium import webdriver 
import time
import requests
from colorama import Fore, Style, init
import os
from google import genai 
from dotenv import load_dotenv

#---------------Final das importações

#---------------Configurações iniciais
os.system('cls' if os.name =='nt' else 'clear')
init()


#---------------Configuração do Gemini
load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
gemini = genai.Client()

#---------------Função que refaz o prompt do usuário
def converter(prompt):
    response = gemini.models.generate_content(
    model="gemini-2.5-flash",contents=f'Refatore esse prompt{prompt} para que ele possa ser usado em uma IA gerador de imagens, refaça o prompt para que ele fique mais detalhado de forma a conseguir a imagem mais detalhada e fiel possível ao que o usuário quer, não é para criar uma nova ideia e sim refinar o prompt do usuário,Preciso que se lembre de que o usuário não quer explicações nem dicas, forneça o texto refeito de forma direta, é a unica coisa que você precisa fazer, comece o prompt com "Crie uma imagem".')
    novo_prompt = response.text
    return novo_prompt 


#---------------Converter o prompt
prompt_original = input('Digite o prompt:')
prompt_convertido = converter(prompt_original)
print(prompt_convertido)



#---------------Configurações do chrome
#chrome = webdriver.Chrome()#Configurar navegador.
#chrome.get('http://www.google.com.br')
#chrome.maximize_window()

#--------------Função para receber input do usuário
def receber_prompt():
    
    prompt = input('Descreva em detalhes a imagem que deseja criar:  ')
    time.sleep(1)
    print(f'Você digitou: {Fore.BLUE+prompt+Style.RESET_ALL}')

    

