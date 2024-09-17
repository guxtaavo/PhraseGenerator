import pyautogui
import pyperclip
import time
import os

# Caminho da pasta de downloads
download_folder = os.path.expanduser("~/Downloads")

def count_files_in_download_folder():
    """Função para contar o número de arquivos na pasta de downloads."""
    return len(os.listdir(download_folder))

def main():
    inicio = "Hello "
    nomes = "Bastián-Cristóbal-Oliver-Damarys-Giselle-Avril-Antonella-Ainhoa-Paula-Patti-Priscilla"
    lista_nomes = nomes.split('-')

    # Arquivo de log para registrar os downloads que falharem
    log_file = "falhas_download.txt"

    # Limpa o log de falhas anteriores
    if os.path.exists(log_file):
        os.remove(log_file)

    for nome in lista_nomes:
        frase = inicio + nome.strip()
        
        # Copiar a frase para a área de transferência
        pyperclip.copy(frase)

        # Pausa para o PC carregar
        time.sleep(1)

        # ABRIR O NAVEGADOR
        pyautogui.hotkey('win')
        pyautogui.write('opera') # Coloque o seu navegador
        pyautogui.press('enter')

        # Espera o navegador abrir
        time.sleep(2)

        # ABRIR O SITE
        pyautogui.write('https://readloud.net/spanish/castilian/18-voz-masculina-enrique.html')
        pyautogui.press('enter')

        # Tempo para o site carregar
        time.sleep(3.4)  # Ajuste conforme necessário para dar tempo do site carregar

        # Mover o mouse até a posição desejada
        pyautogui.moveTo(684, 543)

        # Clicar no ponto para focar no campo de texto
        pyautogui.click()

        # Simular Ctrl+V para colar a frase no site
        pyautogui.hotkey('ctrl', 'v')
        
        # Esperar um pouco para evitar possíveis travamentos
        time.sleep(1)

        # Mover o mouse até a posição de gerar a voz
        pyautogui.moveTo(659, 702)

        # Pausa para garantir que o site esteja pronto
        time.sleep(1)

        # Clicar para gerar a voz
        pyautogui.click()

        # Tempo para gerar o arquivo de voz
        time.sleep(4)

        # Contar arquivos na pasta de downloads antes do download
        files_before = count_files_in_download_folder()

        # Mover o mouse até a posição do botão de download
        pyautogui.moveTo(922, 417)
        pyautogui.click()

        # Esperar o tempo necessário para completar o download
        time.sleep(3)

        # Contar arquivos na pasta de downloads após o download
        files_after = count_files_in_download_folder()

        # Fechar o navegador
        pyautogui.hotkey('ctrl', 'w')

        # Verificar se o download foi bem-sucedido
        if files_after > files_before:
            print(f"Download bem-sucedido para: {frase}")
            # ABRIR A PASTA DOWLOADS PARA RENOMEAR
            pyautogui.hotkey('win')
            pyautogui.write('e')
            pyautogui.press('enter')
            
            # Tempo para o explorador de arquivos carregar
            time.sleep(1.5)  # Ajuste conforme necessário para dar tempo do site carregar
        
            # Mover o mouse até a posição da pasta download
            pyautogui.moveTo(95, 149)

            # Clicar na pasta para abrir
            pyautogui.click()
            
            # Tempo para a pasta download carregar
            time.sleep(1.5)

            # Mover o mouse até a posição do arquivo baixado na pasta download
            pyautogui.moveTo(241, 119)

            # Clicar para selecionar o arquivo
            pyautogui.click()

            # Tempo para carregar 
            time.sleep(1.0)

            # Pressionar tecla F2 para renomear o arquivo
            pyautogui.hotkey('f2')

            # Inicializa a frase
            frase = frase.lower()

            # Converte a frase em uma lista onde espaços são substituídos por '_'
            nova_frase_lista = []
            for letra in frase:
                if letra == " ":
                    nova_frase_lista.append('_')
                else:
                    nova_frase_lista.append(letra)

            # Transforma a lista em uma string
            nova_frase = ''.join(nova_frase_lista)

            # Copiar a frase para a área de transferência
            pyperclip.copy(nova_frase)

            # Simular Ctrl+V para colar a frase formatada no nome do arquivo
            pyautogui.hotkey('ctrl', 'v')
            
            # Esperar carregar
            time.sleep(1.0)
            
            # Enter para por a frase
            pyautogui.press('enter')

            # Espera para não travar
            time.sleep(1.0)

            # Fechar o arquivo
            pyautogui.hotkey('ctrl', 'w')
        else:
            # Se o número de arquivos não aumentar, registrar a frase no log
            with open(log_file, "a") as f:
                f.write(frase + "\n")
            print(f"Falha ao baixar a frase: {frase}")

if __name__ == "__main__":
    main()