# importamos todos los modulos que vamos a usar para crear
# nuestra calculadora
import kivy
from kivy.app import App
from kivi.uix.gridlayout import GridLayout

# creamos un ojbeto usando el comando class,
# esta se encargara de agrupar todos los widgets que necesitamos
# como botones y cuadros de texo.
class calculadora_screen(GridLayout):
    # creamos la función que se encargara
    # de hacer las operaciones matemáticas

    def calculate(self, calculation):
        # usamos "if" para saber si el usuario a intentado
        # realizar una operación, ya que si no fuera así
        # aunque presionesmos "=" no pasara nada

        if calculation:
            # una vez que se confirme que el usuario si quiere
            # realizar una operación usamos "try", de esta
            # forma si algún error ocurre podemos controlarlo
            # ya que si no lo hacemos nustra app se cerraría inmediatamente.

            try:
                # aqui nuestro cuadro de texto cambiara y nos mostrará el
                # resultado de la operación, para evaluar las operaciones
                # usamos "eval" que evaluara todo lo que esta en "calculation"
                # y el resultado lo transformaremos a text usando "str"
                self.display.text = str(eval(calculation))
            # aqui no importando el error que ocurra
            # controlaremos que no se cierre nuestra app

            except Exception:
                # cuando un error ocurra mostraremos el texto error
                self.display.text = "Error"
                