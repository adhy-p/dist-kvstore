from kvstore_lib.application import Application
from kvstore_lib.message import Message


class AMOApp(Application):
    """
    AMOApp is a wrapper around an Application to ensure that all commands
    are executed at most once.
    """
    def __init__(self, app: Application):
        self.app: Application = app
        self.__last_cmds: dict[int, Message] = {}
        self.__executed_cmds: dict[Message, Message] = {}

    def execute(self, amo_cmd: Message) -> Message:
        if amo_cmd in self.__executed_cmds:
            return self.__executed_cmds[amo_cmd]
        if self._already_executed(amo_cmd):
            raise Exception('Error: result has been garbage-collected')

        app_cmd: dict[str, str] = amo_cmd.msg
        sender: int = amo_cmd.src
        receiver: int = amo_cmd.dst
        seq_num: int = amo_cmd.seq_num

        ret: str = ""
        try:
            ret = self.app.execute(app_cmd)
        except Exception as e:
            ret = str(e)
        execution_result: Message = Message(receiver, sender, {'ret_msg': ret}, seq_num+1)

        # garbage collection
        if sender in self.__last_cmds:
            self.__executed_cmds.pop(self.__last_cmds[sender])
        self.__last_cmds[sender] = amo_cmd
        self.__executed_cmds[amo_cmd] = execution_result
        return execution_result

    def _already_executed(self, command: Message) -> bool:
        if command in self.__executed_cmds:
            return True
        cmd_src: int = command.src
        if not cmd_src:
            return False
        if cmd_src in self.__last_cmds:
            last_cmd: Message = self.__last_cmds[cmd_src]
            return self.__executed_cmds[last_cmd].seq_num >= command.seq_num
        return False
