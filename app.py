from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# Instancia de una aplicación de Flask
# Si el script se ejecuta directamente (es decir, como el programa principal), __name__ toma el valor de '__main__'.
# Si el script es importado como un módulo en otro script, entonces __name__ toma el nombre del módulo (es decir, el nombre del archivo sin la extensión .py).
app = Flask(__name__)

# SQLAlchemy es una librería que facilita la interacción con bases de datos a través de un ORM
# 'sqlite:///blog.db' especifica que se usará SQLite como base de datos y creará un archivo llamado blog.db.
# 'sqlite:///' es la sintaxis usada en Flask-SQLAlchemy para bases de datos SQLite locales
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instancia de SQLAlchemy asociada a la aplicacion de Flask para poder definir modelos
db = SQLAlchemy(app)

# Definicion de una clase que será tabla de la BD
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    
    # __repr__ define cómo se verá el objeto cuando se represente como cadena, por ejemplo al hacer print de un objeto de esta clase
    # self en los argumentos permite a la función acceder a los atributos del objeto.
    def __rpr__(self):
        return f'<Article {self.title}>'

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return 'Hola, Flask'

@app.route('/create-article', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
       title =  request.form.get('title')
       content = request.form.get('content')
       new_article = Article(title=title, content=content)
       db.session.add(new_article)
       db.session.commit()

       return f'Articulo creado {new_article}, contenido {new_article.content}'

    return '''
        <form method='POST' action="create-article">
            <label for='title'>Título del artículo:</label><br>
            <input type='text' id='title' name='title'><br><br>
            <label for='content'>Contenido del artículo:</label><br>
            <textarea name='content' id='content'></textarea><br><br>
            <input type='submit' id='title' value='Crear Articulo'>

'''

# Crear endpoint con variable que llega a través de la url
@app.route('/article/<int:article_id>')
def view_article(article_id):
    return f'Estas viendo el articulo número {article_id}'















if __name__ == '__main__':
    app.run(debug=True)