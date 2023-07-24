from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"messege": "Hello!"}


@app.get("/hello")
async def world():
    return {"message": "world"}

# Crear entorno "myenv" $: python -m venv myenv
# Activar entorno $: myenv\Scripts\activate
# Instalar framework $: pip install "fastapi[all]"
# Inicar api en consola con $: uvicorn main:app --reload
# @app.get()
# @app.post()
# @app.put()
# @app.delete()
