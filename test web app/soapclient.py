from pysimplesoap.client import SoapClient

client = SoapClient(
    location='http://localhost:8000',
    trace=False
    )
print client.Add(a=1, b=2).res
print client.Hello().res
