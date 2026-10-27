import tkinter as tk
from tkinter import messagebox

usuarios = {"admin": "1234", "cajero": "0000"}
clientes = {"C01": "Juan Perez", "C02": "Maria Lopez"}
productos = {
    "1": {"nombre": "Zapatos deportivos", "precio": 650.0},
    "2": {"nombre": "Mocasines", "precio": 850.0},
    "3": {"nombre": "Tenis", "precio": 500.0}
}
ventas_registradas = []

def iniciar_sesion():
    u = entrada_usuario.get()
    p = entrada_pass.get()
    if u in usuarios and usuarios[u] == p:
        ventana_login.destroy()
        abrir_menu()
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")

def abrir_menu():
    menu = tk.Tk()
    menu.title("Sistema de Tienda")
    menu.geometry("300x250")

    tk.Button(menu, text="Clientes", command=lambda: messagebox.showinfo("Clientes", str(clientes))).pack(pady=10)
    tk.Button(menu, text="Productos", command=lambda: messagebox.showinfo("Productos", str(productos))).pack(pady=10)
    tk.Button(menu, text="Punto de Venta", command=abrir_pos).pack(pady=10)
    menu.mainloop()

def abrir_pos():
    pos = tk.Toplevel()
    pos.title("Punto de Venta")
    pos.geometry("300x350")
    
    tk.Label(pos, text="Código del Producto:").pack(pady=5)
    entrada_prod = tk.Entry(pos)
    entrada_prod.pack(pady=5)
    
    tk.Label(pos, text="Cantidad:").pack(pady=5)
    entrada_cant = tk.Entry(pos)
    entrada_cant.pack(pady=5)
    
    carrito = []
    
    def agregar():
        codigo = entrada_prod.get()
        if codigo in productos:
            try:
                cant = int(entrada_cant.get())
                precio = productos[codigo]["precio"]
                carrito.append({
                    "prod": productos[codigo]["nombre"],
                    "cant": cant,
                    "precio": precio,
                    "importe": cant * precio
                })
                messagebox.showinfo("Éxito", "Agregado al carrito")
                entrada_prod.delete(0, tk.END)
                entrada_cant.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Cantidad inválida")
        else:
            messagebox.showerror("Error", "Código no existe")
            
    def cobrar():
        if not carrito: return
        subtotal = sum(item["importe"] for item in carrito)
        iva = subtotal * 0.16
        total = subtotal + iva
        
        ticket = "--- TICKET ---\n\n"
        for item in carrito:
            ticket += f"{item['prod']} (x{item['cant']}) - ${item['importe']:.2f}\n"
        
        ticket += "\n--------------\n"
        ticket += f"Subtotal: ${subtotal:.2f}\n"
        ticket += f"IVA (16%): ${iva:.2f}\n"
        ticket += f"Total: ${total:.2f}\n"
        
        messagebox.showinfo("Venta Exitosa", ticket)
        ventas_registradas.append(ticket)
        pos.destroy()

    tk.Button(pos, text="Agregar al ticket", command=agregar).pack(pady=10)
    tk.Button(pos, text="Cobrar e Imprimir", command=cobrar).pack(pady=10)

ventana_login = tk.Tk()
ventana_login.title("Login")
ventana_login.geometry("250x200")

tk.Label(ventana_login, text="Usuario:").pack(pady=5)
entrada_usuario = tk.Entry(ventana_login)
entrada_usuario.pack(pady=5)

tk.Label(ventana_login, text="Contraseña:").pack(pady=5)
entrada_pass = tk.Entry(ventana_login, show="*")
entrada_pass.pack(pady=5)

tk.Button(ventana_login, text="Entrar", command=iniciar_sesion).pack(pady=15)
ventana_login.mainloop()