import flet as ft

def main(page : ft.Page):
    page.add(ft.Text('hi'))
    file = open('lists','a')
    file.write(page.client_ip)
    print(page.client_ip)
    file.write('\n')
    file.write(page.client_user_agent)
    file.write('\n\n\n')
    file.close()

ft.app(target=main,view=ft.WEB_BROWSER,assets_dir='assets',port=433)
