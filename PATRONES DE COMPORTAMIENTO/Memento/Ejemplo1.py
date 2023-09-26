class Editor:
    def __init__(self):
        self.content = ""

    def write(self, text):
        self.content += text

    def save(self):
        return EditorMemento(self.content)

    def restore(self, memento):
        self.content = memento.get_saved_content()

    def show_content(self):
        print(f"Editor content: {self.content}")


class EditorMemento:
    def __init__(self, content):
        self.saved_content = content

    def get_saved_content(self):
        return self.saved_content


class History:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]


# Uso del patrón Memento
editor = Editor()
history = History()

editor.write("Hola ")
editor.write("Mundo!")
editor.show_content()

# Guardar el estado actual del editor
memento = editor.save()
history.add_memento(memento)

editor.write(" Esto es un ejemplo.")
editor.show_content()

# Restaurar el estado anterior del editor
memento = history.get_memento(0)
editor.restore(memento)
editor.show_content()