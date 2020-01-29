import pandas as pd
import pytest
from songs import rate_songs, _read_header, _read_song_list

def test_can_check_if_file_exists():
    with pytest.raises(FileNotFoundError):
        _read_header('data\\not_existing_file.dat')

def test_can_read_header():
    assert _read_header('data\\sample_4_2.dat') == 2 

def test_can_detect_missing_header_param():
    with pytest.raises(ValueError):
        _read_header('data\\sample_missing_header_param.dat')

def test_can_detect_non_num_header_param():
    with pytest.raises(ValueError):
        _read_header('data\\sample_not_num_header_param.dat')

def test_can_read_song_list():
    songs = _read_song_list('data\\sample_4_2.dat')
    print(songs.values.tolist())
    assert songs.values.tolist() == \
        [[30, 'one'], [30, 'two'], [15, 'three'], [25, 'four']]

def test_can_detect_non_num_in_song_list():
    with pytest.raises(ValueError):
        _read_song_list('data\\sample_not_num_in_song_list.dat')

def test_can_rate_song():
    assert rate_songs('data\\sample_15_3.dat') == \
        ['19_2000', 'clint_eastwood', 'tomorrow_comes_today']

def test_can_tolerate_lose_formatting():
    assert rate_songs('data\\sample_4_2_with_spaces.dat') == \
        ['four', 'two']
