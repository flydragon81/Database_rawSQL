"""
name
"""
x_file_pattern = '"XPS (*.xps, *.x, *.XPS, *.X )"'
s_file_pattern = '"SPS (*.sps, *.s, *.SPS, *.S )"'
r_file_pattern = '"RPS (*.rps, *.r, *.RPS, *.R )"'
sps_file_pattern='"RPS (*.rps, *.r, *.RPS, *.R );;SPS (*.sps, *.s, *.SPS, *.S );;XPS (*.xps, *.x, *.XPS, *.X )"'
db_file_pattern = '"SQLite (*.sqlite )"'

'''
table config
'''
point_table_content = '''(
                        line real NOT NULL,
                        point real NOT NULL,
                        idx int NOT NULL,
                        easting real NOT NULL,
                        northing real NOT NULL,
                        elevation real NOT NULL,
                        PRIMARY KEY(line, point, idx)'''
relation_table_content = '''(
                        line real NOT NULL,
                        point real NOT NULL,
                        idx int NOT NULL,
                        relation array NOT NULL,
                        PRIMARY KEY(line, point, idx)'''
table_dict = {'R': point_table_content,
              'S': point_table_content,
              'X': relation_table_content
              }

# SQL_CREATE_TABLE = """ CREATE TABLE IF NOT EXISTS  {}{}
# ); """.format(list(table_dict.keys())[0], table_dict[list(table_dict.keys())[0]])
#
# print(SQL_CREATE_TABLE)
