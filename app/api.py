from fastapi import FastAPI, File, UploadFile
import subprocess
import shutil

app = FastAPI()

@app.get('/')
def root():
    return {'estado': 'Funciona'}

@app.post("/predict_video")  # Cambiado a POST para manejar la carga de archivos
async def predict(file: UploadFile = File(...)):
    local_filename = "video_bonito.mp4"
    with open(local_filename, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Asegúrate de que la ruta al modelo y al archivo de entrada sean correctas
    test = subprocess.Popen(["python", "modelo/prediction.py"], stdout=subprocess.PIPE)
    output = test.communicate()[0]

    tiempos = []
    # Asegúrate de que la ruta al archivo tiempos_goles.txt sea la correcta
    with open('modelo/tiempos_goles.txt') as f:
        tiempos = [line.strip() for line in f.readlines()]

    return {'prediction': tiempos}
