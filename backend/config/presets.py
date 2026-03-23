from config.blueprint import PresentationConfig


def student_mode():
    return PresentationConfig(
        mode="student",
        tone="simple",
        length="short",
        audience="beginner"
    )


def startup_pitch_mode():
    return PresentationConfig(
        mode="startup",
        tone="persuasive",
        length="medium",
        audience="investors"
    )


def professional_mode():
    return PresentationConfig(
        mode="professional",
        tone="formal",
        length="detailed",
        audience="experts"
    )
