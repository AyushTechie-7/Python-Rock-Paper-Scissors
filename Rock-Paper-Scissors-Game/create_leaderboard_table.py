# import sqlite3

# # Connect to the LeaderBoard database
# conn = sqlite3.connect('LeaderBoard.db')
# cursor = conn.cursor()

# # Create the LEADERBOARD table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS LEADERBOARD (
#     firstname TEXT NOT NULL,
#     GamesWon INTEGER DEFAULT 0,
#     GamesLost INTEGER DEFAULT 0,
#     GamesTied INTEGER DEFAULT 0,
#     GamesPlayed INTEGER DEFAULT 0,
#     WiningRate REAL DEFAULT 0
# )
# """)

# conn.commit()
# conn.close()

# print("✅ Leaderboard table created successfully!")
