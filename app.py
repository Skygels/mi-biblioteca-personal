from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Archivo de datos
ARCHIVO_DATOS = 'datos.json'

def cargar_datos():
    """Carga los datos desde JSON"""
    if os.path.exists(ARCHIVO_DATOS):
        try:
            with open(ARCHIVO_DATOS, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def guardar_datos(datos):
    """Guarda datos en JSON"""
    with open(ARCHIVO_DATOS, 'w') as f:
        json.dump(datos, f, indent=2)

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/agregar', methods=['POST'])
def agregar_elemento():
    """Agrega un nuevo elemento (mínimo)"""
    try:
        datos = cargar_datos()
        
        nuevo_elemento = {
            'id': len(datos) + 1,
            'tipo': request.json.get('tipo', 'libro'),
            'titulo': request.json.get('titulo', ''),
            'autor': request.json.get('autor', ''),
            'genero': request.json.get('genero', ''),
            'anio': request.json.get('anio', ''),
            'calificacion': request.json.get('calificacion', 0)
        }
        
        datos.append(nuevo_elemento)
        guardar_datos(datos)
        
        return jsonify({'success': True, 'mensaje': 'Elemento agregado!'})
    
    except Exception as e:
        return jsonify({'success': False, 'mensaje': str(e)})

@app.route('/api/elementos')
def obtener_elementos():
    """Obtiene todos los elementos"""
    datos = cargar_datos()
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)