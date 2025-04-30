from django.core.management.base import BaseCommand
from faker import Faker # type: ignore
import random
from apps.accounts.models import CustomUser

fake = Faker()

class Command(BaseCommand):
    help = "Populate dummy user data"

    def handle(self, *args, **options):
        # create dummy users
        for _ in range(5):
            user = CustomUser.objects.create_user(
                username=fake.user_name()[:20],
                email=fake.email(),
                password='password',
                phone_number=fake.phone_number()[:20],
                gender=random.choice(['male', 'female'])
            )
        self.stdout.write(self.style.SUCCESS("Created 5 Users"))