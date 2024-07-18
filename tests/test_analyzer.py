# -*- coding: utf-8 -*-
"""CrowdSec analyzer unittest."""
import json
import os
import unittest
from unittest.mock import MagicMock, patch

from crowdsec_analyzer import CrowdsecAnalyzer


def load_file(filename: str):
    """Utility function to load a json file to a dict."""
    filepath = os.path.join(os.path.dirname(__file__), "resources", filename)
    with open(filepath, encoding="utf-8") as json_file:
        return json.load(json_file)


class CrowdSecAnalyzerTest(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        cls.crowdsec_client = MagicMock()
        cls.job_directory = os.path.join(os.path.dirname(__file__), "resources")

    def test_init_analyzer(self):
        analyzer = CrowdsecAnalyzer(job_directory=self.job_directory)
        self.assertEqual(analyzer.crowdsec_key, "TEST_KEY")

    def test_run_analyzer(self):
        mock_client = MagicMock()
        with patch("crowdsec_analyzer.Crowdsec", mock_client):
            crowdsec_result = load_file("malicious_ip.json")
            mock_client.return_value.summary.return_value = crowdsec_result
            analyzer = CrowdsecAnalyzer(job_directory=self.job_directory)
            analyzer.run()
            mock_client.assert_called_once_with("TEST_KEY")
            analyzer_output = load_file("output/output.json")
            self.assertEqual(crowdsec_result, analyzer_output["full"])
            expected_summary = load_file("malicious_ip_summary.json")
            self.assertEqual(expected_summary, analyzer_output["summary"])
