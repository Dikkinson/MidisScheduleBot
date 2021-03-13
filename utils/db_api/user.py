from typing import Union

from aiogram import types

from .storages import MysqlConnection


class User(MysqlConnection):
    @staticmethod
    async def is_user(user: types.User) -> bool:
        """Возвращает тру, если юзер с таким ид есть в базе"""
        sql = 'SELECT * FROM `Users_info` WHERE `user_id` = %s'
        params = (user.id,)
        r = await User._make_request(sql, params, fetch=True)
        return bool(r)

    @staticmethod
    async def set_user(user: types.User):
        """В случае, если юзер есть в базе - обновляем его юзернейм, если нет - заносим"""
        if await User.is_user(user):
            sql = 'UPDATE `Users_info` SET `username` = %s WHERE `user_id` = %s'
            params = (user.username, user.id)
        else:
            sql = 'INSERT INTO `Users_info` (`user_id`, `username`) VALUES (%s, %s)'
            params = (user.id, user.username)
        await User._make_request(sql, params)
