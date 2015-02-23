import csv
file = open('rock.csv')
rock_songs = csv.DictReader(file)

rel_in_81 = 0
rock_song_rows = []

for row in rock_songs:
    # add each row to list for sorting
    rock_song_rows.append(row)
    # track if released in 1981
    if row['Release Year'] == '1981':
        rel_in_81 += 1

print("songs from 1981: %s \n" % rel_in_81)

# Get top 20 songs by play count
sorted_songs = sorted(rock_song_rows, key = lambda song: song['PlayCount'], reverse = True)
top_20_songs_by_plays = sorted_songs[0:19]

for song in top_20_songs_by_plays:
    print(song['COMBINED'] + ' plays: ' + song['PlayCount'])

