from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* CSS to change the color of text to green */
            body {
                background-color: black;
                color: green;
            }
        </style>
    </head>
    <body>
        <h1>Hello, World!</h1>
    </body>
    </html>
    """



