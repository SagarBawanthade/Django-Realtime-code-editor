import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import editor.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(editor.routing.websocket_urlpatterns),
})
