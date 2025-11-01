# from pydub import AudioSegment
import subprocess

def convert_opus_to_mp3(opus_path: str, file_name: str, mp3_path: str ="./download"):
    # audio = AudioSegment.from_file(opus_path, format="opus")
    # audio.export(f"{mp3_path}/{file_name}", format="mp3")
    subprocess.run(['ffmpeg', '-i', f"{opus_path}", f"{mp3_path}/{file_name}.mp3"])


# TESTING
if __name__ == "__main__":
    try:
        opus_file = input("Enter location of opus audio file: ")
        mp3_file = input("Enter name of the converted mp3 file: ")
        convert_opus_to_mp3(opus_path=opus_file, file_name=mp3_file)
        print("File convert success!🎉")
    except Exception as err:
        print(f"Error converting opus file to mp3: {str(err)}")
