class ImageFileValidator:


    def __init__(self, path):
        self.path = path

    def valid(self):
        # TODO: jpg or png or jpeg
        return str(self.path).endswith(self.valid_formats)




class DocumentValidator:
    def __init__(self, path,pages):
        self.path = path
        self.pages = pages

    def valid(self):
        # Path = pdf and pages > 0
        is_valid = False
        return (
            str(self.path).endswith("PDF")
            and self.pages > 0
        )



class AudioFileValidator:
    def __init__(self, path, length):
        self.path = path
        self.length = length

    def valid(self):
        # TODO: path = mp3 wav and length > 0
        valid_formats = ("MP3", "WAV")
        return (
            str(self.path).endswith(valid_formats)
            and self.length > 0
        )




class VideoFileValidator:
    def __init__(self,path,length,res):
        self.path = path
        self.length = length
        self.res = res

    def valid(self):
        # TODO: path = Mp4 and res = 720 or 1080 and length >0
        valid_formats = "MP4"
        valid_res = (720, 1080)

        return (
            str(self.path).endswith(valid_formats)
            and self.length > 0
            and self.res in valid_res
        )






document_1 = DocumentValidator("PDF",2)
print(f"DocumentValidator: {document_1.valid()}")

image_1 = ImageFileValidator("PNG")
print(f"ImageFileValidator: {image_1.valid()}")

audio_1 = AudioFileValidator("MP3",2)
print(f"AudioFileValidator: {audio_1.valid()}")

video_1 = VideoFileValidator("MP4",1, 1080)
print(f"VideoFileValidator: {video_1.valid()}")
