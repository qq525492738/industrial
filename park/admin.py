from .models import ParkClassify, ParkCategory, Park, Investment, Factory, FactoryRelease
import xadmin
# Register your models here.


xadmin.site.register(ParkClassify)
xadmin.site.register(ParkCategory)
xadmin.site.register(Park)
xadmin.site.register(Investment)
xadmin.site.register(Factory)
xadmin.site.register(FactoryRelease)
