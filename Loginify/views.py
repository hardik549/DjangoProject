from django.shortcuts import render, redirect
from .models import UserDetails
from django.contrib import messages
from rest_framework.decorators import api_view
from .serializers import UserDetailsSerializer
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import json

def hello_world(request):
    return HttpResponse("Hello World!!!")

# View for signup
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('signup')
        
        user = UserDetails(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Signup successful! Please log in.')
        return redirect('login')
    return render(request, 'signup.html')

# View to login
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = UserDetails.objects.get(email=email, password=password)
            messages.success(request, f'Welcome, {user.username}!')
            return render(request, 'login_success.html', {'user': user})

        except UserDetails.DoesNotExist:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    return render(request, 'login.html')

# View to get all user details
@api_view(['GET'])
def get_all_users(request):
    if request.method == 'GET':
        try:
            all_users = UserDetails.objects.all()
            serializer_data = UserDetailsSerializer(all_users, many=True)
            return JsonResponse(serializer_data.data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)})
        
# View to get a single user by email
@api_view(['GET'])
def get_user_by_email(request, email):
    if request.method == 'GET':
        try:
            user_by_email = UserDetails.objects.get(email=email)
            serializer_data = UserDetailsSerializer(user_by_email)
            return JsonResponse(serializer_data.data, safe=False)
        except UserDetails.DoesNotExist:
                    return Response({'error': 'User not found'}, status=404)

# View to update a user's details
@api_view(['PUT'])
def update_user(request, email):
    if request.method == 'PUT':
        try:
            user_data = UserDetails.objects.get(email=email)
            input_data= json.loads(request.body)
            serializer_data = UserDetailsSerializer(user_data, data=input_data)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({'message': 'User data updated successfully'}, status=200)
            else:
                return JsonResponse(serializer_data.errors, status=400)
        except UserDetails.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

# View to update a partial user's details
@api_view(['PATCH'])
def update_partial_user(request, username):
    if request.method == 'PATCH':
        try:
            user_data = UserDetails.objects.get(username=username)
            input_data= json.loads(request.body)
            serializer_data = UserDetailsSerializer(user_data, data=input_data, partial=True)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({'message': 'User data updated successfully'}, status=200)
            else:
                return JsonResponse(serializer_data.errors, status=400)
        except UserDetails.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

@api_view(['DELETE'])
def delete_user(request, username):
    if request.method == 'DELETE':
        try:
            user_data = UserDetails.objects.get(username=username)
            user_data.delete()
            return JsonResponse({'message': 'User deleted successfully'}, status=204)
        except UserDetails.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)