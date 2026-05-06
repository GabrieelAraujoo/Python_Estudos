"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

"""

velocidade = 61  # velocidade atual do carro
posicao  = 101  # local em que o carro está na estrada

LIMITE_RADAR_1  = 60  # velocidade máxima do radar 1
POSICAO_RADAR_1  = 100  # local onde o radar 1 está
ALCANCE_RADAR  = 1  # A distância onde o radar pega

passou_velocidade_radar_1 = velocidade > LIMITE_RADAR_1

passou_pelo_radar_1 = (posicao >= (POSICAO_RADAR_1 - ALCANCE_RADAR) and posicao <= (POSICAO_RADAR_1 + ALCANCE_RADAR))

foi_multado_radar_1 = passou_pelo_radar_1 and passou_velocidade_radar_1

if passou_velocidade_radar_1:
    print('passou da velocidade no radar 1')

if passou_pelo_radar_1:
    print('passou pelo radar 1')

if foi_multado_radar_1:
    print('foi multado no radar 1')