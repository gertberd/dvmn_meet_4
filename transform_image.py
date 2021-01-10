import argparse
from PIL import Image


def crop_and_blend(image, one_side_coordinates, sides_coordinates, opacity) -> Image:
    one_side_cropped_image = image.crop(one_side_coordinates)
    sides_cropped_image = image.crop(sides_coordinates)
    return Image.blend(one_side_cropped_image, sides_cropped_image, opacity)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Стилизует картинку в стиле Энди Уорхола и сохраняет её в миниатюру заданного размера.')
    parser.add_argument(
        '--source',
        help="Исходное изображение (с расширением)",
        required=True)
    parser.add_argument(
        '--dest',
        default="result.jpg",
        help="Имя для миниатюры (с расширением) (по умолчанию - result.jpg)")
    parser.add_argument(
        '--opacity',
        default=0.2,
        type=float,
        help="Коэффициент прозрачности слоёв (по умолчанию - 0.2).")
    parser.add_argument(
        '--crop_coefficient',
        default=0.03,
        type=float,
        help='Коэффициент смещения цветовых каналов (по умолчанию - 0.03)')
    parser.add_argument(
        '--thumb_max_size',
        default=80,
        help='Максимальный размер стороны миниатюры в пикселях (по умолчанию - 80).')
    args = parser.parse_args()
    filename = args.source
    result_filename = args.dest
    crop_coefficient = args.crop_coefficient
    opacity = args.opacity
    thumbnail_max_size = args.thumb_max_size

    image = Image.open(filename).convert("RGB")
    red, green, blue = image.split()
    crop_size = round(image.width * crop_coefficient)

    left_crop_coordinates = (crop_size * 2, 0, image.width, image.height)
    right_crop_coordinates = (0, 0, image.width - crop_size * 2, image.height)
    sides_crop_coordinates = (crop_size, 0, image.width - crop_size, image.height)

    red = crop_and_blend(red, left_crop_coordinates, sides_crop_coordinates, opacity)
    blue = crop_and_blend(blue, right_crop_coordinates, sides_crop_coordinates, opacity)
    green = green.crop(sides_crop_coordinates)

    result_image = Image.merge("RGB", (red, green, blue))
    result_image.thumbnail((thumbnail_max_size, thumbnail_max_size))
    result_image.save(result_filename)
