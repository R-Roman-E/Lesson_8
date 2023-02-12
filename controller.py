import modul
import view

def randomdict():
    modul.subjgenerator()
    modul.namegenerator()
    modul.markgenerator()

def go():
    
    print('\n')
    pick = view.start()
    if pick == 12:
        return 0
    if pick == 1:
        modul.addstudent()
        print('\n')
        return go()
    if pick == 2:
        modul.addsubject()
        print('\n')
        return go()
    if pick == 3:
        modul.mark()
        print('\n')
        return go()
    if pick == 4:
        modul.showstudents()
        print('\n')
        return go()
        
    if pick == 5:
        modul.showmarks()
        print('\n')
        return go()
        
    if pick == 6:
        modul.showsubj()
        print('\n')
        return go()
    if pick == 7:
        randomdict()
        return go()
    if pick == 8:
        modul.avgmark()
        print('\n')
        return go()
    if pick == 9:
        modul.globalavg()
        print('\n')
        return go()
    if pick == 10:
        modul.goldmedal()
        print('\n')
        return go()
    if pick == 11:
        modul.importer()
        print('\n')
        return go()
    
    else:
        print('Некорректый ввод \n')
        return go()
