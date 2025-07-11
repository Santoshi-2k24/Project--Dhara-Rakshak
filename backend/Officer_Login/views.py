from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.hashers import make_password, check_password

from .models import Officer
from .serializers import Officer_Serializer

class OfficerLoginView(APIView):
    def post(self, request):
        officer_id = request.data.get("id")
        password = request.data.get("password")

        if not officer_id or not password:
            return Response({"error": "ID and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            officer = Officer.objects.get(id=officer_id)
            if check_password(password, officer.password):  # ✅ compare hashed
                return Response({"message": "Login successful", "officer": officer.name})
            else:
                return Response({"error": "Invalid password."}, status=status.HTTP_401_UNAUTHORIZED)
        except Officer.DoesNotExist:
            return Response({"error": "Officer ID not found."}, status=status.HTTP_404_NOT_FOUND)

class OfficerCreateView(APIView):
    permission_classes = [permissions.IsAdminUser]  # ✅ only admins can access this view

    def post(self, request):
        data = request.data.copy()
        raw_password = data.get('password')
        if raw_password:
            data['password'] = make_password(raw_password)  # ✅ hash the password

        serializer = Officer_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Officer created successfully.", "officer": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
