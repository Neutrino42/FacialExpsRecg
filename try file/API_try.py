import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_api_key='pBwT3fGN4RBkPGyHhlI5mauax570lg3tjjP68bCdT4jJ')

with open('./fruitbowl.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        parameters = json.dumps({
            'classifier_ids': ["food"]
        }))
print(json.dumps(classes, indent=2))