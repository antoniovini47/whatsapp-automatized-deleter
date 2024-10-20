import pyautogui

def deleteLeads(amount):
    print('Iniciando exclusão de leads...')
    position = 1
    for lead in range(amount):
        print(f'Excluindo lead {lead+1} de {amount} - {round((lead+1)/amount*100, 2)}%')
        if (position==1):
            pyautogui.click(1417, 623, duration=0.6)
            pyautogui.click(1412, 703, duration=0.4)
            position = 2
        elif(position==2):
            pyautogui.click(1417, 573, duration=0.6)
            pyautogui.click(1412, 653, duration=0.4)
            position = 3
        else:
            pyautogui.click(1417, 524, duration=0.6)
            pyautogui.click(1412, 604, duration=0.4)
            position = 1
        pyautogui.countdown(1)
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

read = input('Quantos leads deseja excluir? ')
deleteLeads(int(read))