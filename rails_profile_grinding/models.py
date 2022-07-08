from .model_templates import Template
from django.db import models


class SLM01_18045_MDE(Template):
    pass


class SLM11_06058_MDE(Template):
    pass


class SLM13_06260_MDE(Template):
    pass


class SLM15_06262_MDE(Template):
    pass


class SLM18_09742_MDE(Template):
    pass


class SLM20_09741_MDE(Template):
    pass


class SLM26_13996_MDE(Template):
    pass


class SLM27_14391_MDE(Template):
    pass


class SLM28_14390_MDE(Template):
    pass


class SLM29_14389_MDE(Template):
    pass


class SLM30_14388_MDE(Template):
    pass


class SLM31_14387_MDE(Template):
    pass


class SLM32_14386_MDE(Template):
    pass


class Specification(models.Model):
    prog_name = models.CharField(max_length=50)
    plant = models.CharField(max_length=50)
    target_process_time = models.FloatField()
    target_grinding_time = models.FloatField()
    target_dressing_time = models.FloatField()

    def __str__(self):
        return self.prog_name
