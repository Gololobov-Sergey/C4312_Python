import datetime
import os
import shutil

# print(datetime.datetime.now())
# dt = datetime.datetime(year=2025, month=3, day=29, hour=9, minute=0)
# print(type(dt))
# print(dt)
# print(dt.date())
# print(dt.time())
#
# d1 = datetime.date(2025, 5, 20)
# t1 = datetime.time(9,0,30)
#
# dt1 = datetime.datetime.combine(d1, t1)
# print(dt1)
#
# dt1 = dt1.replace(day=28)
# print(dt1)
#
# dn = datetime.datetime.now().date()
# print(dn)
# print(datetime.datetime.today())
#
# print(dn.weekday())
# print(dn.isoweekday())


# f = os.path.getctime(path)
#
# print(os.path.getctime(path))
# print(os.path.getmtime(path))
# print(os.path.getatime(path))
# print(os.path.getsize(path))
#
# df = datetime.datetime.fromtimestamp(f)
# print(df)
#
# print(dn.strftime("%d.%m.%Y"))
# print(dn.strftime("%d %B %Y, %A"))
#
# td = d1 - dn
# print(td)

path = "C:\\Users\\gololobov\\Downloads\\Test"
res_path = "C:\\Test"

def spy2(path, res_path):
    path = os.path.normpath(path)
    res_path = os.path.normpath(res_path)
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_date = os.path.getmtime(f"{dirpath}\\{file}")
            norm_date = datetime.datetime.fromtimestamp(file_date)
            str_date = norm_date.strftime("%d.%m.%Y")

            if os.path.isdir(f"{res_path}\\{str_date}"):
                shutil.copy(f"{dirpath}\\{file}", f"{res_path}\\{str_date}\\{file}")
            else:
                os.mkdir(f"{res_path}//{str_date}")
                shutil.copy(f"{dirpath}\\{file}", f"{res_path}\\{str_date}\\{file}")

spy2(path, res_path)