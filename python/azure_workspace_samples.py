# Project Workspace created once

import __init__
import os
from azureml.core import Workspace
from azureml.core.model import Model

MODEL_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "models")
MODEL_NAME = "plant"
MODEL_FILE_NAME = MODEL_FOLDER + "\mydemomodel.TensorFlow.zip"
# ws = Workspace.create(name='plant', subscription_id='f8cdef31-a31e-4b4a-93e4-5f571e91255a',
# ws = Workspace.create(name='plant', subscription_id='47858321-923d-4b6f-9a3f-4a5aa2299dd4',

#ws = Workspace.create(name=MODEL_NAME, subscription_id=__init__.azure_subscription_id,
#                      resource_group=__init__.azure_resource_group, create_resource_group=False,
#                      location=__init__.azure_location)
ws = Workspace(subscription_id=__init__.azure_subscription_id, resource_group=__init__.azure_resource_group, workspace_name=MODEL_NAME)
ws_obj = ws.get(name=MODEL_NAME, subscription_id=__init__.azure_subscription_id, resource_group=__init__.azure_resource_group)
print("Model File:", MODEL_FILE_NAME)
md = Model.register(ws, model_path=MODEL_FILE_NAME, model_name=MODEL_NAME)

print ("Register Model Done!")