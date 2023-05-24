# Generated by Django 3.2.18 on 2023-05-16 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Ad')),
                ('image', models.ImageField(upload_to='media/team', verbose_name='Şəkil')),
                ('program', models.CharField(max_length=256, verbose_name='İştirak etdiyi program')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Ad')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('number', models.CharField(max_length=20, verbose_name='Telefon nömrəsi')),
                ('message', models.TextField(max_length=2000, verbose_name='Mesaj')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Involved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Ad')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('number', models.CharField(max_length=20, verbose_name='Telefon nömrəsi')),
                ('membership_type', models.CharField(choices=[('1', 'Become *'), ('2', 'Speaker'), ('3', 'Partner'), ('4', 'Member')], default='Become *', max_length=256, verbose_name='Membership type')),
                ('message', models.TextField(max_length=2000, verbose_name='Mesaj')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/partners', verbose_name='Logo')),
            ],
        ),
        migrations.CreateModel(
            name='Statitics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('events', models.IntegerField(default=0, verbose_name='Events')),
                ('members', models.IntegerField(default=0, verbose_name='Members')),
                ('collaborations', models.IntegerField(default=0, verbose_name='Collaborations')),
                ('participants', models.IntegerField(default=0, verbose_name='Participants')),
                ('initiatives', models.IntegerField(default=0, verbose_name='Initiatives')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Ad')),
                ('image', models.ImageField(upload_to='media/team', verbose_name='Şəkil')),
                ('positions', models.CharField(max_length=256, verbose_name='Vəzifə')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('linkedin_link', models.CharField(max_length=200, verbose_name='Linkedin link')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
