# Mi Biblioteca Personal Multimedia 📚🎬🎵

## 📋 Tabla de Contenidos
- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Características Principales](#-características-principales)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Demo en Vivo](#-demo-en-vivo)
- [Instalación y Configuración](#-instalación-y-configuración)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [API Endpoints](#-api-endpoints)
- [Autores](#-autores)
- [Agradecimientos](#-agradecimientos)
- [Licencia](#-licencia)

## 🚀 Descripción del Proyecto

**Mi Biblioteca Personal Multimedia** es una aplicación web desarrollada para gestionar y organizar tu colección personal de contenido multimedia. Permite catalogar, clasificar y realizar seguimiento de libros, series, películas y música en una interfaz intuitiva y moderna.

Este proyecto fue desarrollado como parte del la materia de ProgramacioI-sis-112 de la carrera de Ingieneria en Sistemas, demostrando habilidades en desarrollo web.

### ¿Qué problema resuelve?
- **Organización centralizada**: Unifica todas tus colecciones multimedia en un solo lugar
- **Seguimiento personalizado**: Controla tu progreso en libros, series y más
- **Estadísticas inteligentes**: Visualiza tus hábitos de consumo cultural
- **Recomendaciones**: Descubre nuevo contenido basado en tus preferencias

## ✨ Características Principales

### 🎯 Funcionalidades Implementadas
- ✅ **Gestión Multi-Tipo**: Libros, series, películas y música
- ✅ **Sistema de Estados**: Por ver, viendo, completado, pausado, abandonado
- ✅ **Búsqueda Avanzada**: Por múltiples criterios y filtros
- ✅ **Estadísticas Visuales**: Gráficos y métricas de tu consumo
- ✅ **Etiquetado Personalizado**: Categoriza con tus propias etiquetas
- ✅ **Sistema de Calificación**: De 0 a 5 estrellas con reseñas personales
- ✅ **Seguimiento de Progreso**: Páginas leídas, capítulos vistos, etc.
- ✅ **Interfaz Responsive**: Compatible con todos los dispositivos


## 🛠️ Tecnologías Utilizadas

### Backend
- **Lenguaje**: Python 3.9+
- **Framework Web**: Flask 2.3.3
- **ORM**: SQLAlchemy 3.0.5
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Formularios**: Flask-WTF 1.1.1
- **Autenticación**: Flask-Login 0.6.3
- **Almacenamiento**: Json

### Frontend
- **Lenguajes**: HTML, CSS, JavaScript (ES6+)
- **Framework CSS**: Bootstrap 5.1.3
- **Iconos**: Bootstrap Icons 1.7.2
- **Gráficos**: Chart.js (integrado)
- **Interactividad**: JavaScript vanilla + Fetch API

### Herramientas de Desarrollo
- **Entorno**: Conda + VS Code
- **Control de Versiones**: Git + GitHub
- **Gestor de Paquetes**: Conda + pip
- **Análisis de Datos**: Pandas 2.0.3 + Matplotlib 3.7.2

## 🌐 Demo en Vivo

**URL del sitio desplegado**: [Próximamente...](#)

**Credenciales de prueba**:
- Usuario: `aun no necesario`
- Contraseña: `aun no necesario`

## ⚙️ Instalación y Configuración

### Prerrequisitos
- Python 3.9 o superior
- Conda (recomendado) o pip
- Git

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tuusuario/mi-biblioteca-personal.git
   cd mi-biblioteca-personal
   ```

2. **Crear y activar entorno Conda**
   ```bash
   conda env create -f environment.yml
   conda activate biblioteca-personal
   ```

3. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   # Editar el archivo .env con tus configuraciones
   ```

4. **Inicializar la base de datos**
   ```bash
   python init_db.py
   ```

5. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

6. **Abrir en el navegador**
   ```
   http://localhost:5000
   ```

### Configuración de Desarrollo
```bash
# Instalar en modo desarrollo
pip install -e .

# Ejecutar con debug activado
FLASK_DEBUG=1 python app.py
```

## 📁 Estructura del Proyecto

```
mi_biblioteca_personal/
├── app.py                 # Aplicación principal Flask
├── config.py             # Configuraciones
├── environment.yml       # Entorno Conda
├── requirements.txt      # Dependencias pip
├── init_db.py           # Inicialización de BD
│
├── src/                  # Código fuente modularizado
│   ├── models/          # Modelos de datos
│   │   ├── base.py      # Modelo base
│   │   ├── libro.py     # Modelo libros
│   │   ├── serie.py     # Modelo series
│   │   ├── pelicula.py  # Modelo películas
│   │   └── musica.py    # Modelo música
│   │
│   ├── services/        # Lógica de negocio
│   │   ├── database_service.py
│   │   ├── search_service.py
│   │   ├── stats_service.py
│   │   └── file_service.py
│   │
│   ├── routes/          # Controladores y rutas
│   │   ├── main_routes.py
│   │   ├── api_routes.py
│   │   └── auth_routes.py
│   │
│   └── utils/           # Utilidades
│       ├── validators.py
│       ├── formatters.py
│       └── constants.py
│
├── static/              # Archivos estáticos
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
├── templates/           # Templates Jinja2
│   ├── base.html
│   ├── index.html
│   ├── agregar.html
│   ├── buscar.html
│   ├── coleccion.html
│   ├── estadisticas.html
│   └── componentes/
│       ├── navbar.html
│       ├── footer.html
│       └── tarjeta_elemento.html
│
└── tests/               # Pruebas unitarias
    ├── test_models.py
    ├── test_routes.py
    └── test_services.py
```

## 📸 Capturas de Pantalla

| Dashboard Principal | Gestión de Libros |
|---------------------|-------------------|
| ![Dashboard](screenshots/dashboard.png) | ![Libros](screenshots/libros.png) |

| Búsqueda Avanzada | Estadísticas |
|-------------------|--------------|
| ![Búsqueda](screenshots/busqueda.png) | ![Stats](screenshots/estadisticas.png) |

## 🚀 API Endpoints

### Elementos
- `GET /api/elementos` - Listar elementos
- `POST /api/elementos` - Crear nuevo elemento
- `GET /api/elementos/<id>` - Obtener elemento específico
- `PUT /api/elementos/<id>` - Actualizar elemento
- `DELETE /api/elementos/<id>` - Eliminar elemento

### Búsqueda
- `GET /api/buscar?q=termino` - Búsqueda general
- `GET /api/buscar/avanzada` - Búsqueda con múltiples filtros

### Estadísticas
- `GET /api/estadisticas/generales` - Estadísticas generales
- `GET /api/estadisticas/progreso` - Progreso por tipo

## 👥 Autores

### Desarrollador Principal
- Angeles Paola Muraña Miranda - [@Skygels](https://github.com/tuusuario) - Desarrollo web

### Información Académica
- **Universidad**: Catolica Boliviana "San Pablo"
- **Carrera**: Ingenieria en Sistemas
- **Asignatura**: ProgramaciónI-sis-112
- **Profesor**: Alan Cornejo
- **Semestre**: Segundo Semestre

## 🙏 Agradecimientos

- **Comunidad Flask**: Por la excelente documentación y recursos
- **Bootstrap**: Por el sistema de componentes frontend
- **YouTube**: Por la guia en creacion de sitios web 
- **Equipo de VS Code**: Por el excelente editor de código

### Recursos Utilizados


## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

<div align="center">

### ⭐ GRACIAS

</div>