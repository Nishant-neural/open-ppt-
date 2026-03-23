class PresentationConfig:
    def __init__(
        self,
        mode="default",          # student | startup | professional
        tone="clear",            # simple | detailed | persuasive
        length="medium",         # short | medium | long
        audience="general",      # beginner | technical | business
        theme="default"          # minimal | dark | pitch
    ):
        self.mode = mode
        self.tone = tone
        self.length = length
        self.audience = audience
        self.theme = theme