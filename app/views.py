from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class IndexPageAPIView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the Index Page"}, status=status.HTTP_200_OK)


class HomePageAPIView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the Home Page"}, status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # Dummy authentication check
        if username == "admin" and password == "password":
            return Response({"message": "Login successful", "token": "fake-jwt-token"}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class TextAPIView(APIView):
    def get(self, request):
        return Response({"data": "Sample text response"}, status=status.HTTP_200_OK)


class ImageAPIView(APIView):
    def get(self, request):
        return Response({"image_url": "https://example.com/sample-image.jpg"}, status=status.HTTP_200_OK)


class CodeAPIView(APIView):
    def get(self, request):
        return Response({"code_snippet": "print('Hello, API!')"}, status=status.HTTP_200_OK)


class SettingsAPIView(APIView):
    def get(self, request):
        return Response({"settings": {"theme": "dark", "notifications": True}}, status=status.HTTP_200_OK)
