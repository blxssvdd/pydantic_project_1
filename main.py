from typing import List

from fastapi import FastAPI, status, HTTPException, Path
from fastapi.responses import JSONResponse
import uvicorn

from data_actions import get_db, save_db
from models import MovieModel, MovieModelResponse


app = FastAPI()



@app.get("/movies", response_model=List[MovieModel], status_code=status.HTTP_202_ACCEPTED)
def get_movies():
    return get_db()


@app.get("/movies/{movie_id}", response_model=MovieModelResponse, status_code=status.HTTP_202_ACCEPTED)
async def get_movie(movie_id: int):
    movie = next((movie for movie in get_db() if movie["id"] == movie_id), None)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with id {movie_id} not found")
    return movie


@app.post("/movies", status_code=status.HTTP_201_CREATED)
async def add_movie(movie_model: MovieModel):
    db = get_db()
    db.append(movie_model.model_dump())
    save_db(db)
    return JSONResponse("Movie added successfully!")


@app.delete("/movies/{movie_id}", status_code=status.HTTP_200_OK)
async def delete_movie(movie_id: int):
    db = get_db()
    movie = next((movie for movie in db if movie["id"] == movie_id), None)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with id {movie_id} not found")
    db.remove(movie)
    save_db(db)
    return JSONResponse("Movie deleted successfully!")



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)