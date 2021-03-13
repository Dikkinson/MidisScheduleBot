from typing import Union

from aiogram import types

from .storages import MysqlConnection


class Logs(MysqlConnection):
    @staticmethod
    async def is_new(lines: int) -> str:
        sql = 'SELECT * FROM `Logs` ORDER BY `time` DESC LIMIT %s'
        params = (lines,)
        r = await Logs._make_request(sql, params, fetch=True)
        return r

    @staticmethod
    async def log(chat: types.Chat, message: types.Message):
        sql = 'INSERT INTO `Logs` (`user_id`, `action`, `time`) VALUES (%s, %s, NOW())'
        params = (chat.id, message.text)
        await Logs._make_request(sql, params)
