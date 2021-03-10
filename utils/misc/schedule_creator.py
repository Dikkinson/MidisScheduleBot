from utils.misc.weeks import days


def create_rasp_text(week: int, group_name: str, rasp):
    text = f"Расписание на {'вторую' if week else 'первую'} неделю {group_name}:\n\n"
    for day in rasp[week][group_name]:
        text += f"<i>{days[day]}</i>\n"
        try:
            text += f"{rasp[week][group_name][day]}\n"
        except KeyError:
            pass
    return text
