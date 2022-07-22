# How to use tag in container

class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud["Python"] = 10    # for line 10
len(cloud)  # for line 13
cloud.add("Python")     # tag.lower() makes upper to lower
cloud.add("python")
cloud.add("python")
print(cloud.tags)
print(len(cloud))
