# Generated by Django 2.2.7 on 2019-12-20 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Rating', models.IntegerField()),
                ('Date', models.DateTimeField(max_length=100)),
                ('Feedback', models.CharField(max_length=100)),
            ],
        ),
    ]
