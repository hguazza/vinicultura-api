import requests
from app.schemas.schema import Commercialization, CommercializationResponse
from app.services.extractions.base import BaseExtraction
import httpx
from bs4 import BeautifulSoup
from typing import Any, List, Dict
import pandas as pd


class CommercializationExtractor(BaseExtraction):
    """
    Class to extract data from the Embrapa VitiBrasil website.
    """
    def __init__(self) -> None:
        pass


    def fetch_data(self, year: int) -> List[dict[str, str]]:

        extracted_data: List[Dict[str, str]] = []
        commercializations = []
        url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_04"    

        # Faz a requisição para a página
        response = httpx.get(url, timeout=10)
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

            extracted_data = self.normalize(extracted_data)
            for item in extracted_data:
                commercialization = Commercialization(
                    product=item['product'],
                    quantity=item['quantity'],
                    product_type=item['product_type']
                )
                commercializations.append(commercialization)
        else:
            print(f"Erro ao acessar {url}")

        return CommercializationResponse(commercializations=commercializations)
    
    def normalize(self, data: List[dict[str, str]], *args: Any) -> List[dict[str, str]]:
        """
        Normalize the data extracted from the source.
        """
        normalized: List[dict[str, str]] = []   
        product_type = None
        for item in data:
            if item['Produto'].isupper(): #define product type
                product_type = item['Produto']
            else: 
                normalized_item = {
                    'product': item['Produto'],
                    'quantity': int(item['Quantidade (L.)'].replace('.', '')) if item['Quantidade (L.)'] not in ['-', '*'] else 0,
                    'product_type': product_type
                }
                normalized.append(normalized_item)
        return normalized


# test extractor
if __name__ == "__main__":

    year = 2023

    extractor = CommercializationExtractor()
    data = extractor.fetch_data(year)
    for i in range(5):
        print(f"data: {data[i]}, type: {type(data[i])}")
    df = pd.DataFrame(data)
    print(df.head())
    # print(f"data: {data[0]}, type: {type(data[0])}")