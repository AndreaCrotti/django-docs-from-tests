# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiCall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_time', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headers', models.CharField(max_length=1024)),
                ('path', models.CharField(max_length=128)),
                ('method', models.CharField(default=b'GET', max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headers', models.CharField(max_length=1024)),
                ('content', models.TextField()),
                ('status_code', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestReportResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('docstring', models.TextField(null=True, blank=True)),
                ('name', models.CharField(max_length=128)),
                ('passed', models.BooleanField()),
                ('calls', models.ManyToManyField(to='django_docs_from_tests.ApiCall')),
                ('queries', models.ManyToManyField(to='django_docs_from_tests.Query')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='apicall',
            name='request',
            field=models.ForeignKey(to='django_docs_from_tests.Request'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='apicall',
            name='response',
            field=models.ForeignKey(to='django_docs_from_tests.Response'),
            preserve_default=True,
        ),
    ]
