#Muhammad Yousaf Iqbal

class Time:

    __slots__ = ["hours", "minutes", "seconds"]

    def __init__(self, hours=0, minutes=0, seconds=0):
    
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

def get_time(time):

    return("{}:{:02}:{:02}".format(time.hours, time.minutes, time.seconds))

class Song:

    __slots__ = ["title" , "recording_artist" , "running_duration"]

    def __init__(self, title, recording_artist, running_duration):
    
        self.title = title
        self.recording_artist = recording_artist
        self.running_duration = running_duration

class Album:

    __slots__ = ["title" , "artist" , "number_of_tracks" , "total_running_duration", "tracks"]

    def __init__(self, title, artist, number_of_tracks, total_running_duration):
    
        self.title = title
        self.artist = artist
        self.number_of_tracks = number_of_tracks
        self.total_running_duration = total_running_duration
        self.tracks = []

    def add_song(self, song):

        hours, minutes, seconds = Song.running_duration.split(':')
        song_running_duration = Time(hours=hours, minutes=minutes, seconds=seconds)
        self.tracks.append(song, song_running_duration)
        self.number_of_tracks += 1
        self.total_running_duration += song_running_duration 

    def print_album(album):

        print(f"{album.title} - {album.artist} - ({get_time(album.total_running_duration)})")
        for i in range(album.number_of_tracks):
            track, duration = album.tracks[i]
            print(f"{i+1}. {track.title} - {track.artist} - ({get_time(duration)})") + "\n"

def main():

    song_1 = Song("Fast", "Juice WRLD", "3:30")
    song_2 = Song("Feeling", "Juice WRLD", "3:15")
    song_3 = Song("Robbery", "Juice WRLD", "4:00")
    album_1 = Album("Death Race For Love", "Juice WRLD", 0, 0)
    album_1.add_song(song_1)
    album_1.add_song(song_2)
    album_1.add_song(song_3)
    album_1.print_album(album_1)

if __name__ == "__main__":

    main()

#Done