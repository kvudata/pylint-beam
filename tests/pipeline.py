import apache_beam as beam

class MyDoFn(beam.DoFn):
    def process(self, element):
        return [{'field1': 1, 'field2': 'foo'}]

p = beam.Pipeline()
data = p | 'Create data' >> beam.Create([1, 2, 3])
_ = data | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
    'my-project:my_dataset.my_table',
    write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
    create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
    schema='field1:INTEGER,field2:STRING',
)
