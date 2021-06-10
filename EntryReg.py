from datetime import datetime
def EntryLog(name):
    with open('EntryLog.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            daString = now.strftime('%Y-%m-%d')
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{daString},{dtString}')