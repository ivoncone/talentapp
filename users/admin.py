from django.contrib import admin
from django.contrib.auth.models import Permission 
from users.models import User, Role
from company.models import Empresa
from intereses.models import State, Area, jobRole, Modalidad, tipoTrabajo
from members.models import (Persona, Gender, CivilStatus, DatosAcademicos, Status, NivelAcademico) 
from vacantes.models import Vacante
from applications.models import Application
from chat.models import Notification, Message

admin.site.register(User)
admin.site.register(Permission)


admin.site.register(Role)

admin.site.register(jobRole)
admin.site.register(Area)
admin.site.register(Modalidad)
admin.site.register(tipoTrabajo)
admin.site.register(State)

admin.site.register(Empresa)

admin.site.register(DatosAcademicos)
admin.site.register(NivelAcademico)
admin.site.register(Status)
admin.site.register(CivilStatus)
admin.site.register(Gender)
admin.site.register(Persona)

admin.site.register(Vacante)

admin.site.register(Application)

admin.site.register(Message)
admin.site.register(Notification)


