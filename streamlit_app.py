import tkinter as tk

# Funciones del chatbot
def enviar_mensaje():
    mensaje = entrada_mensaje.get()
    if mensaje:
        chat_area.config(state="normal")
        chat_area.insert(tk.END, f"Tú: {mensaje}\n")
        chat_area.config(state="disabled")
        entrada_mensaje.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Chatbot")
ventana.configure(bg="#007bff")

# Área de chat
chat_area = tk.Text(ventana, wrap=tk.WORD, bg="#007bff", fg="white", font=("Arial", 12))
chat_area.pack(padx=10, pady=10, expand=True, fill="both")
chat_area.config(state="disabled")

# Barra de entrada
entrada_mensaje = tk.Entry(ventana, bg="white", fg="#007bff", font=("Arial", 12))
entrada_mensaje.pack(padx=10, pady=5)

# Botón de enviar
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje, bg="#007bff", fg="white", font=("Arial", 12))
boton_enviar.pack(pady=5)

ventana.mainloop()
