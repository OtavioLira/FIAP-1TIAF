import face_recognition
from PIL import Image

# Carregar a imagem
image = face_recognition.load_image_file("caminho da imagem\imagem.jpg")

# Detectar as localizações das faces
face_locations = face_recognition.face_locations(image)

# Percorrer as localizações das faces
for face_location in face_locations:
    # Extrair as coordenadas da caixa delimitadora
    top, right, bottom, left = face_location
    
    # Recortar a imagem usando as coordenadas da caixa delimitadora
    face_image = image[top:bottom, left:right]

    # Converter o array numpy em uma imagem PIL
    pil_image = Image.fromarray(face_image)

    # Salvar a imagem recortada
    pil_image.save("caminho da imagem/imagem_recortada.jpg")
