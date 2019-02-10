import os, datetime, shutil
'''Программа проверяет системное время, создает папки Desktop и Block_Screen, в зависимости от времени суток 
(утро, день, вечер, ночь) и помещает подходящие изображения из папки desktop_images в созданные директории.'''
try:
    shutil.rmtree(r'C:\Desktop_changer_gallery\Desktop')
    shutil.rmtree(r'C:\Desktop_changer_gallery\Block_screen')

    path = r'C:\Desktop_changer_gallery\Desktop'
    os.mkdir(path)

    path = r'C:\Desktop_changer_gallery\Block_screen'
    os.mkdir(path)
except Exception:
    pass

try:
    path = r'C:\Desktop_changer_gallery'
    os.mkdir(path)

    path = r'C:\Desktop_changer_gallery\Desktop'
    os.mkdir(path)

    path = r'C:\Desktop_changer_gallery\Block_screen'
    os.mkdir(path)
except Exception:
    pass

evening_time = datetime.time(18, 0, 0)
night_time = datetime.time(23, 0, 0)
morning_time = datetime.time(5, 0, 0)
afternoon_time = datetime.time(12, 0, 0)

current_time = datetime.datetime.now().time()
print('Текущее время - ', current_time)

if night_time <= current_time < morning_time:
    print('Сейчас ночь, загружаю ночные обои')
    path_src = r'C:\desktop_images\dsk_night_1'
    path_dst = r'C:\Desktop_changer_gallery\Desktop'
    shutil.copy(os.path.join(path_src), path_dst)

    path_src = r'C:\desktop_images\dsk_night_2'
    path_dst = r'C:\Desktop_changer_gallery\Desktop'
    shutil.copy(os.path.join(path_src), path_dst)

    path_src = r'C:\desktop_images\dsk_night_3'
    path_dst = r'C:\Desktop_changer_gallery\Desktop'
    shutil.copy(os.path.join(path_src), path_dst)

    path_src = r'C:\desktop_images\bs_night_1'
    path_dst = r'C:\Desktop_changer_gallery\Desktop'
    shutil.copy(os.path.join(path_src), path_dst)
    print('Загрузка успешно завершена')

if morning_time <= current_time < afternoon_time:
    print('Сейчас утро, загружаю утренние обои')
    path_src = r'C:\desktop_images\dsk_morning_1.jpg'
    path_dst = r'C:\Desktop_changer_gallery\Desktop'
    shutil.copy(os.path.join(path_src), path_dst)

    path_src = r'C:\desktop_images\dsk_morning_2.jpg'
    path_dst = r'C:\Desktop_changer_gallery\Desktop'
    shutil.copy(os.path.join(path_src), path_dst)

    path_src = r'C:\desktop_images\dsk_morning_3.png'
    path_dst = r'C:\Desktop_changer_gallery\Desktop'
    shutil.copy(os.path.join(path_src), path_dst)

    path_src = r'C:\desktop_images\bs_morning_1.jpg'
    path_dst = r'C:\Desktop_changer_gallery\Block_screen'
    shutil.copy(os.path.join(path_src), path_dst)
    print('Загрузка успешно завершена')

if afternoon_time <= current_time < evening_time:
    print('Сейчас день, загружаю дневные обои')
    path_src = r'C:\desktop_images\dsk_afternoon_1.jpg'
    path_dst = r'C:\Desktop_changer_gallery\Desktop'
    shutil.copy(os.path.join(path_src), path_dst)

    path_src = r'C:\desktop_images\bs_afternoon_1.jpg'
    path_dst = r'C:\Desktop_changer_gallery\Block_screen'
    shutil.copy(os.path.join(path_src), path_dst)
    print('Загрузка успешно завершена')

if evening_time <= current_time < night_time:
    print('Сейчас вечер, загружаю вечерние обои')
    path_src = r'C:\desktop_images\dsk_evening_1.jpg'
    path_dst = r'C:\Desktop_changer_gallery\Desktop'
    shutil.copy(os.path.join(path_src), path_dst)

    path_src = r'C:\desktop_images\dsk_evening_2.png'
    path_dst = r'C:\Desktop_changer_gallery\Desktop'
    shutil.copy(os.path.join(path_src), path_dst)

    path_src = r'C:\desktop_images\dsk_evening_3.jpg'
    path_dst = r'C:\Desktop_changer_gallery\Desktop'
    shutil.copy(os.path.join(path_src), path_dst)

    path_src = r'C:\desktop_images\bs_evening_1.jpg'
    path_dst = r'C:\Desktop_changer_gallery\Block_screen'
    shutil.copy(os.path.join(path_src), path_dst)
    print('Загрузка успешно завершена')