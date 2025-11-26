# Proyecto de prueba
Este proyecto solo es con fines academicos. 
Se utilizaron librerías como fastapi, pydantic, starlette y pytest.

En este proyecto se buscar ejecutar pruebas SCA, SAST, PU, Contruir la imagen y correr el servicio con K8S.
## Ejecución

### instalación de dependencias
Correr el siguiente comando
```
pip install -r requirements.tx
```

### Ejecutar servicio
Correr el servicio con uvicorn desde la carpeta `/app`

```
uvicorn main:app --host 0.0.0.0 --port 8083
```

### Ejecutar pruebas

```
pytest
```

## Probar api
Primero debe hacer el login para obtener el token.

```
curl -X POST 
\-H "Content-Type: application/json"
\-d '{"username": "admin", "password": "devopsapitest"}'
\http://localhost:8083/login
```
Ejemplo de la respuesta:
```
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiJ9.1_CnC0KDu_wyKv8boyG2sT5phlUvhA5DVg4BtsbM3rg",
    "token_type": "Bearer"
}
```

Luego puede ejecutar el servicio teniendo en cuenta los valores del api-key y el token.
```
curl -X POST 
\-H "X-Parse-REST-API-Key: ${API_KEY}"
\-H "X-JWT-KWY: ${JWT_TOKEN}"
\-H "Content-Type: application/json"
\-d '{ "message" : "This is a test", "to": "Juan Perez", "from": "Rita Asturia", "timeToLifeSec" : 45 }'
\http://localhost:8083/DevOps
```

Ejemplo de la respuesta:
```
{
    "message": "Hello Juan Felipe, your message will be send"
}
```

## Ejecución con kubernete minikube
```
minikube image build . -t my-devops-api

kubectl apply -f deployment.yaml

kubectl rollout restart deployment devops-api
```

## Ejecución automática
### Requisitos
- Tener una organización en Azure DevOps.
- Configurar grupo de variables secret con api-key, jwt-secret, jwt-algorithm y snyk-org.
- Configurar servicios de conexión para SonarQube Cloud y Snyk.
- Configurar el agente donde se ejecutará el servicio.

### Pasos en Azure DevOps
- Acceder a la organización
- Ubicarse en Azure DevOps Pipeline
- Crear un nuevo pipeline
- Seleccionar la opción de GitHub
- Seleccionar la opción de pipeline exitente
- Seleccionar el archivo azure-pipeline.yml
- Ejecutar el proceso para autorizar el uso de diferentes recursos.