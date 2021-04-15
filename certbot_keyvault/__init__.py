import datetime
import logging
import os
from typing import List

import azure.functions as func


class Config:

    def __init__(self):
        domains = os.getnev('domains', '')
        if instance(domains, str):
            self._domains = domains.split(',')
        elif instance(domains, List):
            self._domains = domains
        else:
            raise ValueError("invalid domains")
        self._domains = [domain.strip().lower() for domain in self._domains
                         if instance(domain, str) and domain.strip() != '']

        cert_name = os.getenv('cert_name', '')
        if cert_name == '':
            if len(self._domains) > 0:
                self._cert_name = Config._trim_wildcard(self._domains[0])
            else:
                self._cert_name = ''
        else:
            self._cert_name = cert_name.lower()

    def _trim_wildcard(cls, domain):
        if domain.startswith('*.'):
            return domain[2:]
        return domain


def certonly():
    pass


def main(mytimer: func.TimerRequest) -> None:
    certonly()
    logging.info('OK')
