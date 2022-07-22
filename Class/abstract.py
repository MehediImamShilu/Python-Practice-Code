# An example of abstract base method

from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already close")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading from a network")


class MemoryStream(Stream):
    def read(self):
        print("Reading from a memory stream")


stream = MemoryStream()
stream.open()
