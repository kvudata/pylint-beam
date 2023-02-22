"""Test suite for the checkers module."""
import astroid
from pylint.testutils import CheckerTestCase, MessageTest

from pylint_beam.checkers import WriteToBQChecker


class TestWriteToBQChecker(CheckerTestCase):
    """Test suite for the WriteToBQChecker class."""

    CHECKER_CLASS = WriteToBQChecker

    def test_write_invoked_with_write_truncate(self):
        """Test that the checker flags when WRITE_TRUNCATE is specified."""
        node = astroid.extract_node("""
        beam.io.WriteToBigQuery(
            'my-project:my_dataset.my_table',
            write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
            schema='field1:INTEGER,field2:STRING',
        )
        """)
        with self.assertAddsMessages(
            MessageTest('write-to-bq-write-truncate', node=node),
            ignore_position=True,
        ):
            self.checker.visit_call(node)
