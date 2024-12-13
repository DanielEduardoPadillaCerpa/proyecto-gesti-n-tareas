import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurar la base de datos con SQLite
DATABASE_URL = "sqlite:///gestion_tareas.db"
engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

# Definir el modelo de la tabla de tareas
class Tarea(Base):
    __tablename__ = 'tareas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    descripcion = Column(String(250), nullable=False)
    completada = Column(Boolean, default=False)

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Clase de gestión de tareas
class TaskManager:
    def add_task(self, title, description):
        new_task = Tarea(titulo=title, descripcion=description)
        session.add(new_task)
        session.commit()

    def list_tasks(self):
        return session.query(Tarea).all()
    
    def complete_task(self, task_id):
        task = session.query(Tarea).filter_by(id=task_id).first()
        if task:
            task.completada = True
            session.commit()

    def delete_task(self, task_id):
        task = session.query(Tarea).filter_by(id=task_id).first()
        if task:
            session.delete(task)
            session.commit()

    def save_tasks(self, filename):
        tasks = self.list_tasks()
        tasks_json = [{"id": task.id, "titulo": task.titulo, "descripcion": task.descripcion, "completada": task.completada} for task in tasks]
        with open(filename, 'w') as file:
            json.dump(tasks_json, file)

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks = json.load(file)
                for task in tasks:
                    new_task = Tarea(titulo=task['titulo'], descripcion=task['descripcion'], completada=task['completada'])
                    session.add(new_task)
                session.commit()
        except FileNotFoundError:
            pass

# Clase de ventana de inicio de sesión
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("300x200")
        self.root.configure(bg="#003366")  # Azul oscuro
        self.root.resizable(False, False)  # Desactivar la opción de maximizar
        self.setup_ui()

    def setup_ui(self):
        self.label_username = ttk.Label(self.root, text="Usuario:", background="#003366", foreground="white", font=("Arial", 12, "bold"))
        self.label_username.pack(pady=5)
        self.entry_username = ttk.Entry(self.root)
        self.entry_username.pack(pady=5)

        self.label_password = ttk.Label(self.root, text="Contraseña:", background="#003366", foreground="white", font=("Arial", 12, "bold"))
        self.label_password.pack(pady=5)
        self.entry_password = ttk.Entry(self.root, show="*")
        self.entry_password.pack(pady=5)

        self.login_button = tk.Button(self.root, text="Iniciar Sesión", command=self.login, bg="#F44336", fg="white", font=("Arial", 10, "bold"))
        self.login_button.pack(pady=20)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if username == "Daniel" and password == "12345":
            self.root.destroy()
            self.open_task_app()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def open_task_app(self):
        task_root = tk.Tk()
        TaskApp(task_root)
        task_root.mainloop()

# Clase de la interfaz gráfica
class TaskApp:
    def __init__(self, root):
        self.manager = TaskManager()

        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("800x600")
        self.root.configure(bg="#f5f5f5")

        self.setup_ui()

    def setup_ui(self):
        # Encabezado
        self.header_frame = tk.Frame(self.root, bg="#0078D7")
        self.header_frame.pack(fill=tk.X)
        self.title_label = ttk.Label(self.header_frame, text="Gestión de Tareas", font=("Arial", 18, "bold"), foreground="white", background="#0078D7")
        self.title_label.pack(pady=10)

        # Campos de entrada
        self.input_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.input_frame.pack(pady=10)

        self.title_label = ttk.Label(self.input_frame, text="Título:")
        self.title_label.grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = ttk.Entry(self.input_frame, width=40)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        self.desc_label = ttk.Label(self.input_frame, text="Descripción:")
        self.desc_label.grid(row=1, column=0, padx=5, pady=5)
        self.desc_entry = ttk.Entry(self.input_frame, width=40)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botones principales
        self.button_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Agregar Tarea", bg="#4CAF50", fg="white", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.list_button = tk.Button(self.button_frame, text="Listar Tareas", bg="#2196F3", fg="white", command=self.update_task_list)
        self.list_button.grid(row=0, column=1, padx=5)

        self.save_button = tk.Button(self.button_frame, text="Guardar Tareas", bg="#FFC107", command=self.save_tasks)
        self.save_button.grid(row=0, column=2, padx=5)

        self.load_button = tk.Button(self.button_frame, text="Cargar Tareas", bg="#FF5722", fg="white", command=self.load_tasks)
        self.load_button.grid(row=0, column=3, padx=5)

        # Tabla de tareas
        self.tree_frame = tk.Frame(self.root)
        self.tree_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.tree_frame, columns=("#1", "#2", "#3", "#4"), show="headings")
        self.tree.heading("#1", text="Número")
        self.tree.heading("#2", text="Título")
        self.tree.heading("#3", text="Descripción")
        self.tree.heading("#4", text="Estado")

        self.tree.column("#1", width=50, anchor=tk.CENTER)
        self.tree.column("#2", width=200)
        self.tree.column("#3", width=300)
        self.tree.column("#4", width=100, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Botones secundarios
        self.action_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.action_frame.pack(pady=10)

        self.complete_button = tk.Button(self.action_frame, text="Completar Tarea", bg="#8BC34A", command=self.complete_task)
        self.complete_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(self.action_frame, text="Eliminar Tarea", bg="#F44336", fg="white", command=self.delete_task)
        self.delete_button.grid(row=0, column=1, padx=5)

    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get()
        if title and description:
            self.manager.add_task(title, description)
            self.update_task_list()
            self.title_entry.delete(0, tk.END)  # Vaciar campo de título
            self.desc_entry.delete(0, tk.END)  # Vaciar campo de descripción
        else:
            messagebox.showwarning("Error", "Debe ingresar un título y una descripción")

    def save_tasks(self):
        self.manager.save_tasks("tareas.json")
        messagebox.showinfo("Información", "Tareas guardadas exitosamente")

    def load_tasks(self):
        self.manager.load_tasks("tareas.json")
        self.update_task_list()

    def complete_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            task_id = int(self.tree.item(selected_item, "values")[0])
            self.manager.complete_task(task_id)
            self.update_task_list()
        else:
            messagebox.showwarning("Error", "Debe seleccionar una tarea")

    def delete_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            task_id = int(self.tree.item(selected_item, "values")[0])
            self.manager.delete_task(task_id)
            self.update_task_list()
        else:
            messagebox.showwarning("Error", "Debe seleccionar una tarea")

    def update_task_list(self):
        self.tree.delete(*self.tree.get_children())
        for task in self.manager.list_tasks():
            status = "Completada" if task.completada else "Pendiente"
            self.tree.insert("", tk.END, values=(task.id, task.titulo, task.descripcion, status))

# Ejecutar aplicativo
if __name__ == "__main__":
    login_root = tk.Tk()
    LoginWindow(login_root)
    login_root.mainloop()
