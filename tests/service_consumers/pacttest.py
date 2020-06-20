from pact_test import ServiceConsumerTest, honours_pact_with, pact_uri, state

from service import producerService

host = 'https://pact.broker.url.domain.com:8443'
broker_url = '{host}/pacts/provider/{provider}/consumer/{consumer}/version/{consumerApplicationVersion}'.format(host=host,
    provider='pipeline-state-manager', consumer='consumer', consumerApplicationVersion='1.0.0')


@honours_pact_with('consumer')
@pact_uri('https://pact.broker.url.domain.com:8443/pacts/provider/python-producer/consumer/consumer/consumer'
          '-python-producer.json')
class ConsumerTest(ServiceConsumerTest):
    @state('inventory exists')
    def get_inventory(self):
        producerService.get_inventory()

    @state('create inventory')
    def create_inventory(self):
        data = dict(productName="Laptops", locationName="Bangalore", quantity=1000)
        producerService.save_inventory(data)
