from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            password=password,
            username=username,
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=8, 
        blank=False, 
        unique=True
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        # ordering = ('-date_joined')

    def __str__(self):
        return self.username

    def get_full_name(self):        
        return self.username

    def get_short_name(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_superuser

    
    # 사용자 구분용 필드 중복되지 않게 유니크 필드만 가능하다.
    USERNAME_FIELD = 'username'

    # createsuperuser에서 요구하는 필드
    # 비밀번호와 USERNAME_FIELD에서 지정한 항목은 기본으로 적용되며 
    # 그 외에 추가로 더 입력해야 하는 필드를 추가한다.
    REQUIRED_FIELD = ['email']

    
    objects = CustomUserManager()




