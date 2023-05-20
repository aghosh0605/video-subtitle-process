import subprocess
from django.conf import settings
import os
import uuid
from .tasks import uploads3
from .tasks import *

def extractSubtitle(video_path):
    filename = uuid.uuid1()
    subtitle_path = os.path.join(settings.BASE_DIR,f'media/subtitles/{filename}.txt')
    # print(save_path)
    
    if os.path.isfile(video_path):
        cmd = f"ccextractor {video_path} -out=ttxt -o {subtitle_path}"
    # returns output as byte string
        returned_output = subprocess.check_output(cmd,shell=True)
    # using decode() function to convert byte string to string
    # print(returned_output.decode("utf-8"))
    
    if os.path.isfile(subtitle_path):
        task_id = uploads3.delay(subtitle_path)
        puItems.delay(subtitle_path,video_path)
    return task_id