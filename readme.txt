Task description
----------------

BpCoding Dojo / Songkata challenge solution (offline):
https://github.com/BpCodingDojo/SongKata/blob/master/README.md


Solution
--------

Python 3. solution using only pandas module as extra. Implementing using
TDD approach via pytest and VS Code.

TDD steps
---------

Some test cases are deprecated during the TDD process as new
steps are covering them fully.

+ can return a number: test_can_call_solution() [DEPRECATED]
+ can read header row from file: test_can_read_header_line() [DEPRECATED]
+ can check file open error: test_can_check_if_file_exists()
+ can interpret header: test_can_read_header()
+ can detect if header is invalid: test_can_detect_missing_header_param()
+ can detect if header is invalid: test_can_detect_non_num_header_param()
+ can interpret song lines: test_can_read_song_list()
+ can detect if song lines are invalid: test_can_detect_non_num_in_song_list()
+ can return ordered hit list: test_can_rate_song()
+ can tolerate lose data format: test_can_tolerate_lose_formatting()
