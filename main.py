import time
from pynput import keyboard
from pynput import mouse

coord_first_button = []
coord_second_button = []
help_message = '''1) Наведи на кнопку "Повторить" первого гремлина и нажми "1" чтобы запомнить координаты первой кнопки.
2) Наведи на кнопку "Повторить" второго гремлина и нажми "2" чтобы запомнить координаты второй кнопки.
3) Открой окно с гремлинами и нажми "0" чтобы запустить процесс автоматической добычи ресурсов.
Для остановки добычи закрой данное окно.
'''


def toggle_event(key):
    if key == keyboard.KeyCode(char='1'):
        global coord_first_button
        coord_first_button = mouse.Controller().position
        print(f"Координаты первого гремлина: {coord_first_button}")
    if key == keyboard.KeyCode(char='2'):
        global coord_second_button
        coord_second_button = mouse.Controller().position
        print(f"Координаты второго гремлина: {coord_second_button}")
    if key == keyboard.KeyCode(char='0'):
        print('Процесс добычи ресурсов включен!')
        clicker()
    if key == keyboard.Key.esc:
        return False  # Stop listener


def clicker():
    while True:
        mouse.Controller().position = coord_first_button
        mouse.Controller().click(mouse.Button.left, 1)
        time.sleep(1)
        mouse.Controller().position = coord_second_button
        mouse.Controller().click(mouse.Button.left, 1)
        time.sleep(65)


def main():
    print(help_message)
    with keyboard.Listener(on_release=toggle_event) as listener:
        listener.join()


if __name__ == "__main__":
    main()
