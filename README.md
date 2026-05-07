@"
# El Legado del Padrino

Aplicación web creada con [Reflex](https://reflex.dev) que rinde homenaje a la película *El Padrino*.
Cada clic en **"HACER UNA OFERTA"** revela una frase mítica, el personaje y sus estadísticas de poder y respeto,
mientras se consume el honor familiar.

## Requisitos
- Python 3.10 – 3.13
- Poetry (gestor de dependencias)

## Instalación y ejecución
1. Clona este repositorio:
   `""git clone https://github.com/tu-usuario/el-legado-del-padrino.git`"
   `cd el-legado-del-padrino`
2. Instala dependencias:
   `poetry install`
3. Inicializa Reflex (primera vez):
   `poetry run reflex init`  (opción 0)
4. Ejecuta:
   `poetry run reflex run`
5. Abre http://localhost:3000

## Estructura
- `assets/` – imágenes de los personajes
- `el_proyecto_godfather/el_proyecto_godfather.py` – código fuente
- `pyproject.toml` – configuración de Poetry

## Créditos
Proyecto desarrollado como práctica de ANÁLISIS Y DISEÑO DE REPORTE con Reflex.
Temática inspirada en *El Padrino* (1972).
"@ | Out-File -FilePath README.md -Encoding utf8
