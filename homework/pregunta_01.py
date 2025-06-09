# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envíos
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`
    * `Mode_of_Shipment`
    * `Customer_rating`
    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:
    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Cambios respecto al video:
    * El archivo de datos se encuentra en la carpeta `files`.
    * Todos los archivos deben ser creados en la carpeta `docs`.
    * Su código debe crear la carpeta `docs` si no existe.
    """
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    os.makedirs("docs", exist_ok=True)

    datos_envios = pd.read_csv("files/input/shipping-data.csv")

    def graficar_envios_por_bodega(df):
        plt.figure()
        conteo_bodegas = df["Warehouse_block"].value_counts()
        conteo_bodegas.plot.bar(
            title="Envíos por Bloque de Bodega",
            xlabel="Bloque de Bodega",
            ylabel="Cantidad de Registros",
            color="tab:blue",
            fontsize=8,
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.tight_layout()
        plt.savefig("docs/envios_por_bodega.png")

    def graficar_modalidad_envio(df):
        plt.figure()
        conteo_modalidad = df["Mode_of_Shipment"].value_counts()
        conteo_modalidad.plot.pie(
            title="Modalidad de Envío",
            wedgeprops=dict(width=0.35),
            ylabel="",
            colors=["tab:blue", "tab:orange", "tab:green"],
        )
        plt.tight_layout()
        plt.savefig("docs/modalidad_envio.png")

    def graficar_calificacion_promedio(df):
        plt.figure()
        resumen_calificaciones = df.groupby("Mode_of_Shipment")["Customer_rating"].describe()
        resumen_calificaciones = resumen_calificaciones[["mean", "min", "max"]]
        plt.barh(
            y=resumen_calificaciones.index,
            width=resumen_calificaciones["max"] - 1,
            left=resumen_calificaciones["min"],
            height=0.9,
            color="lightgray",
            alpha=0.8,
        )
        colores = ["tab:green" if val >= 3 else "tab:orange" for val in resumen_calificaciones["mean"]]
        plt.barh(
            y=resumen_calificaciones.index,
            width=resumen_calificaciones["mean"] - 1,
            left=resumen_calificaciones["min"],
            color=colores,
            height=0.5,
        )
        plt.title("Calificación Promedio del Cliente")
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.gca().spines["left"].set_color("gray")
        plt.gca().spines["bottom"].set_color("gray")
        plt.tight_layout()
        plt.savefig("docs/calificacion_promedio.png")

    def graficar_distribucion_peso(df):
        plt.figure()
        df["Weight_in_gms"].plot.hist(
            title="Distribución del Peso Enviado",
            color="tab:orange",
            edgecolor="white",
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.tight_layout()
        plt.savefig("docs/distribucion_peso.png")

    graficar_envios_por_bodega(datos_envios)
    graficar_modalidad_envio(datos_envios)
    graficar_calificacion_promedio(datos_envios)
    graficar_distribucion_peso(datos_envios)

    # Crear HTML con las gráficas embebidas
    html_dashboard = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dashboard de Envíos</title>
    </head>
    <body>
        <h1>Dashboard de Envíos</h1>
        <img src="envios_por_bodega.png" alt="Gráfico de envíos por bodega"><br><br>
        <img src="modalidad_envio.png" alt="Gráfico de modalidad de envío"><br><br>
        <img src="calificacion_promedio.png" alt="Gráfico de calificación promedio"><br><br>
        <img src="distribucion_peso.png" alt="Gráfico de distribución de peso">
    </body>
    </html>
    """

    with open("docs/index.html", "w") as archivo_html:
        archivo_html.write(html_dashboard)

# Ejecutar la función
pregunta_01()
