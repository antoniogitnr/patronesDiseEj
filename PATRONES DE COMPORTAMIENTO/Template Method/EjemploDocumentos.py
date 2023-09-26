from abc import ABC, abstractmethod

class DocumentAnalyzer(ABC):
    """
    La clase abstracta DocumentAnalyzer define el método de plantilla analyze_document,
    que representa el algoritmo general para analizar un documento.
    """
    def analyze_document(self, document_path: str) -> None:
        self.open_document(document_path)
        self.extract_content()
        self.analyze_content()
        self.close_document()

    @abstractmethod
    def open_document(self, document_path: str) -> None:
        pass

    @abstractmethod
    def extract_content(self) -> None:
        pass

    @abstractmethod
    def analyze_content(self) -> None:
        pass

    @abstractmethod
    def close_document(self) -> None:
        pass

class PDFAnalyzer(DocumentAnalyzer):
    """
    La clase PDFAnalyzer implementa los pasos específicos para analizar un documento PDF.
    """
    def open_document(self, document_path: str) -> None:
        print(f"Abriendo el documento PDF en la ruta: {document_path}")

    def extract_content(self) -> None:
        print("Extrayendo el contenido del documento PDF")

    def analyze_content(self) -> None:
        print("Analizando el contenido del documento PDF")

    def close_document(self) -> None:
        print("Cerrando el documento PDF")

class DOCAnalyzer(DocumentAnalyzer):
    """
    La clase DOCAnalyzer implementa los pasos específicos para analizar un documento DOC.
    """
    def open_document(self, document_path: str) -> None:
        print(f"Abriendo el documento DOC en la ruta: {document_path}")

    def extract_content(self) -> None:
        print("Extrayendo el contenido del documento DOC")

    def analyze_content(self) -> None:
        print("Analizando el contenido del documento DOC")

    def close_document(self) -> None:
        print("Cerrando el documento DOC")

class CSVAnalyzer(DocumentAnalyzer):
    """
    La clase CSVAnalyzer implementa los pasos específicos para analizar un documento CSV.
    """
    def open_document(self, document_path: str) -> None:
        print(f"Abriendo el documento CSV en la ruta: {document_path}")

    def extract_content(self) -> None:
        print("Extrayendo el contenido del documento CSV")

    def analyze_content(self) -> None:
        print("Analizando el contenido del documento CSV")

    def close_document(self) -> None:
        print("Cerrando el documento CSV")

if __name__ == "__main__":
    print("Simulación del análisis de documentos en varios formatos:")
    
    pdf_analyzer = PDFAnalyzer()
    doc_analyzer = DOCAnalyzer()
    csv_analyzer = CSVAnalyzer()

    document_path = "ruta_del_documento"

    print("\nAnálisis de documento PDF:")
    pdf_analyzer.analyze_document(document_path)

    print("\nAnálisis de documento DOC:")
    doc_analyzer.analyze_document(document_path)

    print("\nAnálisis de documento CSV:")
    csv_analyzer.analyze_document(document_path)