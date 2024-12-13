from pathlib import Path
from django.conf import settings
from PIL import Image

def resize_image(image_django, new_width=16, new_height=16, optimize=True, quality=60):
    """
    Redimensiona uma imagem carregada via Django para o tamanho especificado (padrão: 16x16 pixels).

    :param image_django: Instância de arquivo de imagem do Django.
    :param new_width: Largura da imagem final. Padrão: 48 pixels.
    :param new_height: Altura da imagem final. Padrão: 48 pixels.
    :param optimize: Se True, otimiza a imagem ao salvar. Padrão: True.
    :param quality: Qualidade da imagem ao salvar (0-100). Padrão: 60.
    :return: Objeto da imagem redimensionada.
    """
    try:
        image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()
        image_pillow = Image.open(image_path)
        original_width, original_height = image_pillow.size

        if original_width <= new_width and original_height <= new_height:
            image_pillow.close()
            print("Imagem já está no tamanho apropriado.")
            return image_pillow

        new_image = image_pillow.resize((new_width, new_height), Image.Resampling.LANCZOS)
        new_image.save(
            image_path, format='PNG', optimize=optimize, quality=quality
        )
        print(f"Imagem redimensionada salva em: {image_path}")
        return new_image
    except Exception as e:
        print(f"Erro ao redimensionar a imagem: {e}")
        return None

# Exemplo de uso
# resize_image(imagem_carregada_django, new_width=48, new_height=48)

#Outra Função com o mesmo objetivo:
# def resize_image(image_django, new_width=800, optmize=True, quality=60):
#     image_path=Path(settings.MEDIA_ROOT / image_django.name).resolve()
#     image_pillow = Image.open(image_path)
#     original_width, original_height = image_pillow.size

#     if original_width <= new_width:
#         image_pillow.close()
#         return image_pillow
#     new_height = round(new_width * original_height / original_width)
#     new_image = image_pillow.resize((new_width, new_height), Image.ANTIALIAS)
#     new_image.save(
#         image_path, optmize=optmize, quality=quality
#     )
#     return new_image
