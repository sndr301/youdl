from rest_framework import views
from youtube_dl import YoutubeDL
from youtube_dl.version import __version__
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from rest_framework.response import Response

class GetUrl(views.APIView):
    parser_classes = ( MultiPartParser, FormParser, JSONParser)

    def post(self, request, *args, **kwargs):
    	content = {}
    	youtube = YoutubeDL()
        you_id = request.data['url']
        try:
            info = youtube.extract_info(you_id, download=False)
        except:
            return Response(status=404)
        content['version'] = __version__
        content['url'] = info['url']
        return Response(content)


get_url = GetUrl.as_view()