import os
import time
import __init__
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
import http.client, urllib.request, urllib.parse, urllib.error

IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "images")
headers = {
    # Request headers
    'Training-Key': __init__.SUBSCRIPTION_KEY_ENV_NAME,
    'Training-key': __init__.SUBSCRIPTION_KEY_ENV_NAME,
}

def train_project(subscription_key):

    trainer = CustomVisionTrainingClient(subscription_key, endpoint=__init__.ENDPOINT)

    # Create a new project
    print("Creating project...")
    print(__init__.SAMPLE_PROJECT_NAME)
    #project = trainer.create_project(name=__init__.SAMPLE_PROJECT_NAME, domain_id="0732100f-1a38-4e49-a514-c9b44c697ab5")
    project = trainer.create_project(name=__init__.SAMPLE_PROJECT_NAME)
    # Make two tags in the new project
    hemlock_tag = trainer.create_tag(project.id, "Hemlock")
    cherry_tag = trainer.create_tag(project.id, "Japanese Cherry")

    print("Adding images...")
    hemlock_dir = os.path.join(IMAGES_FOLDER, "Hemlock")
    for image in os.listdir(hemlock_dir):
        with open(os.path.join(hemlock_dir, image), mode="rb") as img_data: 
            trainer.create_images_from_data(project.id, img_data.read(), [ hemlock_tag.id ])
    
    cherry_dir = os.path.join(IMAGES_FOLDER, "Japanese Cherry")
    for image in os.listdir(cherry_dir):
        with open(os.path.join(cherry_dir, image), mode="rb") as img_data: 
            trainer.create_images_from_data(project.id, img_data.read(), [ cherry_tag.id ])

    print ("Training...")
    iteration = trainer.train_project(project.id)
    while (iteration.status == "Training"):
        iteration = trainer.get_iteration(project.id, iteration.id)
        print ("Training status: " + iteration.status)
        time.sleep(1)

    # The iteration is now trained. Make it the default project endpoint
    trainer.update_iteration(project.id, iteration.id, is_default=True)
    print("Training Done!")
    params = urllib.parse.urlencode({
    })
    print("Export model ...")
    try:
        conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
        conn.request("GET",
                     "/customvision/v2.2/Training/projects/{"+project.id+"}/iterations/{"+iteration.id+"}/export?%s" % params,
                     "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
        model_file = open("../models/plant.export", "wb")
        model_file.write(data)
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    return project

if __name__ == "__main__":
    import sys, os.path
    sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
    my_project = train_project(__init__.SUBSCRIPTION_KEY_ENV_NAME)

    trainer = CustomVisionTrainingClient(__init__.SUBSCRIPTION_KEY_ENV_NAME, endpoint=__init__.ENDPOINT)
    # trainer.delete_project(my_project.id)
    # from tools import execute_samples
    # execute_samples(globals(), SUBSCRIPTION_KEY_ENV_NAME)