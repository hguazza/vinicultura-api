from bs4 import BeautifulSoup
import httpx

url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04"
        

# Faz a requisição para a página
response = httpx.get(url, timeout=10)
soup = BeautifulSoup(response.content, "html.parser")
max_year_value = soup.select_one("table.tb_base.tb_header.no_print input.text_pesq")["max"]
min_year_value = soup.select_one("table.tb_base.tb_header.no_print input.text_pesq")["min"]


print(f"commercialization min year: {min_year_value}\n"
      f"commercialization max year: {max_year_value}")

