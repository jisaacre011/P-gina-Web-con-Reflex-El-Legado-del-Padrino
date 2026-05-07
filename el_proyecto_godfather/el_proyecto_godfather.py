import reflex as rx
import random

# Lista de escenas/frases épicas de El Padrino
QUOTES = [
    {
        "frase": "Voy a hacerle una oferta que no podrá rechazar.",
        "personaje": "Vito Corleone",
        "descripcion": "El Don muestra su poder de persuasión.",
        "poder": 95,
        "respeto": 100,
        "imagen": "/vito.png",
        "color": "crimson"
    },
    {
        "frase": "No es personal, Sonny. Son solo negocios.",
        "personaje": "Michael Corleone",
        "descripcion": "La transformación de Michael en el nuevo Don.",
        "poder": 90,
        "respeto": 85,
        "imagen": "/michael.png",
        "color": "darkred"
    },
    {
        "frase": "Nunca le digas a nadie fuera de la familia lo que estás pensando.",
        "personaje": "Vito Corleone",
        "descripcion": "Consejo fundamental de la famiglia.",
        "poder": 88,
        "respeto": 95,
        "imagen": "/vito2.png",
        "color": "darkgoldenrod"
    },
    {
        "frase": "Deja el arma, toma los cannoli.",
        "personaje": "Peter Clemenza",
        "descripcion": "Instrucciones después de un trabajo.",
        "poder": 70,
        "respeto": 80,
        "imagen": "/clemenza.png",
        "color": "saddlebrown"
    },
    {
        "frase": "Un abogado con un maletín puede robar más que cien hombres con pistolas.",
        "personaje": "Tom Hagen",
        "descripcion": "El poder del consigliere.",
        "poder": 75,
        "respeto": 90,
        "imagen": "/tom.png",
        "color": "steelblue"
    },
    {
        "frase": "Acepté el trabajo, pero no soy un asesino.",
        "personaje": "Luca Brasi",
        "descripcion": "La línea entre lealtad y violencia.",
        "poder": 85,
        "respeto": 70,
        "imagen": "/luca.png",
        "color": "dimgray"
    },
]

class State(rx.State):
    personaje: str = "???"
    frase: str = "Presiona el botón para recibir una oferta."
    descripcion: str = ""
    poder: int = 0
    respeto: int = 0
    color: str = "gray"
    imagen: str = ""

    honor: int = 1000          # "Puntos de honor" de la familia
    ofertas: int = 0
    mensaje: str = "¡Bienvenido a la famiglia!"
    mostrar_oferta: bool = False

    def hacer_oferta(self):
        # Si ya no hay honor, no hacemos nada
        if self.honor <= 0:
            return

        escena = random.choice(QUOTES)
        self.personaje = escena["personaje"]
        self.frase = escena["frase"]
        self.descripcion = escena["descripcion"]
        self.poder = escena["poder"]
        self.respeto = escena["respeto"]
        self.color = escena["color"]
        self.imagen = escena["imagen"]
        self.mostrar_oferta = True

        costo = random.randint(50, 300)
        self.honor = max(0, self.honor - costo)
        self.ofertas += 1

        if self.honor <= 0:
            self.mensaje = "¡Los Corleone han caído en desgracia! Game Over..."
        else:
            self.mensaje = f"Oferta de {escena['personaje']} aceptada."

def index():
    return rx.box(
        rx.vstack(
            # Título principal
            rx.heading(
                "El Legado del Padrino",
                size="9",
                color="#DAA520",  # dorado
                text_align="center",
            ),
            rx.text(
                "Cada oferta cambia el destino de la famiglia.",
                color="#B0B0B0",
                size="4",
                text_align="center",
            ),
            # Badges de Honor y Ofertas
            rx.hstack(
                rx.box(
                    rx.text(f"Honor: {State.honor}", color="white", font_weight="bold"),
                    background="#2E2E2E",
                    padding="8px 16px",
                    border_radius="8px",
                ),
                rx.box(
                    rx.text(f"Ofertas: {State.ofertas}", color="white", font_weight="bold"),
                    background="#4A0E0E",
                    padding="8px 16px",
                    border_radius="8px",
                ),
                spacing="4",
            ),
            # Mensaje dinámico
            rx.text(State.mensaje, color="#FFD700", font_size="1.2em", font_weight="bold", text_align="center"),
            # Contenido condicional: bienvenida o tarjeta de la frase
            rx.cond(
                State.mostrar_oferta,
                rx.vstack(
                    rx.image(src=State.imagen, width="200px", height="auto", border_radius="10px", border="2px solid gold"),
                    rx.heading(State.frase, size="6", color="white", text_align="center"),
                    rx.text(State.descripcion, color="gray", text_align="center"),
                    rx.hstack(
                        rx.badge(f"Poder: {State.poder}", variant="solid", color_scheme="red"),
                        rx.badge(f"Respeto: {State.respeto}", variant="solid", color_scheme="green"),
                        spacing="4",
                    ),
                    rx.text(f"― {State.personaje}", color="gold", font_style="italic"),
                    spacing="3",
                    align_items="center",
                ),
                rx.vstack(
                    rx.icon("handshake", size=50, color="gold"),
                    rx.text("Haz clic en el botón para recibir una oferta...", color="gray"),
                    spacing="2",
                    align_items="center",
                ),
            ),
            # Botón principal
            rx.button(
                "HACER UNA OFERTA",
                on_click=State.hacer_oferta,
                color_scheme="yellow",
                size="4",
                width="100%",
                is_disabled=State.honor <= 0,  # Se deshabilita si no hay honor
            ),
            spacing="6",
            align_items="center",
            padding="2em",
        ),
        background="linear-gradient(135deg, #0D0D0D 0%, #2B1B0E 100%)",
        min_height="100vh",
        display="flex",
        justify_content="center",
        align_items="center",
    )

app = rx.App()
app.add_page(index, title="El Legado del Padrino")