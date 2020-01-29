import pandas as pd

def rate_songs(file_name):
    ''' Kata task as defined:
    https://github.com/BpCodingDojo/SongKata/blob/master/README.md'''
    try:
        top_list_lgt = _read_header(file_name)
        songs = _read_song_list(file_name)
        top_list = _create_top_list(songs, top_list_lgt)
        return top_list
    except FileNotFoundError as e:
        raise FileNotFoundError('ERROR: Data file can\'t be found.')
    except ValueError as e:
        raise ValueError('ERROR: Data format is invalid.')

def _read_header(file_name):
    top_list_lgt = pd.read_csv(file_name, delimiter=r'\s+', header=None, nrows=1,
        names=['SongListLgt', 'TopListLgt'], dtype={'SongListLgt': 'int64', 'TopListLgt': 'int64'}
        ).loc[0]['TopListLgt']
    return top_list_lgt

def _read_song_list(file_name):
    songs = pd.read_csv(file_name, skiprows=1, skip_blank_lines=True, delimiter=r'\s+', 
        header=None, names=['Listened', 'Title'], dtype={'Listened': 'int64', 'Title': 'str'})
    return songs

def _create_top_list(songs, top_list_lgt):
    songs['AlbumIndex'] = songs.index.values + 1
    songs['Quality'] = songs['AlbumIndex'] * songs['Listened']
    sorted = songs.sort_values(['Quality', 'AlbumIndex'], ascending=[False, True])
    return sorted.head(top_list_lgt)['Title'].tolist()

if __name__ == '__main__':
    print('Top hits: {}'.format(rate_songs('data\\sample_15_3.dat')))
    print('Top hits: {}'.format(rate_songs('data\\sample_4_2.dat')))
