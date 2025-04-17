from typing import List, Dict, Union, Optional, Annotated
from enum import Enum
from datetime import date 
from pydantic import BaseModel, HttpUrl, EmailStr, field_validator, Field


class MovieModel(BaseModel):
    id: Annotated[int, Field(..., description="ID фільму")]
    title: Annotated[str, Field(..., description="Назва фільму")]
    director: Annotated[str, Field(..., description="Режисер фільму")]
    release_year: Annotated[date, Field(..., description="Рік виходу фільму")]
    rating: Annotated[float, Field(..., description="Рейтинг фільму")]


    @field_validator("id")
    def check_id(cls, id: int):
        if id < 0:
            raise ValueError("ID не може бути від'ємним")
        return id

     
    @field_validator("title")
    def check_title(cls, title: str):
        if len(title) < 3:
            raise ValueError("Назва фільму повинна містити не менше 3 символів")
        return title
    

    @field_validator("director")
    def check_director(cls, director: str):
        if len(director) < 3:
            raise ValueError("Ім'я режисера повинно містити не менше 3 символів")
        return director
    

    @field_validator("release_year")
    def check_release_year(cls, release_year: date):
        if release_year > date.today():
            raise ValueError("Рік виходу фільму не може бути у майбутньому")
        return release_year

    
    @field_validator("rating")
    def check_rating(cls, rating: float):
        if rating < 0 or rating > 10:
            raise ValueError("Рейтинг фільму повинен бути в діапазоні від 0 до 10")
        return rating