from datetime import datetime

from pydantic import BaseModel


class Movie(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True


class Auditorium(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Screening(BaseModel):
    id: int
    movie_id: int
    movie: Movie
    auditorium_id: int
    auditorium: Auditorium
    screening_start: datetime

    class Config:
        orm_mode = True


class Seat(BaseModel):
    id: int
    row: int
    number: int
    auditorium_id: int
    auditorium: Auditorium

    class Config:
        orm_mode = True


class Employee(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        orm_mode = True


class Reservation(BaseModel):
    id: int
    screening_id: int
    screening: Screening
    employee_id: int
    employee: Employee
    paid: bool
    active: bool

    class Config:
        orm_mode = True


class SeatReserved(BaseModel):
    id: int
    seat_id: int
    seat: Seat
    reservation_id: int
    reservation: Reservation
    screening_id: int
    screening: Screening

    class Config:
        orm_mode = True
