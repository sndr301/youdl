from rest_framework import views
from youtube_dl import YoutubeDL
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from rest_framework.response import Response

class GetUrl(views.APIView):
    parser_classes = ( MultiPartParser, FormParser, JSONParser)

    def post(self, request, *args, **kwargs):
    	content = {}
    	youtube = YoutubeDL()
        you_id = request.data['ID']
        if len(you_id) != 11:
        	return Response(status=404)
        you_url = "http://youtube.com/watch?v=" + you_id
        try:
            info = youtube.extract_info(you_url, download=False)
        except:
            return Response(status=404)
        content['url'] = info['url']
        return Response(content)


get_url = GetUrl.as_view()