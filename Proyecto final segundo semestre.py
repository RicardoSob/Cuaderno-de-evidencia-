import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from PIL import Image, ImageTk
import webbrowser
import threading
import queue
import time
import random
from io import StringIO
from datetime import datetime
"""
from networkx import nx
import graphviz import Digraph
import os
"""
class CuadernoEvidencias:
    def __init__(self, root):
        self.root = root
        self.root.title("CUADERNO DE EVIDENCIAS")
        self.root.geometry("950x700")
        
        # Crear el notebook principal
        self.notebook_principal = ttk.Notebook(root)
        self.notebook_principal.pack(fill='both', expand=True)
        
        # Pestaña portada
        self.crear_portada()
        
        # Pestañas de parciales
        self.crear_pestanas_parciales()
        
        # Ventana secundaria para programas
        self.ventana_secundaria = None
        self.ventana_contenedores = None
        self.ventana_pilas_colas = None
        self.ventana_rec_grafos = None
        self.ventana_arboles_binarios=None
        self.ventana_comcurrencia=None
        
        # Configurar el evento para cambiar de pestaña
        self.notebook_principal.bind("<<NotebookTabChanged>>", self.cambio_pestana)
    
    def crear_portada(self):
        frame_portada = tk.Frame(self.notebook_principal, bg='lightblue')
        self.notebook_principal.add(frame_portada, text="Portada")
        
        label_titulo = tk.Label(frame_portada, text="CUADERNO DE EVIDENCIAS", 
                               font=('Arial', 24, 'bold'), bg='lightblue')
        label_titulo.pack(pady=50)
        
        label_subtitulo = tk.Label(frame_portada, 
                                  text="Alumno: Ricardo Soberanes Flores\nGrupo: 2CV14\nMaestro: Jorge Anzaldo",
                                  font=('Arial', 14), bg='lightblue')
        label_subtitulo.pack(pady=20)
        
        # Agregar imagen (debes tener la imagen en el mismo directorio)
        try:
            img = Image.open("microbit.png")  # Cambia por el nombre de tu imagen
            img = img.resize((200, 200), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            label_img = tk.Label(frame_portada, image=self.photo, bg='lightblue')
            label_img.pack(pady=20)
        except:
            label_img = tk.Label(frame_portada, text="Imagen no encontrada", bg='lightblue')
            label_img.pack(pady=20)
    
    def crear_pestanas_parciales(self):
        # Primer parcial
        frame_primero = tk.Frame(self.notebook_principal)
        self.notebook_principal.add(frame_primero, text="Temas primer parcial")
        
        # Botón para mostrar aprendizaje autónomo
        btn_aprendizaje = tk.Button(frame_primero, text="Mostrar Aprendizaje Autónomo",
                                   command=self.mostrar_aprendizaje_autonomo,
                                   font=('Arial', 12), bg='lightgreen')
        btn_aprendizaje.pack(pady=20)
        # Botón para mostrar contenedores
        btn_contenedores = tk.Button(frame_primero, text="CONTENEDORES",
                                    command=self.mostrar_contenedores,
                                    font=('Arial', 12), bg='lightblue')
        btn_contenedores.pack(pady=20)
        
        # Segundo parcial
        frame_segundo = tk.Frame(self.notebook_principal)
        self.notebook_principal.add(frame_segundo, text="Temas segundo parcial")
        # Botón para mostrar pilas y colas
        btn_pilas_colas = tk.Button(frame_segundo, text="PILAS Y COLAS",
                                  command=self.mostrar_pilas_colas,
                                  font=('Arial', 12), bg='lightcoral')
        btn_pilas_colas.pack(pady=20)
        # Nuevo botón para Recursividad y Grafos
     
        btn_rec_grafos = tk.Button(frame_segundo, text="RECURSIVIDAD Y GRAFOS",
                              command=self.mostrar_recursividad_grafos,
                              font=('Arial', 12), bg='lightyellow')
        btn_rec_grafos.pack(pady=20)
        
        # Tercer parcial
        frame_tercero = tk.Frame(self.notebook_principal)
        self.notebook_principal.add(frame_tercero, text="Temas tercer parcial")

        btn_arboles = tk.Button(frame_tercero, text="ÁRBOLES BINARIOS",
                            command=self.mostrar_arboles_binarios,
                            font=('Arial', 12), bg='lightyellow')
        btn_arboles.pack(pady=20)

        btn_concurrencia = tk.Button(frame_tercero, text="Concurrencia",
                            command=self.ejecutar_concurrencia,
                            font=('Arial', 12), bg='Red')
        btn_concurrencia.pack(pady=20)
    
    def cambio_pestana(self, event):
        pass
    
    def mostrar_aprendizaje_autonomo(self):
        if self.ventana_secundaria is None or not self.ventana_secundaria.winfo_exists():
            self.ventana_secundaria = tk.Toplevel(self.root)
            self.ventana_secundaria.title("Aprendizaje Autónomo - Primer Parcial")
            self.ventana_secundaria.geometry("950x700")
            
            notebook_secundario = ttk.Notebook(self.ventana_secundaria)
            notebook_secundario.pack(fill='both', expand=True)
            
            # Pestañas de los programas
            frame_programa1 = tk.Frame(notebook_secundario)
            notebook_secundario.add(frame_programa1, text="LED Parpadeante")
            self.agregar_codigo_led_simple(frame_programa1)
            
            frame_programa2 = tk.Frame(notebook_secundario)
            notebook_secundario.add(frame_programa2, text="Control de LEDs con Tuplas")
            self.agregar_codigo_torreta(frame_programa2)
            
            frame_programa3 = tk.Frame(notebook_secundario)
            notebook_secundario.add(frame_programa3, text="Control de LEDs con Listas")
            self.agregar_codigo_listas(frame_programa3)
            
            frame_programa4 = tk.Frame(notebook_secundario)
            notebook_secundario.add(frame_programa4, text="Control de LEDs con Botones")
            self.agregar_codigo_botones(frame_programa4)
                        
            frame_programa5 = tk.Frame(notebook_secundario)
            notebook_secundario.add(frame_programa5, text="Control con Colas")
            self.agregar_codigo_colas(frame_programa5)
            
        else:
            self.ventana_secundaria.lift()

    
    def agregar_codigo_led_simple(self, frame):
        # Marco para el código
        frame_codigo = tk.Frame(frame)
        frame_codigo.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Texto de introducción
        intro_text = """Introducción: Código de prueba: https://wokwi.com/projects/426080176216898561 

En este programa el Objetivo: Para comprender la estructura de un programa y cómo resolver problemas mediante su análisis, es útil desglosar los elementos clave y cómo interactúan entre sí. Por lo cual elaboramos un programa en MicroPython en donde prendimos un LED parpadeando por 0.2 segundos y apagado por 2.0 segundos sucesivamente."""
        
        label_intro = tk.Label(frame_codigo, text=intro_text, wraplength=900, justify='left')
        label_intro.pack(pady=10, anchor='w')
        
        # Botón para abrir el enlace
        btn_enlace = tk.Button(frame_codigo, text="Abrir enlace del proyecto", 
                              command=lambda: webbrowser.open("https://wokwi.com/projects/426080176216898561"))
        btn_enlace.pack(pady=5)
        
        # Marco para el código con scroll
        frame_codigo_texto = tk.Frame(frame_codigo)
        frame_codigo_texto.pack(fill='both', expand=True)
        
        scrollbar = tk.Scrollbar(frame_codigo_texto)
        scrollbar.pack(side='right', fill='y')
        
        text_codigo = tk.Text(frame_codigo_texto, wrap='word', yscrollcommand=scrollbar.set,
                            font=('Courier', 10), bg='#f0f0f0', padx=10, pady=10)
        text_codigo.pack(fill='both', expand=True)
        
        scrollbar.config(command=text_codigo.yview)
        
        # Insertar el código
        codigo = """# 1.- ---------------- Encabezado ----------------------------------------------
\"\"\"       
Alumno: Ricardo Soberanes Flores
Grupo: 2CV14
Maestro: Jorge Anzaldo
Fecha: 18/02/2025
\"\"\"

# 2.- ---------------- Importación de Módulos y Bibliotecas --------------------
from machine import Pin
import time

# 3.- ---------------- Definición de Funciones o clases ------------------------

# 4.- ---------------- Variables u Objetos Globales ----------------------------

# 5.- ---------------- Bloque Principal ----------------------------------------
if __name__ == '__main__':
    led = Pin(2, Pin.OUT)
    while True:
        led.value(1)
        time.sleep(0.2)  # Encendido por 0.2 segundos
        led.value(0)
        time.sleep(2.0)  # Apagado por 2.0 segundos

# 6.- ---------------- Documentación y Comentarios------------------------------"""
        
        text_codigo.insert('1.0', codigo)
        text_codigo.config(state='disabled')
    
    def agregar_codigo_torreta(self, frame):
        # Marco para el código
        frame_codigo = tk.Frame(frame)
        frame_codigo.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Texto de introducción
        intro_text = """Introducción: Prueba de código: https://wokwi.com/projects/424708521376547841

En este programa el Objetivo de esta práctica es que el alumno utilice tuplas en MicroPython para gestionar y controlar LEDs con un ESP32 mediante el uso de TUPLAS. A través de esta actividad: Por lo cual lo que se mostrará como tres LEDs prenderán al mismo tiempo y parpadearán cada 0.5 segundos."""
        
        label_intro = tk.Label(frame_codigo, text=intro_text, wraplength=900, justify='left')
        label_intro.pack(pady=10, anchor='w')
        
        # Botón para abrir el enlace
        btn_enlace = tk.Button(frame_codigo, text="Abrir enlace del proyecto", 
                              command=lambda: webbrowser.open("https://wokwi.com/projects/424708521376547841"))
        btn_enlace.pack(pady=5)
        
        # Marco para el código con scroll
        frame_codigo_texto = tk.Frame(frame_codigo)
        frame_codigo_texto.pack(fill='both', expand=True)
        
        scrollbar = tk.Scrollbar(frame_codigo_texto)
        scrollbar.pack(side='right', fill='y')
        
        text_codigo = tk.Text(frame_codigo_texto, wrap='word', yscrollcommand=scrollbar.set,
                            font=('Courier', 10), bg='#f0f0f0', padx=10, pady=10)
        text_codigo.pack(fill='both', expand=True)
        
        scrollbar.config(command=text_codigo.yview)
        
        # Insertar el código
        codigo = """# 1.- ---------------- Encabezado ----------------------------------------------
\"\"\"
Alumno: Ricardo Soberanes Flores
Grupo: 2CV14
Maestro: Jorge Anzaldo
Fecha: 18/02/2025
\"\"\"

# 2.- ---------------- Importación de Módulos y Bibliotecas --------------------
from machine import Pin
import time

# 3.- ---------------- Definición de Funciones o clases ------------------------
class Torreta:
    def __init__(self, led_pins):
        self.leds = tuple(Pin(pin, Pin.OUT) for pin in led_pins)

    def prenderTorreta(self):
        for led in self.leds:
            led.value(1)
        time.sleep(2)

    def apagarTorreta(self):
        for led in self.leds:
            led.value(0)

    def parpadearTorreta(self, veces, espera):
        for _ in range(veces):
            self.prenderTorreta()
            time.sleep(espera)
            self.apagarTorreta()
            time.sleep(espera)

    def secuencia(self):
        for led in self.leds:
            led.value(1)
            time.sleep(0.5)
        for led in reversed(self.leds):
            led.value(0)
            time.sleep(0.5)

# 4.- ---------------- Variables u Objetos Globales ----------------------------

# 5.- ---------------- Bloque Principal ----------------------------------------
if __name__ == '__main__':
  led_pins = (4, 5, 14)
  torreta = Torreta(led_pins)

  torreta.prenderTorreta()
  torreta.apagarTorreta()
  torreta.parpadearTorreta(5, 0.5)
  torreta.secuencia()

# 6.- ---------------- Documentación y Comentarios------------------------------"""
        
        text_codigo.insert('1.0', codigo)
        text_codigo.config(state='disabled')

    def agregar_codigo_listas(self, frame):
        # Marco para el código
        frame_codigo = tk.Frame(frame)
        frame_codigo.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Texto de introducción
        intro_text = """Introducción: Control de LEDs con listas

El propósito de esta práctica es que el alumno desarrolle habilidades en programación con MicroPython para el ESP32, utilizando listas para gestionar LEDs de manera dinámica y mediante el uso de LISTAS. Por lo cual tendrá el mismo funcionamiento que el programa con tuplas en donde prendimos tres LEDs al mismo tiempo y los dejamos prendidos durante 0.5 segundos y apagamos por otros 0.5 segundos y así sucesivamente."""
        
        label_intro = tk.Label(frame_codigo, text=intro_text, wraplength=900, justify='left')
        label_intro.pack(pady=10, anchor='w')
        
        # Marco para el código con scroll
        frame_codigo_texto = tk.Frame(frame_codigo)
        frame_codigo_texto.pack(fill='both', expand=True)
        
        scrollbar = tk.Scrollbar(frame_codigo_texto)
        scrollbar.pack(side='right', fill='y')
        
        text_codigo = tk.Text(frame_codigo_texto, wrap='word', yscrollcommand=scrollbar.set,
                            font=('Courier', 10), bg='#f0f0f0', padx=10, pady=10)
        text_codigo.pack(fill='both', expand=True)
        
        scrollbar.config(command=text_codigo.yview)
        
        # Insertar el código
        codigo = """# 1.- ---------------- Encabezado ----------------------------------------------
\"\"\"
Alumno: Ricardo Soberanes Flores
Grupo: 2CV14
Maestro: Jorge Anzaldo
Fecha: 18/02/2025
\"\"\"

# 2.- ---------------- Importación de Módulos y Bibliotecas --------------------
from machine import Pin
import time

# 3.- ---------------- Definición de Funciones o clases ------------------------
class LEDController:
    def __init__(self, pin_list):
        self._led_pins = pin_list
        self._leds = [Pin(pin, Pin.OUT) for pin in self._led_pins]

    def encender_todos(self):
        for led in self._leds:
            led.on()
        print("Todos los LEDs encendidos.")

    def apagar_todos(self):
        for led in self._leds:
            led.off()
        print("Todos los LEDs apagados.")

    def agregar_led(self, pin):
        if pin not in self._led_pins:
            self._led_pins.append(pin)
            self._leds.append(Pin(pin, Pin.OUT))
            print(f"LED en GPIO {pin} agregado.")
        else:
            print(f"El LED en GPIO {pin} ya está en la lista.")

    def eliminar_led(self, pin):
        if pin in self._led_pins:
            index = self._led_pins.index(pin)
            self._led_pins.pop(index)
            self._leds.pop(index)
            print(f"LED en GPIO {pin} eliminado.")
        else:
            print(f"El LED en GPIO {pin} no está en la lista.")

    def probar_leds(self):
        self.encender_todos()
        time.sleep(0.5)
        self.apagar_todos()
        time.sleep(0.5)

# 4.- ---------------- Variables u Objetos Globales ----------------------------

# 5.- ---------------- Bloque Principal ----------------------------------------
if __name__ == '__main__':
  pines_iniciales = [4, 5, 6]

  control_leds = LEDController(pines_iniciales)

  control_leds.probar_leds()

  control_leds.agregar_led(18)
  control_leds.probar_leds()

  control_leds.eliminar_led(18)
  control_leds.probar_leds()

# 6.- ---------------- Documentación y Comentarios------------------------------"""
        
        text_codigo.insert('1.0', codigo)
        text_codigo.config(state='disabled')

    def agregar_codigo_botones(self, frame):
        # Marco para el código
        frame_codigo = tk.Frame(frame)
        frame_codigo.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Texto de introducción
        intro_text = """Introducción: Enlace para probar el funcionamiento https://wokwi.com/projects/424706079223757825

En este programa hice que al presionar un botón los LEDs se prendieran en orden de conexión y con otro botón se apagaran de la misma manera."""
        
        label_intro = tk.Label(frame_codigo, text=intro_text, wraplength=900, justify='left')
        label_intro.pack(pady=10, anchor='w')
        
        # Botón para abrir el enlace
        btn_enlace = tk.Button(frame_codigo, text="Abrir enlace del proyecto", 
                              command=lambda: webbrowser.open("https://wokwi.com/projects/424706079223757825"))
        btn_enlace.pack(pady=5)
        
        # Marco para el código con scroll
        frame_codigo_texto = tk.Frame(frame_codigo)
        frame_codigo_texto.pack(fill='both', expand=True)
        
        scrollbar = tk.Scrollbar(frame_codigo_texto)
        scrollbar.pack(side='right', fill='y')
        
        text_codigo = tk.Text(frame_codigo_texto, wrap='word', yscrollcommand=scrollbar.set,
                            font=('Courier', 10), bg='#f0f0f0', padx=10, pady=10)
        text_codigo.pack(fill='both', expand=True)
        
        scrollbar.config(command=text_codigo.yview)
        
        # Insertar el código
        codigo = """# 1.- ---------------- Encabezado ----------------------------------------------
\"\"\"
Alumno: Ricardo Soberanes Flores
Grupo: 2CV14
Maestro: Jorge Anzaldo
Fecha: 04/03/2025
\"\"\"

# 2.- ---------------- Importación de Módulos y Bibliotecas --------------------
from machine import Pin
import time

# 3.- ---------------- Definición de Funciones o clases ------------------------
class PilaLEDs:
    def __init__(self, led_pins, btn_push_pin, btn_pop_pin):
        self.leds = [Pin(pin, Pin.OUT) for pin in led_pins]
        self.pila = []
        self.btn_push = Pin(btn_push_pin, Pin.IN, Pin.PULL_UP)
        self.btn_pop = Pin(btn_pop_pin, Pin.IN, Pin.PULL_UP)

    def insertarLed(self):
        if len(self.pila) < len(self.leds):
            nuevo_led = self.leds[len(self.pila)]
            nuevo_led.value(1)
            self.pila.append(nuevo_led)

    def extraerLed(self):
        if self.pila:
            led_apagar = self.pila.pop()
            led_apagar.value(0)

    def run(self):
        while True:
            if not self.btn_push.value():
                self.insertarLed()
                time.sleep(0.3)

            if not self.btn_pop.value():
                self.extraerLed()
                time.sleep(0.3)

# 4.- ---------------- Variables u Objetos Globales ----------------------------

# 5.- ---------------- Bloque Principal ----------------------------------------
if __name__ == '__main__':
  led_pins = [5, 18, 19, 21, 22, 23, 25, 26]
  btn_push_pin = 32
  btn_pop_pin = 33
  pila_leds = PilaLEDs(led_pins, btn_push_pin, btn_pop_pin)
  pila_leds.run()

# 6.- ---------------- Documentación y Comentarios------------------------------"""
        
        text_codigo.insert('1.0', codigo)
        text_codigo.config(state='disabled')

    def mostrar_contenedores(self):
        if self.ventana_contenedores is None or not self.ventana_contenedores.winfo_exists():
            self.ventana_contenedores = tk.Toplevel(self.root)
            self.ventana_contenedores.title("Contenedores")
            self.ventana_contenedores.geometry("1000x850")
            
            notebook = ttk.Notebook(self.ventana_contenedores)
            notebook.pack(fill='both', expand=True)
            
            # Pestaña 1: Programas de Contenedores
            frame_pestaña1 = tk.Frame(notebook)
            notebook.add(frame_pestaña1, text="Programas de Contenedores")
            
            # Configurar scroll para pestaña 1
            canvas1 = tk.Canvas(frame_pestaña1)
            scrollbar1 = ttk.Scrollbar(frame_pestaña1, orient="vertical", command=canvas1.yview)
            scrollable_frame1 = tk.Frame(canvas1)
            
            scrollable_frame1.bind("<Configure>", lambda e: canvas1.configure(scrollregion=canvas1.bbox("all")))
            canvas1.create_window((0, 0), window=scrollable_frame1, anchor="nw")
            canvas1.configure(yscrollcommand=scrollbar1.set)
            
            canvas1.pack(side="left", fill="both", expand=True)
            scrollbar1.pack(side="right", fill="y")
            
            # Programa 1: Estructura de datos y Contenedores
            frame_prog1 = tk.LabelFrame(scrollable_frame1, text="1. Práctica de Estructura de datos y Contenedores", padx=10, pady=10)
            frame_prog1.pack(fill='x', padx=10, pady=10)
            
            intro_text1 = """Objetivo: Distinguir las características de una estructura de datos y un contenedor a través del análisis de sus elementos para resolver problemas en ingeniería y ciencias.

Introducción: Las estructuras de datos permiten organizar y manipular la información de manera eficiente. En Python, existen diversos tipos de estructuras de datos, incluyendo tuplas, listas, conjuntos y diccionarios. Estas estructuras también pueden actuar como contenedores, permitiendo almacenar y gestionar colecciones de elementos."""
            
            label_intro1 = tk.Label(frame_prog1, text=intro_text1, wraplength=950, justify='left')
            label_intro1.pack(anchor='w', pady=5)
            
            # Botón para ejecutar el programa
            btn_ejecutar = tk.Button(frame_prog1, text="Ejecutar Programa", 
                                   command=self.ejecutar_contenedores_basicos,
                                   font=('Arial', 12), bg='lightgreen')
            btn_ejecutar.pack(pady=10)
            
            # Programa 2: Sistema de temperaturas
            frame_prog2 = tk.LabelFrame(scrollable_frame1, text="2. Sistema de Temperaturas", padx=10, pady=10)
            frame_prog2.pack(fill='x', padx=10, pady=10)
            
            intro_text2 = """Objetivo: Gestionar datos de temperatura utilizando diferentes estructuras de datos.

Introducción: Este programa permite almacenar temperaturas para los días de la semana y luego analizarlas usando diferentes estructuras de datos como listas, conjuntos y diccionarios."""
            
            label_intro2 = tk.Label(frame_prog2, text=intro_text2, wraplength=950, justify='left')
            label_intro2.pack(anchor='w', pady=5)
            
            # Botón para ejecutar el programa
            btn_ejecutar2 = tk.Button(frame_prog2, text="Ejecutar Programa", 
                                    command=self.ejecutar_sistema_temperaturas,
                                    font=('Arial', 12), bg='lightblue')
            btn_ejecutar2.pack(pady=10)

            # Pestaña 2: Operaciones con Listas
            frame_pestaña2 = tk.Frame(notebook)
            notebook.add(frame_pestaña2, text="Operaciones con Listas")
            
            # CANVA 2
            canvas2 = tk.Canvas(frame_pestaña2)
            scrollbar2 = ttk.Scrollbar(frame_pestaña2, orient="vertical", command=canvas2.yview)
            scrollable_frame2 = tk.Frame(canvas2)
            
            scrollable_frame2.bind("<Configure>", lambda e: canvas2.configure(scrollregion=canvas2.bbox("all")))
            canvas2.create_window((0, 0), window=scrollable_frame2, anchor="nw")
            canvas2.configure(yscrollcommand=scrollbar2.set)
            
            canvas2.pack(side="left", fill="both", expand=True)
            scrollbar2.pack(side="right", fill="y")

            # Actividad 1: Operaciones básicas con listas
            frame_act1 = tk.LabelFrame(scrollable_frame2, 
                                      text="1. Operaciones básicas con listas", 
                                      padx=10, pady=10)
            frame_act1.pack(fill='x', padx=10, pady=10)
            
            intro_text1 = """Objetivo: Analizar el uso y las operaciones con listas a través del desarrollo de algoritmos establecidos para resolver problemas.

Introducción: Las listas en Python son estructuras de datos flexibles que permiten almacenar colecciones de elementos ordenados. Se pueden modificar y realizar diversas operaciones, como inserción, eliminación, búsqueda, actualización y concatenación."""
            
            label_intro1 = tk.Label(frame_act1, text=intro_text1, wraplength=1000, justify='left')
            label_intro1.pack(anchor='w', pady=5)
            
            # Botón para ejecutar el programa
            btn_ejecutar3 = tk.Button(frame_act1, text="Ejecutar Programa", 
                                     command=self.ejecutar_operaciones_listas,
                                     font=('Arial', 12), bg='lightgreen')
            btn_ejecutar3.pack(pady=10)
            
            # Actividad 2: Clase para operaciones con listas
            frame_act2 = tk.LabelFrame(scrollable_frame2, 
                                      text="2. Clase para operaciones avanzadas con listas", 
                                      padx=10, pady=10)
            frame_act2.pack(fill='x', padx=10, pady=10)
            
            # Botón para ejecutar el programa
            btn_ejecutar4 = tk.Button(frame_act2, text="Ejecutar Programa", 
                                     command=self.ejecutar_clase_listas,
                                     font=('Arial', 12), bg='lightblue')
            btn_ejecutar4.pack(pady=10)
            
            # Actividad 3: Aplicación en problema real (Temperaturas)
            frame_act3 = tk.LabelFrame(scrollable_frame2, 
                                      text="3. Aplicación práctica: Sistema de Temperaturas", 
                                      padx=10, pady=10)
            frame_act3.pack(fill='x', padx=10, pady=10)
            
            intro_text3 = """Objetivo: Implementar un sistema de gestión de temperaturas utilizando listas.

Introducción: Este programa demuestra cómo las listas pueden usarse para resolver problemas reales, permitiendo almacenar, filtrar, ordenar y analizar datos de temperatura de manera eficiente."""
            
            label_intro3 = tk.Label(frame_act3, text=intro_text3, wraplength=1000, justify='left')
            label_intro3.pack(anchor='w', pady=5)
            
            # Botón para ejecutar el programa
            btn_ejecutar5 = tk.Button(frame_act3, text="Ejecutar Programa", 
                                     command=self.ejecutar_sistema_temperaturas_listas,
                                     font=('Arial', 12), bg='lightcoral')
            btn_ejecutar5.pack(pady=10)

            # Nueva Pestaña 3: Operaciones con Conjuntos
            frame_pestaña3 = tk.Frame(notebook)
            notebook.add(frame_pestaña3, text="Operaciones con Conjuntos")
            
            # CANVA 3
            canvas3 = tk.Canvas(frame_pestaña3)
            scrollbar3 = ttk.Scrollbar(frame_pestaña3, orient="vertical", command=canvas3.yview)
            scrollable_frame3 = tk.Frame(canvas3)
            
            scrollable_frame3.bind(
                "<Configure>",
                lambda e: canvas3.configure(
                    scrollregion=canvas3.bbox("all")
                )
            )
            
            canvas3.create_window((0, 0), window=scrollable_frame3, anchor="nw")
            canvas3.configure(yscrollcommand=scrollbar3.set)
            
            canvas3.pack(side="left", fill="both", expand=True)
            scrollbar3.pack(side="right", fill="y")
            
            # Actividad 1: Operaciones básicas con conjuntos
            frame_act1 = tk.LabelFrame(scrollable_frame3, 
                                      text="1. Operaciones básicas con conjuntos", 
                                      padx=10, pady=10)
            frame_act1.pack(fill='x', padx=10, pady=10)
            
            intro_text1 = """Introducción: Los conjuntos en Python son estructuras de datos que permiten almacenar elementos únicos y realizar operaciones matemáticas como unión, intersección y diferencia. Son especialmente útiles cuando se necesita trabajar con colecciones de datos sin elementos duplicados.

Lo que hará el programa es pedirte más de cinco números separados por un espacio y te pedirá la verificación de uno de ellos dando su ubicación y el tamaño del conjunto."""
            
            label_intro1 = tk.Label(frame_act1, text=intro_text1, wraplength=1000, justify='left')
            label_intro1.pack(anchor='w', pady=5)
            
            # Botón para ejecutar el programa
            btn_ejecutar6 = tk.Button(frame_act1, text="Ejecutar Programa", 
                                     command=self.ejecutar_operaciones_conjuntos,
                                     font=('Arial', 12), bg='lightgreen')
            btn_ejecutar6.pack(pady=10)
            
            # Actividad 2: Operaciones avanzadas con conjuntos
            frame_act2 = tk.LabelFrame(scrollable_frame3, 
                                      text="2. Operaciones avanzadas con conjuntos", 
                                      padx=10, pady=10)
            frame_act2.pack(fill='x', padx=10, pady=10)
            
            intro_text2 = """Lo que hará este programa es pedirte que introduzcas dos conjuntos diferentes A y B y hará diversas operaciones con ellos."""
            
            label_intro2 = tk.Label(frame_act2, text=intro_text2, wraplength=1000, justify='left')
            label_intro2.pack(anchor='w', pady=5)
            
            # Botón para ejecutar el programa
            btn_ejecutar7 = tk.Button(frame_act2, text="Ejecutar Programa", 
                                     command=self.ejecutar_operaciones_avanzadas_conjuntos,
                                     font=('Arial', 12), bg='lightblue')
            btn_ejecutar7.pack(pady=10)
            
            # Actividad 3: Aplicación práctica con conjuntos
            frame_act3 = tk.LabelFrame(scrollable_frame3, 
                                      text="3. Aplicación práctica: Gestión de alumnos", 
                                      padx=10, pady=10)
            frame_act3.pack(fill='x', padx=10, pady=10)
            
            intro_text3 = """En este programa implementaremos lo anterior en un problema real como es el caso de alumnos en una lista de un profesor."""
            
            label_intro3 = tk.Label(frame_act3, text=intro_text3, wraplength=1000, justify='left')
            label_intro3.pack(anchor='w', pady=5)
            
            # Botón para ejecutar el programa
            btn_ejecutar8 = tk.Button(frame_act3, text="Ejecutar Programa", 
                                     command=self.ejecutar_gestion_alumnos,
                                     font=('Arial', 12), bg='lightcoral')
            btn_ejecutar8.pack(pady=10)

            # Nueva Pestaña 4: Operaciones con Diccionarios
            frame_pestaña4 = tk.Frame(notebook)
            notebook.add(frame_pestaña4, text="Operaciones con Diccionarios")
            
            # CANVA 4
            canvas4 = tk.Canvas(frame_pestaña4)
            scrollbar4 = ttk.Scrollbar(frame_pestaña4, orient="vertical", command=canvas4.yview)
            scrollable_frame4 = tk.Frame(canvas4)
            
            scrollable_frame4.bind(
                "<Configure>",
                lambda e: canvas4.configure(
                    scrollregion=canvas4.bbox("all")
                )
            )
            
            canvas4.create_window((0, 0), window=scrollable_frame4, anchor="nw")
            canvas4.configure(yscrollcommand=scrollbar4.set)
            
            canvas4.pack(side="left", fill="both", expand=True)
            scrollbar4.pack(side="right", fill="y")
            
            # Actividad 1: Operaciones básicas con diccionarios
            frame_act1 = tk.LabelFrame(scrollable_frame4, 
                                      text="1. Operaciones básicas con diccionarios", 
                                      padx=10, pady=10)
            frame_act1.pack(fill='x', padx=10, pady=10)
            
            intro_text1 = """Introducción: Los diccionarios en Python son estructuras de datos que permiten almacenar pares clave-valor. Son eficientes para la búsqueda y manipulación de datos y se implementan utilizando funciones hash.

En este programa aplicamos el diccionario para que almacene datos ingresados por el usuario y este pueda acceder a ellos por medio de claves."""
            
            label_intro1 = tk.Label(frame_act1, text=intro_text1, wraplength=1000, justify='left')
            label_intro1.pack(anchor='w', pady=5)
            
            # Botón para ejecutar el programa
            btn_ejecutar9 = tk.Button(frame_act1, text="Ejecutar Programa", 
                                     command=self.ejecutar_diccionarios_basicos,
                                     font=('Arial', 12), bg='lightgreen')
            btn_ejecutar9.pack(pady=10)
            
            # Actividad 2: Operaciones avanzadas con diccionarios
            frame_act2 = tk.LabelFrame(scrollable_frame4, 
                                      text="2. Operaciones avanzadas con diccionarios", 
                                      padx=10, pady=10)
            frame_act2.pack(fill='x', padx=10, pady=10)
            
            intro_text2 = """Volvemos a aplicar diccionarios pero esta vez buscaremos elementos, su ubicación o estado, juntar diccionarios, etc."""
            
            label_intro2 = tk.Label(frame_act2, text=intro_text2, wraplength=1000, justify='left')
            label_intro2.pack(anchor='w', pady=5)
            
            # Botón para ejecutar el programa
            btn_ejecutar10 = tk.Button(frame_act2, text="Ejecutar Programa", 
                                      command=self.ejecutar_diccionarios_avanzados,
                                      font=('Arial', 12), bg='lightblue')
            btn_ejecutar10.pack(pady=10)
            
            # Actividad 3: Aplicación práctica con diccionarios
            frame_act3 = tk.LabelFrame(scrollable_frame4, 
                                      text="3. Aplicación práctica: Registro de empleados", 
                                      padx=10, pady=10)
            frame_act3.pack(fill='x', padx=10, pady=10)
            
            intro_text3 = """En este programa se empleará lo anterior pero en un problema real como es Los registros de empleados."""
            
            label_intro3 = tk.Label(frame_act3, text=intro_text3, wraplength=1000, justify='left')
            label_intro3.pack(anchor='w', pady=5)
            
            # Botón para ejecutar el programa
            btn_ejecutar11 = tk.Button(frame_act3, text="Ejecutar Programa", 
                                      command=self.ejecutar_registro_empleados,
                                      font=('Arial', 12), bg='lightcoral')
            btn_ejecutar11.pack(pady=10)
        
        else:
            self.ventana_contenedores.lift()

    def ejecutar_contenedores_basicos(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Estructura de datos y Contenedores")
        ventana.geometry("800x600")
        
        frame = tk.Frame(ventana)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        label = tk.Label(frame, text="Ejecutando programa de contenedores básicos", font=('Arial', 14))
        label.pack(pady=10)
        
        output = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=25)
        output.pack(fill='both', expand=True)
        
        # Función para capturar la salida
        import sys
        from io import StringIO
        
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        
        # Ejecutar el código
        try:
            # Código del programa de contenedores básicos
            Tupla = (3, 5, 7, 3, 5)
            print("Tupla:", Tupla)
            Lista = [3, 5, 7, 3, 5, 7]
            print("Lista:", Lista)

            Conjunto = set(Lista)
            print("Conjunto:", Conjunto)

            diccionario = {numero: numero**2 for numero in Conjunto}
            print("Diccionario (número: cuadrado):", diccionario)

            class Contenedores:
                def __init__(self, tupla, lista, conjunto, diccionario):
                    self.tupla = tupla
                    self.lista = lista
                    self.conjunto = conjunto
                    self.diccionario = diccionario

                def ver(self):
                    print("En la Tupla:", self.tupla)
                    print("En la Lista:", self.lista)
                    print("En Conjunto:", self.conjunto)
                    print("En el Diccionario:", self.diccionario)

            c = Contenedores(Tupla, Lista, Conjunto, diccionario)
            c.ver()
            
            print("\nPreguntas:")
            print("1. ¿Cuál es la principal diferencia entre una lista y un conjunto?")
            print("R= Que en los conjuntos se encuentran caracteres únicos")
            print("\n2. ¿Cómo se estructuran los datos en un diccionario y cuál es su ventaja?")
            print("R= Los elementos se pueden acceder a través de la clave")
            print("Las claves pueden ser cualquier tipo de dato inmutable")
            print("Los valores pueden ser cualquier tipo de dato")
            
        except Exception as e:
            print(f"Error al ejecutar el programa: {str(e)}")
        
        # Restaurar stdout y mostrar la salida
        sys.stdout = old_stdout
        output.insert(tk.END, mystdout.getvalue())
        output.config(state='disabled')
        
        btn_cerrar = tk.Button(frame, text="Cerrar", command=ventana.destroy)
        btn_cerrar.pack(pady=10)

    def ejecutar_sistema_temperaturas(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Sistema de Temperaturas")
        ventana.geometry("800x600")
        
        frame = tk.Frame(ventana)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        label = tk.Label(frame, text="Sistema de Temperaturas", font=('Arial', 14))
        label.pack(pady=10)
        
        output = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=25)
        output.pack(fill='both', expand=True)
        
        # Frame para entrada de datos
        input_frame = tk.Frame(frame)
        input_frame.pack(fill='x', pady=10)
        
        lbl_opcion = tk.Label(input_frame, text="Seleccione una opción:")
        lbl_opcion.pack(side='left')
        
        entry_opcion = tk.Entry(input_frame, width=10)
        entry_opcion.pack(side='left', padx=5)
        
        btn_enviar = tk.Button(input_frame, text="Enviar", 
                            command=lambda: self.procesar_opcion_temperaturas(entry_opcion, output))
        btn_enviar.pack(side='left')
        
        # Variables para almacenar datos
        self.temperaturas = []
        self.dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        
        # Mostrar menú inicial
        output.insert(tk.END, "\nMenú de Opciones:")
        output.insert(tk.END, "\n1. Almacenar temperaturas para la semana")
        output.insert(tk.END, "\n2. Mostrar temperaturas almacenadas")
        output.insert(tk.END, "\n3. Identificar las temperaturas únicas")
        output.insert(tk.END, "\n4. Crear diccionario de temperaturas")
        output.insert(tk.END, "\n5. Mostrar temperatura máxima y mínima")
        output.insert(tk.END, "\n0. Salir\n")
        output.config(state='disabled')
        
        btn_cerrar = tk.Button(frame, text="Cerrar", command=ventana.destroy)
        btn_cerrar.pack(pady=10)

    def procesar_opcion_temperaturas(self, entry_opcion, output):
        opcion = entry_opcion.get()
        entry_opcion.delete(0, tk.END)
        
        output.config(state='normal')
        output.delete(1.0, tk.END)
        
        if opcion == "1":
            # Almacenar temperaturas
            ventana_temp = tk.Toplevel(self.root)
            ventana_temp.title("Ingresar Temperaturas")
            ventana_temp.geometry("400x400")
            
            frame_temp = tk.Frame(ventana_temp)
            frame_temp.pack(fill='both', expand=True, padx=10, pady=10)
            
            self.temperaturas = []  # Reiniciar las temperaturas
            
            # Crear campos para cada día
            self.entries_temp = []
            for i, dia in enumerate(self.dias_semana):
                tk.Label(frame_temp, text=f"Temperatura para {dia}:").grid(row=i, column=0, padx=5, pady=5)
                entry = tk.Entry(frame_temp, width=10)
                entry.grid(row=i, column=1, padx=5, pady=5)
                self.entries_temp.append(entry)
            
            def guardar_temperaturas():
                try:
                    self.temperaturas = []
                    for entry in self.entries_temp:
                        temp = float(entry.get())
                        self.temperaturas.append(temp)
                    
                    output.insert(tk.END, "Temperaturas almacenadas correctamente:\n")
                    for dia, temp in zip(self.dias_semana, self.temperaturas):
                        output.insert(tk.END, f"{dia}: {temp}°C\n")
                    
                    ventana_temp.destroy()
                except ValueError:
                    output.insert(tk.END, "Error: Ingrese valores numéricos válidos para todas las temperaturas\n")
            
            btn_guardar = tk.Button(frame_temp, text="Guardar", command=guardar_temperaturas)
            btn_guardar.grid(row=len(self.dias_semana), column=0, columnspan=2, pady=10)
            
        elif opcion == "2":
            # Mostrar temperaturas almacenadas
            if not self.temperaturas:
                output.insert(tk.END, "No hay temperaturas almacenadas. Use la opción 1 primero.\n")
            else:
                output.insert(tk.END, "Temperaturas almacenadas:\n")
                for dia, temp in zip(self.dias_semana, self.temperaturas):
                    output.insert(tk.END, f"{dia}: {temp}°C\n")
        
        elif opcion == "3":
            # Identificar temperaturas únicas
            if not self.temperaturas:
                output.insert(tk.END, "No hay temperaturas almacenadas. Use la opción 1 primero.\n")
            else:
                temperaturas_unicas = list(set(self.temperaturas))
                output.insert(tk.END, f"Temperaturas únicas: {temperaturas_unicas}\n")
        
        elif opcion == "4":
            # Crear diccionario de temperaturas
            if not self.temperaturas:
                output.insert(tk.END, "No hay temperaturas almacenadas. Use la opción 1 primero.\n")
            else:
                diccionario_temp = dict(zip(self.dias_semana, self.temperaturas))
                output.insert(tk.END, "Diccionario de temperaturas:\n")
                for dia, temp in diccionario_temp.items():
                    output.insert(tk.END, f"{dia}: {temp}°C\n")
        
        elif opcion == "5":
            # Mostrar temperatura máxima y mínima
            if not self.temperaturas:
                output.insert(tk.END, "No hay temperaturas almacenadas. Use la opción 1 primero.\n")
            else:
                temp_max = max(self.temperaturas)
                temp_min = min(self.temperaturas)
                output.insert(tk.END, f"Temperatura máxima: {temp_max}°C\n")
                output.insert(tk.END, f"Temperatura mínima: {temp_min}°C\n")
        
        elif opcion == "0":
            output.insert(tk.END, "Saliendo del programa...\n")
        else:
            output.insert(tk.END, "Opción no válida, intente de nuevo.\n")
        
        output.insert(tk.END, "\nMenú de Opciones:")
        output.insert(tk.END, "\n1. Almacenar temperaturas para la semana")
        output.insert(tk.END, "\n2. Mostrar temperaturas almacenadas")
        output.insert(tk.END, "\n3. Identificar las temperaturas únicas")
        output.insert(tk.END, "\n4. Crear diccionario de temperaturas")
        output.insert(tk.END, "\n5. Mostrar temperatura máxima y mínima")
        output.insert(tk.END, "\n0. Salir\n")
        output.config(state='disabled')
    
    def procesar_opcion_temperaturas(self, entry_opcion, output):
        opcion = entry_opcion.get()
        entry_opcion.delete(0, tk.END)
        
        output.config(state='normal')
        output.delete(1.0, tk.END)
        
        if not hasattr(self, 'temperaturas_app'):
            class Temperaturas:
                def __init__(self):
                    self._temperaturas = []
                    self._dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
                    self._temperaturas_diccionario = {}

                def almacenar(self):
                    self._temperaturas = []
                    for i in self._dias_semana:
                        while True:
                            try:
                                temp = float(input(f"Ingrese la temperatura del {i}: "))
                                self._temperaturas.append(temp)
                                break
                            except ValueError:
                                print("Por favor, ingrese un número válido.")

                def identificar(self):
                    temperaturas_unicas = set(self._temperaturas)
                    print("Temperaturas únicas:", temperaturas_unicas)

                def crear_diccionario(self):
                    self._temperaturas_diccionario = dict(zip(self._dias_semana, self._temperaturas))
                    print("Diccionario de temperaturas:", self._temperaturas_diccionario)

            self.temperaturas_app = Temperaturas()
        
        if opcion == "1":
            # Simular entrada de datos
            self.temperaturas_app._temperaturas = [22.5, 23.0, 24.5, 25.0, 22.5, 23.5, 24.0]
            output.insert(tk.END, "Temperaturas almacenadas:\n")
            for dia, temp in zip(self.temperaturas_app._dias_semana, self.temperaturas_app._temperaturas):
                output.insert(tk.END, f"{dia}: {temp}°C\n")
        elif opcion == "2":
            self.temperaturas_app.identificar()
            output.insert(tk.END, "\nTemperaturas únicas: 22.5, 23.0, 24.5, 25.0, 23.5, 24.0\n")
        elif opcion == "3":
            self.temperaturas_app.crear_diccionario()
            output.insert(tk.END, "\nDiccionario de temperaturas:\n")
            for dia, temp in zip(self.temperaturas_app._dias_semana, self.temperaturas_app._temperaturas):
                output.insert(tk.END, f"{dia}: {temp}°C\n")
        elif opcion == "0":
            output.insert(tk.END, "\nSaliendo del programa...\n")
        else:
            output.insert(tk.END, "\nOpción no válida, intente de nuevo.\n")
        
        output.insert(tk.END, "\nMenú de Opciones:")
        output.insert(tk.END, "\n1. Almacenar temperaturas")
        output.insert(tk.END, "\n2. Identificar las temperaturas únicas")
        output.insert(tk.END, "\n3. Crear diccionario de temperaturas")
        output.insert(tk.END, "\n0. Salir\n")
        output.config(state='disabled')

    # Implementar funciones similares para los otros programas...
    def ejecutar_operaciones_listas(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Operaciones Básicas con Listas")
        ventana.geometry("800x600")
        
        frame = tk.Frame(ventana)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        label = tk.Label(frame, text="Ejecutando Operaciones Básicas con Listas", font=('Arial', 14))
        label.pack(pady=10)
        
        output = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=25)
        output.pack(fill='both', expand=True)
        
        # Ejecutar el código
        output.insert(tk.END, "Resultado del programa:\n\n")
        numeros = [10, 20, 30, 40, 50]
        output.insert(tk.END, f"Lista: {numeros}\n")
        output.insert(tk.END, f"Primer elemento: {numeros[0]}\n")
        output.insert(tk.END, f"Último elemento: {numeros[-1]}\n")
        output.insert(tk.END, f"Tamaño de la lista: {len(numeros)}\n")
        
        output.insert(tk.END, "\nPreguntas:\n")
        output.insert(tk.END, "1. ¿Cómo se accede a los elementos de una lista?\n")
        output.insert(tk.END, "R= Utilizando el número de orden del elemento entre corchetes.\n")
        output.insert(tk.END, "\n2. ¿Cuál es la importancia del tamaño de la lista en un algoritmo?\n")
        output.insert(tk.END, "R= Representa una colección de elementos ordenados y puede contener elementos repetidos.\n")
        
        output.config(state='disabled')
        
        btn_cerrar = tk.Button(frame, text="Cerrar", command=ventana.destroy)
        btn_cerrar.pack(pady=10)

    def ejecutar_clase_listas(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Clase para Operaciones con Listas")
        ventana.geometry("800x600")
        
        frame = tk.Frame(ventana)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        label = tk.Label(frame, text="Ejecutando Clase para Operaciones con Listas", font=('Arial', 14))
        label.pack(pady=10)
        
        output = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=20)
        output.pack(fill='both', expand=True)
        
        # Frame para entrada de datos
        input_frame = tk.Frame(frame)
        input_frame.pack(fill='x', pady=10)
        
        lbl_opcion = tk.Label(input_frame, text="Opción:")
        lbl_opcion.pack(side='left')
        
        entry_opcion = tk.Entry(input_frame, width=10)
        entry_opcion.pack(side='left', padx=5)
        
        btn_enviar = tk.Button(input_frame, text="Enviar", command=lambda: self.procesar_opcion_listas(entry_opcion, output))
        btn_enviar.pack(side='left')
        
        # Mostrar menú inicial
        output.insert(tk.END, "\nOperaciones con listas:")
        output.insert(tk.END, "\n1. Insertar un elemento")
        output.insert(tk.END, "\n2. Eliminar un elemento")
        output.insert(tk.END, "\n3. Buscar un elemento")
        output.insert(tk.END, "\n4. Actualizar un elemento")
        output.insert(tk.END, "\n5. Concatenar otra lista")
        output.insert(tk.END, "\n6. Salir\n")
        output.config(state='disabled')
        
        # Inicializar la lista
        self.lista_numeros = [1, 2, 3, 4, 5]
        
        btn_cerrar = tk.Button(frame, text="Cerrar", command=ventana.destroy)
        btn_cerrar.pack(pady=10)
    
    def procesar_opcion_listas(self, entry_opcion, output):
        opcion = entry_opcion.get()
        entry_opcion.delete(0, tk.END)
        
        output.config(state='normal')
        output.delete(1.0, tk.END)
        
        if opcion == "1":
            # Simular inserción
            elemento = 6
            posicion = 2
            self.lista_numeros.insert(posicion, elemento)
            output.insert(tk.END, f"Lista después de insertar {elemento} en la posición {posicion}: {self.lista_numeros}\n")
        elif opcion == "2":
            # Simular eliminación
            elemento = 3
            if elemento in self.lista_numeros:
                self.lista_numeros.remove(elemento)
                output.insert(tk.END, f"Lista después de eliminar {elemento}: {self.lista_numeros}\n")
            else:
                output.insert(tk.END, "El elemento no está en la lista\n")
        elif opcion == "3":
            # Simular búsqueda
            elemento = 4
            if elemento in self.lista_numeros:
                output.insert(tk.END, f"El elemento {elemento} está en la lista\n")
            else:
                output.insert(tk.END, f"El elemento {elemento} no está en la lista\n")
        elif opcion == "4":
            # Simular actualización
            posicion = 1
            nuevo_valor = 10
            if 0 <= posicion < len(self.lista_numeros):
                self.lista_numeros[posicion] = nuevo_valor
                output.insert(tk.END, f"Lista después de actualizar la posición {posicion}: {self.lista_numeros}\n")
            else:
                output.insert(tk.END, "Posición fuera de rango\n")
        elif opcion == "5":
            # Simular concatenación
            otra_lista = [7, 8, 9]
            nueva_lista = self.lista_numeros + otra_lista
            output.insert(tk.END, f"Lista después de la concatenación: {nueva_lista}\n")
        elif opcion == "6":
            output.insert(tk.END, "Saliendo del programa...\n")
        else:
            output.insert(tk.END, "Opción no válida, intente de nuevo.\n")
        
        output.insert(tk.END, "\nOperaciones con listas:")
        output.insert(tk.END, "\n1. Insertar un elemento")
        output.insert(tk.END, "\n2. Eliminar un elemento")
        output.insert(tk.END, "\n3. Buscar un elemento")
        output.insert(tk.END, "\n4. Actualizar un elemento")
        output.insert(tk.END, "\n5. Concatenar otra lista")
        output.insert(tk.END, "\n6. Salir\n")
        
        output.insert(tk.END, "\nPreguntas:")
        output.insert(tk.END, "\n1. ¿Qué sucede cuando intentamos eliminar un elemento que no está en la lista?")
        output.insert(tk.END, "\nR= Se genera un Error")
        output.insert(tk.END, "\n\n2. ¿Cómo podría afectar la concatenación de listas al rendimiento de un programa?")
        output.insert(tk.END, "\nR= Podría consumir más memoria al crear una nueva lista\n")
        
        output.config(state='disabled')

    def ejecutar_sistema_temperaturas_listas(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Sistema de Temperaturas con Listas")
        ventana.geometry("800x600")
        
        frame = tk.Frame(ventana)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        label = tk.Label(frame, text="Ejecutando Sistema de Temperaturas con Listas", font=('Arial', 14))
        label.pack(pady=10)
        
        output = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=20)
        output.pack(fill='both', expand=True)
        
        # Frame para entrada de datos
        input_frame = tk.Frame(frame)
        input_frame.pack(fill='x', pady=10)
        
        lbl_opcion = tk.Label(input_frame, text="Opción:")
        lbl_opcion.pack(side='left')
        
        entry_opcion = tk.Entry(input_frame, width=10)
        entry_opcion.pack(side='left', padx=5)
        
        btn_enviar = tk.Button(input_frame, text="Enviar", command=lambda: self.procesar_opcion_temp_listas(entry_opcion, output))
        btn_enviar.pack(side='left')
        
        # Inicializar la lista de temperaturas
        self.temperaturas = [22.5, 23.0, 24.5, 25.0, 22.5, 23.5, 24.0]
        
        # Mostrar menú inicial
        output.insert(tk.END, "\nMenú de opciones:")
        output.insert(tk.END, "\n1. Almacenar temperaturas")
        output.insert(tk.END, "\n2. Agregar una temperatura")
        output.insert(tk.END, "\n3. Eliminar temperaturas fuera de un rango")
        output.insert(tk.END, "\n4. Encontrar temperatura más alta y más baja")
        output.insert(tk.END, "\n5. Ordenar temperaturas")
        output.insert(tk.END, "\n6. Salir\n")
        output.config(state='disabled')
        
        btn_cerrar = tk.Button(frame, text="Cerrar", command=ventana.destroy)
        btn_cerrar.pack(pady=10)
    
    def procesar_opcion_temp_listas(self, entry_opcion, output):
        opcion = entry_opcion.get()
        entry_opcion.delete(0, tk.END)
        
        output.config(state='normal')
        output.delete(1.0, tk.END)
        
        if opcion == "1":
            # Simular almacenamiento
            output.insert(tk.END, "Temperaturas almacenadas:\n")
            for temp in self.temperaturas:
                output.insert(tk.END, f"{temp}°C\n")
        elif opcion == "2":
            # Simular agregar temperatura
            nueva_temp = 26.0
            self.temperaturas.append(nueva_temp)
            output.insert(tk.END, f"Temperatura {nueva_temp}°C agregada\n")
            output.insert(tk.END, f"Temperaturas actuales: {self.temperaturas}\n")
        elif opcion == "3":
            # Simular filtrado
            min_temp = 23.0
            max_temp = 25.0
            self.temperaturas = [temp for temp in self.temperaturas if min_temp <= temp <= max_temp]
            output.insert(tk.END, f"Temperaturas después de filtrar entre {min_temp}°C y {max_temp}°C:\n")
            output.insert(tk.END, f"{self.temperaturas}\n")
        elif opcion == "4":
            # Encontrar máximos y mínimos
            if self.temperaturas:
                output.insert(tk.END, f"Temperatura más alta: {max(self.temperaturas)}°C\n")
                output.insert(tk.END, f"Temperatura más baja: {min(self.temperaturas)}°C\n")
            else:
                output.insert(tk.END, "No hay temperaturas registradas\n")
        elif opcion == "5":
            # Ordenar temperaturas
            self.temperaturas.sort()
            output.insert(tk.END, f"Temperaturas ordenadas: {self.temperaturas}\n")
        elif opcion == "6":
            output.insert(tk.END, "Saliendo del programa...\n")
        else:
            output.insert(tk.END, "Opción no válida, intente de nuevo.\n")
        
        output.insert(tk.END, "\nMenú de opciones:")
        output.insert(tk.END, "\n1. Almacenar temperaturas")
        output.insert(tk.END, "\n2. Agregar una temperatura")
        output.insert(tk.END, "\n3. Eliminar temperaturas fuera de un rango")
        output.insert(tk.END, "\n4. Encontrar temperatura más alta y más baja")
        output.insert(tk.END, "\n5. Ordenar temperaturas")
        output.insert(tk.END, "\n6. Salir\n")
        
        output.insert(tk.END, "\nPreguntas:")
        output.insert(tk.END, "\n1. ¿Cómo ayuda el uso de listas a manejar grandes cantidades de datos?")
        output.insert(tk.END, "\nR= Ayuda en que puede agregar y ordenar los elementos agregados a la lista y que estos se pueden modificar")
        output.insert(tk.END, "\n\n2. ¿Qué métodos de listas son más eficientes para manipular datos?")
        output.insert(tk.END, "\nR= append(num), insert(index, num), extend(OtraLista)\n")
        
        output.config(state='disabled')

    def ejecutar_operaciones_conjuntos(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Operaciones Básicas con Conjuntos")
        ventana.geometry("800x600")
        
        frame = tk.Frame(ventana)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        label = tk.Label(frame, text="Ejecutando Operaciones Básicas con Conjuntos", font=('Arial', 14))
        label.pack(pady=10)
        
        output = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=20)
        output.pack(fill='both', expand=True)
        
        # Frame para entrada de datos
        input_frame = tk.Frame(frame)
        input_frame.pack(fill='x', pady=10)
        
        lbl_elementos = tk.Label(input_frame, text="Elementos (separados por espacios):")
        lbl_elementos.pack(side='left')
        
        entry_elementos = tk.Entry(input_frame, width=30)
        entry_elementos.pack(side='left', padx=5)
        
        lbl_buscar = tk.Label(input_frame, text="Elemento a buscar:")
        lbl_buscar.pack(side='left', padx=10)
        
        entry_buscar = tk.Entry(input_frame, width=10)
        entry_buscar.pack(side='left')
        
        btn_ejecutar = tk.Button(input_frame, text="Ejecutar", 
                                command=lambda: self.procesar_conjuntos(entry_elementos, entry_buscar, output))
        btn_ejecutar.pack(side='left', padx=10)
        
        # Mostrar instrucciones
        output.insert(tk.END, "Instrucciones:\n")
        output.insert(tk.END, "1. Ingrese al menos cinco elementos numéricos separados por espacios\n")
        output.insert(tk.END, "2. Ingrese un elemento a buscar en el conjunto\n")
        output.insert(tk.END, "3. Presione 'Ejecutar' para ver los resultados\n\n")
        output.config(state='disabled')
        
        btn_cerrar = tk.Button(frame, text="Cerrar", command=ventana.destroy)
        btn_cerrar.pack(pady=10)
    
    def procesar_conjuntos(self, entry_elementos, entry_buscar, output):
        elementos = entry_elementos.get().split()
        buscar = entry_buscar.get()
        
        output.config(state='normal')
        output.delete(1.0, tk.END)
        
        try:
            # Convertir a números
            numeros = [float(e) for e in elementos]
            
            # Crear conjunto
            conjunto = set(numeros)
            output.insert(tk.END, f"Conjunto creado: {conjunto}\n")
            
            # Buscar elemento
            if buscar:
                try:
                    elemento = float(buscar)
                    if elemento in conjunto:
                        output.insert(tk.END, f"El elemento {elemento} está en el conjunto.\n")
                    else:
                        output.insert(tk.END, f"El elemento {elemento} no está en el conjunto.\n")
                except ValueError:
                    output.insert(tk.END, "Por favor ingrese un número válido para buscar.\n")
            
            output.insert(tk.END, f"Tamaño del conjunto: {len(conjunto)}\n")
            
            output.insert(tk.END, "\nPreguntas:\n")
            output.insert(tk.END, "1. ¿Cuál es la diferencia entre un conjunto y una lista en Python?\n")
            output.insert(tk.END, "R= No permiten elementos duplicados, mientras que las listas sí\n")
            output.insert(tk.END, "\n2. ¿Por qué los conjuntos no permiten elementos duplicados?\n")
            output.insert(tk.END, "R= Porque un objeto solo puede pertenecer o no a un conjunto\n")
            
        except ValueError:
            output.insert(tk.END, "Error: Por favor ingrese solo números válidos.\n")
        
        output.config(state='disabled')

    def ejecutar_operaciones_avanzadas_conjuntos(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Operaciones Avanzadas con Conjuntos")
        ventana.geometry("800x600")
        
        frame = tk.Frame(ventana)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        label = tk.Label(frame, text="Ejecutando Operaciones Avanzadas con Conjuntos", font=('Arial', 14))
        label.pack(pady=10)
        
        output = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=20)
        output.pack(fill='both', expand=True)
        
        # Frame para entrada de datos
        input_frame = tk.Frame(frame)
        input_frame.pack(fill='x', pady=10)
        
        lbl_conjunto_a = tk.Label(input_frame, text="Conjunto A:")
        lbl_conjunto_a.pack(side='left')
        
        entry_conjunto_a = tk.Entry(input_frame, width=20)
        entry_conjunto_a.pack(side='left', padx=5)
        
        lbl_conjunto_b = tk.Label(input_frame, text="Conjunto B:")
        lbl_conjunto_b.pack(side='left', padx=10)
        
        entry_conjunto_b = tk.Entry(input_frame, width=20)
        entry_conjunto_b.pack(side='left')
        
        btn_ejecutar = tk.Button(input_frame, text="Ejecutar", 
                                command=lambda: self.procesar_conjuntos_avanzados(entry_conjunto_a, entry_conjunto_b, output))
        btn_ejecutar.pack(side='left', padx=10)
        
        # Mostrar instrucciones
        output.insert(tk.END, "Instrucciones:\n")
        output.insert(tk.END, "1. Ingrese elementos del conjunto A separados por espacios\n")
        output.insert(tk.END, "2. Ingrese elementos del conjunto B separados por espacios\n")
        output.insert(tk.END, "3. Presione 'Ejecutar' para ver las operaciones entre conjuntos\n\n")
        output.config(state='disabled')
        
        btn_cerrar = tk.Button(frame, text="Cerrar", command=ventana.destroy)
        btn_cerrar.pack(pady=10)
    
    def procesar_conjuntos_avanzados(self, entry_conjunto_a, entry_conjunto_b, output):
        conjunto_a = entry_conjunto_a.get().split()
        conjunto_b = entry_conjunto_b.get().split()
        
        output.config(state='normal')
        output.delete(1.0, tk.END)
        
        try:
            # Convertir a números
            numeros_a = [float(e) for e in conjunto_a]
            numeros_b = [float(e) for e in conjunto_b]
            
            # Crear conjuntos
            set_a = set(numeros_a)
            set_b = set(numeros_b)
            
            output.insert(tk.END, f"Conjunto A: {set_a}\n")
            output.insert(tk.END, f"Conjunto B: {set_b}\n\n")
            
            # Operaciones
            output.insert(tk.END, "Operaciones:\n")
            output.insert(tk.END, f"Unión de A y B: {set_a | set_b}\n")
            output.insert(tk.END, f"Intersección de A y B: {set_a & set_b}\n")
            output.insert(tk.END, f"Diferencia A - B: {set_a - set_b}\n")
            output.insert(tk.END, f"Diferencia B - A: {set_b - set_a}\n")
            output.insert(tk.END, f"Diferencia simétrica A ^ B: {set_a ^ set_b}\n")
            
            output.insert(tk.END, "\nPreguntas:\n")
            output.insert(tk.END, "1. ¿Cuándo es más útil un conjunto que una lista?\n")
            output.insert(tk.END, "R= Depende de la situación pero mayormente son mejores las listas\n")
            output.insert(tk.END, "\n2. ¿Cómo podría usarse la diferencia simétrica en un problema real?\n")
            output.insert(tk.END, "R= En las listas de ventas, si uno quiere saber qué usuarios compraron un producto o ambos\n")
            
        except ValueError:
            output.insert(tk.END, "Error: Por favor ingrese solo números válidos.\n")
        
        output.config(state='disabled')

    def ejecutar_gestion_alumnos(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Gestión de Alumnos con Conjuntos")
        ventana.geometry("800x600")
        
        frame = tk.Frame(ventana)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        label = tk.Label(frame, text="Ejecutando Gestión de Alumnos con Conjuntos", font=('Arial', 14))
        label.pack(pady=10)
        
        output = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=20)
        output.pack(fill='both', expand=True)
        
        # Frame para entrada de datos
        input_frame = tk.Frame(frame)
        input_frame.pack(fill='x', pady=10)
        
        lbl_opcion = tk.Label(input_frame, text="Opción:")
        lbl_opcion.pack(side='left')
        
        entry_opcion = tk.Entry(input_frame, width=10)
        entry_opcion.pack(side='left', padx=5)
        
        btn_enviar = tk.Button(input_frame, text="Enviar", command=lambda: self.procesar_gestion_alumnos(entry_opcion, output))
        btn_enviar.pack(side='left')
        
        # Inicializar conjuntos de alumnos
        self.curso1 = {"Juan", "María", "Pedro", "Ana"}
        self.curso2 = {"María", "Luis", "Ana", "Carlos"}
        
        # Mostrar menú inicial
        output.insert(tk.END, "\nMenú:")
        output.insert(tk.END, "\n1. Almacenar alumnos")
        output.insert(tk.END, "\n2. Encontrar alumnos duplicados")
        output.insert(tk.END, "\n3. Encontrar alumnos exclusivos")
        output.insert(tk.END, "\n4. Listar todos los alumnos sin duplicados")
        output.insert(tk.END, "\n5. Salir\n")
        output.config(state='disabled')
        
        btn_cerrar = tk.Button(frame, text="Cerrar", command=ventana.destroy)
        btn_cerrar.pack(pady=10)
    
    def procesar_gestion_alumnos(self, entry_opcion, output):
        opcion = entry_opcion.get()
        entry_opcion.delete(0, tk.END)
        
        output.config(state='normal')
        output.delete(1.0, tk.END)
        
        if opcion == "1":
            # Simular almacenamiento
            output.insert(tk.END, "Alumnos almacenados:\n")
            output.insert(tk.END, f"Curso 1: {self.curso1}\n")
            output.insert(tk.END, f"Curso 2: {self.curso2}\n")
        elif opcion == "2":
            # Alumnos en ambos cursos
            duplicados = self.curso1 & self.curso2
            output.insert(tk.END, f"Alumnos en ambos cursos: {duplicados}\n")
        elif opcion == "3":
            # Alumnos exclusivos
            exclusivos_curso1 = self.curso1 - self.curso2
            exclusivos_curso2 = self.curso2 - self.curso1
            output.insert(tk.END, f"Alumnos exclusivos de curso 1: {exclusivos_curso1}\n")
            output.insert(tk.END, f"Alumnos exclusivos de curso 2: {exclusivos_curso2}\n")
        elif opcion == "4":
            # Todos los alumnos sin duplicados
            total = self.curso1 | self.curso2
            output.insert(tk.END, f"Total de alumnos sin duplicados: {total}\n")
        elif opcion == "5":
            output.insert(tk.END, "¡Hasta luego!\n")
        else:
            output.insert(tk.END, "Opción no válida. Por favor, intente nuevamente.\n")
        
        output.insert(tk.END, "\nMenú:")
        output.insert(tk.END, "\n1. Almacenar alumnos")
        output.insert(tk.END, "\n2. Encontrar alumnos duplicados")
        output.insert(tk.END, "\n3. Encontrar alumnos exclusivos")
        output.insert(tk.END, "\n4. Listar todos los alumnos sin duplicados")
        output.insert(tk.END, "\n5. Salir\n")
        
        output.insert(tk.END, "\nPreguntas:")
        output.insert(tk.END, "\n1. ¿Cómo se podría usar la operación de intersección en otros contextos?")
        output.insert(tk.END, "\nR= Podría utilizarse para la identificación de identidades")
        output.insert(tk.END, "\n\n2. ¿Por qué los conjuntos son una opción eficiente para manejar listas de elementos únicos?")
        output.insert(tk.END, "\nR= Permiten realizar operaciones de búsqueda y eliminación de duplicados de manera rápida\n")
        
        output.config(state='disabled')

    def ejecutar_diccionarios_basicos(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Operaciones Básicas con Diccionarios")
        ventana.geometry("800x600")
        
        frame = tk.Frame(ventana)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        label = tk.Label(frame, text="Ejecutando Operaciones Básicas con Diccionarios", font=('Arial', 14))
        label.pack(pady=10)
        
        output = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=20)
        output.pack(fill='both', expand=True)
        
        # Frame para entrada de datos
        input_frame = tk.Frame(frame)
        input_frame.pack(fill='x', pady=10)
        
        lbl_nombre = tk.Label(input_frame, text="Nombre:")
        lbl_nombre.pack(side='left')
        
        entry_nombre = tk.Entry(input_frame, width=15)
        entry_nombre.pack(side='left', padx=5)
        
        lbl_edad = tk.Label(input_frame, text="Edad:")
        lbl_edad.pack(side='left')
        
        entry_edad = tk.Entry(input_frame, width=5)
        entry_edad.pack(side='left', padx=5)
        
        lbl_bebida = tk.Label(input_frame, text="Bebida:")
        lbl_bebida.pack(side='left')
        
        entry_bebida = tk.Entry(input_frame, width=15)
        entry_bebida.pack(side='left', padx=5)
        
        lbl_comida = tk.Label(input_frame, text="Comida:")
        lbl_comida.pack(side='left')
        
        entry_comida = tk.Entry(input_frame, width=15)
        entry_comida.pack(side='left', padx=5)
        
        lbl_deporte = tk.Label(input_frame, text="Deporte:")
        lbl_deporte.pack(side='left')
        
        entry_deporte = tk.Entry(input_frame, width=15)
        entry_deporte.pack(side='left', padx=5)
        
        btn_crear = tk.Button(input_frame, text="Crear", 
                             command=lambda: self.crear_diccionario(
                                 entry_nombre, entry_edad, entry_bebida, 
                                 entry_comida, entry_deporte, output))
        btn_crear.pack(side='left', padx=10)
        
        # Segundo frame para consulta
        input_frame2 = tk.Frame(frame)
        input_frame2.pack(fill='x', pady=10)
        
        lbl_consulta = tk.Label(input_frame2, text="Consultar:")
        lbl_consulta.pack(side='left')
        
        entry_consulta = tk.Entry(input_frame2, width=20)
        entry_consulta.pack(side='left', padx=5)
        
        btn_consultar = tk.Button(input_frame2, text="Consultar", 
                                 command=lambda: self.consultar_diccionario(entry_consulta, output))
        btn_consultar.pack(side='left')
        
        # Inicializar diccionario
        self.diccionario_persona = {}
        
        # Mostrar instrucciones
        output.insert(tk.END, "Instrucciones:\n")
        output.insert(tk.END, "1. Complete los datos de la persona\n")
        output.insert(tk.END, "2. Presione 'Crear' para crear el diccionario\n")
        output.insert(tk.END, "3. Ingrese un campo a consultar (nombre, edad, etc.)\n")
        output.insert(tk.END, "4. Presione 'Consultar' para ver el valor\n\n")
        output.config(state='disabled')
        
        btn_cerrar = tk.Button(frame, text="Cerrar", command=ventana.destroy)
        btn_cerrar.pack(pady=10)
    
    def crear_diccionario(self, entry_nombre, entry_edad, entry_bebida, entry_comida, entry_deporte, output):
        nombre = entry_nombre.get()
        edad = entry_edad.get()
        bebida = entry_bebida.get()
        comida = entry_comida.get()
        deporte = entry_deporte.get()
        
        output.config(state='normal')
        output.delete(1.0, tk.END)
        
        try:
            self.diccionario_persona = {
                "nombre": nombre,
                "edad": int(edad),
                "Bebida favorita": bebida,
                "Comida favorita": comida,
                "Deporte favorito": deporte
            }
            
            output.insert(tk.END, "Diccionario creado:\n")
            for clave, valor in self.diccionario_persona.items():
                output.insert(tk.END, f"{clave}: {valor}\n")
            
            output.insert(tk.END, f"\nTamaño del diccionario: {len(self.diccionario_persona)}\n")
            
            output.insert(tk.END, "\nPreguntas:\n")
            output.insert(tk.END, "1. ¿Cuál es la diferencia entre una lista y un diccionario?\n")
            output.insert(tk.END, "R= En una lista se accede por medio de índices, mientras que en un diccionario se accede por medio de claves\n")
            output.insert(tk.END, "\n2. ¿Por qué es útil almacenar datos en pares clave-valor?\n")
            output.insert(tk.END, "R= Permite organizar y ordenar grandes cantidades de información de manera sencilla\n")
            
        except ValueError:
            output.insert(tk.END, "Error: La edad debe ser un número entero\n")
        
        output.config(state='disabled')
    
    def consultar_diccionario(self, entry_consulta, output):
        clave = entry_consulta.get()
        
        output.config(state='normal')
        output.delete(1.0, tk.END)
        
        if not self.diccionario_persona:
            output.insert(tk.END, "Primero debe crear el diccionario\n")
        else:
            if clave in self.diccionario_persona:
                output.insert(tk.END, f"{clave.capitalize()}: {self.diccionario_persona[clave]}\n")
            else:
                output.insert(tk.END, f"La clave '{clave}' no existe en el diccionario\n")
            
            # Mostrar diccionario completo
            output.insert(tk.END, "\nDiccionario completo:\n")
            for clave, valor in self.diccionario_persona.items():
                output.insert(tk.END, f"{clave}: {valor}\n")
        
        output.config(state='disabled')

    def ejecutar_diccionarios_avanzados(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Operaciones Avanzadas con Diccionarios")
        ventana.geometry("800x600")
        
        frame = tk.Frame(ventana)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        label = tk.Label(frame, text="Ejecutando Operaciones Avanzadas con Diccionarios", font=('Arial', 14))
        label.pack(pady=10)
        
        output = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=20)
        output.pack(fill='both', expand=True)
        
        # Frame para entrada de datos
        input_frame = tk.Frame(frame)
        input_frame.pack(fill='x', pady=10)
        
        lbl_opcion = tk.Label(input_frame, text="Opción:")
        lbl_opcion.pack(side='left')
        
        entry_opcion = tk.Entry(input_frame, width=10)
        entry_opcion.pack(side='left', padx=5)
        
        btn_enviar = tk.Button(input_frame, text="Enviar", 
                              command=lambda: self.procesar_diccionarios_avanzados(entry_opcion, output))
        btn_enviar.pack(side='left')
        
        # Inicializar diccionario
        self.diccionario_avanzado = {}
        
        # Mostrar menú inicial
        output.insert(tk.END, "\nMenú de operaciones con diccionarios:")
        output.insert(tk.END, "\n1. Insertar un nuevo par clave-valor")
        output.insert(tk.END, "\n2. Eliminar un elemento")
        output.insert(tk.END, "\n3. Buscar un valor a partir de su clave")
        output.insert(tk.END, "\n4. Actualizar un valor existente")
        output.insert(tk.END, "\n5. Concatenar dos diccionarios")
        output.insert(tk.END, "\n6. Salir\n")
        output.config(state='disabled')
        
        btn_cerrar = tk.Button(frame, text="Cerrar", command=ventana.destroy)
        btn_cerrar.pack(pady=10)
    
    def procesar_diccionarios_avanzados(self, entry_opcion, output):
        opcion = entry_opcion.get()
        entry_opcion.delete(0, tk.END)
        
        output.config(state='normal')
        output.delete(1.0, tk.END)
        
        if opcion == "1":
            # Simular inserción
            clave = "ciudad"
            valor = "Ciudad de México"
            self.diccionario_avanzado[clave] = valor
            output.insert(tk.END, f"Diccionario después de insertar {clave}: {self.diccionario_avanzado}\n")
        elif opcion == "2":
            # Simular eliminación
            clave = "ciudad"
            if clave in self.diccionario_avanzado:
                del self.diccionario_avanzado[clave]
                output.insert(tk.END, f"Diccionario después de eliminar {clave}: {self.diccionario_avanzado}\n")
            else:
                output.insert(tk.END, f"La clave {clave} no se encuentra en el diccionario.\n")
        elif opcion == "3":
            # Simular búsqueda
            clave = "ciudad"
            valor = self.diccionario_avanzado.get(clave, "No encontrado")
            output.insert(tk.END, f"Valor para la clave {clave}: {valor}\n")
        elif opcion == "4":
            # Simular actualización
            clave = "ciudad"
            nuevo_valor = "Guadalajara"
            if clave in self.diccionario_avanzado:
                self.diccionario_avanzado[clave] = nuevo_valor
                output.insert(tk.END, f"Diccionario después de actualizar {clave}: {self.diccionario_avanzado}\n")
            else:
                output.insert(tk.END, f"La clave {clave} no existe en el diccionario.\n")
        elif opcion == "5":
            # Simular concatenación
            otro_diccionario = {"pais": "México", "codigo": 52}
            self.diccionario_avanzado.update(otro_diccionario)
            output.insert(tk.END, f"Diccionario combinado: {self.diccionario_avanzado}\n")
        elif opcion == "6":
            output.insert(tk.END, "¡Hasta luego!\n")
        else:
            output.insert(tk.END, "Opción no válida, intente de nuevo.\n")
        
        output.insert(tk.END, "\nMenú de operaciones con diccionarios:")
        output.insert(tk.END, "\n1. Insertar un nuevo par clave-valor")
        output.insert(tk.END, "\n2. Eliminar un elemento")
        output.insert(tk.END, "\n3. Buscar un valor a partir de su clave")
        output.insert(tk.END, "\n4. Actualizar un valor existente")
        output.insert(tk.END, "\n5. Concatenar dos diccionarios")
        output.insert(tk.END, "\n6. Salir\n")
        
        output.insert(tk.END, "\nPreguntas:")
        output.insert(tk.END, "\n1. ¿Qué sucede si intentamos acceder a una clave inexistente?")
        output.insert(tk.END, "\nR= Se lanzará una excepción KeyError.")
        output.insert(tk.END, "\n\n2. ¿Cuál es la ventaja de usar el método .get() en vez de acceder directamente con []?")
        output.insert(tk.END, "\nR= Acceder a propiedades de objetos sin conocer la forma en que se implementaron las clases\n")
        
        output.config(state='disabled')

    def ejecutar_registro_empleados(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Registro de Empleados con Diccionarios")
        ventana.geometry("800x600")
        
        frame = tk.Frame(ventana)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        label = tk.Label(frame, text="Ejecutando Registro de Empleados con Diccionarios", font=('Arial', 14))
        label.pack(pady=10)
        
        output = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=20)
        output.pack(fill='both', expand=True)
        
        # Frame para entrada de datos
        input_frame = tk.Frame(frame)
        input_frame.pack(fill='x', pady=10)
        
        lbl_opcion = tk.Label(input_frame, text="Opción:")
        lbl_opcion.pack(side='left')
        
        entry_opcion = tk.Entry(input_frame, width=10)
        entry_opcion.pack(side='left', padx=5)
        
        btn_enviar = tk.Button(input_frame, text="Enviar", 
                              command=lambda: self.procesar_registro_empleados(entry_opcion, output))
        btn_enviar.pack(side='left')
        
        # Inicializar diccionario de empleados
        self.empleados = {
            "E001": {"nombre": "Carlos", "puesto": "Analista", "salario": 35000},
            "E002": {"nombre": "María", "puesto": "Desarrollador", "salario": 40000},
            "E003": {"nombre": "Elena", "puesto": "Gerente", "salario": 60000}
        }
        
        # Mostrar menú inicial
        output.insert(tk.END, "\n--- Menú de Registro de Empleados ---")
        output.insert(tk.END, "\n1. Agregar un empleado")
        output.insert(tk.END, "\n2. Actualizar salario de un empleado")
        output.insert(tk.END, "\n3. Eliminar empleados")
        output.insert(tk.END, "\n4. Listar todos los empleados")
        output.insert(tk.END, "\n5. Salir\n")
        output.config(state='disabled')
        
        btn_cerrar = tk.Button(frame, text="Cerrar", command=ventana.destroy)
        btn_cerrar.pack(pady=10)
    
    def procesar_registro_empleados(self, entry_opcion, output):
        opcion = entry_opcion.get()
        entry_opcion.delete(0, tk.END)
        
        output.config(state='normal')
        output.delete(1.0, tk.END)
        
        if opcion == "1":
            # Simular agregar empleado
            id_empleado = "E004"
            nombre = "Juan"
            puesto = "Diseñador"
            salario = 38000
            self.empleados[id_empleado] = {"nombre": nombre, "puesto": puesto, "salario": salario}
            output.insert(tk.END, f"Empleado {nombre} agregado con éxito.\n")
        elif opcion == "2":
            # Simular actualizar salario
            id_empleado = "E001"
            nuevo_salario = 38000
            if id_empleado in self.empleados:
                self.empleados[id_empleado]["salario"] = nuevo_salario
                output.insert(tk.END, f"Salario actualizado de {self.empleados[id_empleado]['nombre']} a {nuevo_salario}.\n")
            else:
                output.insert(tk.END, "Empleado no encontrado.\n")
        elif opcion == "3":
            # Simular eliminar empleado
            id_empleado = "E003"
            if id_empleado in self.empleados:
                del self.empleados[id_empleado]
                output.insert(tk.END, f"Empleado {id_empleado} eliminado.\n")
            else:
                output.insert(tk.END, "Empleado no encontrado.\n")
        elif opcion == "4":
            # Listar empleados
            output.insert(tk.END, "\nLista de empleados:\n")
            for id_empleado, datos in self.empleados.items():
                output.insert(tk.END, f"ID: {id_empleado}, Nombre: {datos['nombre']}, Puesto: {datos['puesto']}, Salario: {datos['salario']}\n")
        elif opcion == "5":
            output.insert(tk.END, "¡Adios!\n")
        else:
            output.insert(tk.END, "Opción no válida. Por favor, intente nuevamente.\n")
        
        output.insert(tk.END, "\n--- Menú de Registro de Empleados ---")
        output.insert(tk.END, "\n1. Agregar un empleado")
        output.insert(tk.END, "\n2. Actualizar salario de un empleado")
        output.insert(tk.END, "\n3. Eliminar empleados")
        output.insert(tk.END, "\n4. Listar todos los empleados")
        output.insert(tk.END, "\n5. Salir\n")
        
        output.insert(tk.END, "\nPreguntas:")
        output.insert(tk.END, "\n1. ¿Cómo podría optimizarse la manipulación de grandes volúmenes de datos con diccionarios?")
        output.insert(tk.END, "\nR= ")
        output.insert(tk.END, "\n\n2. ¿Cuándo es mejor usar un diccionario en vez de una lista o un conjunto?")
        output.insert(tk.END, "\nR= Cuando se necesita asignar un valor a una variable o buscar un objeto de forma rápida\n")
        
        output.config(state='disabled')

    def agregar_codigo_colas(self, frame):
        # Marco para el código
        frame_codigo = tk.Frame(frame)
        frame_codigo.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Texto de introducción
        intro_text = """Introducción: PRUEBA DE FUNCIONAMIENTO https://wokwi.com/projects/426014789605622785

Objetivo: El alumno implementará el concepto de COLAS en MicroPython usando un ESP32 en la plataforma wokwi.com. Convertirá un código basado en funciones a un enfoque orientado a objetos (POO), organizando mejor el código y facilitando su reutilización.

En este programa lo que se debe observar que se aplicarán colas en Python por lo que con un botón prenderás los LEDs consecutivamente y con el otro botón se irán reemplazando y apagando."""
        
        label_intro = tk.Label(frame_codigo, text=intro_text, wraplength=950, justify='left')
        label_intro.pack(pady=10, anchor='w')
        
        # Botón para abrir el enlace
        btn_enlace = tk.Button(frame_codigo, text="Abrir enlace del proyecto", 
                              command=lambda: webbrowser.open("https://wokwi.com/projects/426014789605622785"))
        btn_enlace.pack(pady=5)
        
        # Marco para el código con scroll
        frame_codigo_texto = tk.Frame(frame_codigo)
        frame_codigo_texto.pack(fill='both', expand=True)
        
        scrollbar = tk.Scrollbar(frame_codigo_texto)
        scrollbar.pack(side='right', fill='y')
        
        text_codigo = tk.Text(frame_codigo_texto, wrap='word', yscrollcommand=scrollbar.set,
                            font=('Courier', 10), bg='#f0f0f0', padx=10, pady=10)
        text_codigo.pack(fill='both', expand=True)
        
        scrollbar.config(command=text_codigo.yview)
        
        # Insertar el código
        codigo = """# 1.- ---------------- Encabezado ----------------------------------------------
\"\"\"
Alumno: Ricardo Soberanes Flores
Grupo: 2CV14
Maestro: Jorge Anzaldo
Fecha: 18/03/2025
\"\"\"

# 2.- ---------------- Importación de Módulos y Bibliotecas --------------------
from machine import Pin
import time

# 3.- ---------------- Definición de Funciones o clases ------------------------
class ColaLEDs:
    def __init__(self, led_pins, boton_insertar, boton_extraer):
        self.leds = [Pin(pin, Pin.OUT) for pin in led_pins]
        self.cola = []
        self.boton_insertar = Pin(boton_insertar, Pin.IN, Pin.PULL_UP)
        self.boton_extraer = Pin(boton_extraer, Pin.IN, Pin.PULL_UP)

    def insertarLed(self):
        if len(self.cola) < len(self.leds):
            for led in self.leds:
                if led not in self.cola:
                    self.cola.append(led)
                    led.value(1)
                    break

    def extraerLed(self):
        if self.cola:
            led = self.cola.pop(0)
            led.value(0)

    def ejecutar(self):
        while True:
            if not self.boton_insertar.value():
                self.insertarLed()
                time.sleep(0.3)
            if not self.boton_extraer.value():
                self.extraerLed()
                time.sleep(0.3)

# 4.- ---------------- Variables u Objetos Globales ----------------------------

# 5.- ---------------- Bloque Principal ----------------------------------------
if __name__ == '__main__':
    led_pins = [2, 4, 5, 18, 19, 21, 22, 23]
    boton_insertar = 13
    boton_extraer = 12

    cola_leds = ColaLEDs(led_pins, boton_insertar, boton_extraer)
    cola_leds.ejecutar()

# 6.- ---------------- Documentación y Comentarios------------------------------"""
        
        text_codigo.insert('1.0', codigo)
        text_codigo.config(state='disabled')

    def mostrar_pilas_colas(self):
        if self.ventana_pilas_colas is None or not self.ventana_pilas_colas.winfo_exists():
            self.ventana_pilas_colas = tk.Toplevel(self.root)
            self.ventana_pilas_colas.title("Pilas y Colas - Segundo Parcial")
            self.ventana_pilas_colas.geometry("1000x800")
            
            notebook = ttk.Notebook(self.ventana_pilas_colas)
            notebook.pack(fill='both', expand=True)
            
            # ----------------- PESTAÑA DE PILAS -----------------
            frame_pilas = tk.Frame(notebook)
            notebook.add(frame_pilas, text="Programas de Pilas")
            
            # Panel izquierdo (Menú y operaciones)
            panel_izquierdo_pilas = tk.Frame(frame_pilas, width=300, padx=10, pady=10, bg='#f0f0f0')
            panel_izquierdo_pilas.pack(side='left', fill='y')
            panel_izquierdo_pilas.pack_propagate(False)
            
            # Panel derecho (Salida y resultados)
            panel_derecho_pilas = tk.Frame(frame_pilas, padx=10, pady=10)
            panel_derecho_pilas.pack(side='right', fill='both', expand=True)
            
            # Título y descripción
            tk.Label(panel_izquierdo_pilas, text="OPERACIONES CON PILAS", 
                    font=('Arial', 12, 'bold'), bg='#f0f0f0').pack(pady=10)
            
            # Estado actual de la pila
            self.estado_pila_label = tk.Label(panel_izquierdo_pilas, text="Pila: []", 
                                            font=('Courier', 10), bg='#f0f0f0')
            self.estado_pila_label.pack(pady=5)
            
            # Botones de operaciones básicas
            tk.Button(panel_izquierdo_pilas, text="Push (Insertar)", command=self.pila_push,
                    bg='lightgreen', width=20).pack(pady=5)
            tk.Button(panel_izquierdo_pilas, text="Pop (Extraer)", command=self.pila_pop,
                    bg='lightcoral', width=20).pack(pady=5)
            tk.Button(panel_izquierdo_pilas, text="Peek (Ver tope)", command=self.pila_peek,
                    bg='lightblue', width=20).pack(pady=5)
            
            # Separador
            tk.Label(panel_izquierdo_pilas, text="Aplicaciones", font=('Arial', 10, 'underline'), 
                    bg='#f0f0f0').pack(pady=10)
            
            # Botones de aplicaciones
            tk.Button(panel_izquierdo_pilas, text="Validar paréntesis", 
                    command=self.validar_parentesis, width=20).pack(pady=5)
            tk.Button(panel_izquierdo_pilas, text="Infija a Postfija", 
                    command=self.infija_a_postfija, width=20).pack(pady=5)
            
            # Área de salida con scroll
            self.output_pilas = scrolledtext.ScrolledText(panel_derecho_pilas, wrap=tk.WORD, 
                                                        width=70, height=30, font=('Consolas', 10))
            self.output_pilas.pack(fill='both', expand=True)
            
            # Inicializar la pila
            self.pila = []
            self.mostrar_estado_pila()
            
            # ----------------- PESTAÑA DE COLAS -----------------
            frame_colas = tk.Frame(notebook)
            notebook.add(frame_colas, text="Programas de Colas")
            
            # Panel izquierdo (Menú y operaciones)
            panel_izquierdo_colas = tk.Frame(frame_colas, width=300, padx=10, pady=10, bg='#f0f0f0')
            panel_izquierdo_colas.pack(side='left', fill='y')
            panel_izquierdo_colas.pack_propagate(False)
            
            # Panel derecho (Salida y resultados)
            panel_derecho_colas = tk.Frame(frame_colas, padx=10, pady=10)
            panel_derecho_colas.pack(side='right', fill='both', expand=True)
            
            # Título y descripción
            tk.Label(panel_izquierdo_colas, text="SIMULACIÓN DE ESTACIÓN DE SERVICIO", 
                    font=('Arial', 12, 'bold'), bg='#f0f0f0').pack(pady=10)
            
            # Estado actual de la cola
            self.estado_cola_label = tk.Label(panel_izquierdo_colas, text="Cola: []", 
                                            font=('Courier', 10), bg='#f0f0f0')
            self.estado_cola_label.pack(pady=5)
            
            # Estadísticas
            self.stats_label = tk.Label(panel_izquierdo_colas, 
                                    text="Autos atendidos: 0\nTiempo promedio: 0.00", 
                                    bg='#f0f0f0', justify='left')
            self.stats_label.pack(pady=10)
            
            # Botones de operaciones
            tk.Button(panel_izquierdo_colas, text="Llegada de auto", command=self.llegada_auto,
                    bg='lightgreen', width=20).pack(pady=5)
            tk.Button(panel_izquierdo_colas, text="Atender auto", command=self.atender_auto,
                    bg='lightcoral', width=20).pack(pady=5)
            tk.Button(panel_izquierdo_colas, text="Mostrar cola", command=self.mostrar_cola,
                    bg='lightblue', width=20).pack(pady=5)
            
            # Área de salida con scroll
            self.output_colas = scrolledtext.ScrolledText(panel_derecho_colas, wrap=tk.WORD, 
                                                        width=70, height=30, font=('Consolas', 10))
            self.output_colas.pack(fill='both', expand=True)
            
            # Inicializar variables de cola
            self.cola_autos = []
            self.tiempo_actual = 0
            self.tiempo_total_espera = 0
            self.autos_atendidos = 0
            self.actualizar_estado_cola()
        else:
            self.ventana_pilas_colas.lift()

        # Mostrar ventana
        self.ventana_pilas_colas.mainloop()

    def mostrar_estado_pila(self):
        self.estado_pila_label.config(text=f"Pila: {self.pila}")
        
    def pila_push(self):
        # Crear una pequeña ventana emergente para ingresar el valor
        ventana_push = tk.Toplevel(self.ventana_pilas_colas)
        ventana_push.title("Insertar elemento")
        ventana_push.geometry("300x150")
        
        tk.Label(ventana_push, text="Ingrese el valor a insertar:").pack(pady=10)
        
        entry_valor = tk.Entry(ventana_push, width=20)
        entry_valor.pack(pady=5)
        entry_valor.focus_set()
        
        def insertar():
            valor = entry_valor.get()
            if valor:
                self.pila.append(valor)
                self.mostrar_estado_pila()
                self.agregar_salida_pilas(f"Operación Push: Se insertó '{valor}'")
                ventana_push.destroy()
        
        tk.Button(ventana_push, text="Insertar", command=insertar).pack(pady=10)
        ventana_push.bind('<Return>', lambda e: insertar())
        
    def pila_pop(self):
        if not self.pila:
            self.agregar_salida_pilas("Error: La pila está vacía, no se puede hacer Pop")
            return
        
        valor = self.pila.pop()
        self.mostrar_estado_pila()
        self.agregar_salida_pilas(f"Operación Pop: Se extrajo '{valor}'")
        
    def pila_peek(self):
        if not self.pila:
            self.agregar_salida_pilas("Error: La pila está vacía, no hay elemento para ver")
            return
        
        self.agregar_salida_pilas(f"Operación Peek: Elemento en el tope: '{self.pila[-1]}'")
        
    def validar_parentesis(self):
        # Ventana para ingresar expresión
        ventana_parentesis = tk.Toplevel(self.ventana_pilas_colas)
        ventana_parentesis.title("Validar paréntesis")
        ventana_parentesis.geometry("400x200")
        
        tk.Label(ventana_parentesis, text="Ingrese la expresión a validar:").pack(pady=10)
        
        entry_expresion = tk.Entry(ventana_parentesis, width=40)
        entry_expresion.pack(pady=5)
        entry_expresion.focus_set()
        
        def validar():
            expresion = entry_expresion.get()
            if not expresion:
                return
            
            # Algoritmo de validación de paréntesis
            pila_temp = []
            balanceado = True
            
            for caracter in expresion:
                if caracter in "([{":
                    pila_temp.append(caracter)
                elif caracter in ")]}":
                    if not pila_temp:
                        balanceado = False
                        break
                    ultimo = pila_temp.pop()
                    if (caracter == ")" and ultimo != "(") or \
                    (caracter == "]" and ultimo != "[") or \
                    (caracter == "}" and ultimo != "{"):
                        balanceado = False
                        break
            
            if pila_temp:
                balanceado = False
                
            resultado = "balanceada" if balanceado else "NO balanceada"
            
            self.agregar_salida_pilas(f"Validación de paréntesis:")
            self.agregar_salida_pilas(f"Expresión: {expresion}")
            self.agregar_salida_pilas(f"Resultado: {resultado}\n")
            ventana_parentesis.destroy()
        
        tk.Button(ventana_parentesis, text="Validar", command=validar).pack(pady=10)
        ventana_parentesis.bind('<Return>', lambda e: validar())
        
    def infija_a_postfija(self):
        # Ventana para ingresar expresión infija
        ventana_infija = tk.Toplevel(self.ventana_pilas_colas)
        ventana_infija.title("Convertir infija a postfija")
        ventana_infija.geometry("400x200")
        
        tk.Label(ventana_infija, text="Ingrese la expresión infija:").pack(pady=10)
        
        entry_expresion = tk.Entry(ventana_infija, width=40)
        entry_expresion.pack(pady=5)
        entry_expresion.focus_set()
        
        def convertir():
            expresion = entry_expresion.get()
            if not expresion:
                return
            
            # Algoritmo simplificado de conversión infija a postfija
            precedencia = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
            pila_operadores = []
            postfija = []
            
            for token in expresion:
                if token.isalnum():  # Operando
                    postfija.append(token)
                elif token == '(':
                    pila_operadores.append(token)
                elif token == ')':
                    while pila_operadores and pila_operadores[-1] != '(':
                        postfija.append(pila_operadores.pop())
                    pila_operadores.pop()  # Sacar el '('
                else:  # Operador
                    while (pila_operadores and 
                        precedencia[pila_operadores[-1]] >= precedencia[token]):
                        postfija.append(pila_operadores.pop())
                    pila_operadores.append(token)
            
            while pila_operadores:
                postfija.append(pila_operadores.pop())
            
            resultado = ' '.join(postfija)
            
            self.agregar_salida_pilas(f"Conversión infija a postfija:")
            self.agregar_salida_pilas(f"Expresión infija: {expresion}")
            self.agregar_salida_pilas(f"Expresión postfija: {resultado}\n")
            ventana_infija.destroy()
        
        tk.Button(ventana_infija, text="Convertir", command=convertir).pack(pady=10)
        ventana_infija.bind('<Return>', lambda e: convertir())

    def limpiar_salida_pilas(self):
        self.output_pilas.config(state='normal')
        self.output_pilas.delete(1.0, tk.END)
        self.output_pilas.config(state='disabled')
        
    def agregar_salida_pilas(self, texto):
        self.output_pilas.config(state='normal')
        self.output_pilas.insert(tk.END, texto + "\n")
        self.output_pilas.config(state='disabled')
        self.output_pilas.see(tk.END)



    # ============ MÉTODOS PARA COLAS ============
    def actualizar_estado_cola(self):
        self.estado_cola_label.config(text=f"Cola: {self.cola_autos}")
        self.stats_label.config(text=f"Autos atendidos: {self.autos_atendidos}\nTiempo promedio: {self.calcular_promedio():.2f}")
        
    def calcular_promedio(self):
        return self.tiempo_total_espera / self.autos_atendidos if self.autos_atendidos > 0 else 0
        
    def llegada_auto(self):
        self.cola_autos.append(self.tiempo_actual)
        self.agregar_salida_colas(f"Auto llegó en minuto {self.tiempo_actual}")
        self.tiempo_actual += 1
        self.actualizar_estado_cola()
        
    def atender_auto(self):
        if not self.cola_autos:
            self.agregar_salida_colas("No hay autos en la cola")
            return
        
        tiempo_llegada = self.cola_autos.pop(0)
        tiempo_espera = self.tiempo_actual - tiempo_llegada
        self.tiempo_total_espera += tiempo_espera
        self.autos_atendidos += 1
        
        tiempo_atencion = 3  # minutos fijos de atención
        self.tiempo_actual += tiempo_atencion
        
        self.agregar_salida_colas(f"Auto atendido - Espera: {tiempo_espera} min - Tiempo atención: {tiempo_atencion} min")
        self.actualizar_estado_cola()
        
    def mostrar_cola(self):
        self.agregar_salida_colas(f"\nEstado actual de la cola: {self.cola_autos}")
        self.agregar_salida_colas(f"Minuto actual: {self.tiempo_actual}")
        self.agregar_salida_colas(f"Autos en cola: {len(self.cola_autos)}")
        self.agregar_salida_colas(f"Autos atendidos: {self.autos_atendidos}")
        self.agregar_salida_colas(f"Tiempo promedio de espera: {self.calcular_promedio():.2f} min\n")
        
    def agregar_salida_colas(self, texto):
        self.output_colas.config(state='normal')
        self.output_colas.insert(tk.END, texto + "\n")
        self.output_colas.config(state='disabled')
        self.output_colas.see(tk.END)


    def mostrar_recursividad_grafos(self):
        if self.ventana_rec_grafos is None or not self.ventana_rec_grafos.winfo_exists():
            self.ventana_rec_grafos = tk.Toplevel(self.root)
            self.ventana_rec_grafos.title("Recursividad y Grafos - Segundo Parcial")
            self.ventana_rec_grafos.geometry("1000x800")
            
            notebook = ttk.Notebook(self.ventana_rec_grafos)
            notebook.pack(fill='both', expand=True)
            
            # Pestaña 1: Recursividad
            frame_recursividad = tk.Frame(notebook)
            notebook.add(frame_recursividad, text="Programas de Recursividad")
            
            # Panel izquierdo (Menú y operaciones)
            panel_izquierdo_rec = tk.Frame(frame_recursividad, width=300, padx=10, pady=10, bg='#f0f0f0')
            panel_izquierdo_rec.pack(side='left', fill='y')
            panel_izquierdo_rec.pack_propagate(False)
            
            # Panel derecho (Salida y resultados)
            panel_derecho_rec = tk.Frame(frame_recursividad)
            panel_derecho_rec.pack(side='right', fill='both', expand=True)
            
            # Título y descripción
            tk.Label(panel_izquierdo_rec, text="RECURSIVIDAD: RESISTENCIAS", 
                    font=('Arial', 12, 'bold'), bg='#f0f0f0').pack(pady=10)
            
            # Estado actual de las resistencias
            self.resistencias = []
            self.estado_resistencias_label = tk.Label(panel_izquierdo_rec, text="Resistencias: []", 
                                                    font=('Courier', 10), bg='#f0f0f0')
            self.estado_resistencias_label.pack(pady=5)
            
            # Botones de operaciones básicas
            tk.Button(panel_izquierdo_rec, text="Agregar resistencia", command=self.agregar_resistencia,
                    bg='lightgreen', width=20).pack(pady=5)
            tk.Button(panel_izquierdo_rec, text="Mostrar resistencias", command=self.mostrar_resistencias,
                    bg='lightblue', width=20).pack(pady=5)
            
            # Frame para operaciones mixtas
            frame_operaciones = tk.Frame(panel_izquierdo_rec, bg='#f0f0f0')
            frame_operaciones.pack(pady=10)
            
            tk.Label(frame_operaciones, text="Operación Mixta:", bg='#f0f0f0').pack()
            
            self.tipo_operacion = tk.StringVar(value="serie")
            tk.Radiobutton(frame_operaciones, text="Serie", variable=self.tipo_operacion, 
                        value="serie", bg='#f0f0f0').pack(anchor='w')
            tk.Radiobutton(frame_operaciones, text="Paralelo", variable=self.tipo_operacion, 
                        value="paralelo", bg='#f0f0f0').pack(anchor='w')
            
            tk.Label(frame_operaciones, text="Resistencias (ej: R1 R2):", bg='#f0f0f0').pack()
            self.entry_resistencias = tk.Entry(frame_operaciones, width=20)
            self.entry_resistencias.pack()
            
            tk.Button(frame_operaciones, text="Calcular", command=self.calcular_mixta,
                    bg='lightcoral').pack(pady=5)
            
            # Área de salida con scroll
            self.output_recursividad = scrolledtext.ScrolledText(panel_derecho_rec, wrap=tk.WORD, 
                                                            width=70, height=30, font=('Consolas', 10))
            self.output_recursividad.pack(fill='both', expand=True)
            
            # Pestaña 2: Grafos
            frame_grafos = tk.Frame(notebook)
            notebook.add(frame_grafos, text="Programas de Grafos")
            
            # Panel izquierdo (Menú y operaciones)
            panel_izquierdo_grafos = tk.Frame(frame_grafos, width=300, padx=10, pady=10, bg='#f0f0f0')
            panel_izquierdo_grafos.pack(side='left', fill='y')
            panel_izquierdo_grafos.pack_propagate(False)
            
            # Panel derecho (Salida y resultados)
            panel_derecho_grafos = tk.Frame(frame_grafos)
            panel_derecho_grafos.pack(side='right', fill='both', expand=True)
            
            # Título y descripción
            tk.Label(panel_izquierdo_grafos, text="GRAFOS: SENDERISMO", 
                    font=('Arial', 12, 'bold'), bg='#f0f0f0').pack(pady=10)
            
            # Nivel de experiencia
            tk.Label(panel_izquierdo_grafos, text="Nivel de experiencia:", bg='#f0f0f0').pack()
            
            self.nivel_experiencia = tk.StringVar(value="1")
            tk.Radiobutton(panel_izquierdo_grafos, text="Principiante", variable=self.nivel_experiencia, 
                        value="1", bg='#f0f0f0').pack(anchor='w')
            tk.Radiobutton(panel_izquierdo_grafos, text="Experimentado", variable=self.nivel_experiencia, 
                        value="2", bg='#f0f0f0').pack(anchor='w')
            tk.Radiobutton(panel_izquierdo_grafos, text="Avanzado", variable=self.nivel_experiencia, 
                        value="3", bg='#f0f0f0').pack(anchor='w')
            
            # Destinos
            tk.Label(panel_izquierdo_grafos, text="Destino:", bg='#f0f0f0').pack()
            
            self.destinos = ["Mirador-Princ", "Cascada-Princ", "Zona-Rocosa"]
            self.destino_seleccionado = tk.StringVar(value=self.destinos[0])
            tk.OptionMenu(panel_izquierdo_grafos, self.destino_seleccionado, *self.destinos).pack()
            
            # Botones de operaciones
            tk.Button(panel_izquierdo_grafos, text="Mostrar ruta", command=self.mostrar_ruta_senderismo,
                    bg='lightgreen', width=20).pack(pady=10)
            tk.Button(panel_izquierdo_grafos, text="Mostrar mapa completo", command=self.mostrar_mapa_completo,
                    bg='lightblue', width=20).pack(pady=5)
            
            # Área de salida con scroll
            self.output_grafos = scrolledtext.ScrolledText(panel_derecho_grafos, wrap=tk.WORD, 
                                                        width=70, height=30, font=('Consolas', 10))
            self.output_grafos.pack(fill='both', expand=True)
            
            # Inicializar grafo de senderismo
            self.inicializar_grafo_senderismo()
        else:
            self.ventana_rec_grafos.lift()

    # Métodos para recursividad (resistencias)
    def agregar_resistencia(self):
        ventana = tk.Toplevel(self.ventana_rec_grafos)
        ventana.title("Agregar resistencia")
        ventana.geometry("300x150")
        
        tk.Label(ventana, text="Valor de la resistencia (Ω):").pack(pady=10)
        
        entry_valor = tk.Entry(ventana, width=20)
        entry_valor.pack(pady=5)
        entry_valor.focus_set()
        
        def agregar():
            try:
                valor = float(entry_valor.get())
                self.resistencias.append(valor)
                self.estado_resistencias_label.config(text=f"Resistencias: {self.resistencias}")
                self.agregar_salida_recursividad(f"Resistencia agregada: {valor}Ω")
                ventana.destroy()
            except ValueError:
                self.agregar_salida_recursividad("Error: Ingrese un valor numérico válido")
        
        tk.Button(ventana, text="Agregar", command=agregar).pack(pady=10)
        ventana.bind('<Return>', lambda e: agregar())

    def mostrar_resistencias(self):
        if not self.resistencias:
            self.agregar_salida_recursividad("No hay resistencias agregadas")
            return
        
        texto = "Resistencias actuales:\n"
        for i, r in enumerate(self.resistencias, 1):
            texto += f"R{i}: {r}Ω\n"
        self.agregar_salida_recursividad(texto)

    def calcular_mixta(self):
        if not self.resistencias:
            self.agregar_salida_recursividad("Error: No hay resistencias para calcular")
            return
        
        try:
            # Obtener las resistencias a usar
            texto_resistencias = self.entry_resistencias.get()
            if not texto_resistencias:
                indices = range(len(self.resistencias))
            else:
                partes = texto_resistencias.split()
                indices = [int(r[1:])-1 for r in partes if r.startswith('R')]
            
            valores = [self.resistencias[i] for i in indices if 0 <= i < len(self.resistencias)]
            
            if not valores:
                self.agregar_salida_recursividad("Error: No se especificaron resistencias válidas")
                return
            
            # Calcular según el tipo de operación
            tipo = self.tipo_operacion.get()
            if tipo == "serie":
                resultado = sum(valores)
                self.agregar_salida_recursividad(f"Resistencia equivalente en serie: {resultado:.2f}Ω")
            else:
                resultado = 1 / sum(1/r for r in valores)
                self.agregar_salida_recursividad(f"Resistencia equivalente en paralelo: {resultado:.2f}Ω")
            
        except (ValueError, IndexError) as e:
            self.agregar_salida_recursividad(f"Error: {str(e)}")
    def mostrar_arboles_binarios(self):
        if not hasattr(self, 'ventana_arboles') or not self.ventana_arboles.winfo_exists():
            self.ventana_arboles = tk.Toplevel(self.root)
            self.ventana_arboles.title("Árboles Binarios de Búsqueda")
            self.arbol = ABB()
            
            # Frame para entrada de datos
            frame_entrada = ttk.LabelFrame(self.ventana_arboles, text="Insertar Nuevo Nodo")
            frame_entrada.pack(padx=10, pady=10, fill='x')
            
            ttk.Label(frame_entrada, text="Código:").grid(row=0, column=0, padx=5, pady=5)
            self.entry_codigo = ttk.Entry(frame_entrada)
            self.entry_codigo.grid(row=0, column=1, padx=5, pady=5)
            
            ttk.Label(frame_entrada, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
            self.entry_nombre = ttk.Entry(frame_entrada)
            self.entry_nombre.grid(row=1, column=1, padx=5, pady=5)
            
            ttk.Label(frame_entrada, text="Domicilio:").grid(row=2, column=0, padx=5, pady=5)
            self.entry_domicilio = ttk.Entry(frame_entrada)
            self.entry_domicilio.grid(row=2, column=1, padx=5, pady=5)
            
            ttk.Button(frame_entrada, text="Insertar", command=self.insertar_nodo_arbol).grid(row=3, column=0, columnspan=2, pady=5)
            
            # Frame para recorridos
            frame_recorridos = ttk.LabelFrame(self.ventana_arboles, text="Recorridos del Árbol")
            frame_recorridos.pack(padx=10, pady=10, fill='x')
            
            ttk.Button(frame_recorridos, text="Inorden", command=self.mostrar_inorden).pack(side='left', padx=5, pady=5)
            ttk.Button(frame_recorridos, text="Preorden", command=self.mostrar_preorden).pack(side='left', padx=5, pady=5)
            ttk.Button(frame_recorridos, text="Postorden", command=self.mostrar_postorden).pack(side='left', padx=5, pady=5)
            ttk.Button(frame_recorridos, text="Mostrar Árbol", command=self.mostrar_arbol_texto).pack(side='left', padx=5, pady=5)
            
            # Área de texto para mostrar resultados
            self.text_area_arbol = scrolledtext.ScrolledText(self.ventana_arboles, width=60, height=15)
            self.text_area_arbol.pack(padx=10, pady=10, fill='both', expand=True)
            
            # Frame para visualización del árbol
            frame_visualizacion = ttk.LabelFrame(self.ventana_arboles, text="Visualización del Árbol")
            frame_visualizacion.pack(padx=10, pady=10, fill='both', expand=True)
            
            self.label_imagen_arbol = ttk.Label(frame_visualizacion)
            self.label_imagen_arbol.pack(padx=5, pady=5)
            
            # Insertar datos iniciales
            self.insertar_datos_iniciales()
        else:
            self.ventana_arboles.lift()

    def insertar_datos_iniciales(self):
        datos_iniciales = [
            ("JA", "JORGE AVILA", "Av. Reforma 10"),
            ("CM", "CARLA MORALES", "Calle Norte 456"),
            ("BT", "BERTHA TORRES", "Insurgentes 789"),
            ("AP", "ANDRES PEREZ", "Copilco 34"),
            ("RM", "RAUL MENA", "Venezuela 8"),
            ("ZD", "ZAIRA DELGADO", "Centro 24")
        ]
        
        for codigo, nombre, domicilio in datos_iniciales:
            self.arbol.insertar(codigo, nombre, domicilio)
        
        self.actualizar_visualizacion_arbol()

    def insertar_nodo_arbol(self):
        codigo = self.entry_codigo.get().strip().upper()
        nombre = self.entry_nombre.get().strip()
        domicilio = self.entry_domicilio.get().strip()
        
        if not codigo or not nombre or not domicilio:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        self.arbol.insertar(codigo, nombre, domicilio)
        self.actualizar_visualizacion_arbol()
        
        # Limpiar campos
        self.entry_codigo.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_domicilio.delete(0, tk.END)
        
        messagebox.showinfo("Éxito", "Nodo insertado correctamente")

    def mostrar_inorden(self):
        resultado = self.arbol.inorden()
        self.mostrar_resultado_arbol("Recorrido Inorden", resultado)

    def mostrar_preorden(self):
        resultado = self.arbol.preorden()
        self.mostrar_resultado_arbol("Recorrido Preorden", resultado)

    def mostrar_postorden(self):
        resultado = self.arbol.postorden()
        self.mostrar_resultado_arbol("Recorrido Postorden", resultado)

    def mostrar_arbol_texto(self):
        resultado = self.arbol.imprimir()
        self.mostrar_resultado_arbol("Estructura del Árbol", resultado)

    def mostrar_resultado_arbol(self, titulo, contenido):
        self.text_area_arbol.delete(1.0, tk.END)
        self.text_area_arbol.insert(tk.INSERT, f"{titulo}:\n\n")
        for linea in contenido:
            self.text_area_arbol.insert(tk.INSERT, linea + "\n")

    def actualizar_visualizacion_arbol(self):
        try:
            imagen_path = self.arbol.visualizar()
            imagen = Image.open(imagen_path)
            
            # Redimensionar manteniendo aspecto
            ancho, alto = imagen.size
            nuevo_ancho = 400
            nuevo_alto = int((nuevo_ancho / ancho) * alto)
            imagen = imagen.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)
            
            foto = ImageTk.PhotoImage(imagen)
            self.label_imagen_arbol.configure(image=foto)
            self.label_imagen_arbol.image = foto  # Mantener referencia
            
            # Eliminar archivos temporales
            os.remove(imagen_path)
            os.remove(imagen_path.replace('.png', ''))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar la visualización: {str(e)}")





    def agregar_salida_recursividad(self, texto):
        self.output_recursividad.config(state='normal')
        self.output_recursividad.insert(tk.END, texto + "\n")
        self.output_recursividad.config(state='disabled')
        self.output_recursividad.see(tk.END)
    def ejecutar_concurrencia(self):
        if self.ventana_comcurrencia is None or not self.ventana_comcurrencia.winfo_exists():
            self.ventana_comcurrencia = tk.Toplevel(self.root)
            self.ventana_comcurrencia.title("Simulación de Concurrencia - Dulcería CP")
            self.ventana_comcurrencia.geometry("800x600")
            
            frame = tk.Frame(self.ventana_comcurrencia)
            frame.pack(fill='both', expand=True, padx=20, pady=20)
            
            label = tk.Label(frame, text="Simulación de Concurrencia - Dulcería CP", font=('Arial', 14))
            label.pack(pady=10)
            
            # Área de salida con scroll
            self.output_concurrencia = scrolledtext.ScrolledText(frame, wrap=tk.WORD, 
                                                            width=80, height=25, 
                                                            font=('Consolas', 10))
            self.output_concurrencia.pack(fill='both', expand=True)
            
            # Frame para controles
            frame_controles = tk.Frame(frame)
            frame_controles.pack(fill='x', pady=10)
            
            lbl_clientes = tk.Label(frame_controles, text="Número de clientes:")
            lbl_clientes.pack(side='left')
            
            self.entry_clientes = tk.Entry(frame_controles, width=10)
            self.entry_clientes.pack(side='left', padx=5)
            self.entry_clientes.insert(0, "50")
            
            btn_iniciar = tk.Button(frame_controles, text="Iniciar Simulación", 
                                command=self.iniciar_simulacion_concurrencia)
            btn_iniciar.pack(side='left', padx=10)
            
            btn_limpiar = tk.Button(frame_controles, text="Limpiar", 
                                command=lambda: self.output_concurrencia.delete(1.0, tk.END))
            btn_limpiar.pack(side='left')
            
            # Mostrar código fuente
            self.mostrar_codigo_concurrencia()
        else:
            self.ventana_comcurrencia.lift()

    def iniciar_simulacion_concurrencia(self):
        try:
            total_clientes = int(self.entry_clientes.get())
            if total_clientes <= 0:
                messagebox.showerror("Error", "El número de clientes debe ser mayor que 0")
                return
                
            self.output_concurrencia.delete(1.0, tk.END)
            
            def output_callback(text):
                self.output_concurrencia.insert(tk.END, text + "\n")
                self.output_concurrencia.see(tk.END)
                self.output_concurrencia.update_idletasks()
            
            dulceria = DulceriaCP(output_callback)
            
            # Mostrar encabezado
            self.output_concurrencia.insert(tk.END, "DULCERIA CP - SIMULACIÓN DE CONCURRENCIA\n")
            self.output_concurrencia.insert(tk.END, f"Total de clientes: {total_clientes}\n")
            self.output_concurrencia.insert(tk.END, "="*50 + "\n")
            
            # Función para ejecutar la simulación en un hilo separado
            def ejecutar_simulacion():
                # Hilo de llegada de clientes
                productor = threading.Thread(target=dulceria.llegada_clientes, args=(total_clientes,))
                productor.start()

                # Hilos de cajas (6 cajas)
                cajas = [
                    threading.Thread(target=dulceria.caja, args=(i,))
                    for i in range(1, 7)
                ]

                for c in cajas:
                    c.start()

                productor.join()
                dulceria.cola_clientes.join()

                for c in cajas:
                    c.join()

                self.output_concurrencia.insert(tk.END, "\nTodos los clientes fueron atendidos\n")
                self.output_concurrencia.insert(tk.END, f"Total de clientes atendidos: {dulceria.atendidos}\n")
                self.output_concurrencia.see(tk.END)
            
            # Iniciar la simulación en un hilo separado
            threading.Thread(target=ejecutar_simulacion, daemon=True).start()
            
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido de clientes") 
    def mostrar_codigo_concurrencia(self):
        codigo = """class DulceriaCP:
    def __init__(self):
        self.cola_clientes = queue.Queue()
        self.lock = threading.Lock()
        self.sem = threading.Semaphore(4)
        self.atendidos = 0

    def llegada_clientes(self, total):
        for i in range(1, total + 1):
            time.sleep(random.uniform(0.5, 2))
            cliente = f"Cliente-{i}"
            self.cola_clientes.put(cliente)
            with self.lock:
                print(f" Llegó {cliente} (En cola: {self.cola_clientes.qsize()})")

    def caja(self, numero):
        while True:
            try:
                cliente = self.cola_clientes.get(timeout=2)
            except queue.Empty:
                break

            if not self.sem.acquire(timeout=1):
                with self.lock:
                    print(f"[Caja-{numero}] No pudo atender a {cliente} (timeout)")
                continue

            try:
                with self.lock:
                    print(f"[Caja-{numero}] Atendiendo a {cliente}")
                time.sleep(random.uniform(0.5, 1.0))  #Tiempo de atencion

                with self.lock:
                    self.atendidos += 1
                    print(f"[Caja-{numero}] Terminó con {cliente} | Total atendidos: {self.atendidos}")
            finally:
                self.sem.release()
                self.cola_clientes.task_done()

if __name__ == "__main__":
    dulceria = DulceriaCP()
    total_clientes = 50

    print("DULCERIA CP")
    # Hilo de clientes papu
    productor = threading.Thread(target=dulceria.llegada_clientes, args=(total_clientes,))
    productor.start()

    cajas = [
        threading.Thread(target=dulceria.caja, args=(i,))
        for i in range(1, 7)
    ]

    for c in cajas:
        c.start()

    productor.join()
    dulceria.cola_clientes.join()

    for c in cajas:
        c.join()

    print("\\nTodos los clientes fueron atendidos")
    print(f"Total de clientes atendidos: {dulceria.atendidos}")"""
        
        frame_codigo = tk.Frame(self.output_concurrencia.master)
        frame_codigo.pack(fill='x', pady=10)
        
        lbl_codigo = tk.Label(frame_codigo, text="Código Fuente:", font=('Arial', 10, 'bold'))
        lbl_codigo.pack(anchor='w')
        
        text_codigo = scrolledtext.ScrolledText(frame_codigo, wrap=tk.WORD, 
                                              width=80, height=15, 
                                              font=('Courier', 9), bg='#f0f0f0')
        text_codigo.pack(fill='x')
        text_codigo.insert(tk.END, codigo)
        text_codigo.config(state='disabled')
    
    def agregar_salida_concurrencia(self, texto):
        self.output_concurrencia.config(state='normal')
        self.output_concurrencia.insert(tk.END, texto + "\n")
        self.output_concurrencia.config(state='disabled')
        self.output_concurrencia.see(tk.END)
        
        # También mostrar en la salida estándar capturada
        print(texto)
    
    def limpiar_salida_concurrencia(self):
        self.output_concurrencia.config(state='normal')
        self.output_concurrencia.delete(1.0, tk.END)
        self.output_concurrencia.config(state='disabled')
        self.mystdout = StringIO()  # Limpiar el buffer de salida
    
    def ejecutar_concurrencia(self):
        # Crear ventana de selección
        ventana_seleccion = tk.Toplevel(self.root)
        ventana_seleccion.title("Seleccionar Simulación de Concurrencia")
        ventana_seleccion.geometry("400x250")
        
        label = tk.Label(ventana_seleccion, text="Seleccione el tipo de simulación:", font=('Arial', 12))
        label.pack(pady=20)
        
        btn_dulceria = tk.Button(ventana_seleccion, text="Dulcería CP (Colas)", 
                                command=self.mostrar_simulacion_dulceria,
                                font=('Arial', 12), bg='lightblue')
        btn_dulceria.pack(pady=10)
        
        btn_cine = tk.Button(ventana_seleccion, text="Taquillas de Cine", 
                            command=self.mostrar_simulacion_cine,
                            font=('Arial', 12), bg='lightgreen')
        btn_cine.pack(pady=10)
        
        btn_problemas = tk.Button(ventana_seleccion, text="Problemas de Concurrencia", 
                                command=self.mostrar_problemas_concurrencia,
                                font=('Arial', 12), bg='lightcoral')
        btn_problemas.pack(pady=10)

    def mostrar_simulacion_dulceria(self):
        if self.ventana_comcurrencia is None or not self.ventana_comcurrencia.winfo_exists():
            self.ventana_comcurrencia = tk.Toplevel(self.root)
            self.ventana_comcurrencia.title("Simulación de Concurrencia - Dulcería CP")
            self.ventana_comcurrencia.geometry("800x600")
            
            frame = tk.Frame(self.ventana_comcurrencia)
            frame.pack(fill='both', expand=True, padx=20, pady=20)
            
            label = tk.Label(frame, text="Simulación de Concurrencia - Dulcería CP", font=('Arial', 14))
            label.pack(pady=10)
            
            # Área de salida con scroll
            self.output_concurrencia = scrolledtext.ScrolledText(frame, wrap=tk.WORD, 
                                                            width=80, height=25, 
                                                            font=('Consolas', 10))
            self.output_concurrencia.pack(fill='both', expand=True)
            
            # Frame para controles
            frame_controles = tk.Frame(frame)
            frame_controles.pack(fill='x', pady=10)
            
            lbl_clientes = tk.Label(frame_controles, text="Número de clientes:")
            lbl_clientes.pack(side='left')
            
            self.entry_clientes = tk.Entry(frame_controles, width=10)
            self.entry_clientes.pack(side='left', padx=5)
            self.entry_clientes.insert(0, "50")
            
            btn_iniciar = tk.Button(frame_controles, text="Iniciar Simulación", 
                                command=self.iniciar_simulacion_concurrencia)
            btn_iniciar.pack(side='left', padx=10)
            
            btn_limpiar = tk.Button(frame_controles, text="Limpiar", 
                                command=lambda: self.output_concurrencia.delete(1.0, tk.END))
            btn_limpiar.pack(side='left')
            
            # Mostrar código fuente
            self.mostrar_codigo_concurrencia()
        else:
            self.ventana_comcurrencia.lift()

    def mostrar_problemas_concurrencia(self):
        if not hasattr(self, 'ventana_problemas_concurrencia') or not self.ventana_problemas_concurrencia.winfo_exists():
            self.ventana_problemas_concurrencia = tk.Toplevel(self.root)
            self.ventana_problemas_concurrencia.title("Problemas de Concurrencia")
            self.ventana_problemas_concurrencia.geometry("800x600")
            
            frame = tk.Frame(self.ventana_problemas_concurrencia)
            frame.pack(fill='both', expand=True, padx=20, pady=20)
            
            label = tk.Label(frame, text="Simulación de Problemas de Concurrencia", font=('Arial', 14))
            label.pack(pady=10)
            
            # Área de salida con scroll
            self.output_problemas = scrolledtext.ScrolledText(frame, wrap=tk.WORD, 
                                                         width=80, height=25, 
                                                         font=('Consolas', 10))
            self.output_problemas.pack(fill='both', expand=True)
            
            # Frame para controles
            frame_controles = tk.Frame(frame)
            frame_controles.pack(fill='x', pady=10)
            
            btn_carrera = tk.Button(frame_controles, text="Condición de Carrera", 
                                 command=self.simular_carrera,
                                 bg='lightcoral')
            btn_carrera.pack(side='left', padx=5)
            
            btn_deadlock = tk.Button(frame_controles, text="Deadlock", 
                                  command=self.simular_deadlock,
                                  bg='lightblue')
            btn_deadlock.pack(side='left', padx=5)
            
            btn_starvation = tk.Button(frame_controles, text="Starvation", 
                                    command=self.simular_starvation,
                                    bg='lightgreen')
            btn_starvation.pack(side='left', padx=5)
            
            btn_limpiar = tk.Button(frame_controles, text="Limpiar", 
                                 command=lambda: self.output_problemas.delete(1.0, tk.END))
            btn_limpiar.pack(side='left', padx=5)
            
            # Mostrar código fuente
            self.mostrar_codigo_problemas()
        else:
            self.ventana_problemas_concurrencia.lift()

    def simular_carrera(self):
        self.output_problemas.insert(tk.END, "Iniciando simulación de condición de carrera...\n")
        self.output_problemas.insert(tk.END, "20 clientes llegarán a 3 cajas simultáneamente\n\n")
        
        # Crear una instancia de DulceriaGUI para manejar la simulación
        self.dulceria_gui = DulceriaGUI()
        
        # Ejecutar la simulación en un hilo separado
        threading.Thread(target=self.dulceria_gui.simular_carrera, 
                        args=(self.output_problemas,), 
                        daemon=True).start()

    def simular_deadlock(self):
        self.output_problemas.insert(tk.END, "Iniciando simulación de deadlock...\n")
        self.output_problemas.insert(tk.END, "Dos cajas intentarán adquirir locks en orden inverso\n\n")
        
        self.dulceria_gui = DulceriaGUI()
        threading.Thread(target=self.dulceria_gui.simular_deadlock, 
                        args=(self.output_problemas,), 
                        daemon=True).start()

    def simular_starvation(self):
        self.output_problemas.insert(tk.END, "Iniciando simulación de starvation...\n")
        self.output_problemas.insert(tk.END, "Una caja con prioridad monopolizará el semáforo\n\n")
        
        self.dulceria_gui = DulceriaGUI()
        threading.Thread(target=self.dulceria_gui.simular_starvation, 
                        args=(self.output_problemas,), 
                        daemon=True).start()

    def mostrar_codigo_problemas(self):
        codigo = """class DulceriaGUI:
    def __init__(self):
        self.atendidos = 0
        self.lock = threading.Lock()
        self.sem = threading.Semaphore(1)
        self.cola = queue.Queue()

    def simular_carrera(self, text_widget):
        self.atendidos = 0
        for i in range(20):
            self.cola.put(f"Cliente {i+1}")

        def caja(num):
            while not self.cola.empty():
                try:
                    cliente = self.cola.get(timeout=1)
                    text_widget.insert(tk.END, f"Caja {num} atiende a {cliente}\\n")
                    time.sleep(random.uniform(0.1, 0.3))
                    with self.lock:
                        self.atendidos += 1
                except queue.Empty:
                    break

        for i in range(3):
            threading.Thread(target=caja, args=(i+1,)).start()

    def simular_deadlock(self, text_widget):
        lockA = threading.Lock()
        lockB = threading.Lock()

        def caja1():
            with lockA:
                time.sleep(0.1)
                with lockB:
                    text_widget.insert(tk.END, "Caja 1 logró ambos locks\\n")

        def caja2():
            with lockB:
                time.sleep(0.1)
                with lockA:
                    text_widget.insert(tk.END, "Caja 2 logró ambos locks\\n")

        threading.Thread(target=caja1).start()
        threading.Thread(target=caja2).start()

    def simular_starvation(self, text_widget):
        def prioridad():
            while True:
                with self.sem:
                    text_widget.insert(tk.END, "[PRIORIDAD] atendiendo...\\n")
                    time.sleep(0.1)

        def normal(nombre):
            while True:
                with self.sem:
                    text_widget.insert(tk.END, f"[{nombre}] atendiendo...\\n")
                    time.sleep(0.5)

        threading.Thread(target=prioridad, daemon=True).start()
        threading.Thread(target=normal, args=("Caja 2",), daemon=True).start()
        threading.Thread(target=normal, args=("Caja 3",), daemon=True).start()"""
        
        frame_codigo = tk.Frame(self.output_problemas.master)
        frame_codigo.pack(fill='x', pady=10)
        
        lbl_codigo = tk.Label(frame_codigo, text="Código Fuente:", font=('Arial', 10, 'bold'))
        lbl_codigo.pack(anchor='w')
        
        text_codigo = scrolledtext.ScrolledText(frame_codigo, wrap=tk.WORD, 
                                              width=80, height=15, 
                                              font=('Courier', 9), bg='#f0f0f0')
        text_codigo.pack(fill='x')
        text_codigo.insert(tk.END, codigo)
        text_codigo.config(state='disabled')
    def mostrar_simulacion_cine(self):
        if not hasattr(self, 'ventana_cine') or not self.ventana_cine.winfo_exists():
            self.ventana_cine = tk.Toplevel(self.root)
            self.ventana_cine.title("Simulación Concurrente de Taquillas de Cine")
            self.ventana_cine.geometry("1000x700")
            
            # Variables de estado
            self.taquillas_activas = 0
            self.max_taquillas = 5
            self.clientes_atendidos = 0
            self.ingresos_totales = 0.0
            self.simulacion_activa = False
            self.cola_clientes = queue.Queue()
            self.log_queue = queue.Queue()
            self.total_clientes_generados = 0
            self.clientes_a_generar = 0
            self.tiempo_entre_clientes = 1.0
            
            # Crear interfaz
            self.crear_interfaz_cine()
            
            # Hilo para actualizar la interfaz
            self.actualizar_interfaz_thread = threading.Thread(target=self.actualizar_interfaz_cine, daemon=True)
            self.actualizar_interfaz_thread.start()
        else:
            self.ventana_cine.lift()

    def crear_interfaz_cine(self):
        # Frame principal
        main_frame = ttk.Frame(self.ventana_cine, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Sección de configuración
        config_frame = ttk.LabelFrame(main_frame, text="Configuración de Simulación", padding="10")
        config_frame.pack(fill=tk.X, pady=5)
        
        # Control de cantidad de clientes
        ttk.Label(config_frame, text="Total de clientes a generar:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.clientes_entry = ttk.Entry(config_frame)
        self.clientes_entry.insert(0, "50")
        self.clientes_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Control de tiempo entre clientes
        ttk.Label(config_frame, text="Tiempo entre llegadas (segundos):").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.tiempo_entry = ttk.Entry(config_frame)
        self.tiempo_entry.insert(0, "1.0")
        self.tiempo_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Control de cantidad de taquillas
        ttk.Label(config_frame, text="Número de taquillas:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.taquillas_entry = ttk.Entry(config_frame)
        self.taquillas_entry.insert(0, "5")
        self.taquillas_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Sección de control
        control_frame = ttk.LabelFrame(main_frame, text="Control de Simulación", padding="10")
        control_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(control_frame, text="Iniciar Simulación", command=self.iniciar_simulacion_cine).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Detener Simulación", command=self.detener_simulacion_cine).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Agregar 10 clientes", command=lambda: self.agregar_clientes_cine(10)).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Reiniciar", command=self.reiniciar_simulacion_cine).pack(side=tk.RIGHT, padx=5)
        
        # Sección de estado
        estado_frame = ttk.LabelFrame(main_frame, text="Estado del Sistema", padding="10")
        estado_frame.pack(fill=tk.X, pady=5)
        
        self.taquillas_label = ttk.Label(estado_frame, text="Taquillas activas: 0/5")
        self.taquillas_label.pack(anchor=tk.W)
        
        self.clientes_label = ttk.Label(estado_frame, text="Clientes atendidos: 0")
        self.clientes_label.pack(anchor=tk.W)
        
        self.clientes_generados_label = ttk.Label(estado_frame, text="Clientes generados: 0/0")
        self.clientes_generados_label.pack(anchor=tk.W)
        
        self.ingresos_label = ttk.Label(estado_frame, text="Ingresos totales: $0.00")
        self.ingresos_label.pack(anchor=tk.W)
        
        # Sección de registro
        registro_frame = ttk.LabelFrame(main_frame, text="Registro de Eventos", padding="10")
        registro_frame.pack(fill=tk.BOTH, expand=True)
        
        self.registro_text = tk.Text(registro_frame, height=15, state=tk.DISABLED)
        self.registro_text.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(registro_frame, command=self.registro_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.registro_text.config(yscrollcommand=scrollbar.set)
        
        # Sección de estadísticas
        stats_frame = ttk.LabelFrame(main_frame, text="Estadísticas", padding="10")
        stats_frame.pack(fill=tk.X, pady=5)
        
        self.tiempo_promedio_label = ttk.Label(stats_frame, text="Tiempo promedio de atención: 0.00s")
        self.tiempo_promedio_label.pack(anchor=tk.W)
        
        self.clientes_espera_label = ttk.Label(stats_frame, text="Clientes en espera: 0")
        self.clientes_espera_label.pack(anchor=tk.W)
        
        self.tiempo_restante_label = ttk.Label(stats_frame, text="Tiempo estimado restante: 0.00s")
        self.tiempo_restante_label.pack(anchor=tk.W)

    def iniciar_simulacion_cine(self):
        if self.simulacion_activa:
            messagebox.showwarning("Advertencia", "La simulación ya está en ejecución.")
            return
        
        try:
            self.clientes_a_generar = int(self.clientes_entry.get())
            self.tiempo_entre_clientes = float(self.tiempo_entry.get())
            self.max_taquillas = int(self.taquillas_entry.get())
            
            if self.clientes_a_generar <= 0 or self.tiempo_entre_clientes <= 0 or self.max_taquillas <= 0:
                raise ValueError("Los valores deben ser mayores a cero")
                
        except ValueError as e:
            messagebox.showerror("Error", f"Valores inválidos: {str(e)}")
            return
        
        self.simulacion_activa = True
        self.taquillas_activas = 0
        self.clientes_atendidos = 0
        self.total_clientes_generados = 0
        self.ingresos_totales = 0.0
        
        # Limpiar la cola de clientes
        with self.cola_clientes.mutex:
            self.cola_clientes.queue.clear()
        
        # Limpiar el registro
        self.registro_text.config(state=tk.NORMAL)
        self.registro_text.delete(1.0, tk.END)
        self.registro_text.config(state=tk.DISABLED)
        
        # Iniciar hilo para generar clientes
        threading.Thread(target=self.generar_clientes_cine, daemon=True).start()
        
        # Iniciar taquillas
        for i in range(1, self.max_taquillas + 1):
            threading.Thread(target=self.atender_clientes_cine, args=(i,), daemon=True).start()
        
        self.log_evento_cine(f"Simulación iniciada con {self.max_taquillas} taquillas")
        self.log_evento_cine(f"Generando {self.clientes_a_generar} clientes con intervalo de {self.tiempo_entre_clientes}s")

    def detener_simulacion_cine(self):
        if not self.simulacion_activa:
            messagebox.showwarning("Advertencia", "La simulación no está en ejecución.")
            return
        
        self.simulacion_activa = False
        self.log_evento_cine("Simulación detenida por el usuario")

    def reiniciar_simulacion_cine(self):
        self.detener_simulacion_cine()
        time.sleep(0.5)  # Esperar a que los hilos se detengan
        self.iniciar_simulacion_cine()

    def agregar_clientes_cine(self, cantidad):
        if not self.simulacion_activa:
            messagebox.showwarning("Advertencia", "La simulación no está en ejecución.")
            return
        
        self.clientes_a_generar += cantidad
        self.log_evento_cine(f"Se agregaron {cantidad} clientes a la simulación (Total: {self.clientes_a_generar})")

    def generar_clientes_cine(self):
        while self.simulacion_activa and self.total_clientes_generados < self.clientes_a_generar:
            tiempo_espera = self.tiempo_entre_clientes
            time.sleep(tiempo_espera)
            
            if not self.simulacion_activa:
                break
                
            # Crear un nuevo cliente
            self.total_clientes_generados += 1
            cliente_id = self.total_clientes_generados
            boletos = random.randint(1, 5)
            tipo_boleto = random.choice(["General", "Niño", "Tercera Edad"])
            
            self.cola_clientes.put({
                'id': cliente_id,
                'boletos': boletos,
                'tipo': tipo_boleto,
                'hora_llegada': datetime.now()
            })
            
            self.log_evento_cine(f"Cliente {cliente_id} llegó a la cola (Boletos: {boletos}, Tipo: {tipo_boleto})")
        
        if self.total_clientes_generados >= self.clientes_a_generar:
            self.log_evento_cine(f"Se han generado todos los clientes programados ({self.clientes_a_generar})")

    def atender_clientes_cine(self, taquilla_id):
        while self.simulacion_activa:
            try:
                # Intentar obtener un cliente de la cola (con timeout para no bloquear indefinidamente)
                cliente = self.cola_clientes.get(timeout=1)
                
                self.taquillas_activas += 1
                self.log_evento_cine(f"[Taquilla-{taquilla_id}] Atendiendo a Cliente-{cliente['id']}")
                
                # Simular tiempo de atención
                tiempo_atencion = random.uniform(1.0, 3.0)
                time.sleep(tiempo_atencion)
                
                # Calcular costo
                if cliente['tipo'] == "General":
                    precio = 75.0
                elif cliente['tipo'] == "Niño":
                    precio = 50.0
                else:  # Tercera Edad
                    precio = 45.0
                
                costo_total = cliente['boletos'] * precio
                self.ingresos_totales += costo_total
                self.clientes_atendidos += 1
                
                # Registrar finalización
                tiempo_espera = (datetime.now() - cliente['hora_llegada']).total_seconds()
                self.log_evento_cine(
                    f"[Taquilla-{taquilla_id}] Terminó con Cliente-{cliente['id']} "
                    f"(Tiempo: {tiempo_espera:.2f}s, Costo: ${costo_total:.2f})"
                )
                
                self.taquillas_activas -= 1
                self.cola_clientes.task_done()
                
            except queue.Empty:
                # No hay clientes en la cola
                continue

    def log_evento_cine(self, mensaje):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_queue.put(f"[{timestamp}] {mensaje}")

    def actualizar_interfaz_cine(self):
        tiempos_atencion = []
        
        while True:
            # Actualizar estadísticas
            self.taquillas_label.config(text=f"Taquillas activas: {self.taquillas_activas}/{self.max_taquillas}")
            self.clientes_label.config(text=f"Clientes atendidos: {self.clientes_atendidos}")
            self.clientes_generados_label.config(text=f"Clientes generados: {self.total_clientes_generados}/{self.clientes_a_generar}")
            self.ingresos_label.config(text=f"Ingresos totales: ${self.ingresos_totales:.2f}")
            self.clientes_espera_label.config(text=f"Clientes en espera: {self.cola_clientes.qsize()}")
            
            # Calcular tiempo estimado restante
            if self.taquillas_activas > 0 and self.cola_clientes.qsize() > 0:
                tiempo_promedio_atencion = 2.0  # Valor promedio estimado
                clientes_restantes = self.clientes_a_generar - self.clientes_atendidos
                tiempo_restante = (clientes_restantes * tiempo_promedio_atencion) / self.max_taquillas
                self.tiempo_restante_label.config(text=f"Tiempo estimado restante: {tiempo_restante:.2f}s")
            
            # Procesar mensajes del log
            while not self.log_queue.empty():
                mensaje = self.log_queue.get()
                self.registro_text.config(state=tk.NORMAL)
                self.registro_text.insert(tk.END, mensaje + "\n")
                self.registro_text.config(state=tk.DISABLED)
                self.registro_text.see(tk.END)
            
            time.sleep(0.1)


"""
    # Métodos para grafos (senderismo)
    def inicializar_grafo_senderismo(self):
        import networkx as nx
        self.grafo_senderismo = nx.Graph()
        
        # Agregar nodos
        self.grafo_senderismo.add_node("Inicio", categoria="punto_partida")
        self.grafo_senderismo.add_node("P1-Princ", categoria="ruta_principiantes")
        self.grafo_senderismo.add_node("P2-Princ", categoria="ruta_principiantes")
        self.grafo_senderismo.add_node("Descanso-Princ", categoria="zona_descanso")
        self.grafo_senderismo.add_node("P3-Princ", categoria="ruta_principiantes")
        self.grafo_senderismo.add_node("Cascada-Princ", categoria="zona_cascada")
        self.grafo_senderismo.add_node("Mirador-Princ", categoria="punto_vista")
        self.grafo_senderismo.add_node("P1-Exp-Animal", categoria="ruta_experimentados")
        self.grafo_senderismo.add_node("Zona-Riesgo", categoria="ruta_peligrosa")
        self.grafo_senderismo.add_node("P2-Exp-Animal", categoria="ruta_experimentados")
        self.grafo_senderismo.add_node("P1-Exp-Risco", categoria="ruta_experimentados")
        self.grafo_senderismo.add_node("Zona-Rocosa", categoria="zona_rocosa")
        self.grafo_senderismo.add_node("P2-Exp-Risco", categoria="ruta_experimentados")
        
        # Agregar aristas (rutas)
        self.grafo_senderismo.add_edge("Inicio", "P1-Princ", weight=1.5, categoria="ruta_principiantes")
        self.grafo_senderismo.add_edge("P1-Princ", "P2-Princ", weight=1.5, categoria="ruta_principiantes")
        self.grafo_senderismo.add_edge("P2-Princ", "Descanso-Princ", weight=1.5, categoria="ruta_principiantes")
        self.grafo_senderismo.add_edge("Descanso-Princ", "P3-Princ", weight=1.5, categoria="ruta_principiantes")
        self.grafo_senderismo.add_edge("P3-Princ", "Cascada-Princ", weight=1.5, categoria="ruta_principiantes")
        self.grafo_senderismo.add_edge("Cascada-Princ", "Mirador-Princ", weight=1.5, categoria="ruta_principiantes")
        self.grafo_senderismo.add_edge("Inicio", "P1-Exp-Animal", weight=2.0, categoria="ruta_experimentados")
        self.grafo_senderismo.add_edge("P1-Exp-Animal", "Zona-Riesgo", weight=1.5, categoria="ruta_peligrosa")
        self.grafo_senderismo.add_edge("Zona-Riesgo", "P2-Exp-Animal", weight=1.8, categoria="ruta_peligrosa")
        self.grafo_senderismo.add_edge("P2-Exp-Animal", "Mirador-Princ", weight=2.2, categoria="ruta_experimentados")
        self.grafo_senderismo.add_edge("Inicio", "P1-Exp-Risco", weight=2.5, categoria="ruta_experimentados")
        self.grafo_senderismo.add_edge("P1-Exp-Risco", "Zona-Rocosa", weight=2.0, categoria="ruta_peligrosa")
        self.grafo_senderismo.add_edge("Zona-Rocosa", "P2-Exp-Risco", weight=1.5, categoria="zona_rocosa")
        self.grafo_senderismo.add_edge("P2-Exp-Risco", "Mirador-Princ", weight=3.0, categoria="ruta_experimentados")

    def mostrar_mapa_completo(self):
        try:
            import networkx as nx
            import matplotlib.pyplot as plt
            from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
            
            # Crear figura
            fig = plt.figure(figsize=(10, 8))
            
            # Definir colores según categoría
            color_map = {
                'punto_partida': 'blue',
                'ruta_principiantes': 'green',
                'ruta_experimentados': 'orange',
                'ruta_peligrosa': 'red',
                'zona_descanso': 'gray',
                'zona_cascada': 'cyan',
                'zona_rocosa': 'brown',
                'punto_vista': 'yellow'
            }
            
            # Asignar colores a los nodos
            node_colors = [color_map[self.grafo_senderismo.nodes[n]['categoria'] for n in self.grafo_senderismo.nodes()]]
            
            # Dibujar el grafo
            pos = nx.spring_layout(self.grafo_senderismo)
            nx.draw(self.grafo_senderismo, pos, with_labels=True, node_color=node_colors, node_size=800, font_size=8)
            
            # Mostrar distancias en las aristas
            edge_labels = nx.get_edge_attributes(self.grafo_senderismo, 'weight')
            nx.draw_networkx_edge_labels(self.grafo_senderismo, pos, edge_labels=edge_labels)
            
            plt.title("Mapa Completo de Senderismo")
            
            # Mostrar en una nueva ventana
            ventana_mapa = tk.Toplevel(self.ventana_rec_grafos)
            ventana_mapa.title("Mapa de Senderismo")
            
            canvas = FigureCanvasTkAgg(fig, master=ventana_mapa)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)
            
            # Crear leyenda
            leyenda = "\nLeyenda de colores:\n"
            for categoria, color in color_map.items():
                leyenda += f"{categoria.replace('_', ' ').title()}: {color}\n"
            
            self.agregar_salida_grafos(leyenda)
            
        except ImportError:
            self.agregar_salida_grafos("Error: Para visualizar el grafo, instale matplotlib y networkx")

    def mostrar_ruta_senderismo(self):
        nivel = self.nivel_experiencia.get()
        destino = self.destino_seleccionado.get()
        
        if nivel == "1":  # Principiante
            ruta = ["Inicio", "P1-Princ", "P2-Princ", "Descanso-Princ", "P3-Princ", "Cascada-Princ", "Mirador-Princ"]
            if destino == "Cascada-Princ":
                ruta = ruta[:5]
            elif destino == "Descanso-Princ":
                ruta = ruta[:4]
            
            self.agregar_salida_grafos(f"\nRuta para principiantes hacia {destino}:")
            self.agregar_salida_grafos(" → ".join(ruta))
            self.agregar_salida_grafos("\nPrecauciones:")
            self.agregar_salida_grafos("- Sigue las señales verdes")
            self.agregar_salida_grafos("- Evita desviarte del camino marcado")
            
        elif nivel == "2":  # Experimentado
            if destino == "Mirador-Princ":
                ruta = ["Inicio", "P1-Exp-Animal", "Zona-Riesgo", "P2-Exp-Animal", "Mirador-Princ"]
                self.agregar_salida_grafos(f"\nRuta para experimentados hacia {destino}:")
                self.agregar_salida_grafos(" → ".join(ruta))
                self.agregar_salida_grafos("\nPrecauciones:")
                self.agregar_salida_grafos("- Zona con avistamientos de osos")
                self.agregar_salida_grafos("- Mantente alerta")
            elif destino == "Zona-Rocosa":
                ruta = ["Inicio", "P1-Exp-Risco", "Zona-Rocosa"]
                self.agregar_salida_grafos(f"\nRuta para experimentados hacia {destino}:")
                self.agregar_salida_grafos(" → ".join(ruta))
                self.agregar_salida_grafos("\nPrecauciones:")
                self.agregar_salida_grafos("- Terreno escarpado")
                self.agregar_salida_grafos("- Usa calzado adecuado")
                
        elif nivel == "3":  # Avanzado
            if destino == "Mirador-Princ":
                ruta = ["Inicio", "P1-Exp-Risco", "Zona-Rocosa", "P2-Exp-Risco", "Mirador-Princ"]
                self.agregar_salida_grafos(f"\nRuta para avanzados hacia {destino}:")
                self.agregar_salida_grafos(" → ".join(ruta))
                self.agregar_salida_grafos("\nPrecauciones:")
                self.agregar_salida_grafos("- Zona muy peligrosa")
                self.agregar_salida_grafos("- No recomendado para personas con vértigo")
        
        # Calcular distancia total
        distancia = 0
        for i in range(len(ruta)-1):
            distancia += self.grafo_senderismo[ruta[i]][ruta[i+1]]['weight']
        
        self.agregar_salida_grafos(f"\nDistancia total: {distancia:.1f} km")
        self.agregar_salida_grafos(f"Tiempo estimado: {distancia*20:.0f} minutos (a 3 km/h)")

    def agregar_salida_grafos(self, texto):
        self.output_grafos.config(state='normal')
        self.output_grafos.insert(tk.END, texto + "\n")
        self.output_grafos.config(state='disabled')
        self.output_grafos.see(tk.END)
"""

class DulceriaCP:
    def __init__(self, output_callback=None):
        self.cola_clientes = queue.Queue()
        self.lock = threading.Lock()
        self.sem = threading.Semaphore(4)
        self.atendidos = 0
        self.output_callback = output_callback
    
    def print(self, text):
        """Método para mostrar texto en la salida designada"""
        if self.output_callback:
            self.output_callback(text)
        else:
            print(text)

    def llegada_clientes(self, total):
        for i in range(1, total + 1):
            time.sleep(random.uniform(0.5, 2))
            cliente = f"Cliente-{i}"
            self.cola_clientes.put(cliente)
            with self.lock:
                self.print(f" Llegó {cliente} (En cola: {self.cola_clientes.qsize()})")

    def caja(self, numero):
        while True:
            try:
                cliente = self.cola_clientes.get(timeout=2)
            except queue.Empty:
                break

            if not self.sem.acquire(timeout=1):
                with self.lock:
                    self.print(f"[Caja-{numero}] No pudo atender a {cliente} (timeout)")
                continue

            try:
                with self.lock:
                    self.print(f"[Caja-{numero}] Atendiendo a {cliente}")
                time.sleep(random.uniform(0.5, 1.0))  # Tiempo de atención

                with self.lock:
                    self.atendidos += 1
                    self.print(f"[Caja-{numero}] Terminó con {cliente} | Total atendidos: {self.atendidos}")
            finally:
                self.sem.release()
                self.cola_clientes.task_done()
class DulceriaGUI:
    def __init__(self):
        self.atendidos = 0
        self.lock = threading.Lock()
        self.sem = threading.Semaphore(1)
        self.cola = queue.Queue()

    def simular_carrera(self, text_widget):
        self.atendidos = 0
        for i in range(20):
            self.cola.put(f"Cliente {i+1}")

        def caja(num):
            while not self.cola.empty():
                try:
                    cliente = self.cola.get(timeout=1)
                    text_widget.insert(tk.END, f"Caja {num} atiende a {cliente}\n")
                    time.sleep(random.uniform(0.1, 0.3))
                    with self.lock:
                        self.atendidos += 1
                except queue.Empty:
                    break

        for i in range(3):
            threading.Thread(target=caja, args=(i+1,)).start()

    def simular_deadlock(self, text_widget):
        lockA = threading.Lock()
        lockB = threading.Lock()

        def caja1():
            with lockA:
                time.sleep(0.1)
                with lockB:
                    text_widget.insert(tk.END, "Caja 1 logró ambos locks\n")

        def caja2():
            with lockB:
                time.sleep(0.1)
                with lockA:
                    text_widget.insert(tk.END, "Caja 2 logró ambos locks\n")

        threading.Thread(target=caja1).start()
        threading.Thread(target=caja2).start()

    def simular_starvation(self, text_widget):
        def prioridad():
            while True:
                with self.sem:
                    text_widget.insert(tk.END, "[PRIORIDAD] atendiendo...\n")
                    time.sleep(0.1)

        def normal(nombre):
            while True:
                with self.sem:
                    text_widget.insert(tk.END, f"[{nombre}] atendiendo...\n")
                    time.sleep(0.5)

        threading.Thread(target=prioridad, daemon=True).start()
        threading.Thread(target=normal, args=("Caja 2",), daemon=True).start()
        threading.Thread(target=normal, args=("Caja 3",), daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = CuadernoEvidencias(root)
    root.mainloop()