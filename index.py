import sqlite3, os
from modules import intro, dotnet, interview
import common
import createDB
checkpoint = ["intro", 0]

if not os.path.exists('state.db'):
    createDB.create()


# Create table
while True:
    # Get Current Checkpoint
    conn = sqlite3.connect('state.db')
    cur = conn.cursor()
    cur.execute('''SELECT module, number FROM checkpoints ORDER BY Timestamp DESC LIMIT 1''')
    checkpoint = cur.fetchall()[0]
    conn.close()
    if checkpoint[0] == "__finished__":
        break

    # Run Module at checkpoint
    try:
        locals()[checkpoint[0]].main(checkpoint[1], common)
    except KeyError:
        print(Exception("Module "+str(checkpoint[0])+" not found!"))

print(r"""
             .#############. 
          .###################. 
       .####%####################.,::;;;;;;;;;;, 
      .####%###############%######:::;;;;;;;;;;;;;, 
      ####%%################%######:::;;;;;;;;@;;;;;;, 
      ####%%################%%#####:::;;;;;;;;;@;;;;;;, 
      ####%%################%%#####:::;;;;;;;;;@@;;;;;; 
      `####%################%#####:::;;;;;;;;;;@@;;;;;; 
        `###%##############%####:::;;;;;;;;;;;;@@;;;;;; 
           `#################'::%%%%%%%%%%%%;;;@;;;;;;' 
             `#############'.%%%%%%%%%%%%%%%%%%;;;;;' 
               `#########'%%%%#%%%%%%%%%%%%%%%%%%%, 
                 `#####'.%%%%#%%%%%%%%%%%%%%#%%%%%%, 
                   `##' %%%%##%%%%%%%%%%%%%%%##%%%%% 
                   ###  %%%%##%%%%%%%%%%%%%%%##%%%%% 
                    '   %%%%##%%%%%%%%%%%%%%%##%%%%% 
                   '    `%%%%#%%%%%%%%%%%%%%%#%%%%%' 
                  '       `%%%#%%%%%%%%%%%%%#%%%%' 
                  `         `%%%%%%%%%%%%%%%%%%' 
                   `          `%%%%%%%%%%%%%%' 
                    `           `%%%%%%%%%%'  ' 
                     '            `%%%%%%'   ' 
                    '              `%%%'    ' 
                   '               .%%      ` 
                  `                %%%       ' 
                   `                '       ' 
                    `              '      ' 
                    '            '      ' 
                   '           '       ` 
                  '           '        ' 
                              `       ' 
                               ' 
                              ' 
                             ' 
        Congrats!!! You finished the training!! Bravo!
""")


