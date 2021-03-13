import pandas as pd  # для работы с датафреймами
from aiogram.utils.markdown import bold

from utils.misc.SORT import emoji_list
from utils.misc.weeks import para_time_alldays, para_time_saturday


class Parser:
    def __init__(self, filename):
        # подгружаю файл
        df = pd.read_excel(filename, sheet_name='TDSheet', header=None)
        df.columns = [f'col_{x}' for x in range(df.shape[1])]
        # откидываем колонки с днями недели и номерами пар
        df.drop([f'col_{x}' for x in sorted(list(range(0, df.shape[1], 22)) + list(range(1, df.shape[1], 22)))],
                inplace=True, axis=1)
        # Дропаем ненужные строки
        df.drop([0, 1, 2, 36, 69, 102, 103], inplace=True)
        # сбрасываем индексацию строк
        df.reset_index(drop=True, inplace=True)
        # именуем колонки по новой
        df.columns = [f'col_{x}' for x in range(df.shape[1])]
        # заменяем наны
        df.fillna('', inplace=True)

        # создание словаря с группами
        groups = [df.iloc[:, item:item + 4] for item in range(0, df.shape[1], 4)]
        self.rasp = dict()
        for group in groups:
            name = group.iloc[0, 0]
            self.rasp[name] = []
            for i in range(1, group.shape[0], 16):
                self.rasp[name].append(group.iloc[i:i + 16])

    def get_rasp(self):
        cl_rasp = [{}, {}]
        # берем отдельный день
        for key in self.rasp.keys():
            cl_rasp[0][key] = {}
            cl_rasp[1][key] = {}

            # Проходим по всем дням
            for i, day in enumerate(self.rasp[key]):
                # Если нет пары в первую неделю, или вообще нет пары
                # if not any(day.iloc[:, 0]):
                #    continue
                # Проходимся по всем парам(Первая неделя)
                for num_para in range(0, day.shape[0], 2):
                    para = day.iloc[num_para:num_para + 2, :]
                    if para.iloc[0, 0] and para.iloc[0, 1]:
                        _num_para = emoji_list[int(num_para / 2)]
                        _time = para_time_saturday[int(num_para / 2)] if int(num_para / 2) == [5, 6] else para_time_alldays[int(num_para / 2)]
                        _para = para.iloc[0, 0]
                        _teacher = para.iloc[1, 0]
                        _cabinet = str(para.iloc[0, 1]).replace('.0', '')
                        try:
                            cl_rasp[0][key][i] += f"{_num_para} [{_time}] <b>{_para}</b>\n" \
                                                  f" {_teacher} <b>({_cabinet})</b>\n"
                        except KeyError:
                            cl_rasp[0][key][i] = f"{_num_para} [{_time}] <b>{_para}</b>\n" \
                                                 f" {_teacher} <b>({_cabinet})</b>\n"
                    elif para.iloc[0, 0] and not para.iloc[0, 2]:
                        _num_para = emoji_list[int(num_para / 2)]
                        _time = para_time_saturday[int(num_para / 2)] if int(num_para / 2) == [5, 6] else para_time_alldays[int(num_para / 2)]
                        _para = para.iloc[0, 0]
                        _teacher = para.iloc[1, 0]
                        _cabinet = str(para.iloc[0, 3]).replace('.0', '')
                        try:
                            cl_rasp[0][key][i] += f"{_num_para} [{_time}] <b>{_para}</b>\n" \
                                                  f" {_teacher} <b>({_cabinet})</b>\n"
                        except KeyError:
                            cl_rasp[0][key][i] = f"{_num_para} [{_time}] <b>{_para}</b>\n" \
                                                  f" {_teacher} <b>({_cabinet})</b>\n"

            for i, day in enumerate(self.rasp[key]):
                #if not any(day.iloc[:, 0]) and not any(day.iloc[:, 2]):
                #    continue
                #elif not any(day.iloc[:, 2]) and not any(day.iloc[:, 3]):
                #    continue
                #elif not any(day.iloc[:, 2]):
                #    continue

                # По второй
                # берем отдельную пару
                for num_para in range(0, day.shape[0], 2):
                    para = day.iloc[num_para:num_para + 2, :]

                    if para.iloc[0, 2]:
                        _num_para = emoji_list[int(num_para / 2)]
                        _time = para_time_saturday[int(num_para / 2)] if int(num_para / 2) == [5, 6] else para_time_alldays[int(num_para / 2)]
                        _para = para.iloc[0, 2]
                        _teacher = para.iloc[1, 2]
                        _cabinet = str(para.iloc[0, 3]).replace('.0', '')
                        try:
                            cl_rasp[1][key][i] += f"{_num_para} [{_time}] <b>{_para}</b>\n" \
                                                  f" {_teacher} <b>({_cabinet})</b>\n"
                        except KeyError:
                            cl_rasp[1][key][i] = f"{_num_para} [{_time}] <b>{_para}</b>\n" \
                                                  f" {_teacher} <b>({_cabinet})</b>\n"
                    elif para.iloc[0, 0] and not para.iloc[0, 1]:
                        _num_para = emoji_list[int(num_para / 2)]
                        _time = para_time_saturday[int(num_para / 2)] if int(num_para / 2) == [5, 6] else para_time_alldays[int(num_para / 2)]
                        _para = para.iloc[0, 0]
                        _teacher = para.iloc[1, 0]
                        _cabinet = str(para.iloc[0, 3]).replace('.0', '')
                        try:
                            cl_rasp[1][key][i] += f"{_num_para} [{_time}] <b>{_para}</b>\n" \
                                                  f" {_teacher} <b>({_cabinet})</b>\n"
                        except KeyError:
                            cl_rasp[1][key][i] = f"{_num_para} [{_time}] <b>{_para}</b>\n" \
                                                 f" {_teacher} <b>({_cabinet})</b>\n"
        return cl_rasp
