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
    inicio = "Hola "
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
        pyautogui.write('opera')
        pyautogui.press('enter')

        # Espera o navegador abrir
        time.sleep(2)

        # ABRIR O SITE
        pyautogui.write('https://readloud.net/spanish/castilian/18-voz-masculina-enrique.html')
        pyautogui.press('enter')

        # Tempo para o site carregar
        time.sleep(5)  # Ajuste conforme necessário para dar tempo do site carregar

        # Mover o mouse até a posição desejada
        pyautogui.moveTo(810, 633)

        # Clicar no ponto para focar no campo de texto
        pyautogui.click()

        # Simular Ctrl+V para colar a frase no site
        pyautogui.hotkey('ctrl', 'v')
        
        # Esperar um pouco para evitar possíveis travamentos
        time.sleep(1)

        # Mover o mouse até a posição de gerar a voz
        pyautogui.moveTo(810, 797)

        # Pausa para garantir que o site esteja pronto
        time.sleep(1)

        # Clicar para gerar a voz
        pyautogui.click()

        # Tempo para gerar o arquivo de voz
        time.sleep(4)

        # Contar arquivos na pasta de downloads antes do download
        files_before = count_files_in_download_folder()

        # Mover o mouse até a posição do botão de download
        pyautogui.moveTo(1133, 438)
        pyautogui.click()

        # Esperar o tempo necessário para completar o download
        time.sleep(3)

        # Contar arquivos na pasta de downloads após o download
        files_after = count_files_in_download_folder()

        # Verificar se o download foi bem-sucedido
        if files_after > files_before:
            print(f"Download bem-sucedido para: {frase}")
        else:
            # Se o número de arquivos não aumentar, registrar a frase no log
            with open(log_file, "a") as f:
                f.write(frase + "\n")
            print(f"Falha ao baixar a frase: {frase}")

        # Fechar o navegador
        pyautogui.hotkey('ctrl', 'w')

if __name__ == "__main__":
    main()
