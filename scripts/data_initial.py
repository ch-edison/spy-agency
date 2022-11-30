# scripts/data_initial.py
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from apps.users.models import User
from apps.system_hits.models import Hit


def create_users(type_user, i, hitmen_group, manager_group, boss_group):
    name = type_user + str(i)
    user, created = User.objects.get_or_create(
        email=name + "@spy.com",
        name=name,
        username=name
    )
    if created:
        user.set_password('password12345')
        user.save()
    if type_user == "hitmen":
        hitmen_group.user_set.add(user.pk)
    if type_user == "manager":
        manager_group.user_set.add(user.pk)
    if type_user == "boss":
        boss_group.user_set.add(user.pk)
    return user


def run():
    hitmen_group, created = Group.objects.get_or_create(name="Hitmen")
    manager_group, created = Group.objects.get_or_create(name="Manager")
    boss_group, created = Group.objects.get_or_create(name="Boss")

    content_type = ContentType.objects.get_for_model(Hit)
    post_permission = Permission.objects.filter(content_type=content_type)
    print([perm.codename for perm in post_permission])
    # => ['add_post', 'change_post', 'delete_post', 'view_post']

    for perm in post_permission:
        if perm.codename == "add_hit":
            boss_group.permissions.add(perm)
            manager_group.permissions.add(perm)

        elif perm.codename == "change_post":
            hitmen_group.permissions.add(perm)
            boss_group.permissions.add(perm)
        else:
            manager_group.permissions.add(perm)
            hitmen_group.permissions.add(perm)
            boss_group.permissions.add(perm)
    number_users_hitmen = 9
    number_users_manager = 3
    number_users_boss = 1

    list_user_hitmen_created = [
        create_users("hitmen", i, hitmen_group, manager_group, boss_group)
        for i in range(1, number_users_hitmen)
    ]
    list_user_manager_created = [
        create_users("manager", i, hitmen_group, manager_group, boss_group)
        for i in range(1, number_users_manager)
    ]
    list_user_boss_created = [
        create_users("boss", i, hitmen_group, manager_group, boss_group)
        for i in range(1, number_users_boss+1)
    ]

    print(list_user_hitmen_created)
    print(list_user_manager_created)
    print(list_user_boss_created)


