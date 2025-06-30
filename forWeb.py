import pyautogui

firstClickPosition = (900, 900);
firstClickDuration = 0.3;
secondClickDuration = 0.3;

def deleteLeads(amount):
    pyautogui.moveTo(firstClickPosition[0], firstClickPosition[1], duration=0.5)
    pyautogui.click()
    print('Iniciando exclusão de leads...')
    for lead in range(amount):
        estimated_time = (amount - lead - 1) * (firstClickDuration + secondClickDuration + 1)
        minutes, seconds = divmod(estimated_time, 60)
        print(f'Excluindo lead {lead+1} de {amount} - {round((lead+1)/amount*100, 1)}% - Tempo estimado restante: {int(minutes)}m {int(seconds)}s')
        pyautogui.click(firstClickPosition[0], firstClickPosition[1], duration=firstClickDuration)
        pyautogui.click(firstClickPosition[0]+100, firstClickPosition[1]-150, duration=secondClickDuration)
        pyautogui.countdown(1)
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

read = input('Quantos leads deseja excluir? ')
deleteLeads(int(read))