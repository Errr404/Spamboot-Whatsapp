
import pyautogui, time 
time.sleep(4)
for p in range(2000):  ## o número de vezes que sua mensagem vai ser enviada, aqui no caso ela vai ser enviada 2000 vezes
    pyautogui.typewrite("sua mensagem aqui") ## aqui voce escreve a mensagem que voce quer que seja enviada
    pyautogui.press("enter")
