import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def guardar_grafico():
    plt.savefig("mi_grafico.png")

def reiniciar_datos():
    entry_pendiente.delete(0, tk.END)
    entry_ordenada.delete(0, tk.END)
    ax.clear()

    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.legend()

    canvas.draw()
    
def graficar():
    m = float(entry_pendiente.get())
    b = float(entry_ordenada.get())

    x = range(-10, 11)
    y = [m * xi + b for xi in x]

    ax.clear()
    ax.plot(x, y)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_title(f'Línea: y = {m}x + {b}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    canvas.draw()

root = tk.Tk()
root.title('Graficador de Líneas')

barra_menu = tk.Menu(root)

menu_archivo = tk.Menu(barra_menu, tearoff=False)
menu_archivo.add_command(label="Guardar gráfico", accelerator="Ctrl+G", command=guardar_grafico)
menu_archivo.add_command(label="Reiniciar datos", accelerator="Ctrl+R", command=reiniciar_datos)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", accelerator="Ctrl+Q", command=root.destroy)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

root.config(menu=barra_menu)

tk.Label(root, text='Pendiente (m):').grid(row=0, column=0)
entry_pendiente = tk.Entry(root)
entry_pendiente.grid(row=0, column=1)

tk.Label(root, text='Ordenada al origen (b):').grid(row=1, column=0)
entry_ordenada = tk.Entry(root)
entry_ordenada.grid(row=1, column=1)

btn_graficar = tk.Button(root, text='Graficar', command=graficar)
btn_graficar.grid(row=2, column=0, columnspan=2)

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=3, column=0, columnspan=2)

# Bucle principal
root.mainloop()




"""Crear un software que permita elegir la pendiente y la ordenada al origen para luego graficar una línea en un eje cartesiano:

1. **Importamos lo necesarios:**
2. **Creamos la interfaz gráfica con Tkinter:**
   - Creamos una ventana principal.
   - Agregamos etiquetas y cuadros de entrada para que el usuario pueda ingresar la pendiente y la ordenada al origen.
   - Agregamos un botón que, al hacer clic, llamará a una función para graficar.
3. **Manejar eventos y graficar:**
   - Esto crea una función que obtenga los valores de los cuadros de entrada, genere los datos para la línea y grafique usando Matplotlib.
4. **Ejecutamos la aplicación:**
   - Ejecutamos el script y probamos la aplicación. Ingresamos los valores para la pendiente y la ordenada al origen, luego hacemos clic en el botón para ver la línea graficada."""
