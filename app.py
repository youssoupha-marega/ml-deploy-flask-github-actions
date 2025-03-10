from flask import Flask,  jsonify
from transformers import MgpstrProcessor, MgpstrForSceneTextRecognition
#from torch.nn.functional import relu

import torch
#import pkg_resources
import flask
import PIL
import transformers

print("Flask version:", flask.__version__)
print("Pillow version:", PIL.__version__)
print("Torch version:",torch.__version__)
print("Transformers version:",transformers.__version__)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! good 111'

if __name__ == '__main__':
    app.run()




#@app.route('/versions')
#def get_versions():
#    # Lire le fichier requirements.txt
#    with open("requirements.txt", "r") as f:
#        required_packages = [line.strip().split("==")[0] for line in f.readlines() if "==" in line]
#
#    # Récupérer les versions installées
#    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}#
#
#    # Filtrer uniquement les packages présents dans requirements.txt
#    filtered_versions = {pkg: installed_packages.get(pkg, "Not Installed") for pkg in required_packages}#
#
#    return jsonify(filtered_versions)

if __name__ == '__main__':
    app.run()
