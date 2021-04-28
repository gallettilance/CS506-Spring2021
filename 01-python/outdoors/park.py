from random import choices

# helper function to draw a garden
def draw_garden(season):
    ''' takes: season as a string ('spring', 'summer', 'fall', or 'winter')
        returns:
            
        prints semi-random garden, based on season
    '''
    
    # lists containing each line for ascii printed items
    # all 6 lines high
    height = 6
    
    tulip = ['   ','|WW|','\__/',' || ','\||/','wWWw']
    cosmos = ['       ',' _.-._ ', '/ \_/ \\',
              '>-(_)-<','\_/ \_/', "Ww'-'wW"]
    grass = ['     ','     ','     ',
             '     ','     ','wWwwW']
    dirt = ['     ','     ','     ',
             '     ','     ','.v..V']
    acorn = ['       ',' .=|=. ','(XXXXX)',
             ' |   | ',' \   / ',"  '+'  "]
    snow = ['     ','     ','     ',
             '     ','     ','*****']
    snowman = ['   ___   ',' _|___|_ ',"  ('-')  ",
               ' (  .  ) ','(   .   )','*********']        
    
    # sets appropriate objects and weights per season
    if season == 'spring':
        adjective = 'flowery'
        items = [tulip, cosmos, grass]
        weights = [0.5,0.4,0.1]
        
    elif season == 'summer':
        adjective = 'very green'
        items = [tulip, cosmos, grass]
        weights = [0.05,0.45,0.5]
        
    elif season == 'fall':
        adjective = 'fall-ish'
        items = [dirt, cosmos, grass, acorn]
        weights = [0.3,0.1,0.2,0.4]
        
    elif season == 'winter':
        adjective = 'snowy'
        items = [snowman, snow, acorn]
        weights = [0.55,0.4,0.05]
        
    else:
        print('garden not found: season unknown')
        return
    
    # builds three appropriate items
    item1 = choices(items, weights)[0]
    item2 = choices(items, weights)[0]
    item3 = choices(items, weights)[0]
    
    for i in range(height):
        print(item1[i], item2[i], item3[i])
    
    print('This is a', adjective, 'garden')
    
    return

# helper function to draw a bench
def draw_bench():
      
    print('    _._._ ','   {_|_|_}','   /____/|',"***|'   | ***",sep='\n')
    print('This is a bench')
        
    return

# park with two gardens and a bench
def draw_park():
    
    # choose season
    season = choices(['spring', 'summer', 'fall', 'winter'])[0]
    
    draw_garden(season)
    print('---')
    
    draw_bench()
    print('---')
    
    draw_garden(season)
    
    return