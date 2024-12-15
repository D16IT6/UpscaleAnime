from watchdog.events import FileSystemEventHandler


class NewFileWatchHandler(FileSystemEventHandler):
    def __init__(self,log_callback,total_frames):
        self.log_callback = log_callback
        self.total_frames = total_frames

        self.upscaled = 0

    def on_created(self, event):
        if event.is_directory:
            return  # Ignore directories
        if self.log_callback:
            self.upscaled+=1
            self.log_callback(f"Upscaled: {event.src_path}")
