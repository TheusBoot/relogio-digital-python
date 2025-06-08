import flet as ft
import time
import datetime

def main(page: ft.Page):
    page.title = "Digital Clock"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    time_text = ft.Text(
        value=datetime.datetime.now().strftime("%H:%M:%S"),
        size=50,
        weight=ft.FontWeight.BOLD,
    )

    page.add(time_text)

    def update_time():
        while True:
            time_text.value = datetime.datetime.now().strftime("%H:%M:%S")
            page.update()
            time.sleep(1)

    page.run_thread(target=update_time)

ft.app(target=main)
