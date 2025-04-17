from typing import List

from fastapi import FastAPI, status, HTTPException, Path
from fastapi.responses import JSONResponse
import uvicorn

from models import MovieModel


app = FastAPI()
movies = []


@app.get("/movies", response_model=List[MovieModel], status_code=status.HTTP_202_ACCEPTED)
def get_movies():
    return movies


@app.get("/movies/{movie_id}", response_model=MovieModel, status_code=status.HTTP_200_OK)
def get_movie(movie_id: int = Path(...)):
    for movie in movies:
        if movie.id == movie_id:
            return movie
    raise HTTPException(status_code=404, detail=f"Фільм з ID {movie_id} не знайдено")


@app.post("/movies/", response_model=MovieModel, status_code=status.HTTP_201_CREATED)
def create_movie(movie: MovieModel):
    movies.append(movie)
    return JSONResponse("Новий фільм успішно доданий")


@app.delete("/movies/{movie_id}", status_code=status.HTTP_200_OK)
def delete_movie(movie_id: int = Path(...)):
    for movie in movies:
        if movie.id == movie_id:
            movies.remove(movie)
            return JSONResponse("Фільм успішно видалено")
        if not movies:   
          raise HTTPException(status_code=404, detail=f"Фільм з ID {movie_id} не знайдено")




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)