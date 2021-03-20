from main.views import BookViewSet, JournalViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BookViewSet)
router.register('journals', JournalViewSet)
urlpatterns = router.urls