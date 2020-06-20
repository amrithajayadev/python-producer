# python-producer
A sample app for testing pact with a producer

# Prequisites
pip install pact-test
pip install pact-python

# How to run the tests?
Run the application locally in your IDE
Run the below command in the terminal
```
pact-verifier --provider-base-url=http://localhost:9099 --pact-url=pacts/consumer-python-producer.json --provider-states-url=http://localhost:9099/pact/provider_states/all --provi
der-states-setup-url=http://localhost:9099/pact/provider_states --pact-broker-url http://10.118.252.213:8500 --provider python-producer --provider-app-version 1.0.0 --publish-verification-results
```
pact-verifier comes with pact-python module.
--provider-base-url: The URL where the provider application is running
--pact-url: The location of pact files. Can be file path or broker URL where the pact file exists
--provider-states-url: pact-verifier makes calls to this endpoint for verification. Further reference: https://github.com/nikoly/pact-contract-test#implement-provider-state
--provider-states-setup-url: An endpoint implemented in this project to serve the requests when pact-verifier makes call to the above endpoint
--provider: provider application name
--provider-app-version: version
--pact-broker-url: base url to pact-broker
--publish-verification-results: publishes the results to the broker

On successful verification, you should be able to see something like below in the terminal
```
INFO: Fetching pacts for python-producer from http://10.118.252.213:8500
INFO: Reading pact at http://10.118.252.213:8500/pacts/provider/python-producer/consumer/consumer/version/1.0.0

Verifying a pact between consumer and python-producer
  Given inventory exists
    a request to get inventory
      with GET /api/inventory
        returns a response which
          has status code 200
          has a matching body
  Given create inventory
    a request to save inventory
      with POST /api/inventory
        returns a response which
          has status code 200
          has a matching body
          includes headers
            "Content-type" which equals "application/json"

2 interactions, 0 failures
INFO: Verification results published to http://10.118.252.213:8500/pacts/provider/python-producer/consumer/consumer/pact-version/8403a8f60e706f27aad148333a12fdd66c1a2f22/verification-results/112

INFO: Reading pact at pacts/consumer-python-producer.json

Verifying a pact between consumer and python-producer
  Given inventory exists
    a request to get inventory
      with GET /api/inventory
        returns a response which
          has status code 200
          has a matching body
  Given create inventory
    a request to save inventory
      with POST /api/inventory
        returns a response which
          has status code 200
          has a matching body
          includes headers
            "Content-type" which equals "application/json"

2 interactions, 0 failures
```
NOTE: A warning like 'WARN: Cannot publish verification for consumer as there is no link named pb:publish-verification-results in the pact JSON. If you are using a pact broker, please upgrade to version 2.0.0 or later.'
is likely to show in the terminal, but it is indeed published to the broker

Meanwhile, the interactions defined in the pact will get executed on the application and it can be observed like
```
127.0.0.1 - - [14/May/2020 07:00:07] "GET /api/inventory HTTP/1.1" 200 -
127.0.0.1 - - [14/May/2020 07:00:08] "POST /pact/provider_states HTTP/1.1" 200 -
127.0.0.1 - - [14/May/2020 07:00:09] "POST /api/inventory HTTP/1.1" 200 -
127.0.0.1 - - [14/May/2020 07:01:06] "POST /pact/provider_states HTTP/1.1" 200 -
127.0.0.1 - - [14/May/2020 07:01:07] "GET /api/inventory HTTP/1.1" 200 -
127.0.0.1 - - [14/May/2020 07:01:08] "POST /pact/provider_states HTTP/1.1" 200 -
127.0.0.1 - - [14/May/2020 07:01:09] "POST /api/inventory HTTP/1.1" 200 -
127.0.0.1 - - [14/May/2020 07:01:10] "POST /pact/provider_states HTTP/1.1" 200 -
127.0.0.1 - - [14/May/2020 07:01:11] "GET /api/inventory HTTP/1.1" 200 -
127.0.0.1 - - [14/May/2020 07:01:12] "POST /pact/provider_states HTTP/1.1" 200 -
127.0.0.1 - - [14/May/2020 07:01:13] "POST /api/inventory HTTP/1.1" 200 -
```
