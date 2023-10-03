from kvstore_lib.application import Application
from kvstore_lib.amo_command import AMOCommand
from kvstore_lib.command import Command
from kvstore_lib.kvs_result import KVSResult
from kvstore_lib.amo_result import AMOResult
from kvstore_lib.kvs_exception import KVSException


class AMOApp(Application):
    """
    AMOApp is a wrapper around an Application to ensure that all commands
    are executed at most once.
    """
    def __init__(self, app: Application):
        self.app: Application = app
        self.__last_cmds: dict[int, AMOCommand] = {}
        self.__executed_cmds: dict[AMOCommand, AMOResult] = {}

    def execute(self, amo_cmd: Command) -> AMOResult:
        if not isinstance(amo_cmd, AMOCommand):
            raise Exception('Error: did not receive AMOCommand')
        if amo_cmd in self.__executed_cmds:
            return self.__executed_cmds[amo_cmd]
        if self._already_executed(amo_cmd):
            raise Exception('Error: result has been garbage-collected')

        app_cmd: Command = amo_cmd.cmd
        sender: int = amo_cmd.src
        receiver: int = amo_cmd.dst
        seq_num: int = amo_cmd.seq_num

        ret: str = ""
        try:
            ret = self.app.execute(app_cmd)
        except KVSException as e:
            ret = str(e)
        execution_result: AMOResult = AMOResult(receiver, sender, KVSResult(ret), seq_num+1)

        # garbage collection
        if sender in self.__last_cmds:
            self.__executed_cmds.pop(self.__last_cmds[sender])
        self.__last_cmds[sender] = amo_cmd
        self.__executed_cmds[amo_cmd] = execution_result
        return execution_result

    def _already_executed(self, command: AMOCommand) -> bool:
        if command in self.__executed_cmds:
            return True
        cmd_src: int = command.src
        if not cmd_src:
            return False
        if cmd_src in self.__last_cmds:
            last_cmd: AMOCommand = self.__last_cmds[cmd_src]
            return self.__executed_cmds[last_cmd].seq_num >= command.seq_num
        return False
