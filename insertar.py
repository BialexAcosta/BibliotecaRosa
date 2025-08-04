from app import db, Libro
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///libros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    # Lista de libros con tus datos, categorías y etiquetas como strings separados por comas
    libros = [
        {
            "titulo": "El Señor de los Anillos",
            "autor": "J.R.R. Tolkien",
            "categoria": "Fantasía - Épica",
            "etiquetas": "fantasía, aventura, medieval"
        },
        {
            "titulo": "Cien años de soledad",
            "autor": "Gabriel García Márquez",
            "categoria": "Realismo Mágico - Literatura",
            "etiquetas": "realismo mágico, clásico, literatura"
        },
        {
            "titulo": "Drácula",
            "autor": "Bram Stoker",
            "categoria": "Terror - Gótico",
            "etiquetas": "terror, vampiros, clásico"
        },
        {
            "titulo": "La sombra del viento",
            "autor": "Carlos Ruiz Zafón",
            "categoria": "Suspenso - Misterio",
            "etiquetas": "suspenso, misterio, literatura"
        },
        {
            "titulo": "Orgullo y prejuicio",
            "autor": "Jane Austen",
            "categoria": "Romance - Clásico",
            "etiquetas": "romance, clásico, literatura"
        },
        {
            "titulo": "Juego de tronos",
            "autor": "George R.R. Martin",
            "categoria": "Fantasía - Medieval",
            "etiquetas": "fantasía, medieval, aventura"
        },
        {
            "titulo": "El resplandor",
            "autor": "Stephen King",
            "categoria": "Terror - Psicológico",
            "etiquetas": "terror, psicológico, clásico"
        },
        {
            "titulo": "El código Da Vinci",
            "autor": "Dan Brown",
            "categoria": "Suspenso - Thriller",
            "etiquetas": "suspenso, thriller, misterio"
        },
        {
            "titulo": "La princesa prometida",
            "autor": "William Goldman",
            "categoria": "Fantasía - Aventura",
            "etiquetas": "fantasía, aventura, romance"
        },
        {
            "titulo": "Cazadores de sombras",
            "autor": "Cassandra Clare",
            "categoria": "Fantasía - Juvenil",
            "etiquetas": "fantasía, juvenil, aventura"
        },
        {
            "titulo": "El nombre del viento",
            "autor": "Patrick Rothfuss",
            "categoria": "Fantasía - Épica",
            "etiquetas": "fantasía, épica, aventura"
        },
        {
            "titulo": "Jane Eyre",
            "autor": "Charlotte Brontë",
            "categoria": "Romance - Clásico",
            "etiquetas": "romance, clásico, literatura"
        },
        {
            "titulo": "El silencio de los corderos",
            "autor": "Thomas Harris",
            "categoria": "Suspenso - Psicológico",
            "etiquetas": "suspenso, psicológico, thriller"
        },
        {
            "titulo": "La llamada de Cthulhu",
            "autor": "H.P. Lovecraft",
            "categoria": "Terror - Cosmic Horror",
            "etiquetas": "terror, horror cósmico, clásico"
        },
        {
            "titulo": "La catedral del mar",
            "autor": "Ildefonso Falcones",
            "categoria": "Histórico - Medieval",
            "etiquetas": "histórico, medieval, aventura"
        }
    ]

    for libro_data in libros:
        libro = Libro(
            titulo=libro_data['titulo'],
            autor=libro_data['autor'],
            categoria=libro_data['categoria'],
            etiquetas=libro_data['etiquetas']
        )
        db.session.add(libro)

    db.session.commit()
    print("Libros insertados correctamente.")
