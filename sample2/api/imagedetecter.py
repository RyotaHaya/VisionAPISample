from google.cloud import vision

client = vision.ImageAnnotatorClient()


def detect_lable(uri):
    image = vision.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    res = []
    for label in labels:
        print(label.description)
        res.append({
            "name": label.description,
            "score": format(label.score, '.3f')
        })

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return res


def detect_object(uri):
    image = vision.Image()
    image.source.image_uri = uri

    objects = client.object_localization(
        image=image).localized_object_annotations

    res = []
    for object_ in objects:
        res.append({
            "name": object_.name,
            "score": format(object_.score, '.3f')
        })
    return res


def detect_text(uri):
    res_text = ""
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        res_text = '\n"{}"'.format(text.description)
        break

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return res_text
