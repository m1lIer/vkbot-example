import random
import vk_api
import requests
import time
import datetime
from vk_api.longpoll import VkEventType, VkLongPoll
from vk_api.keyboard import VkKeyboard
from vk_api.upload import VkUpload
from vk_api.tools import VkTools
from vk_api.exceptions import VkRequestsPoolException
import reaction

vk_session = vk_api.VkApi(token='group token')
vk = vk_session.get_api()
longpool = vk_api.longpoll.VkLongPoll(vk_session)
upload = VkUpload(vk_session)
get_docs = VkTools(vk_session)
session = requests.Session()



def download_file():
    for event in longpool.listen():
        if event.type != VkEventType.USER_OFFLINE and VkEventType.USER_TYPING and VkEventType.USER_CALL and VkEventType.USER_RECORDING_VOICE and event.type == VkEventType.MESSAGE_NEW and event.to_me:
            get_docs.get_all(method= "docs.get", max_count=2, values=None, key='items', limit=None, stop_fn=None, negative_offset=False)
            print("DOWNLOADING...")
            vk.messages.send(
                user_id = event.user_id,
                message = "Преобразование...",
                random_id = random.randint(0, 10000)
                )
        


try:
    for event in longpool.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            print(event)
            
            if event.text in database.reaction1:
                print(event.text)
            if event.text in database.reaction2:
                print("REACTION2")
                vk.messages.send(
                    user_id=event.user_id,
                    message='Загрузите \".xls\" или другой excel файл',
                    random_id = random.randint(0, 10000)
                    )
                download_file()

except VkRequestsPoolException:
    print(VkRequestsPoolException);



def upload_photo_chat():
    attachments = []
    image_url = 'ССЫЛКА'
    image = session.get(image_url, stream=True)
    photo = upload.photo_messages(photos=image.raw)[0]

    attachments.append(

        'photo{}_{}'.format(photo['owner_id'], photo['id'])
)

    vk.messages.send(

        user_id=event.user_id,
        attachment=','.join(attachments),
        message='Готовое расписание',
        random_id = random.randint(0, 10000)
)