# Reddit Data Engineering Pipeline

## Descripción

Este proyecto es un pipeline de ingeniería de datos diseñado para extraer datos de Reddit, procesarlos y almacenarlos en Amazon S3 utilizando Apache Airflow y AWS Glue. El pipeline está configurado para ejecutarse automáticamente y puede ser utilizado para análisis y reportes de datos.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Configuración](#configuración)
  - [Configuración Local](#configuración-local)
  - [Configuración con Docker](#configuración-con-docker)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Agradecimientos](#agradecimientos)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Características

- Extracción de datos desde Reddit utilizando PRAW (Python Reddit API Wrapper).
- Almacenamiento de datos en Amazon S3.
- Transformación y procesamiento de datos usando AWS Glue.
- Gestión y orquestación del pipeline mediante Apache Airflow.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado:

- Python 3.9 o superior
- Apache Airflow 2.7.2
- Docker y Docker Compose
- AWS CLI configurado con credenciales válidas
- Otros requisitos de Python listados en `requirements.txt`

## Configuración

### Configuración Local

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/apatinor/RedditAirflowAWS-DataEngineering.git
   cd reddit-data-engineering-pipeline

2. **Crear el entorno virtual y activar**

    ```bash 
    python -m venv venv
    source venv/bin/activate   # En Windows: venv\Scripts\activate

3. **Instalar las dependencias**

    ```bash
   pip install -r requirements.txt
   
4. **Configurar el archivo de entorno de Airflow:**

    Asegúrate de que airflow.env está correctamente configurado con las variables necesarias para tu entorno.


5. **Configurar el AWS CLI**

    ```bash
   aws configure

6. **Ajustar la configuración**

    ```bash
   cp config/config-example.conf config/config.conf

7. **Construir y levantar el Docker**

    ```bash
   docker-compose up --build

8. **Acceder a la interfaz web de Airflow con los datos establecidos en el docker-compose.yml**

    [http://localhost:8080](http://localhost:8080)
    

9. **Ejecutar el DAG de Reddit:**

    Activa el DAG reddit_dag desde la interfaz web de Airflow.


## Estructura del Proyecto

```plaintext
.
├── config
│   ├── config-example.conf
├── dags
│   ├── reddit_dag.py
├── data
│   ├── input
│   ├── output
├── etls
│   ├── aws_etl.py
│   ├── reddit_etl.py    
├── logs
├── pipelines
│   ├── aws_s3_pipeline.py
│   ├── reddit_pipeline.py
├── plugins
├── tests
├── utils
│   ├── constants.py
├── .gitignore
├── airflow.env    
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```

# Agradecimientos
Este proyecto fue inspirado por el tutorial [Reddit Data Pipeline Engineering | AWS End to End Data Engineering](https://youtu.be/LSlt6iVI_9Y?si=0yJTO9GXtp_IJjyA). Gracias a 
CodeWithYu por proporcionar una guía detallada que ayudó en la creación de este pipeline.