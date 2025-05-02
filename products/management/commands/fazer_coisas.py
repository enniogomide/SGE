from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Faz coisas'

    def handle(self, *args, **options):
        self.stdout.write('Começando a fazer as coisas...')
        # Aqui você pode adicionar a lógica que deseja executar
        self.stdout.write('Coisas feitas com sucesso!')
