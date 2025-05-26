import requests
from bs4 import BeautifulSoup
from typing import Any, List, Dict
import pandas as pd
from app.schemas.schema import Processing, ProcessingResponse
from app.services.extractions.base import BaseExtraction

class ProcessingExtractor(BaseExtraction):

    def __init__(self) -> None:
        pass


    def fetch_data(self, year: int) -> List[Dict[str, str]]:
        
        extracted_data: List[Dict[str, str]] = []
        processings = []
        urls = [
            f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}opcao=opt_03",
            f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_03&subopcao=subopt_02",
            f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_03&subopcao=subopt_03",
        ]

        for url in urls:
        # Faz a requisição para a página
            response = requests.get(url)
            if response.status_code == 200:
                # Parseia o conteúdo HTML da resposta
                soup = BeautifulSoup(response.content, "html.parser")

                # Encontra a tabela na página
                table = soup.find("table", class_="tb_base tb_dados")
                if not table:
                    print(f"Nenhuma tabela encontrada em {url}")
                    return

                # Extrai os cabeçalhos da tabela
                headers = [header.text.strip() for header in table.find("thead").find_all("th")]

                # Inicializa uma lista para armazenar os dados
                table_data = []

                # Extrai as linhas da tabela
                for row in table.find("tbody").find_all("tr"):
                    cols = row.find_all("td")
                    if cols:
                        cols = [ele.text.strip() for ele in cols]
                        table_data.append(dict(zip(headers, cols)))

                extracted_data = table_data
                extracted_data = self.normalize(extracted_data, url)
                for item in extracted_data:
                    processing = Processing(
                        product=item['product'],
                        quantity=item['quantity'],
                        product_type=item['product_type'],
                        classification=item['classification']
                )   
                    processings.append(processing)
            else:
                print(f"Erro ao acessar {url}")
                
        return ProcessingResponse(processings=processings)
        

    def normalize(self, data: List[dict[str, str]], *args: Any) -> List[dict[str, str]]:
        url = args[0]
        normalized: List[dict[str, str]] = []
        product_type = None

        for item in data:
            product = item["Cultivar"] if "Cultivar" in item else item["Sem definição"]
            if product.isupper():
                product_type = product
            else:
                normalized_item = {
                    "product": product,
                    "quantity": item["Quantidade (Kg)"],
                    "type": product_type,
                    "classification": self.get_classification(url),
                }
                normalized.append(normalized_item)

        return normalized

    def get_classification(self, url: str) -> str:
        sub_option = url.split("subopcao=")[1].split("&")[0]
        classifications = {
            "subopt_01": "Viníferas",
            "subopt_02": "Americanas e Híbridas",
            "subopt_03": "Uvas de mesa",
            "subopt_04": "Sem classificação",
        }
        return classifications[sub_option]
    


if __name__ == "__main__":

    year = 2023
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_04"

    data = web_data_extractor(url)
    for i in range(5):
        print(f"data: {data[i]}, type: {type(data[i])}")
    df = pd.DataFrame(data)
    print(df.head())
    # print(f"data: {data[0]}, type: {type(data[0])}")