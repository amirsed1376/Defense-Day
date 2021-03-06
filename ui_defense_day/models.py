from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django_jalali.db import models as jmodels


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email=None, password=None, job=None, phone_number=None, name=None):
        print("job", job)
        user = self.model(
            username=username,
            job=job,
            phone_number=phone_number,
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_presenter(self, username, supervisor, email=None, password=None, job=None, phone_number=None, name=None):
        print("BBBBBBBB", supervisor)
        user = self.model(
            username=username,
            job=job,
            phone_number=phone_number,
            supervisor=supervisor,
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            job="admin",
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    USERNAME_FIELD = 'username'
    objects = UserManager()
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    state = (
        ('student', 'Student'),
        ('industry', 'Industry'),
        ('professor', 'Professor'),
        ('presenter', 'Presenter'),
        ('admin', 'Admin')

    )
    job = models.CharField(max_length=11, choices=state, default="student", null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    REQUIRED_FIELDS = []

    def __str__(self):
        return '({})'.format(self.username)

    class Meta:
        verbose_name = 'user'


class Professor(User):
    class Meta:
        verbose_name = 'Professor'


class Student(User):
    class Meta:
        verbose_name = 'Student'


class Presenter(User):
    supervisor = models.ForeignKey(Professor, related_name="SupervisorProfessor", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Presenter'


class Industry(User):
    class Meta:
        verbose_name = 'Industry'


class RoleCoefficent(models.Model):
    state = (
        ('student', 'Student'),
        ('industry', 'Industry'),
        ('supervisor', 'Supervisor'),
        ('professor', 'Professor'),
        ('admin', 'Admin')

    )
    job = models.CharField(max_length=20, choices=state , unique=True)
    coefficent = models.IntegerField()

    def __str__(self):
        return self.job

class Document(models.Model):
    presenter = models.OneToOneField(Presenter, on_delete=models.CASCADE)
    file1 = models.FileField(upload_to="document/", null=True, blank=True)
    file2 = models.FileField(upload_to="document/", null=True, blank=True)


class Score(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE,related_name="Score_user")
    presenter = models.ForeignKey(Presenter, on_delete=models.CASCADE )
    score = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        unique_together = ('user', 'presenter',)

class Event(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
