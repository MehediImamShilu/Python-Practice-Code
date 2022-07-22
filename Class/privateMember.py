# NOTE: This code might have some problem but it works
# :D
# How to use tag as private memeber

class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.____tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
print(cloud._TagCloud__tags)
