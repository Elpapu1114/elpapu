# archivo principal
import funciones
funciones.saludar()

from funciones import saludar
saludar()

from funciones import saludar as s
s()

import funciones as f
f.saludar()

from funciones import *
saludar()