import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCS = []
DOCX_DOCS = []
TXT_DOCS = []
PDF_DOCS = []
XLSX_DOCS = []
PPTX_DOCS = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
ARCHIVES = []
OTHER = []



REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCS,
    'DOCX': DOCX_DOCS,
    'TXT': TXT_DOCS,
    'PDF': PDF_DOCS,
    'XLSX': XLSX_DOCS,
    'PPTX': PPTX_DOCS,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    # превращаем расширение файла в название паки jpg -> JPG
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        # если это папка, то добавляем ее в список Folders и переходим к следующему элементу папки
        if item.is_dir():
            # проверяем, чтоб папка не была той, в которую мы складываем уже файлы
            if item.name not in ('images', 'video', 'audio', 'documents', 'archives', 'OTHER'):
                FOLDERS.append(item)
                # сканируем эту вложенную папку - рекурсия
                scan(item)
            # перейти к следующему эдементу в сканируемой папке
            continue

        # Пошла работа с файлом

        ext = get_extension(item.name)  # взять расширение
        fullname = folder / item.name  # взять полный путь к файлу
        if not ext:  # если у файла нет расширения, добавить к неизвестным
            OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSIONS[ext]  # взять список куда положить полный путь к файлу
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                # если мы не регистрировали расширение файла в Register_extension, то добавить в другое
                UNKNOWN.add(ext)
                OTHER.append(fullname)


if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    print(f'Start in folder {folder_for_scan}')

    scan(Path(folder_for_scan))
    print(f'Images JPEG: {JPEG_IMAGES}')
    print(f'Images PNG: {PNG_IMAGES}')
    print(f'Images JPG: {JPG_IMAGES}')
    print(f'Images SVG: {SVG_IMAGES}')
    print(f'Video AVI: {AVI_VIDEO}')
    print(f'Video MP4: {MP4_VIDEO}')
    print(f'Video MOV: {MOV_VIDEO}')
    print(f'Video MKV: {MKV_VIDEO}')
    print(f'Documents DOC: {DOC_DOCS}')
    print(f'Documents DOCX: {DOCX_DOCS}')
    print(f'Documents TXT: {TXT_DOCS}')
    print(f'Documents PDF: {PDF_DOCS}')
    print(f'Documents XLSX: {XLSX_DOCS}')
    print(f'Documents PPTX: {PPTX_DOCS}')
    print(f'Audio MP3: {MP3_AUDIO}')
    print(f'Audio OGG: {OGG_AUDIO}')
    print(f'Audio WAV: {WAV_AUDIO}')
    print(f'Audio AMR: {AMR_AUDIO}')
    print(f'Archives: {ARCHIVES}')

    print(f'There are following types of files: {EXTENSIONS}')
    print(f'Unknown file types: {UNKNOWN}')

    print({FOLDERS})
