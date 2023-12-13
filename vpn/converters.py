class SlashStrip:
    regex = ".*"

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value.lstrip("/")
