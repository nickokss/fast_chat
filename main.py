import flet as ft
from random import randint

class Message():
    def __init__(self, user, text):
        self.user = user
        self.text = text
def main(page:ft.Page):
    user_id = randint(10000, 99999) 
    chat = ft.Column()
    new_message = ft.TextField()

    def on_message(message: Message):
        chat.controls.append(ft.Text(
        " Ususario: {message.user}: {message.text}"))
        page.update()

    def send_click(e):
        page.pubsub.send_all(
            Message(user=user_id,
            text=new_message.value))
        new_message.value = ""
        page.update()

    page.add(chat, ft.Row(controls=[new_message,
                                    ft.ElevatedButton(
                                        "Send",
                                        on_click=send_click
                                    )]))    
ft.app(target=main,
       view=ft.AppView.WEB_BROWSER)

##flet run -v main.py -p 52481 -w 
