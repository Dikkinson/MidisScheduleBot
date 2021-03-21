import mechanicalsoup
import http.cookiejar as cookiejar
from utils.misc.parser import Parser
from utils.notify_admins import notify_admins_def


async def get_rasp(rasp, old_file_id, dp):
    cj = cookiejar.CookieJar()
    br = mechanicalsoup.StatefulBrowser()
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.set_cookiejar(cj)
    br.open("https://portal.midis.info/")
    br.select_form('form[name="form_auth"]')
    br['USER_LOGIN'] = 'qPVSju'
    br['USER_PASSWORD'] = 'LQSTK1'
    br.submit_selected()
    br.open("https://portal.midis.info/docs/timetable/path/Для%20очного%20отделения/")
    file_id = str(br.page).split('items: [{"id":"')[1].split('","name":"')[0]
    if old_file_id[0] != file_id:
        resp = br.session.get(f"https://portal.midis.info/disk/downloadFile/{file_id}/?&ncc=1")
        resp.raise_for_status()  # raise an exception for 404, etc.
        with open('../rasp.xlsx', 'wb') as file:
            file.write(resp.content)
        pars = Parser('rasp.xlsx')
        new_rasp = pars.get_rasp()
        rasp.append(new_rasp[0])
        rasp.append(new_rasp[1])
        rasp.pop(0)
        rasp.pop(0)
        old_file_id.append(file_id)
        old_file_id.pop(0)
        await notify_admins_def(dp, f"АДМИНЫ СОСАТЬ {file_id}")
