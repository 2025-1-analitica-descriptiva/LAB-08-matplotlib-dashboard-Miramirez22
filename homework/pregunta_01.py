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

    df = pd.read_csv("files/input/shipping-data.csv")

    def plot_shipping_per_warehouse(df):
        plt.figure()
        counts = df["Warehouse_block"].value_counts()
        counts.plot.bar(
            title="Shipping per Warehouse",
            xlabel="Warehouse block",
            ylabel="Record Count",
            color="tab:blue",
            fontsize=8,
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.tight_layout()
        plt.savefig("docs/shipping_per_warehouse.png")

    def plot_mode_of_shipment(df):
        plt.figure()
        counts = df["Mode_of_Shipment"].value_counts()
        counts.plot.pie(
            title="Mode of shipment",
            wedgeprops=dict(width=0.35),
            ylabel="",
            colors=["tab:blue", "tab:orange", "tab:green"],
        )
        plt.tight_layout()
        plt.savefig("docs/mode_of_shipment.png")

    def plot_average_customer_rating(df):
        plt.figure()
        resumen = df.groupby("Mode_of_Shipment")["Customer_rating"].describe()
        resumen = resumen[["mean", "min", "max"]]
        plt.barh(
            y=resumen.index,
            width=resumen["max"] - 1,
            left=resumen["min"],
            height=0.9,
            color="lightgray",
            alpha=0.8,
        )
        colores = ["tab:green" if val >= 3 else "tab:orange" for val in resumen["mean"]]
        plt.barh(
            y=resumen.index,
            width=resumen["mean"] - 1,
            left=resumen["min"],
            color=colores,
            height=0.5,
        )
        plt.title("Average Customer Rating")
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.gca().spines["left"].set_color("gray")
        plt.gca().spines["bottom"].set_color("gray")
        plt.tight_layout()
        plt.savefig("docs/average_customer_rating.png")

    def plot_weight_distribution(df):
        plt.figure()
        df["Weight_in_gms"].plot.hist(
            title="Shipped Weight Distribution",
            color="tab:orange",
            edgecolor="white",
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.tight_layout()
        plt.savefig("docs/weight_distribution.png")

    # Ejecutar funciones de graficación
    plot_shipping_per_warehouse(df)
    plot_mode_of_shipment(df)
    plot_average_customer_rating(df)
    plot_weight_distribution(df)

    # Crear HTML con los nombres correctos
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Shipping Dashboard</title>
    </head>
    <body>
        <h1>Shipping Dashboard</h1>
        <img src="shipping_per_warehouse.png" alt="Shipping per Warehouse"><br><br>
        <img src="mode_of_shipment.png" alt="Mode of Shipment"><br><br>
        <img src="average_customer_rating.png" alt="Average Customer Rating"><br><br>
        <img src="weight_distribution.png" alt="Weight Distribution">
    </body>
    </html>
    """
    with open("docs/index.html", "w") as f:
        f.write(html_code)


pregunta_01()
