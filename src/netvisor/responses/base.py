import xmltodict

from ..exc import NetvisorError


class Response(object):
    postprocessor = None

    def __init__(self, response):
        self.response = response
        self.data = self.parse()

    def parse(self):
        return xmltodict.parse(
            self.response.text,
            postprocessor=self.postprocessor,
            xml_attribs=False
        )

    def raise_for_failure(self):
        if not self.is_ok:
            raise NetvisorError.from_status(self.statuses[1])

    @property
    def statuses(self):
        return self.data['Root']['ResponseStatus']['Status']

    @property
    def is_ok(self):
        return self.statuses == 'OK'
