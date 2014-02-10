import xmltodict


class Response(object):
    transformer = None

    def __init__(self, content):
        self.content = content

    def parse(self):
        data = xmltodict.parse(self.content)
        return self.transformer.transform(data)
