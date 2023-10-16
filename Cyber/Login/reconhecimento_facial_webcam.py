import face_recognition
import cv2
import numpy as np

# Pegar o fluxo de entrada (Webcam-0)
capturar_video = cv2.VideoCapture(0)

# Carregar um exemplo e aprender a reconhecer
otavio_exemplo = face_recognition.load_image_file("D:\Otávio\Documentos\Faculdade\Cyber\Login\otavio.jpg")
otavio_rosto_codificado = face_recognition.face_encodings(otavio_exemplo)[0]

# Carregar um segundo exemplo e aprender a reconhecer
grupo_exemplo = face_recognition.load_image_file("D:\Otávio\Documentos\Faculdade\Cyber\Login\grupo.jfif")
grupo_rosto_codificado = face_recognition.face_encodings(grupo_exemplo)[0]

# Criar uma lista de nomes para os rostos conhecidos
rostos_reconhecidos_codificado = [
    otavio_rosto_codificado,
    grupo_rosto_codificado
]
nomes_conhecidos = [
    "Otávio Lira Neves",
    "Alexandre"
]

# Iniciação de variaveis
rosto_posicao = []
rostos_codificados = []
nomes_rosto = []
processar_janela = []

while True:
    # Pegar um frame da Janela
    ret, janela = capturar_video.read()

    # Processe apenas todos os outros quadros de vídeo para economizar tempo
    if processar_janela:
        # Redimensione a janela do video para 1/4 do tamanho para um processamento de reconhecimento facial mais rapido
        frame_menor = cv2.resize(janela, (0, 0), fx=0.25, fy=0.25)

        # Converte a imagem das cores BGR (Se estiver usando o OpenCv) para as cores RGB (Se estiver usando o face_recognition)
        frame_meno_rgb = frame_menor[:, :, ::-1]

        # Encontre todos os rostos e os rostos codificados na janela atual
        rosto_posicao = face_recognition.face_locations(frame_meno_rgb)
        rostos_codificados = face_recognition.face_encodings(frame_meno_rgb, rosto_posicao)

        nome_rosto = []
        for rosto_codificado in rostos_codificados:
            # Verificar se o rosto bate com o rosto conhecido
            matches = face_recognition.compare_faces(rostos_reconhecidos_codificado, rostos_codificados)
            nome = "Unknown"

            rosto_distancia = face_recognition.face_distance(rostos_reconhecidos_codificado, rosto_codificado)
            melhor_indice = np.argmin(rosto_distancia)
            if matches[melhor_indice]:
                nome = nomes_conhecidos[melhor_indice]

            nomes_rosto.append(nome)
    processar_janela = not processar_janela

    # Mostrar Resultados
    for (topo, direita, baixo, esquerda), nome in zip(rosto_posicao, nomes_rosto):
        # Redimensionar
        topo *= 4
        direita *=4
        baixo *= 4
        esquerda *= 4

        # Desenhar uma caixa em volta do rosto
        cv2.rectangle(janela, (esquerda, topo), (direita, baixo), (0, 0, 255), 2)

        # Desenhar o nome em baixo do rosto
        cv2.rectangle(janela, (esquerda, baixo - 35), (direita, baixo), (0,0,255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(janela, nome, (esquerda + 6, baixo - 6), font, 1.0, (255, 255, 255), 1)

    # Mostrar o resultado da imagem
    cv2.imshow("Video", janela)
    
    # Aperte 'q' no teclado para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Solte o indentificador na webcam
    capturar_video.release()
    cv2.destroyAllWindows()