import json
import xml.etree.ElementTree as ET

# Interfaz común para leer datos
class DataReader:
    def read_data(self, filename):
        pass

# Adaptador para leer datos en formato JSON
class JsonReader:
    def read_json(self, filename):
        with open(filename) as file:
            data = json.load(file)
        return data

# Adaptador para leer datos en formato XML
class XmlReader:
    def read_xml(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        data = {}
        for child in root:
            data[child.tag] = child.text
        return data

# Adaptador que implementa la interfaz común utilizando el adaptador de JSON
class JsonAdapter(DataReader):
    def __init__(self, json_reader):
        self.json_reader = json_reader

    def read_data(self, filename):
        return self.json_reader.read_json(filename)

# Adaptador que implementa la interfaz común utilizando el adaptador de XML
class XmlAdapter(DataReader):
    def __init__(self, xml_reader):
        self.xml_reader = xml_reader

    def read_data(self, filename):
        return self.xml_reader.read_xml(filename)

# Función cliente que utiliza la interfaz común para leer datos
def client_code(reader, filename):
    data = reader.read_data(filename)
    print(data)

# Ejemplo de uso del patrón Adapter para leer datos en diferentes formatos
if __name__ == "__main__":
    # Crear adaptadores específicos para JSON y XML
    json_reader = JsonReader()
    xml_reader = XmlReader()

    # Crear adaptadores utilizando los adaptadores específicos
    json_adapter = JsonAdapter(json_reader)
    xml_adapter = XmlAdapter(xml_reader)

    # Utilizar los adaptadores para leer datos en diferentes formatos
    print("Leyendo datos en formato JSON:")
    client_code(json_adapter, "data.json")

    print("\nLeyendo datos en formato XML:")
    client_code(xml_adapter, "data.xml")