from django.core.management.base import NoArgsCommand
from pyftpdlib import ftpserver
from ftpd.django_authorizer import DjangoAuthorizer

class Command(NoArgsCommand):
    help = "Runs a FTP daemon"

    def handle_noargs(self, **options):
        handler = ftpserver.FTPHandler
        handler.authorizer = DjangoAuthorizer()
        address = ("0.0.0.0", 21)
        ftpd = ftpserver.FTPServer(address, handler)
        ftpd.serve_forever()
