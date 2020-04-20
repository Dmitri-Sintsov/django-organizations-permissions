from django.db import models
from django.contrib.auth.models import Permission, Group
from organizations.models import Organization

class OrganizationPermissionManager(models.Manager):

    def add_user(self, organization_name, user):
        org, created = Organization.objects.get_or_create(name=organization_name)
        # We will assign organization admin / owner manually in Django Admin.
        org.add_user(user, is_admin=False)
        return org, created

    def remove_user(self, organization_name, user):
        org, created = Organization.objects.get_or_create(name=organization_name)
        org.users.remove(user)
        return org, created

class OrganizationPermission(models.Model):
    name = models.CharField(max_length=100)
    organizations = models.ManyToManyField(
        Organization, 
        related_name='org_perm', 
        verbose_name='Organizations'
    )
    # Many Permission to many OrganizationPermission.
    permissions = models.ManyToManyField(
        Permission, verbose_name='Permissions'
    )

    objects = OrganizationPermissionManager()

    class Meta:
        verbose_name = 'Organization permission'
        verbose_name_plural = 'Organization permissions'

    def __str__(self):
        return '{}'.format(str(self.name))

class OrganizationStaffGroup(Group):
    organization = models.OneToOneField(
        Organization, 
        on_delete=models.CASCADE, 
        related_name='org_staff_groups', 
        null=False, 
        primary_key=True
    )

    def __str__(self):
        return '{} : {}'.format(str(self.organization), self.name)
