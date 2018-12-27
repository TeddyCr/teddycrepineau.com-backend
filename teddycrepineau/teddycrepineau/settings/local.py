from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY'
                , default='_zm7xfgpfvi%+xl29=*rm4i0*54s9@@i4d43$hz)btid#)ilkp')

DEBUG = env.bool('DJANGO_DEBUG', default=True)

