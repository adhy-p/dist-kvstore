from kvstore_lib.application import Application
from collections import defaultdict
from typing import Any


class KVStore(Application):
    def __init__(self):
        self.__storage: defaultdict[str, str] = defaultdict[str, str](str)
        self.COMMANDS = {
            'GET',
            'PUT',
            'APPEND',
        }

    def execute(self, app_command: dict[Any, Any]) -> str:
        if app_command.get('cmd_type', None) not in self.COMMANDS:
            raise Exception('Error: Unknown command')

        cmd_type: str = app_command['cmd_type']
        key: str | None = app_command.get('key')
        value: str | None = app_command.get('value', None)

        ret: str = ""

        if cmd_type == 'GET':
            if not key:
                raise Exception('Error: Key must be specified')
            ret = self._get(key)
        elif cmd_type == 'PUT':
            if not key or not value:
                raise Exception('Error: Key/Value must be specified')
            ret = self._put(key, value)
        elif cmd_type == 'APPEND':
            if not key or not value:
                raise Exception('Error: Key/Value must be specified')
            ret = self._append(key, value)
        return ret

    def _get(self, key: str) -> str:
        if key not in self.__storage:
            return "KeyNotFound"
        return self.__storage[key]

    def _put(self, key: str, value: str) -> str:
        self.__storage[key] = value
        return "PutOK"

    def _append(self, key: str, value: str):
        self.__storage[key] += value
        return self.__storage[key]
