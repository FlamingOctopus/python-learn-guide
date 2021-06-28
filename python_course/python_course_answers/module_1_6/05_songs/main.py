violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]


def tracks_len(N):
    sum_time = 0
    for song_num in range(0, N):
        current_song = input(f"Название {song_num + 1} песни: ")
        count_list_in_list = 0
        for song in violator_songs:
            if violator_songs[count_list_in_list][0] == current_song:
                sum_time += violator_songs[count_list_in_list][1]
                break
            count_list_in_list += 1
    return sum_time


N = int(input("Сколько песен выбрать? "))
sum_time = tracks_len(N)
print("Общее время звучания песен:", round(sum_time, 2), "минут")
