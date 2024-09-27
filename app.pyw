import flet as ft
from models import Produto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///projeto2.db"

engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind=engine)
session = Session()


def main(page: ft.Page):
    page.title = "Clientes Atendidos"
    
    lista_produtos = ft.ListView()
    
    def cadastro(e):
        novo_produto = Produto(titulo=produto.value, preco=preco.value)
        session.add(novo_produto)
        session.commit()
        lista_produtos.controls.append(ft.Text(produto.value))
        page.update()
            
    txt_titulo = ft.Text("Código do cliente")
    produto = ft.TextField(label="Digite o titulo do produto") # text_align=ft.TextAlign.RIGHT - para caso deseje que o cursor do usuário fique na direita
    txt_preco = ft.Text("Preço do produto")
    preco = ft.TextField(value=0, label="Digite o preço do produto")
    btn_cadastrar = ft.ElevatedButton("Cadastrar", on_click=cadastro)
    
    page.add(
        txt_titulo,
        produto,
        txt_preco,
        preco,
        btn_cadastrar
    )
    
    for c in session.query(Produto).all(): #basicamente dá um query, uma busca, e colhe o banco de dados
        lista_produtos.controls.append(
            ft.Container(
                ft.Text(c.titulo), # puxa especificamente os títulos
                bgcolor = ft.colors.BLACK12, # a cor
                padding=15, # da um espaço entre os textos
                alignment=ft.alignment.center # alinhamento
                )
            )
            
        
    page.add(
        lista_produtos
    )

ft.app(target=main)