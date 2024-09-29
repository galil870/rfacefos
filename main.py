from flet import *




def page2(page: Page):
    page.window_height = 740
    page.window_width = 390
    page.window_top = 5
    page.window_left = 960
    page.bgcolor = "white"
    
    bt1 = ElevatedButton("اذا فيس فوس مطي دوس هنا", color="red", bgcolor="black", on_click=lambda e: page3(page))
    tx1 = Text("فيس فوس المطي ", color="black")

    page.clean()
    page.add(
        Row([tx1], alignment=MainAxisAlignment.CENTER),
        Row([bt1], alignment=MainAxisAlignment.CENTER),
    )

    page.update()

def page3(page: Page):
    page.window_height = 740
    page.window_width = 390
    page.window_top = 5
    page.window_left = 960
    page.bgcolor = "white"

    page.clean()
    page.add(
        Column([
            Row([
                Text("عفية صح هو اصلا مطي", size=15)
                ], alignment=MainAxisAlignment.CENTER),
            
            Row([
                ElevatedButton("الرجوع", color="white", bgcolor="blue", on_click=lambda e: page2(page))
            ], alignment=MainAxisAlignment.CENTER),
        ])
    )

    page.update()

def main(page: Page):
    page2(page)

app(main)
