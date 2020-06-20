from pact_test import ServiceConsumerTest, honours_pact_with, pact_uri, state

from service import producerService

broker_url = 'https://ciqpact.cec.lab.emc.com:8443/pacts/provider/{provider}/consumer/{consumer}/version/{consumerApplicationVersion}'.format(
    provider='pipeline-state-manager', consumer='consumer', consumerApplicationVersion='1.0.0')


@honours_pact_with('consumer')
@pact_uri('https://ciqpact.cec.lab.emc.com:8443/pacts/provider/python-producer/consumer/consumer/consumer'
          '-python-producer.json')
class ConsumerTest(ServiceConsumerTest):
    @state('inventory exists')
    def get_inventory(self):
        producerService.get_inventory()

    @state('create inventory')
    def create_inventory(self):
        data = dict(productName="Laptops", locationName="Bangalore", quantity=1000)
        producerService.save_inventory(data)
