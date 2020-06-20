import subprocess

from pact_test import PactHelper


class ConsumerTestPactHelper(PactHelper):
    test_port = 8080
    process = None

    def setup(self):
        cmd = 'gunicorn start:app -w 3 -b :8080 --log-level error'
        self.process = subprocess.Popen(cmd, shell=True)

    def tear_down(self):
        self.process.kill()