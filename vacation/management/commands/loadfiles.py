from django.core.management import BaseCommand, CommandError
from django.conf import settings
import subprocess
from vacation.models import Image, Gallery


class Command(BaseCommand):
    args = '<extension extension ...>'
    help = 'loads files with given extensions'

    def handle(self, *args, **options):
        for g in Gallery.objects.all():
            dir_name =  settings.LOCAL_RESOURCE + g.dir_name
            try:
                self.stdout.write('Processing %s' % dir_name)
                files = subprocess.check_output(['ls', '%s' % dir_name]).split('\n')
            except subprocess.CalledProcessError:
                raise CommandError('Directory "%s" does not exist' % dir_name)
            else:
                for file in files:
                    for extension in args:
                        if file[-len(extension):] == extension:
                            filename = file[0:len(file)-len(extension)-1]
                            if Image.objects.filter(filename=filename, extension=extension, gallery_id=g.id) > 0:
                                self.stdout.write('Skipping file: %s' % file)
                                break
                            image = Image.objects.create(gallery_id=g.id)
                            image.filename = filename
                            image.extension = extension
                            self.stdout.write('Processed file: %s' % image.filename)
                            image.save()
                            break

                    
