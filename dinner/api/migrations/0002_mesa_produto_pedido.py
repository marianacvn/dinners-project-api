# Generated by Django 4.1 on 2022-08-05 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statusmesa', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeproduto', models.CharField(max_length=100)),
                ('descricaoproduto', models.CharField(max_length=200)),
                ('preco', models.FloatField()),
                ('linkimagem', models.CharField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.cliente')),
                ('mesa', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.mesa')),
                ('produto', models.ManyToManyField(to='api.produto')),
            ],
        ),
    ]
