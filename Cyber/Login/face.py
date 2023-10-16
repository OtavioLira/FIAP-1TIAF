import face_recognition
import cv2

# Carregar a imagem da pessoa que queremos reconhecer
image = face_recognition.load_image_file("Login/Imagens_reconhecidas/otavio.jpg")
# Obter as codificações faciais para essa imagem
codificacao_pessoa = face_recognition.face_encodings(image)[0]

# Carregar uma imagem que queremos verificar
imagem_verificar = face_recognition.load_image_file("Login/Imagens_reconhecidas/grupo.jfif")
# Obter as codificações faciais para essa imagem
codificacoes_verificar = face_recognition.face_encodings(imagem_verificar)

# Verificar se alguma das codificações faciais na imagem para verificar corresponde à codificação facial da pessoa
for codificacao in codificacoes_verificar:
    resultados = face_recognition.compare_faces([codificacao_pessoa], codificacao)
    if resultados[0]:
        print("A pessoa está na imagem!")
        break
else:
    print("A pessoa NÃO está na imagem!")
