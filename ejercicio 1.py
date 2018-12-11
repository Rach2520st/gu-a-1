import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class principal:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("menu principal.glade")

        ventana = builder.get_object("ventana")
        ventana.connect("destroy", Gtk.main_quit)

        self.primer_texto = builder.get_object("entrada_primer_texto")
        self.segundo_texto = builder.get_object("entrada_segundo_texto")
        self.numeros = builder.get_object("numeros")
        self.boton_aceptar = builder.get_object("boton_aceptar")
        self.boton_reset = builder.get_object("boton_reset")

        self.boton_aceptar.connect("clicked", self.mensaje_info)
        self.boton_reset.connect("clicked", self.mensaje_reset)

        # al presionar enter en una entrada de texto calcular la suma
        self.primer_texto.connect("activate", self.calcular)
        self.segundo_texto.connect("activate", self.calcular)

        # mostrar la ventana
        ventana.show_all()

    def calcular(self, btn=None):
        largo1 = len(self.primer_texto.get_text())
        largo2 = len(self.segundo_texto.get_text())
        #largo del primer y segundo texto sumados
        largot = largo1 + largo2

        self.numeros.set_value(largot)

    def borrar(self, btn=None):
        # reiniciar todo
        self.numeros.set_value(0)
        self.primer_texto.set_text("")
        self.segundo_texto.set_text("")

    def mensaje_info(self, btn=None):
        # sumar antes de mostrar la info
        self.calcular()

        # llamar la ventana de info
        dialogo_info(self.primer_texto, self.segundo_texto, self.numeros)

    def mensaje_reset(self, btn=None):
        # mostrar el dialogo
        dialogo_reset(self.primer_texto, self.segundo_texto, self.numeros)


class dialogo_info:
    def __init__(self, primer_texto, segundo_texto, numeros):
        # Creamos un objeto builder para manipular Gtk
        self.builder = Gtk.Builder()
        # Agregamos los objetos Gtk diseñados en Glade
        self.builder.add_from_file("ventana aceptar.glade")

        self.ventana = self.builder.get_object("ventana_info")
        self.info = self.builder.get_object("info")
        self.boton_aceptar = self.builder.get_object("b_aceptar")
        self.boton_cancelar = self.builder.get_object("b_cancelar")

        self.primer_texto = primer_texto
        self.segundo_texto = segundo_texto
        self.numeros = numeros

        texto = ""
        texto = texto + "primer texto ingresado: "
        texto = texto + self.primer_texto.get_text() + "\n"
        texto = texto + "segundo texto ingresado: "
        texto = texto + self.segundo_texto.get_text() + "\n"
        texto = texto + "cantidad de letras en los dos textos: "
        texto = texto + str(self.numeros.get_value()) + "\n\n"
        texto = texto + "desea reiniciar todo?"

        self.info.set_text(texto)

        # borrar todo cuando la persona acepte
        self.boton_aceptar.connect("clicked", self.borrar)

        # cerrar si la persona cancela
        self.boton_cancelar.connect("clicked", self.cerrar)

        self.ventana.show_all()

    def borrar(self, btn=None):
        self.primer_texto.set_text("")
        self.segundo_texto.set_text("")
        self.numeros.set_value(0)
        self.ventana.close()

    def cerrar(self, btn=None):
        self.ventana.close()


class dialogo_reset:
    def __init__(self, primer_texto, segundo_texto, numeros):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("ventana reset.glade")
        self.ventana = self.builder.get_object("ventana_advertencia")
        self.boton_aceptar = self.builder.get_object("boton_Aceptar")
        self.boton_cancelar = self.builder.get_object("boton_Cancelar")

        self.primer_texto = primer_texto
        self.segundo_texto = segundo_texto
        self.numeros = numeros

        self.boton_aceptar.connect("clicked", self.borrar)
        self.boton_cancelar.connect("clicked", self.cerrar)

        self.ventana.show_all()

    def borrar(self, btn=None):
        self.primer_texto.set_text("")
        self.segundo_texto.set_text("")
        self.numeros.set_value(0)
        self.ventana.destroy()

    def cerrar(self, btn=None):
        self.ventana.destroy()


if __name__ == "__main__":
    w = principal()
    Gtk.main()
