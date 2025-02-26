Clase 6 - Chat Completion API
-----------------------------
- tres roles fundamentales: system, assistant, user
- historial de mensajes para dar contexto al asistente
- parametros 
    max_tokens
    temperature
ver ChatCompletionAPI/script.py


Clase 8 - Uso de herramientas
-----------------------------
- el asistente consulta una API externa para dar al usuario informacion del clima

ver ToolsAPI/script.py


Clase 9 - Manejo de Imágenes en GPT-4o
--------------------------------------
- script bastate simple que usa"gpt-4o-mini" para analizar una imagen

ver ImagesAPI/script.py


Clase 10 - Arquitectura de 'PlatziVision'
-----------------------------------------
- en ./docker_project/
1. Dockerfile de alpine con python, bash, npm y nodejs
        docker build -t openai1:latest .
2. clonacion de https://github.com/platzi/platzivision/
3. carpeta github dentro de platzivision/ borrada
4. ejecucion del contenedor mapeando dos puertos y pasando un volumen (en ./docker_project/)
        docker run -d -it -p 3000:3000 -p 5000:5000 -v .:/workspace --name pro openai1
5. dentro del contenedor, y dentro de ./platzivision/ seguir las indicaciones del repositorio
        cd platzi-vision-ui
        npm install
        npm run dev
        cd ..
        cd platzi-vision-api
        python -m venv env
        source env/bin/activate
        pip install -r requirements.txt

* Modificaciones necesarias 
    - poner .env con api_key dentro de /platzi-vision-api/app/
    - modificar /platzi-vision-api/app.py
        app.run(host="0.0.0.0", port=5000, debug=True)

6. finalmente
    python app.py

Se verifica el funcionamiento de la aplicacion en http://0.0.0.0:3000/

Nota: 
''''
La aplicación está completa, se estudiará el paso a paso bajo otra subcarpeta de este mismo repositorio y futuros commits