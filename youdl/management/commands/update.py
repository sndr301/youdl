# vim: set ts=8 sw=4 sts=4 et ai:
import logging
log = logging.getLogger(__name__)

from optparse import make_option
from django.core.management.base import BaseCommand
from django.utils.six.moves import input
from 


class Command(BaseCommand):
    help = 'Update the youtube-dl binaries'
    # respect the language setting
    leave_locale_alone = True

    def handle(self, *args, **qwargs):
        