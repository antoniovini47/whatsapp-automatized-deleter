import pyautogui

def deleteLeads(amount):
    print('Iniciando exclusão de leads...')
    for lead in range(amount):
        print(f'Excluindo lead {lead+1} de {amount} - {round((lead+1)/amount*100, 2)}%')
        pyautogui.click(900, 840, duration=0.8)
        pyautogui.click(1000, 680, duration=0.8)

read = input('Quantos leads deseja excluir? ')
deleteLeads(int(read))