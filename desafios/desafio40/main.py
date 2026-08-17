import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from typing import Any, Dict, List


# 1. Abstração (Interface)
class DataExporter(ABC):
    @abstractmethod
    def export(self, data: List[Dict[str, Any]]) -> str:
        """Exporta uma lista de dicionários para uma string formatada."""
        pass


# 2. Implementação JSON (usando json.dumps)
class JSONExporter(DataExporter):
    def export(self, data: List[Dict[str, Any]]) -> str:
        return json.dumps(data, indent=2, ensure_ascii=False)


# 3. Implementação XML (usando xml.etree.ElementTree)
class XMLExporter(DataExporter):
    def __init__(self, root_name: str = "data", item_name: str = "item"):
        self.root_name = root_name
        self.item_name = item_name

    def export(self, data: List[Dict[str, Any]]) -> str:
        root = ET.Element(self.root_name)

        for entry in data:
            item_elem = ET.SubElement(root, self.item_name)
            for key, val in entry.items():
                child = ET.SubElement(item_elem, key)
                child.text = str(val)

        # Formata a estrutura com indentação legível
        ET.indent(root, space="  ")
        return ET.tostring(root, encoding="unicode")


# 4. Classe de Serviço (Injeção de Dependência)
class ExportService:
    def __init__(self, exporter: DataExporter):
        self._exporter = exporter  # Dependência injetada

    def set_exporter(self, exporter: DataExporter) -> None:
        """Permite alterar o formato de exportação em tempo de execução."""
        self._exporter = exporter

    def process_export(self, data: List[Dict[str, Any]]) -> str:
        return self._exporter.export(data)


# --- Exemplo de Uso ---
if __name__ == "__main__":
    dados = [
        {"id": 1, "nome": "Notebook", "preco": 3500.00},
        {"id": 2, "nome": "Mouse", "preco": 150.50},
    ]

    # Injeção inicial com JSON
    service = ExportService(exporter=JSONExporter())
    print("--- EXPORTAÇÃO JSON ---")
    print(service.process_export(dados))

    # Alternando a dependência para XML
    service.set_exporter(XMLExporter(root_name="produtos", item_name="produto"))
    print("\n--- EXPORTAÇÃO XML ---")
    print(service.process_export(dados))