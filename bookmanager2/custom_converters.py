class PhoneConverter(object):
    regex = "1[3-9]\d{9}"

    def to_python(self, value):
        return int(value)+1

    def to_url(self, value):
        return value