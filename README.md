# Despliegue-mlops
1. Crear env: conda create -n deploy_mlops python=3.10
2. conda activate deploy_mlops
1. Instalar dependencias con: pip install -r requirements.txt
2. Iniciar la app de FastAPI en replit con: uvicorn main:app --reload
3. Iniciar la app de FastAPI en EC2 con: uvicorn main:app --host 0.0.0.0 --port 8000

Con el siguiente dataset https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset se hizo:   
1.Entendimiento de negocio:
- Definir objetivo de negocio según lo que usted considere que puede ser de mayor utilidad según los datos elegidos.
- Definir objetivo analítico.
2. Entendimiento de los datos:
- Análisis univariante, análisis bivariante o cualquier tipo de gráficas o transformación de datos que permitan entender a UN NIVEL MÍNIMO los datos, es decir, para efectos del taller, esta no es la parte más importante ni la que debe gastar más tiempo.
3. Preparación de datos:
- Transformaciones para variables de entrada
- Transformaciones para variable de salida.
- Igual que el punto anterior, hacer las transformaciones mínimas para poder hacer el entrenamiento, esta no es la parte más importa ni la que debe gastar más tiempo.
4. Modelación:
- Utilice por lo menos 3 modelos de ML. Uno de estos debe ser un método de ensamble (RandomForest, xgboost etc.).
- Haga una búsqueda de hiperparámetros para cada uno de los modelos usando Optuna y registrando cada una de las ejecuciones en un solo experimento con ML Flow.
5.Evaluación:
-Para el caso planteado, ¿Cuál es la métrica de desempeño de mayor importancia? ¿Por qué?
-Defina el mejor modelo.
6.Despliegue:
-Cree el pipeline del mejor modelo de manera que solo se le deben ingresar los datos de entrada sin transformaciones y este pueda contestar con la predicción correcta.
-Utilice FastAPI para crear un endpoint en el que se pueda llamar el pipeline creado y guarde los datos de las predicciones en el formato que usted desee en un bucket de S3. Se puede reutilizar un bucket que ya se tenga creado.
-Cree una instancia de EC2 desde cero.
-Instale miniconda3 o python de la manera que usted crea más conveniente.
-Levante el daemon para la app de FastAPI tal que se mantenga el servicio siempre arriba independiente de que la terminar esté abierta o no. Este archivo también se debe subir a GitHub. Tome una captura cuando se tenga el servicio corriendo, para esto puede usar systemctl status.
-Muestre que el endpoint en el servidor funciona usando un comando curl desde la terminal de su computador. Tome una captura de esto.
-Para cualquier otra configuración necesaria o realizada para que el proceso funcione correctamente no olvide tomar capturas de lo que se hizo en AWS.
