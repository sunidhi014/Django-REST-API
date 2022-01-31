from jobpotral.viewsets import JobViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('job',JobViewset)