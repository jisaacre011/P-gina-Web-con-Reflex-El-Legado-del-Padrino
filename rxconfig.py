import reflex as rx

config = rx.Config(
    app_name="el_proyecto_godfather",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)