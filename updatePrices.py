import pandas as pd
import os
import django

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from settingsMetalprotec.models import endpointSystem
from clientsMetalprotec.models import clientSystem
from productsMetalprotec.models import productSystem

# Especifica la ruta de tu archivo Excel
ruta_excel = 'PTRUJILLO.xlsx'

# Lee el archivo Excel y conviértelo en un DataFrame
df = pd.read_excel(ruta_excel)

df = df[[
    'CODIGO',
    'MONEDA_PRODUCTO',
    'PESO_PRODUCTO',
    'PRECIO_COMPRA_NO_IGV',
    'PRECIO_COMPRA_CON_IGV',
    'PRECIO_VENTA_NO_IGV',
    'PRECIO_VENTA_CON_IGV'
]]
# Muestra el DataFrame
print(df.head())

duplicados = df['CODIGO'].duplicated()

# Si la suma de duplicados es cero, entonces todos son únicos
son_todos_unicos = duplicados.sum() == 0

if son_todos_unicos:
    print("Todos los códigos son únicos.")
else:
    print("Hay códigos duplicados en el DataFrame.")

df = df.astype(str)
tipos_de_columnas = df.dtypes

print("Tipos de cada columna:")
print(tipos_de_columnas)


print("Se muestran los codigos de los productos")
endpointEnd3 = endpointSystem.objects.get(codeEndpoint='END-0003')
productosTrujillo = productSystem.objects.filter(endpointProduct=endpointEnd3)

for productInfo in productosTrujillo:
    fila_df = df.loc[df['CODIGO'] == productInfo.codeProduct]
    if not fila_df.empty:
        print('ACTUALIZACION DE COLUMNAS : ')
        print(f"CODIGO : {fila_df['CODIGO'].values[0]}")
        print(f"MONEDA: {fila_df['MONEDA_PRODUCTO'].values[0]}")
        print(f"PESO : {'{:.2f}'.format(float(fila_df['PESO_PRODUCTO'].values[0]))}")
        print(f"PCNIGV : {'{:.2f}'.format(float(fila_df['PRECIO_COMPRA_NO_IGV'].values[0]))}")
        print(f"PCCIGV : {'{:.2f}'.format(float(fila_df['PRECIO_COMPRA_CON_IGV'].values[0]))}")
        print(f"PVNIGV : {'{:.2f}'.format(float(fila_df['PRECIO_VENTA_NO_IGV'].values[0]))}")
        print(f"PVCIGV : {'{:.2f}'.format(float(fila_df['PRECIO_VENTA_CON_IGV'].values[0]))}")

        print(f"ALMACEN : {productInfo.storexproductsystem_set.all()[0].asociatedStore.nameStore}")
        print(f"MONEDA ACTUAL : {productInfo.currencyProduct}")
        print(f"PESO ACTUAL : {productInfo.weightProduct}")
        print(f"PCNIGV ACTUAL : {productInfo.pcnIGV}")
        print(f"PCCIGV ACTUAL : {productInfo.pccIGV}")
        print(f"PVNIGV ACTUAL : {productInfo.pvnIGV}")
        print(f"PVCIGV ACTUAL : {productInfo.pvcIGV}")
        productInfo.currencyProduct = fila_df['MONEDA_PRODUCTO'].values[0]
        productInfo.weightProduct = '{:.2f}'.format(float(fila_df['PESO_PRODUCTO'].values[0]))
        productInfo.pcnIGV = '{:.2f}'.format(float(fila_df['PRECIO_COMPRA_NO_IGV'].values[0]))
        productInfo.pccIGV = '{:.2f}'.format(float(fila_df['PRECIO_COMPRA_CON_IGV'].values[0]))
        productInfo.pvnIGV = '{:.2f}'.format(float(fila_df['PRECIO_VENTA_NO_IGV'].values[0]))
        productInfo.pvcIGV = '{:.2f}'.format(float(fila_df['PRECIO_VENTA_CON_IGV'].values[0]))
        productInfo.save()
        print("------------------------------------------------------------------------------")


print("Muestra de productos terminada")
