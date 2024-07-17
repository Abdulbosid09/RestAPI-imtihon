from rest_framework import viewsets, filters
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.core.mail import send_mail
from django.conf import settings
from .models import Dars, Kurs, Izoh,User, LikeBosish
from .permission import DarsUchunPermission,KursUchunPermission
from .serializers import DarsSerializer,KursSerializer,IzohSerializer,UserSerializer,LikeSerializer,EmailSerializer




class KursViewSet(viewsets.ModelViewSet):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
    permission_classes = [KursUchunPermission]


class DarsViewSet(viewsets.ModelViewSet):
    queryset = Dars.objects.all()
    serializer_class = DarsSerializer
    permission_classes = [DarsUchunPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "izoh"]
    lookup_field = 'pk'

class IzohViewSet(viewsets.ModelViewSet):
    queryset = Izoh.objects.all()
    serializer_class = IzohSerializer
    permission_classes = [IsAuthenticated]

class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes =[IsAdminUser]

class LikeBosishQismi(APIView):
    def get(self, request, pk):
        likes = LikeBosish.objects.filter(like_or_dislike=True, dars_like_id=pk).count()
        dislikes = LikeBosish.objects.filter(like_or_dislike=False, dars_like_id=pk).count()
        
     
        return Response({
            "likes": likes,
            "dislikes": dislikes,
        
        })

class LikeBosish(APIView):
    def post(self, request):
        try:
            likes_or_dislikes = LikeBosish.objects.filter(author_id=request.data.get("author"))
            for l_or_d in likes_or_dislikes:
                l_or_d.delete()
        except:
            pass

        serializer = LikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        like_or_dislike = serializer.save()
        return Response(LikeSerializer(like_or_dislike).data)

class Email(APIView):
    def post(self, request):
        users = User.objects.all()
        user_email = [user.email for user in users]
        user_email.append("anosirjonov320@gmail.com")
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        send_mail(
            serializer.validated_data.get('title'),
            serializer.validated_data.get('message'),
            settings.EMAIL_HOST_USER,
            user_email,
            fail_silently=False,
        )
        return Response({"message": "Ajoyib👍"})
