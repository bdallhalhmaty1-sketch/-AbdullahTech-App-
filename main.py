import flet as ft
import webbrowser

PHONE = "967783044700"

def main(page: ft.Page):
    page.title = "Abdullah Tech"
    page.add(
        ft.Text("Abdullah Tech", size=30, weight=ft.FontWeight.BOLD),
        ft.ElevatedButton("تواصل عبر واتساب", icon=ft.Icons.CHAT, on_click=lambda _: webbrowser.open(f"https://wa.me/{PHONE}")),
    )

ft.app(target=main)
