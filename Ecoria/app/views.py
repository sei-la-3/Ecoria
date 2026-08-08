from django.shortcuts import render, redirect
from django.db import connection




#INDEX

def index(request):
    return render(request, "acesso.html")



#ACESSO 

def acesso(request):

    if request.method == "POST":

        email = request.POST.get("gemail")
        senha = request.POST.get("senha")

        print("EMAIL:", email)
        print("SENHA:", senha)

        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM usuarios
                WHERE email = %s AND senha = %s
                """,
                [email, senha]
            )

            usuario = cursor.fetchone()

        if usuario:
            print("Login correto")
            return redirect("cadastro")

        else:
            
            print("login incorreto")

            return render(request, "acesso.html", {
                "erro": "E-mail ou senha incorretos."
            })

    return render(request, "acesso.html", {
    "erro": "E-mail ou senha incorretos!"
})
#index

def cadastro(request):
    return render(request, "cadastro.html")