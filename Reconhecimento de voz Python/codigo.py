import os
import speech_recognition as sr
import pyautogui
import PySimpleGUI as sg

pyautogui.PAUSE = 1.5
rec = sr.Recognizer()

layout = [
    [sg.Text("Pressione o botão e fale")],
    [sg.Button("Iniciar Reconhecimento de Voz")],
    [sg.Output(size=(40, 10))]
]

window = sg.Window("Controle por Voz", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Iniciar Reconhecimento de Voz":
        with sr.Microphone(1) as mic:
            rec.adjust_for_ambient_noise(mic)
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language="pt-BR")

            if 'navegador' in texto:
                os.system("start Chrome.exe")

            if 'pesquise' in texto:
                pyautogui.hotkey('alt', 'tab')
                pyautogui.click(x=599, y=58)
                pyautogui.write(texto[19:])
                pyautogui.press('enter')

            print(texto)

window.close()