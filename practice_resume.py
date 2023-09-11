from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Bootstrap demo</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
            <link href="/static/style.css" rel="stylesheet">
        </head>
        <body class="custom-background">
            <nav class="navbar navbar-expand-lg bg-body-tertiary">
              <div class="container-fluid">
                <a class="navbar-brand" href="#">MENU</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                  <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                      <a class="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li class="nav-item dropdown">
                      <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Portfolio
                      </a>
                      <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="#">Website</a></li>
                        <li><a class="dropdown-item" href="#">Data_Engineer</a></li>
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item" href="#">etc</a></li>
                      </ul>
                    </li>
                  </ul>
                  <form class="d-flex" role="search">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                  </form>
                </div>
              </div>
            </nav>
            <div class="contianer">
                <div class="jumbotron">
                    <h1 class="text-center">RESUME</h1>
                    <p class="text-center">Name: Chanho Hyun</p>
                    <p class="text-center"><a href="https://www.linkedin.com/in/chanhohyun/?originalSubdomain=kr" class="btn btn-primary">LinkedIn</a>
                    <a href="https://www.instagram.com/hch16/?hl=ko" class="btn btn-secondary">Instagram</a></p>
                </div>
            </div>
            <div class="card mx-auto" style="width: 18rem;">
                <img src="data:image/jpeg;base64,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" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">Name: Chanho Hyun</h5>
                    <p class="card-text">Date of Birth: 1997-02-16
                    <p class="card-text">E-mail: hch970216@gmail.com
                    <p class="card-text">Phone: 010-9428-1464</p>
                </div>
            </div>
            <div class="accordion accordion-flush" id="accordionFlushExample">
              <div class="accordion-item">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
                    Education
                  </button>
                </h2>
                <div id="flush-collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">University of Toronto st.george
                    <p class="small">
                        Bachelor of Science in Mathematics and Statistics
                    </p>
                    <ul>
                        <li>Specialization: Mathematics, Data Analysis, Data Engineering</li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="accordion-item">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
                    Skills
                  </button>
                </h2>
                <div id="flush-collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">Languages:
                    <ul>
                        <li>English</li>
                         <li>Korean</li>
                    </ul>
                  </div>
                  <div class="accordion-body">Programming:
                    <ul>
                        <li>R Studio</li>
                        <li>Python</li>
                        <li>Airflow</li>
                        <li>Shell-Script</li>
                        <li>Elasticsearch</li> 
                        <li>Fastapi</li> 
                        <li>Bootstrap</li>
                  </div>
                  <div class="accordion-body">OS and Microsoft office:
                    <ul>
                        <li>linux</li>
                        <li>windows</li>
                        <li>macos</li>
                        <li>Word</li>
                        <li>PowerPoint</li>
                        <li>Excel</li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="accordion-item">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseThree" aria-expanded="false" aria-controls="flush-collapseThree">
                    Extracurricular Activity
                  </button>
                </h2>
                <div id="flush-collapseThree" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <h>UTKSA (University of Toronto Korean Student Association) chief science director</h>
                        <ul>
                            <li> Tutor of MAT135,136 (AP Calculus A,B) for two years</li>
                            <li> Manage Science Mentorship Seminar Program with alumni of University of Toronto who are working on Statistics, Medical parts (especially financial district, Dental, and Medication)</li>
                        </ul>        
                  </div>
                </div>
              </div>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
        </body>
    </html>
    """