from kvstore_lib.application import Application
from collections import defaultdict
from kvstore_lib.command import Command
from kvstore_lib.kvs_command import KVSCommand
from kvstore_lib.kvs_exception import KVSException


class KVStore(Application):
    def __init__(self):
        self.__storage: defaultdict[str, str] = defaultdict[str, str](str)
        self.COMMANDS = {
            'GET',
            'PUT',
            'APPEND',
        }

    def execute(self, command: Command) -> str:
        if not isinstance(command, KVSCommand):
            raise KVSException('Error: Not a KVS command')

        cmd_type: str = command.cmd_type
        key: str = command.key
        value: str | None = command.value

        ret: str = ""
        if cmd_type not in self.COMMANDS:
            raise KVSException('Error: Unknown command')

        if cmd_type == 'GET':
            ret = self._get(key)
        elif cmd_type == 'PUT':
            if not value:
                raise KVSException('Error: Key/Value must be specified')
            ret = self._put(key, value)
        elif cmd_type == 'APPEND':
            if not value:
                raise KVSException('Error: Key/Value must be specified')
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
