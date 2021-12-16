from __future__ import annotations
from abc import ABC, abstractmethod
import typing

from pygame import Surface


point = typing.Tuple[float, float]


class Tile(ABC):
    @abstractmethod
    def draw(self, screen: Surface) -> None:
        """Рисует себя на экране"""

    @abstractmethod
    def rectangle(self) -> typing.Tuple[point, point]:
        """Возвращает прямоугольник в формате (<левая нижняя точка>, <правая верхняя точка>)"""

    @staticmethod
    @abstractmethod
    def create(_="""Добавьте сюда какие-то аргументы, которые нужны чтобы создать плитку""") -> Tile:
        """Статический метод, создающий Tile"""



