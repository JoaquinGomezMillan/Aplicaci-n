from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#conexión con Google Drive
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class InventarioGrid(GridLayout):

    def __init__(self, **kwargs):
        super(InventarioGrid, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text='Producto:'))
        self.producto = TextInput()
        self.add_widget(self.producto)

        self.add_widget(Label(text='Cantidad:'))
        self.cantidad = TextInput()
        self.add_widget(self.cantidad)

        self.add_widget(Label(text='Precio:'))
        self.precio = TextInput()
        self.add_widget(self.precio)

        self.add_widget(Label(text='Proveedor:'))
        self.proveedor = TextInput()
        self.add_widget(self.proveedor)

class InventarioGrid(GridLayout):

    def __init__(self, **kwargs):
        super(InventarioGrid, self).__init__(**kwargs)

        ...

        guardar_button = Button(text='Guardar', on_press=self.guardar_datos)
        self.add_widget(guardar_button)

    def guardar_datos(self, instance):
        producto = self.producto.text
        cantidad = self.cantidad.text
        precio = self.precio.text
        proveedor = self.proveedor.text

        guardar_datos_en_excel(producto, cantidad, precio, proveedor)

class InventarioApp(App):

    def build(self):
        return InventarioGrid()


#guardar datos en excel
def guardar_datos_en_excel(producto, cantidad, precio, proveedor):
    # Define el nombre del archivo de Excel y la hoja de cálculo
    nombre_archivo = "nombre_del_archivo_de_excel"
    nombre_hoja = "nombre_de_la_hoja_de_calculo"

    # Define las credenciales de la cuenta de servicio
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('path/to/credenciales.json', scope)
    client = gspread.authorize(credentials)

    # Abre el archivo de Excel y la hoja de cálculo correspondiente
    sheet = client.open(nombre_archivo).worksheet(nombre_hoja)

    # Escribe los datos en la hoja de cálculo
    row = [producto, cantidad, precio, proveedor]
    sheet.append_row(row)


if __name__ == '__main__':
    InventarioApp().run()
