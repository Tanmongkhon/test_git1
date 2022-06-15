from conDB import Con2

class Action:
    def getHW():
        data = Con2.getHW()
        return data

    def updateStatusHW(ID, status,value):
        data = Con2.updateStatusHW(ID, status,value)
        return data

    def updateusers(ID, name, last_name):
        data = Con2.updateusers(ID, name, last_name)
        return data

    