from PIL import Image
from PIL import ImageDraw
import gradio as gr
import easyocr

def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image


def inference(img, lang):
    reader = easyocr.Reader(lang, model_storage_directory="/EasyOCR/models", user_network_directory="/EasyOCR/user_network")
    bounds = reader.readtext(img)
    im = Image.fromarray(img)
    draw_boxes(im, bounds)
    im.save('/EasyOCR/result.jpg')
    return ['/EasyOCR/result.jpg', bounds]


title = 'EasyOCR'
description = ('Gradio demo for EasyOCR. EasyOCR demo supports 80+ languages.To use it, simply upload your image and '
               'choose a language from the dropdown menu, or click one of the examples to load them. Read more at the'
               ' links below.')
article = ("<p style='text-align: center'><a href='https://www.jaided.ai/easyocr/'>Ready-to-use OCR with 80+ supported "
           "languages and all popular writing scripts including Latin, Chinese, Arabic, Devanagari, Cyrillic and "
           "etc.</a> | <a href='https://github.com/JaidedAI/EasyOCR'>Github Repo</a></p>")
examples = [
    ['examples/english.png', ['en']],
    ['examples/thai.jpg', ['th']],
    ['examples/french.jpg', ['fr', 'en']],
    ['examples/chinese.jpg', ['ch_sim', 'en']],
    ['examples/japanese.jpg', ['ja', 'en']],
    ['examples/korean.png', ['ko', 'en']]
    ]
css = ".output_image, .input_image {height: 40rem !important; width: 100% !important;}"
choices = [
    "abq",
    "ady",
    "af",
    "ang",
    "ar",
    "as",
    "ava",
    "az",
    "be",
    "bg",
    "bh",
    "bho",
    "bn",
    "bs",
    "ch_sim",
    "ch_tra",
    "che",
    "cs",
    "cy",
    "da",
    "dar",
    "de",
    "en",
    "es",
    "et",
    "fa",
    "fr",
    "ga",
    "gom",
    "hi",
    "hr",
    "hu",
    "id",
    "inh",
    "is",
    "it",
    "ja",
    "kbd",
    "kn",
    "ko",
    "ku",
    "la",
    "lbe",
    "lez",
    "lt",
    "lv",
    "mah",
    "mai",
    "mi",
    "mn",
    "mr",
    "ms",
    "mt",
    "ne",
    "new",
    "nl",
    "no",
    "oc",
    "pi",
    "pl",
    "pt",
    "ro",
    "ru",
    "rs_cyrillic",
    "rs_latin",
    "sck",
    "sk",
    "sl",
    "sq",
    "sv",
    "sw",
    "ta",
    "tab",
    "te",
    "th",
    "tjk",
    "tl",
    "tr",
    "ug",
    "uk",
    "ur",
    "uz",
    "vi"
]
gr.Interface(
    inference,
    [gr.Image(label='Input'), gr.CheckboxGroup(choices, type="value", label='language')],
    [gr.Image(label='Output'), gr.Dataframe(headers=['text', 'confidence'])],
    title=title,
    description=description,
    article=article,
    examples=examples,
    css=css
).launch(debug=True, server_port=8000, server_name="0.0.0.0")
