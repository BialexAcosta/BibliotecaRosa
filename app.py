from collections import defaultdict
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///libros.db'
db = SQLAlchemy(app)

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    autor = db.Column(db.String(100))
    categoria = db.Column(db.String(100))
    etiquetas = db.Column(db.String(200))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    libros = Libro.query.all()
    categorias = defaultdict(list)
    for libro in libros:
        categorias[libro.categoria].append(libro)
    return render_template('index.html', categorias=categorias)

# Rutas agregar, editar, eliminar sin cambios
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nuevo_libro = Libro(
            titulo=request.form['titulo'],
            autor=request.form['autor'],
            categoria=request.form['categoria'],
            etiquetas=request.form['etiquetas']
        )
        db.session.add(nuevo_libro)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('agregar.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    libro = Libro.query.get_or_404(id)
    if request.method == 'POST':
        libro.titulo = request.form['titulo']
        libro.autor = request.form['autor']
        libro.categoria = request.form['categoria']
        libro.etiquetas = request.form['etiquetas']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar.html', libro=libro)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
