from django.core.management import BaseCommand, CommandError
from django.conf import settings
import subprocess
from vacation.models import Image, Gallery


class Command(BaseCommand):
    def handle(self, *args, **options):
        extensions = ['jpg', 'png', ]
        HELP_MSG = 'Usage: ./manage.py loadfiles <dir_name>\nAccepts extensions: %s' % extensions

        if len(args) == 1:
            g = Gallery.objects.get(dir_name=args[0])
        else:
            raise CommandError(HELP_MSG)
        dir_name =  settings.LOCAL_RESOURCE + g.dir_name
        try:
            self.stdout.write('Processing %s' % dir_name)
            files = subprocess.check_output(['ls', '%s' % dir_name]).split('\n')
            tn_dir = subprocess.check_output(['mkdir', '-p', '%s/tn' % dir_name]).split('\n')
        except subprocess.CalledProcessError:
            raise CommandError('Directory "%s" does not exist' % dir_name)
        else:
            for file in files:
                filename, ext = '.'.join(file.split('.')[:-1]), file.split('.')[-1]
                if ext.lower() in extensions:
                    if Image.objects.filter(filename=filename).filter(extension=ext).filter(gallery_id=g.id).exists():
                        self.stdout.write('Skipping file: %s\n' % file)
                    else:
                        image = Image.objects.create(gallery_id=g.id)
                        image.filename = filename
                        image.extension = ext
                        self.stdout.write('Processed file: %s\n' % image.filename)
                        image.save()

                    subprocess.check_output(['convert', '-thumbnail', '200', '%s/%s' % (dir_name, file), '%s/tn/%s' % (dir_name, file)])
