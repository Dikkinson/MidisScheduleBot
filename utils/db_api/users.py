from aiogram import types

from .storages import MysqlConnection


class Users(MysqlConnection):
    @staticmethod
    async def is_user(user: types.User) -> bool:
        """Возвращает тру, если юзер с таким ид есть в базе"""
        sql = 'SELECT * FROM `Users_info` WHERE `user_id` = %s'
        params = (user.id,)
        r = await Users._make_request(sql, params, fetch=True)
        return bool(r)

    @staticmethod
    async def set_user(user: types.User):
        """В случае, если юзер есть в базе - обновляем его юзернейм, если нет - заносим"""
        if await Users.is_user(user):
            sql = 'UPDATE `Users_info` SET `username` = %s WHERE `user_id` = %s'
            params = (user.username, user.id)
        else:
            sql = 'INSERT INTO `Users_info` (`user_id`, `subscribed`, `username`) VALUES (%s, 0, %s)'
            params = (user.id, user.username)
        await Users._make_request(sql, params)

    @staticmethod
    async def is_sub(user: types.User) -> bool:
        """Возвращает тру, если юзер подписался на рассылку"""
        sql = 'SELECT `subscribed` FROM `Users_info` WHERE `user_id` = %s'
        params = (user.id,)
        r = await Users._make_request(sql, params, fetch=True)
        return bool(r['subscribed'])

    @staticmethod
    async def get_sub() -> list:
        sql = 'SELECT `user_id` FROM `Users_info` WHERE `subscribed` = 1'
        params = tuple()
        r = await Users._make_request(sql, params, fetch=True, mult=True)
        return r

    @staticmethod
    async def set_sub(user: types.User):
        sql = 'UPDATE `Users_info` SET `subscribed` = 1  WHERE `user_id` = %s'
        params = (user.id,)
        await Users._make_request(sql, params)

    @staticmethod
    async def switch_sub(user: types.User):
        if await Users.is_sub(user):
            subscribed = 0
        else:
            subscribed = 1
        sql = 'UPDATE `Users_info` SET `subscribed` = %s WHERE `user_id` = %s'
        params = (subscribed, user.id)
        await Users._make_request(sql, params)

    @staticmethod
    async def get_group(user_id: str) -> str:
        sql = 'SELECT `user_group` FROM `Users_info` WHERE `user_id` = %s'
        params = (user_id,)
        r = await Users._make_request(sql, params, fetch=True)
        return r['user_group']

    @staticmethod
    async def set_group(user_group: str, user: types.User):
        sql = 'UPDATE `Users_info` SET `user_group` = %s WHERE `user_id` = %s'
        params = (user_group, user.id)
        await Users._make_request(sql, params)
