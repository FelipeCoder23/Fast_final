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

    # Llamada al script de predicción
    test = subprocess.Popen(["python", "modelo/prediction.py", "--model=best.pt", "--input=video_bonito.mp4"], stdout=subprocess.PIPE)
    output = test.communicate()[0]

    tiempos = []
    with open('tiempos_goles.txt') as f:
        tiempos = [line.strip().split(':')[-1] for line in f.readlines()]

    return {'prediction': tiempos}
