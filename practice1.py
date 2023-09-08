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
            /* CSS to change the background color to black */
            body {
                background-color: black;
                color: green;
                text-align: center; /* Center-align the content */
            }
            .button-container {
                margin-top: 20px; /* Add some margin to space out the buttons */
            }
        </style>
    </head>
    <body>
        <h1>Hello, World!</h1>

        <!-- Button container -->
        <div class="button-container">
            <!-- Green button -->
            <button style="background-color: green; color: white;">Green Button</button>

            <!-- Red button -->
            <button style="background-color: red; color: white;">Red Button</button>
        </div>
    </body>
    </html>
    """
