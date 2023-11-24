import flet as ft

def main(page: ft.Page):
    page.window_height = 200
    page.window_width = 200
    page.title = "Counter"
    page.theme_mode = ft.ThemeMode.DARK

    eingabe = ft.TextField(
        value="0",
        text_align=ft.TextAlign.RIGHT,
        width = 60
    )

    def plus_click(e):
        print("Button Clicked: PLUS")
        value = int(eingabe.value)
        value += 1
        eingabe.value = str(value)
        page.update()

    def minus_click(e):
        print("Button Clicked: MINUS")
        value = int(eingabe.value)
        value -= 1
        eingabe.value = str(value)
        page.update()

    plus_button = ft.IconButton(
        icon=ft.icons.EXPOSURE_PLUS_1,
        icon_color="white",
        on_click=plus_click
    )

    minus_button = ft.IconButton(
        icon=ft.icons.EXPOSURE_MINUS_1,
        icon_color="white",
        on_click=minus_click    )

    eingabe_view = ft.Row(
        controls=[
            minus_button, eingabe, plus_button
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )

    ausgabe = ft.Text(
        value="",
        font_family="Arial",
        size=20,
        italic=True,
        color="white"
    )

    def eingabe_ausgeben(e):
        ausgabe.value = eingabe.value
        page.update()

    ausgabe_speichern_button = ft.TextButton(text = "ausgeben...", on_click=eingabe_ausgeben)

    ausgabe_view = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ausgabe_speichern_button,
                    ausgabe
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(eingabe_view, ausgabe_view)

    page.update()

ft.app(target=main)

