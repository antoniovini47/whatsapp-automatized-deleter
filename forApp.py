import pyautogui

clickPosX = 1545;
posToDeleteButtonFactor = 78;
firstButtonPosY= 732;
firstClickDuration = 2.0;
secondClickDuration = 0.5;

def deleteLeads(amount):
    print('Iniciando exclusão de leads...')
    position = 1
    for lead in range(amount):
        estimated_time = (amount - lead - 1) * (firstClickDuration + secondClickDuration + 1)  # Including countdown
        minutes, seconds = divmod(estimated_time, 60)
        print(f'Excluindo lead {lead+1} de {amount} - {round((lead+1)/amount*100, 1)}% - Tempo estimado restante: {int(minutes)}m {int(seconds)}s')
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