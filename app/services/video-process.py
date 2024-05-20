from app.services.tasks import process_video

def trigger_video_processing(video_id: int):
    process_video.send(video_id)
