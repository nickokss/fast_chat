import flet as ft
from random import randint

def get_random_color():
    # Genera un color en formato hexadecimal
    return "#{:06x}".format(randint(0, 0xFFFFFF))

class Message():
    def __init__(self, user, text, color):
        self.user = user
        self.text = text
        self.color = color
        
def main(page:ft.Page):
    user_id = randint(10000, 99999)
    user_color = get_random_color()  # Asignar un color al usuario
    chat = ft.Column()

    new_message = ft.TextField()

    def on_message(message: Message):
        # Uso de ft.Html para incluir el nombre de usuario en color
        user_display = f'<span style="color: {message.color};">Usuario {message.user}:</span>'
        chat.controls.append(ft.Html(
            content=f"{user_display} {message.text}"))
        page.update()

    def send_click(e):
        msg = Message(user=user_id,
                      text=new_message.value,
                      color=user_color)
        page.pubsub.send_all(msg)
        new_message.value = ""
        page.update()

    page.add(chat, ft.Row(controls=[new_message,
                                    ft.ElevatedButton(
                                        "Send",
                                        on_click=send_click
                                    )]))

    # Suscribirse a los mensajes enviados por cualquier usuario
    page.pubsub.subscribe(on_message)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)

##flet run -v main.py -p 52481 -w 
