from locust import HttpUser, task, between
import random

class WebSiteUser (HttpUser):
    wait_time = between(2,10)
    HttpUser.host = "https://fakerestapi.azurewebsites.net"

    @task
    def acessarPaginaDeUsuarios(self):
        self.client.get("/api/v1/Books", name="Consultando a Lista de Livros")

    @task(1)
    def criandoUmLivro(self):
        # Criar um novo livro
        book_id = random.randint(1000, 9999)
        self.client.post("/api/v1/Books", json={
            "id": book_id,
            "title": "Performance Testing with Locust",
            "description": "Livro criado via teste de performance",
            "pageCount": 250,
            "excerpt": "Um teste de exemplo...",
            "publishDate": "2025-01-01"
        })