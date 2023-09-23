from base_classes.application import Application
from collections import defaultdict


class KVStore(Application):
  def __init__(self):
    self.__storage = defaultdict[str, str](str)

  def get(self, key: str) -> str:
    if key not in self.__storage:
      return "KeyNotFound"
    return self.__storage[key]

  def put(self, key: str, value: str) -> str:
    self.__storage[key] = value
    return "PutOK"

  def append(self, key: str, value: str):
    self.__storage[key] += value
    return self.__storage[key]
