from django.contrib import admin
from .models import pacientes, consultas, especialidade, medico_especialidade, medicos, prontuarios
# Register your models here.


admin.site.register(pacientes)
admin.site.register(consultas)
admin.site.register(especialidade)
admin.site.register(medico_especialidade)
admin.site.register(medicos)
admin.site.register(prontuarios)