from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from eagle.models import SiteDeNoticias
from eagle.serializers import WebSiteSerializer


class SiteDeNoticiasList(APIView):
    def get(self, request):
        sites = SiteDeNoticias.objects.all()
        serializer = WebSiteSerializer(sites, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WebSiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SiteDeNoticiasDetail(APIView):
    def get_object(self, pk):
        try:
            return SiteDeNoticias.objects.get(pk=pk)
        except SiteDeNoticias.DoesNotExist:
            return None

    def get(self, request, pk):
        site = self.get_object(pk)
        if site:
            serializer = WebSiteSerializer(site)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        site = self.get_object(pk)
        if site:
            serializer = WebSiteSerializer(site, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        site = self.get_object(pk)
        if site:
            site.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
