# Утилита стилизации изображений.

Стилизует картинку в стиле Энди Уорхола и сохраняет её в миниатюру заданного размера.

## Установка

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
## Использование

```
usage: transform_image.py [-h] --source SOURCE [--dest DEST] [--opacity OPACITY] [--crop_coefficient CROP_COEFFICIENT] [--thumb_max_size THUMB_MAX_SIZE]

Стилизует картинку в стиле Энди Уорхола и сохраняет её в миниатюру заданного размера.

optional arguments:
  -h, --help            show this help message and exit
  --source SOURCE       Исходное изображение (с расширением)
  --dest DEST           Имя для миниатюры (с расширением) (по умолчанию - result.jpg)
  --opacity OPACITY     Коэффициент прозрачности слоёв (по умолчанию - 0.2).
  --crop_coefficient CROP_COEFFICIENT
                        Коэффициент смещения цветовых каналов (по умолчанию - 0.03)
  --thumb_max_size THUMB_MAX_SIZE
                        Максимальный размер стороны миниатюры в пикселях (по умолчанию - 80).
```
Пример:
```
python transform_image.py --source avatar.jpg --dest thumbnail_avatar.jpg --opacity 0.1 --crop_coefficient 0.05 --thubm_max_size 100
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
