import pyautogui

clickPosX = 1545;
posToDeleteButtonFactor = 78;
firstButtonPosY= 732;
firstClickDuration = 0.8;
secondClickDuration = 0.6;

def deleteLeads(amount):
    print('Iniciando exclusão de leads...')
    position = 1
    for lead in range(amount):
        print(f'Excluindo lead {lead+1} de {amount} - {round((lead+1)/amount*100, 2)}%')
        if (position==1):
            yPos = firstButtonPosY;
            pyautogui.click(clickPosX, yPos, duration=firstClickDuration)
            pyautogui.click(clickPosX, yPos+posToDeleteButtonFactor, duration=secondClickDuration)
            position = 2
        elif(position==2):
            yPos = firstButtonPosY - 45;
            pyautogui.click(clickPosX, yPos, duration=firstClickDuration)
            pyautogui.click(clickPosX, yPos+posToDeleteButtonFactor, duration=secondClickDuration)
            position = 3
        else:
            yPos = firstButtonPosY - 98;
            pyautogui.click(clickPosX, yPos, duration=firstClickDuration)
            pyautogui.click(clickPosX, yPos+posToDeleteButtonFactor, duration=secondClickDuration)
            position = 1
        pyautogui.countdown(1)
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

read = input('Quantos leads deseja excluir? ')
deleteLeads(int(read))