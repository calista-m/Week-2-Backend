#importing fastapi library
from fastapi import FastAPI

#initiallize the FastAPI application
app = FastAPI(
    title="FastAPI Example",
    description="This is an example of using FastAPI"
)

#define endpoints or routes (what are the paths that will be taken care of)
@app.get('/')
def default_route():
    """
    This is the default endpoint for this back-end.
    """
    return "You have reached the default route. Back-end server is listening..."


