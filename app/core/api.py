from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import CardSerializer, BankAccountSerializer, TransactionSerializer
from rest_framework import viewsets, mixins
from .models import Card, BankAccount, Transaction

# class CardViewSet(mixins.CreateModelMixin,
#                                 mixins.ListModelMixin,
#                                 mixins.RetrieveModelMixin,
#                                 viewsets.GenericViewSet):
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer
    
#     def create(self, request):
#         print(request.data)
#         return data, status=status.HTTP_200_OK

class CardView(APIView):
    def post(self, request):
        print(request.data)
        post_data = request.data
        card_number = post_data['card_number'][0]
        event_type = post_data['event_type'][0]
        if event_type == "top_up":
            pass
        elif event_type == "payment":
            pass
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response({"data": serializer.data})
    


# @api_view(['POST'])
# def deposit(reqest):
#     try:
#         amount = int(request.GET.get('amount'))
#     except (KeyError, ValueError):
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     with transaction.atomic():
#         try:
#             account = (
#                 Account.objects
#                 .select_for_update()
#                 .get(user=request.user)
#             )
#         except Account.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         try:
#             account.deposit(
#                 amount=amount,
#                 deposited_by=request.user,
#                 asof=timezone.now()
#             )
#         except (ExceedsLimit, InvalidAmount):
#             return response(status.HTTP_400_BAD_REQUEST)
#         return Response(status=status.HTTP_200_OK)