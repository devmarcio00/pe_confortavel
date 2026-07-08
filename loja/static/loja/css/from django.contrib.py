from django.contrib.auth import get_user_model

User = get_user_model()

for user in User.objects.all():
    print(user.username, user.email, user.is_superuser)