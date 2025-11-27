# Despliegue-mlops
1. Crear env: conda create -n deploy_mlops python=3.9
2. conda activate deploy_mlops
1. Instalar dependencias con: pip install -r requirements.txt
2. Iniciar la app de FastAPI en replit con: uvicorn main:app --reload
3. Iniciar la app de FastAPI en EC2 con: uvicorn app:app --host 0.0.0.0 --port 8000