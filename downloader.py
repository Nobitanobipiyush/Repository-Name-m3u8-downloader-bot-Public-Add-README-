import subprocess, uuid, os

def download_m3u8_to_mp4(url):
    name = f"/tmp/{uuid.uuid4()}.mp4"
    cmd = ["ffmpeg","-y","-i",url,"-c","copy",name]
    subprocess.run(cmd, check=True)
    return name
