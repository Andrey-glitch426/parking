from parkingSession import *
from tariff import *
import datetime

class ParkingManager:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__activeSessions = []
        self.__closeSessions = []
        self.__tariffes = self.loadTariffes()

    def loadTariffes(self):
        tariffes = []
        with open('fileTariff.txt') as file:
            for line in file:
                minutes, rate = list(map(int, line.split()))
                tariff = Tariff(minutes, rate)
                tariffes.append(tariff)
        return tariffes


    def freePlaces(self):
        return self.__capacity - len(self.__activeSessions)

    def nextTicketNumber(self):
        return max((session.ticketNumber for session in self.__activeSessions), default=0) + 1
        #return max(self.__activeSessions, key=lambda session: session.ticketNumber, default=0) + 1

    def enterParking(self, carNumber):
        if self.freePlaces() == 0:
            return None
        if next((session for session in self.__activeSessions if session.carNumber == carNumber), None) is not None:
            return None
        now = datetime.datetime.today()
        ticketNumber = self.nextTicketNumber()
        session = ParkingSession(now, carNumber, ticketNumber)
        self.__activeSessions.append(session)

