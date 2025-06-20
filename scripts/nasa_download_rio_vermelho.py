
import requests

'''
Import de Variáveis do NASA POWER

T2M: Temperatura média a 2 metros (°C)
RH2M: Umidade relativa (%)
PRECTOTCORR: Precipitação (mm/dia)
WS2M: Velocidade do vento (m/s)
ALLSKY_SFC_SW_DWN: Radiação solar (kWh/m²/dia)
'''

def download_nasa_rio_vermelho():
    """
    Baixa dados climáticos diários da NASA POWER para o bairro Rio Vermelho (Florianópolis),
    no período de 2020 a 2024, e salva em data/raw/nasa_rio_vermelho.csv.
    """
    latitude = -27.570
    longitude = -48.400
    start_date = '20200101'
    end_date = '20241231'
    variables = "T2M,RH2M,PRECTOTCORR,WS2M,ALLSKY_SFC_SW_DWN"
    community = "AG"

    url = (
        f"https://power.larc.nasa.gov/api/temporal/daily/point"
        f"?start={start_date}&end={end_date}"
        f"&latitude={latitude}&longitude={longitude}"
        f"&parameters={variables}"
        f"&community={community}"
        f"&format=CSV&user=laissa"
    )

    response = requests.get(url)

    output_path = "data/raw/nasa_rio_vermelho.csv"
    with open(output_path, "w") as f:
        f.write(response.text)

    print(f"✅ Dados salvos em: {output_path}")

if __name__ == "__main__":
    download_nasa_rio_vermelho()

